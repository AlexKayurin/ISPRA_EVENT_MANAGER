import os
import sys
import re
from pathlib import Path
import json
import itertools
from datetime import datetime

import chardet
import pandas as pd
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFileDialog, QMessageBox, QDialog

import _UI_control
import _UI_merge
import _UI_selectcmtsheet
import _QtPl


# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_colwidth', None)


OPTIONS = QFileDialog.Options()


class SelectCmtSheet(_UI_selectcmtsheet.Ui_Dialog, QDialog):
    '''
    Class inherits MODAL(!) QDialog class. This is child class of MergeWindow instance. Since it is modal,
    it suspends eventloop of the parent class until 'accept' func is called.
    It is used to select Excel sheet to import from 'comments' file should it saved as Excel.
    '''
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.setWindowIcon(ic_app)
        self.table_sheet.horizontalHeader().setStyleSheet('::section{border: 1px solid gray;}')


    def accept(self):
        '''
        accept func returns no of sheel to import as selected table row ix
        :return: index of selected 'comments' Excel file sheet
        '''
        ec.selected_cmt_sheet = self.table_sheet.currentRow()
        self.close()


class MainWindow(QtWidgets.QMainWindow, _UI_control.Ui_MainWindow):
    '''
    Class _UI_control QMainWindow class. This is main window of the application used for selecting VisualSoft project
    and exporting merged(!) 'track', 'events' and 'dv index' files as Excel files.

    VisualSoft project is selected as folder containing VisualSoft data structure
    For exported files export folder is selected
    '''
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.table_cameras.horizontalHeader().setStyleSheet('::section{border: 1px solid gray;}')

        self.b_selectproj.clicked.connect(self.selectproject)
        self.b_run.clicked.connect(self.go)
        self.b_comments.clicked.connect(lambda: ec.show())

        self.projectselected = False        # flag for project selected


    def closeEvent(self, e):
        '''
        Track close event and save cfg.json on close
        :param e:
        :return:
        '''
        if not os.path.isdir(os.path.join(parentfold, 'bin')):
            os.makedirs(os.path.join(parentfold, 'bin'))

        try:
            # save cfg file in ..\bin\cfg.json
            CFG = {
                'TRACKEXTENSION' : TRACKEXTENSION,
                'EVTEXTENSION' : EVTEXTENSION,
                'DVEXTENSION' : DVEXTENSION,
                'CAMDELIMITER' : CAMDELIMITER,
                'TRACKSEPARATOR' : TRACKSEPARATOR,
                'EVENTSEPARATOR' : EVENTSEPARATOR,
                'COMMENTSEPARATOR' : COMMENTSEPARATOR,
                'MAXVARIATION' : MAXVARIATION,
                'EVTDATEFIELD' : EVTDATEFIELD,
                'EVTTIMEFIELD': EVTTIMEFIELD,
                'EVTDTFORMAT' : EVTDTFORMAT,
                'CMTDATEFIELD': CMTDATEFIELD,
                'CMTTIMEFIELD': CMTTIMEFIELD,
                'CMTDTFORMAT' : CMTDTFORMAT,
                'ASFDTFROMAT' : ASFDTFROMAT,
                'MAKEDVI' : MAKEDVI,
                'COMMENTFIELDTOMERGE' : COMMENTFIELDTOMERGE,
                'EVENTFIELDTOMERGE' : EVENTFIELDTOMERGE,
                'FIELDSEPARATOR': FIELDSEPARATOR
            }
            json_str = json.dumps(CFG, indent=0)
            with open(configfile, 'w') as outfile:
                outfile.write(json_str)
        except:
            pass

        ec.close()


    def selectproject(self):
        '''
        Selects VisualSoft project as folder

        self.cameraset - set of cameras names in VisualSoft stucture - obtained from parsed filenames
        self.projfolder - full VisualSoft project folder - upper level
        self.projname - basename of project folder
        self.cameralist - self.cameraset as list

        :return: self.projfolder, self.projname, self.cameralist, self.projectselected
        '''
        self.cameraset = set()
        self.table_cameras.setRowCount(0)

        self.projfolder = QFileDialog.getExistingDirectory(self, 'Select project folder', '',options=OPTIONS)

        if self.projfolder:
            self.projname = os.path.basename(self.projfolder)
            self.lab_0.setText(f'Select camera in: {self.projfolder}')

            for (root, dirs, files) in os.walk(self.projfolder, topdown=True):
                for file in files:
                    if CAMDELIMITER in file:
                        self.cameraset.add(Path(file).stem.split(CAMDELIMITER)[1])

            self.cameralist = list(self.cameraset)
            self.table_cameras.setRowCount(len(self.cameralist))
            for i, cam in enumerate(self.cameralist):
                self.table_cameras.setItem(i, 0, QtWidgets.QTableWidgetItem(cam))
            self.table_cameras.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

            self.projectselected = True


    def go(self):
        '''
        Select folder to export 'track', 'events' and 'dv index' Excel files

        self.savefolder - folder to export 'track', 'events' and 'dv index' Excel files
        self.cameraexport - name of camera to export

        :return: self.savefolder, self.cameraexport
        '''
        if not self.projectselected or self.table_cameras.currentRow() == -1:
            messagepop('Select project and camera')

        else:
            self.savefolder = QFileDialog.getExistingDirectory(self, 'Select folder to save to',
                                                               '', options=OPTIONS)

            if (self.savefolder and self.projfolder) and self.table_cameras.currentRow() != -1:
                self.cameraexport = self.table_cameras.item(self.table_cameras.currentRow(), 0).text()

                self.fillxlsx(TRACKEXTENSION, TRACKSEPARATOR, 'track')
                self.fillxlsx(EVTEXTENSION, TRACKSEPARATOR, 'events')

                messagepop('Track and Events files created')


    def fillxlsx(self, filetype, separator, descr):
        '''
        Export 'track', 'events' and 'dv index' Excel files

        :param filetype: This is type of file in VisualSoft structure defined by file extension as per
        VisualSoft practices: Camera Track - TRACKEXTENSION == '.csv'; Events - EVTEXTENSION == '.evt'.
        Specified in cfg.json
        :param separator: Columns seperators in track and events files. Specified in cfg.json
        :param descr: Exported Excel file suffix

        :return: saves merged 'track', 'events' and 'dv index' Excel files
        Files formats:
        'track' and 'events' - same as input files
        'dv index' - EventDate, EventTime, DVFileName(full), ASF(evented position in seconds in the DV)
        '''
        savedfn = os.path.join(self.savefolder, f'{self.projname}_{self.cameraexport}_{descr}.xlsx')
        savedfn_dvix = os.path.join(self.savefolder, f'{self.projname}_{self.cameraexport}_dvix.xlsx')

        fileslist = []
        for (root, dirs, files) in os.walk(self.projfolder, topdown=True):
            for file in files:
                if (self.cameraexport in file) and (Path(file).suffix.lower() == filetype):
                    fileslist.append(os.path.join(root, file))

        if filetype == TRACKEXTENSION:
            allfiles = pd.concat((pd.read_csv(f, sep=separator, header=0) for f in fileslist))
            allfiles.iloc[:, 1:].to_excel(savedfn, index=False, sheet_name=self.cameraexport, header=True)

        if filetype == EVTEXTENSION:
            dflist = []
            for f in fileslist:
                _x = pd.read_csv(f, sep=separator, skiprows=2, skipfooter=1, header=0, index_col=0, engine='python')
                _x['FN'] = f.replace(EVTEXTENSION, DVEXTENSION)
                dflist.append(_x)
            allfiles = pd.concat(dflist)

            # allfiles = pd.concat((pd.read_csv(f, sep=separator, skiprows=2, skipfooter=1, header=0, index_col=0, engine='python') for f in fileslist))
            allfiles.iloc[:, :-1].to_excel(savedfn, index=False, sheet_name=self.cameraexport, header=True)

            if MAKEDVI:
                _ixs = pd.DataFrame(data=allfiles.index.str.split('\t'))
                _ixs['EVTDATE'] = allfiles.iloc[:, 0].to_list()
                _ixs['EVTTIME'] = allfiles.iloc[:, 1].to_list()
                _ixs['FN'] = allfiles.iloc[:, -1].to_list()
                _ixs['ASF'] = list(
                    itertools.chain([(datetime.strptime(it[0], ASFDTFROMAT) - datetime(1900, 1, 1)).total_seconds()
                                     for it in _ixs.iloc[:, 0].to_list()]))
                _ixs.iloc[:, 1:].to_excel(savedfn_dvix, index=False, sheet_name=self.cameraexport, header=True)


class MergeWindow(QtWidgets.QMainWindow, _UI_merge.Ui_MainWindow):
    '''
    Class _UI_merge QMainWindow class. This is secondary window of the application used for managing (merging, editing,
    exporting) events, viewing VisualSoft DV and saving images.
    '''
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.table_evts.horizontalHeader().setStyleSheet('::section{border: 1px solid gray;}')
        self.table_cmts.horizontalHeader().setStyleSheet('::section{border: 1px solid gray;}')
        self.sp_maxvar.setValue(MAXVARIATION)

        self.b_selectevt.clicked.connect(self.select_file)
        self.b_selectcmt.clicked.connect(self.select_file)
        self.b_selectdvix.clicked.connect(self.select_file)
        self.b_merge.clicked.connect(self.merge)
        self.b_saveevts.clicked.connect(self.save_events)
        self.table_evts.cellClicked.connect(self.getclickedevt)
        self.lineed_filter.textEdited.connect(lambda: self.filter_comments('setfilter'))
        self.combo_filter.currentIndexChanged.connect(lambda: self.filter_comments('resetfilter'))

        self.evtfn = None                   # events filename
        self.cmtfn = None                   # comments filename
        self.dvifn = None                   # DV index filename
        self.evts_selected = False          # Events selected flag
        self.cmts_selected = False          # Comments selected flag
        self.dvix_selected = False          # DV index selected flag

        self._dvinit = None                 # DV filename to initialize player

        self.selected_cmt_sheet = 0         # ix of selected Excel sheet of 'comments' file (if it is Excel)

        self.lineed_colsfrom.setText(','.join(map(str, COMMENTFIELDTOMERGE)))   # columns to merge from in 'comments'
        self.sp_colto.setValue(EVENTFIELDTOMERGE)                               # column to merge to in 'events'
        self.lineed_separator.setText(FIELDSEPARATOR)                           # seperator of the merged entries


    def closeEvent(self, e):
        '''
        Track close event and close DV player
        :param e:
        :return:
        '''
        try:
            self.player.close()
        except:
            pass


    def select_file(self):
        '''
        Select exported 'track', 'events' and 'dv index' (optional) Excel files
        :return:
        '''
        sender = self.sender().objectName()

        caption = 'Select events file' if sender == 'b_selectevt' else 'Select comments file'
        filter = 'excel file (*.xlsx);;All Files (*)' if (sender == 'b_selectevt' or sender == 'b_selectdvix') else 'excel file (*.xlsx);;csv file (*.csv);;All Files (*)'

        if (sender == 'b_selectcmt' or sender == 'b_selectdvix') and not self.evts_selected:
            messagepop('Select Events file first')
        else:
            if sender == 'b_selectevt':
                self.clear_table('comments')
                self.clear_table('events')
                self.cmts_selected = False
                self.evts_selected = False
            if sender == 'b_selectcmt':
                self.clear_table('comments')
                self.cmts_selected = False
            if sender == 'b_selectdvix':
                self.dvix_selected = False

            fn, _ = QFileDialog.getOpenFileName(self, caption,'', filter, options=OPTIONS)

            if fn:
                if sender == 'b_selectevt':
                    self.evtfn = fn
                    self.evts_selected = True
                    self.fill_table('events')
                elif sender == 'b_selectdvix':
                    if not self.evtfn:
                        messagepop('Select Events file first')
                    else:
                        self.dvifnv = fn
                        self.dvix_selected = True
                        self.fill_table('dvix')
                elif sender == 'b_selectcmt':
                    if not self.evtfn:
                        messagepop('Select Events file first')
                    else:
                        self.cmtfn = fn
                        self.cmts_selected = True
                        self.fill_table('comments')


    def clear_table(self, table_to_clear):
        '''
        Clear tables
        :param table_to_clear:
        :return:
        '''
        if table_to_clear == 'comments':
            _table_name = self.table_cmts
        if table_to_clear == 'events':
            _table_name = self.table_evts

        try:
            _table_name.clear()
            _table_name.setRowCount(0)
            _table_name.setColumnCount(0)
            self.combo_filter.clear()
        except:
            pass


    def fill_table(self, ft):
        '''
        Fill tables
        :param ft:
        :return:
        '''
        if ft == 'events':
            #  read sheet to pandas df - events
            self.evts = pd.read_excel(self.evtfn, dtype='object')
            self.evts.fillna(value='', inplace=True)

            # replace nan with ''
            self.evts.fillna(value='', inplace=True)
            # convert date column to datetime.date & time column to datetime.time
            self.evts.iloc[:, EVTDATEFIELD] = pd.to_datetime(self.evts.iloc[:, EVTDATEFIELD],
                                                             format=EVTDTFORMAT[0], errors='coerce').dt.date
            self.evts.iloc[:, EVTTIMEFIELD] = pd.to_datetime(self.evts.iloc[:, EVTTIMEFIELD],
                                                             format=EVTDTFORMAT[1], errors='coerce').dt.time
            # drop NaT after conversions
            self.evts = self.evts.dropna()

            # set up events table
            self.table_evts.setRowCount(self.evts.shape[0])
            self.table_evts.setColumnCount(self.evts.shape[1])
            self.table_evts.setHorizontalHeaderLabels(self.evts.columns)

            # fill events table
            for row in range(self.evts.shape[0]):
                for col in range(self.evts.shape[1]):
                    item = QtWidgets.QTableWidgetItem(str(self.evts.iloc[row, col]))
                    # specify editable column
                    col_editable = EVENTFIELDTOMERGE if EVENTFIELDTOMERGE >= 0\
                        else (self.evts.shape[1] + EVENTFIELDTOMERGE)
                    if col == col_editable:
                        # make editable
                        item.setFlags(item.flags() | Qt.ItemIsEditable)
                    else:
                        # make read-only
                        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                    # fill values
                    self.table_evts.setItem(row, col, item)
            # resize to contents
            self.table_evts.resizeColumnsToContents()
            self.table_evts.resizeRowsToContents()

            # create events timestamp
            self.evttimestamps = pd.Series([pd.Timestamp.combine(d, t) for d, t in zip(self.evts.iloc[:, EVTDATEFIELD],
                                                                                       self.evts.iloc[:, EVTTIMEFIELD])])

            # set 'mergeto'  column no to max
            self.sp_colto.setMaximum(self.evts.shape[1])

        if ft == 'comments':
            cmtftype = Path(self.cmtfn).suffix
            if cmtftype == '.csv':
                #  read csv to pandas df - events
                CSVENCODING = detect_encoding(self.cmtfn)
                self.cmts = pd.read_csv(self.cmtfn, delimiter=COMMENTSEPARATOR, encoding=CSVENCODING, na_filter=True)
                # replace nan with ''
                self.cmts.fillna(value='', inplace=True)
                # drop NaT after conversions
                self.cmts = self.cmts.dropna()
                # create timestamp
                self.cmttimestamps = pd.to_datetime(self.cmts.iloc[:, 0] + self.cmts.iloc[:, 1],
                                                    format=(CMTDTFORMAT[0] + CMTDTFORMAT[1]),
                                                    errors='coerce')

            if cmtftype == '.xlsx':
                # read xlsx sheets names
                xl = pd.ExcelFile(self.cmtfn)
                self.cmtsheets = xl.sheet_names
                # call sheet selection dialog
                self.selectcmtsheet = SelectCmtSheet(self)
                #  fill table of sheets in sheets selection dialog
                self.selectcmtsheet.table_sheet.setRowCount(len(self.cmtsheets))
                for i, sheet in enumerate(self.cmtsheets):
                    self.selectcmtsheet.table_sheet.setItem(i, 0, QtWidgets.QTableWidgetItem(sheet))
                self.selectcmtsheet.table_sheet.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
                # exec dialog (not  .show()!, otherwise it will not be modal)
                self.selectcmtsheet.exec()
                #  read sheet to pandas df - comments
                self.cmts = pd.read_excel(ec.cmtfn, sheet_name=self.selected_cmt_sheet, na_filter=True, dtype=object)

                # replace nan with ''
                self.cmts.fillna(value='', inplace=True)
                # convert date column to datetime.date & time column to datetime.time
                self.cmts.iloc[:, CMTDATEFIELD] = pd.to_datetime(self.cmts.iloc[:, CMTDATEFIELD],
                                                                 format=CMTDTFORMAT[0], errors='coerce').dt.date
                self.cmts.iloc[:, CMTTIMEFIELD] = pd.to_datetime(self.cmts.iloc[:, CMTTIMEFIELD],
                                                                 format=CMTDTFORMAT[1], errors='coerce').dt.time
                # drop NaT after conversions
                self.cmts = self.cmts.dropna()
                # create timestamp
                self.cmttimestamps = pd.Series(
                    [pd.Timestamp.combine(d, t) for d, t in zip(self.cmts.iloc[:, CMTDATEFIELD],
                                                                self.cmts.iloc[:, CMTTIMEFIELD])])

            # set up comments table
            self.table_cmts.setRowCount(self.cmts.shape[0])
            self.table_cmts.setColumnCount(self.cmts.shape[1])
            self.table_cmts.setHorizontalHeaderLabels(self.cmts.columns)

            # fill comments table
            for row in range(self.cmts.shape[0]):
                for col in range(self.cmts.shape[1]):
                    self.table_cmts.setItem(row, col, QtWidgets.QTableWidgetItem(str(self.cmts.iloc[row, col])))
            # resize to contents
            self.table_cmts.resizeColumnsToContents()
            self.table_cmts.resizeRowsToContents()
            # set filter options from 'comments' columns names
            self.combo_filter.addItems(self.cmts.columns)


        if ft == 'dvix':
            self.dvix = pd.read_excel(self.dvifnv)
            self._dvinit = self.dvix['FN'][0]
            self.player = _QtPl.Player()
            self.player.setWindowIcon(ic_app)
            self.player.show()
            self.player.loadmedia(self._dvinit, 0, os.path.dirname(self.dvifnv))


    def filter_comments(self, mode):
        # filter column and value
        filtercolumn = self.combo_filter.currentIndex()
        filtervalue = self.lineed_filter.text()

        # filtered comments df
        if mode == 'setfilter' and filtervalue != '':
            filtered_cmts = self.cmts[self.cmts.iloc[:, filtercolumn].astype('str') == filtervalue]
        else:
            self.lineed_filter.setText('')
            filtered_cmts = self.cmts
        self.table_cmts.setRowCount(filtered_cmts.shape[0])

        # fill comments table
        for row in range(filtered_cmts.shape[0]):
            for col in range(filtered_cmts.shape[1]):
                self.table_cmts.setItem(row, col, QtWidgets.QTableWidgetItem(str(filtered_cmts.iloc[row, col])))
        # resize to contents
        self.table_cmts.resizeColumnsToContents()
        self.table_cmts.resizeRowsToContents()


    def merge(self):
        try:
            global COMMENTFIELDTOMERGE
            global EVENTFIELDTOMERGE
            global FIELDSEPARATOR
            # read merging settings from UI
            COMMENTFIELDTOMERGE = list(map(int, re.split(r'[:;,\s\t]+', self.lineed_colsfrom.text())))
            EVENTFIELDTOMERGE = self.sp_colto.value()
            FIELDSEPARATOR = self.lineed_separator.text()

            if self.evts_selected and self.cmts_selected:
                # reading events timestamps
                for i, ts in enumerate(self.evttimestamps):
                    # clear events cells
                    self.table_evts.setItem(i + 1, EVENTFIELDTOMERGE - 1, QtWidgets.QTableWidgetItem(''))
                    # check minimum variation between event and comment timestamps
                    minvar = (ts - self.cmttimestamps).abs().min() / pd.Timedelta(seconds=1)
                    minix = (ts - self.cmttimestamps).abs().argmin()
                    # fill comments to events if timestamp variation < max
                    if minvar <= self.sp_maxvar.value():
                        comment = (' ' + FIELDSEPARATOR + ' ').join([str(self.cmts.iloc[minix, x - 1]) for x
                                                                     in COMMENTFIELDTOMERGE
                                                                     if str(self.cmts.iloc[minix, x - 1]) != ''])
                        self.table_evts.setItem(i, EVENTFIELDTOMERGE - 1, QtWidgets.QTableWidgetItem(comment))
                self.table_evts.resizeColumnsToContents()

            else:
                messagepop('Select events and comments files')

        except:
            messagepop('Check merging settings')


    def save_events(self):
        if self.evts_selected:
            mergedfn = os.path.join(os.path.dirname(self.evtfn), f'{Path(self.evtfn).stem}_merged.xlsx')
            # read events from UI table
            for i in range(self.table_evts.rowCount()):
                for j in range(self.table_evts.columnCount()):
                    self.evts.iloc[i, j] = self.table_evts.item(i, j).text()

            self.evts.to_excel(mergedfn, index=False, sheet_name='Merged_events', header=True)
            messagepop('File saved')

        else:
            messagepop('Select events and comments files')


    def getclickedevt(self, row, column):
        if self.dvix_selected:
            _media = self.dvix['FN'][row]
            _gototime = int(self.dvix['ASF'][row] * 1000)
            _timestamp = (pd.to_datetime(
                self.dvix['EVTDATE'][row] + self.dvix['EVTTIME'][row],
                format=(EVTDTFORMAT[0] + EVTDTFORMAT[1]), errors='coerce').
                          strftime('%Y-%m-%d-%H-%M-%S'))
            if _media != self._dvinit:  # load new media if changed, use the same otherwise
                self.player.loadmedia(_media, _gototime, os.path.dirname(self.dvifnv))
                self._dvinit = _media
            self.player.gototime(_gototime, row, _timestamp)


def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        detector = chardet.universaldetector.UniversalDetector()
        for line in file:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
        # print(detector.result['encoding'])
    return detector.result['encoding']


def messagepop(message):
    msg = QMessageBox()
    msg.setWindowTitle('Warning!')
    msg.setText(message)
    msg.setWindowIcon(ic_app)
    msg.show()
    msg.exec()


def IconFromBase64():
    base64 = b'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'
    pixmap = QtGui.QPixmap()
    pixmap.loadFromData(QtCore.QByteArray.fromBase64(base64))
    icon = QtGui.QIcon(pixmap)
    return icon


def main():
    global ic_app
    global mc
    global ec
    global parentfold
    global configfile
    global file

    global TRACKEXTENSION
    global EVTEXTENSION
    global DVEXTENSION
    global CAMDELIMITER
    global TRACKSEPARATOR
    global EVENTSEPARATOR
    global COMMENTSEPARATOR
    global MAXVARIATION
    global EVTDATEFIELD
    global EVTTIMEFIELD
    global EVTDTFORMAT
    global CMTDATEFIELD
    global CMTTIMEFIELD
    global CMTDTFORMAT
    global ASFDTFROMAT
    global MAKEDVI
    global COMMENTFIELDTOMERGE
    global EVENTFIELDTOMERGE
    global FIELDSEPARATOR


    file = sys.argv[0]
    parentfold = os.path.dirname(file)
    # parentfold = os.path.dirname(os.getcwd())
    configfile = os.path.join(parentfold, 'bin', 'cfg.json')

    try:
        with open(configfile) as cfgfile:
            cfg = json.load(cfgfile)
        TRACKEXTENSION = cfg['TRACKEXTENSION']
        EVTEXTENSION = cfg['EVTEXTENSION']
        DVEXTENSION = cfg['DVEXTENSION']
        CAMDELIMITER = cfg['CAMDELIMITER']
        TRACKSEPARATOR = cfg['TRACKSEPARATOR']
        EVENTSEPARATOR = cfg['EVENTSEPARATOR']
        COMMENTSEPARATOR = cfg['COMMENTSEPARATOR']
        MAXVARIATION = int(cfg['MAXVARIATION'])
        EVTDATEFIELD = int(cfg['EVTDATEFIELD'])
        EVTTIMEFIELD = int(cfg['EVTTIMEFIELD'])
        EVTDTFORMAT = cfg['EVTDTFORMAT']
        CMTDATEFIELD = int(cfg['CMTDATEFIELD'])
        CMTTIMEFIELD = int(cfg['CMTTIMEFIELD'])
        CMTDTFORMAT = cfg['CMTDTFORMAT']
        ASFDTFROMAT = cfg['ASFDTFROMAT']
        MAKEDVI = int(cfg['MAKEDVI'])
        COMMENTFIELDTOMERGE = cfg['COMMENTFIELDTOMERGE']
        EVENTFIELDTOMERGE = int(cfg['EVENTFIELDTOMERGE'])
        FIELDSEPARATOR = cfg['FIELDSEPARATOR']
    except:
        TRACKEXTENSION = '.csv'
        EVTEXTENSION = '.evt'
        DVEXTENSION = '.mp4'
        CAMDELIMITER = '@'
        TRACKSEPARATOR = ','
        EVENTSEPARATOR = ','
        COMMENTSEPARATOR = ';'
        MAXVARIATION = 20
        EVTDATEFIELD = 0
        EVTTIMEFIELD = 1
        EVTDTFORMAT = ['%d/%m/%Y', '%H:%M:%S']
        CMTDATEFIELD = 0
        CMTTIMEFIELD = 1
        CMTDTFORMAT = ['%d/%m/%Y', '%H:%M:%S']
        ASFDTFROMAT = '%H:%M:%S.%f'
        MAKEDVI = 1
        COMMENTFIELDTOMERGE = [6, 7]
        EVENTFIELDTOMERGE = 13
        FIELDSEPARATOR = '/'

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('fusion')
    ic_app = IconFromBase64()

    mc = MainWindow()
    ec = MergeWindow()

    mc.setWindowIcon(ic_app)
    ec.setWindowIcon(ic_app)

    mc.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()