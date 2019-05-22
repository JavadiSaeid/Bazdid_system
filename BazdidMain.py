import os

import dpi, sys, sqlite3, getpass
from PyQt5.QtCore import QRegExp, Qt, QSizeF
from PyQt5.QtPrintSupport import QPrintDialog, QPrintPreviewDialog
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel
from pytz import timezone
from jdatetime import datetime as dt
from PyQt5.QtGui import QIntValidator, QRegExpValidator, QTextDocument, QTextCursor, \
    QTextTableFormat, QColor, QIcon, QPixmap, QTextCharFormat, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDesktopWidget, QDialog, QWidget
from interface_bazdid import Ui_MainWindow
from about import Ui_Form
import icon_rc
from xlsxwriter.workbook import Workbook


class Bazdid():
    def __init__(self):
        app = QApplication(sys.argv)
        self.MainWindow = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.dateTime()
        self.dbPath = r'\\10.120.112.70\baygan-data\ZamanBandi_Bazdid.db'
        # self.dbPath = r'Data\ZamanBandi_Bazdid.db'
        self.onlyInt = QIntValidator()
        regex = QRegExp("[0-9]+")
        validator = QRegExpValidator(regex)
        self.ui.lineEdit_dateYear.setText(self.nowYear)
        self.ui.lineEdit_dateYear_2.setText(self.nowYear)
        self.ui.lineEdit_dateYear.setValidator(validator)
        self.ui.lineEdit_dateYear_2.setValidator(validator)
        self.ui.lineEdit_dateYear.setMaxLength(4)
        self.ui.lineEdit_dateYear_2.setMaxLength(4)
        self.ui.lineEdit_dateMonth.setText(self.nowMonth)
        self.ui.lineEdit_dateMonth.setValidator(validator)
        self.ui.lineEdit_dateMonth_2.setValidator(validator)
        self.ui.lineEdit_dateMonth.setMaxLength(2)
        self.ui.lineEdit_dateMonth_2.setMaxLength(2)
        self.ui.lineEdit_dateDay.setText(self.nowDay)
        self.ui.lineEdit_dateDay.setValidator(validator)
        self.ui.lineEdit_dateDay_2.setValidator(validator)
        self.ui.lineEdit_dateDay.setMaxLength(2)
        self.ui.lineEdit_dateDay_2.setMaxLength(2)
        self.ui.lineEdit_sangAsli.setValidator(validator)
        self.ui.lineEdit_sangFari.setValidator(validator)
        self.ui.lineEdit_sangAsli_2.setValidator(validator)
        self.ui.lineEdit_sangFari_2.setValidator(validator)
        self.ui.lineEdit_sangAsli_2.setMaxLength(3)
        self.ui.lineEdit_sangAsli.setMaxLength(3)
        self.ui.tab1_inputData.keyPressEvent = self.EnterToTab_1
        self.ui.tab2_SearchData.keyPressEvent = self.EnterToTab_2
        self.ui.pushButton_sabt.clicked.connect(self.btn_sbt)
        self.ui.pushButton_search.clicked.connect(self.btn_search)
        self.ui.pushButton_new.clicked.connect(self.btn_New)
        self.ui.checkBox_viaDate.stateChanged.connect(self.viaDate)
        self.ui.checkBox_viaName.stateChanged.connect(self.viaName)
        self.ui.action_about.triggered.connect(self.RunAbout)
        self.ui.action_backup.triggered.connect(self.dbTOxlsx)
        self.ui.pushButton_print.clicked.connect(self.handlePreview)
        self.MainWindow.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.ui.action_help.setEnabled(False)
        self.ui.action_ChangPassword.setEnabled(False)
        MainWindowGetSize = self.MainWindow.frameGeometry()
        DesktopCenter = QDesktopWidget().availableGeometry().center()
        MainWindowGetSize.moveCenter(DesktopCenter)
        self.MainWindow.move(MainWindowGetSize.topLeft())
        self.hamkaran_list()
        self.MainWindow.show()
        sys.exit(app.exec_())

    def hamkaran_list(self):
        try:
            with sqlite3.connect(self.dbPath) as database:
                NAGHSHEBARDAR_LIST = "CREATE TABLE IF NOT EXISTS NAGSHEBARDAR(nb VARCHAR(72)  UNIQUE)"
                NAMAYANDE_LIST = "CREATE TABLE IF NOT EXISTS NAMAYANDE(nm VARCHAR(72)  UNIQUE)"
                DW = "CREATE TABLE IF NOT EXISTS DOWORK(dw TEXT UNIQUE)"
                database.execute(NAGHSHEBARDAR_LIST)
                database.execute(NAMAYANDE_LIST)
                database.execute(DW)
                n1 = "SELECT nb FROM NAGSHEBARDAR"
                n2 = "SELECT nm FROM NAMAYANDE"
                n3 = "SELECT dw FROM DOWORK"
                curser_n1 = database.execute(n1)
                curser_n2 = database.execute(n2)
                curser_n3 = database.execute(n3)
                if curser_n1.fetchone() is None:
                    nb1 = ["کیوان حسنجانی", "اسماعیل دولتی", "سایر"]
                    for n in nb1:
                        naghshebardar_ins = "INSERT INTO NAGSHEBARDAR(nb) values ('{}')".format(n)
                        database.execute(naghshebardar_ins)
                        database.commit()
                if curser_n2.fetchone() is None:
                    nm2 = ["سیدمحمد آتشی", "علی رحمانی", "محسن مهرافشان", "سایر"]
                    for n in nm2:
                        namayande_ins = "INSERT INTO NAMAYANDE(nm) values ('{}')".format(n)
                        database.execute(namayande_ins)
                        database.commit()
                if curser_n3.fetchone() is None:
                    dw = ["تعویض سند", "المثنی", "اصلاح", "افراز", "تفکیک آپارتمان", "تفکیک عرصه", "تجمیع", "قانون تعیین تکلیف", "قانون الحاق و ساماندهی", "تحدید حدود اختصاصی", "تحدید حدود عمومی", "تعیین باقیمانده", "ماده 45", "بازدید", "سایر"]
                    for d in dw:
                        dow = "INSERT INTO DOWORK(dw) values ('{}')".format(d)
                        database.execute(dow)
                        database.commit()
                N1 = "SELECT nb FROM NAGSHEBARDAR"
                N2 = "SELECT nm FROM NAMAYANDE"
                N3 = "SELECT dw FROM DOWORK"
                curser1 = database.execute(N1)
                curser2 = database.execute(N2)
                curser3 = database.execute(N3)
                r = 0
                for i in curser1:
                    self.ui.comboBox_naghshebardar.addItem("")
                    self.ui.comboBox_naghshebardar.setItemText(r, i[0])
                    r += 1
                r = 0
                for j in curser2:
                    self.ui.comboBox_namaiande.addItem("")
                    self.ui.comboBox_namaiande.setItemText(r, j[0])
                    r += 1
                r = 0
                for n in curser3:
                    self.ui.comboBox_noeAnjamKar.addItem("")
                    self.ui.comboBox_noeAnjamKar.setItemText(r, n[0])
                    r += 1
        except:
            try:
                nb1 = ["کیوان حسنجانی", "اسماعیل دولتی", "سایر"]
                nm2 = ["سیدمحمد آتشی", "علی رحمانی", "محسن مهرافشان", "سایر"]
                dw3 = ["تعویض سند", "تعویض سند", "المثنی", "اصلاح", "افراز", "تفکیک آپارتمان", "تفکیک عرصه", "تجمیع", "قانون تعیین تکلیف", "قانون الحاق و ساماندهی", "تحدید حدود اختصاصی", "تحدید حدود عمومی", "تعیین باقیمانده", "ماده 45", "بازدید", "سایر"]
                r = 0
                for i in nb1:
                    self.ui.comboBox_naghshebardar.addItem("")
                    self.ui.comboBox_naghshebardar.setItemText(r, i)
                    r += 1
                r = 0
                for j in nm2:
                    self.ui.comboBox_namaiande.addItem("")
                    self.ui.comboBox_namaiande.setItemText(r, j)
                    r += 1
                r = 0
                for d in dw3:
                    self.ui.comboBox_noeAnjamKar.addItem("")
                    self.ui.comboBox_noeAnjamKar.setItemText(r, d)
                    r += 1
            except:
                self.ui.comboBox_naghshebardar.setEditable(True)
                self.ui.comboBox_namaiande.setEditable(True)
                self.ui.comboBox_noeAnjamKar.setEditable(True)
                self.errorM("خطا در خواندن لیست نام همکاران از دیتابیس!")

    def RunAbout(self):
        self.Form = QWidget()
        self.uiForm = Ui_Form()
        self.uiForm.setupUi(self.Form)
        self.uiForm.label_email.setOpenExternalLinks(True)
        self.Form.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.Form.setWindowFlags(self.Form.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        MainWindowGetSize = self.Form.frameGeometry()
        DesktopCenter = QDesktopWidget().availableGeometry().center()
        MainWindowGetSize.moveCenter(DesktopCenter)
        self.Form.move(MainWindowGetSize.topLeft())
        self.Form.keyPressEvent = self.CustomClose
        self.Form.show()

    def CustomClose(self, e):
        if e.key() == Qt.Key_Return or e.key() == Qt.Key_Enter:
            self.Form.close()

    def dateTime(self):
        self.tz = timezone('Asia/Tehran')
        self.TimeSabt = dt.now(self.tz)
        self.nowYear = self.TimeSabt.strftime("%Y")
        self.nowMonth = self.TimeSabt.strftime("%m")
        self.nowDay = self.TimeSabt.strftime("%d")
        self.nowHour = self.TimeSabt.strftime("%H")
        self.nowMinute = self.TimeSabt.strftime("%M")

    def EnterToTab_1(self, e):
        if e.key() == Qt.Key_Return or e.key() == Qt.Key_Enter:
            self.btn_sbt()

    def EnterToTab_2(self, e):
        if e.key() == Qt.Key_Return or e.key() == Qt.Key_Enter:
            self.btn_search()

    def viaDate(self):
        if self.ui.checkBox_viaDate.isChecked():
            self.ui.lineEdit_dateDay.setEnabled(True)
            self.ui.lineEdit_dateMonth.setEnabled(True)
            self.ui.lineEdit_dateYear.setEnabled(True)
            self.ui.lineEdit_sangAsli_2.setEnabled(False)
            self.ui.lineEdit_sangAsli_2.setText('')
            self.ui.lineEdit_sangFari_2.setEnabled(False)
            self.ui.lineEdit_sangFari_2.setText('')
            self.ui.checkBox_viaName.setEnabled(False)
            self.ui.lineEdit_moteqazi_2.setEnabled(False)
        else:
            self.ui.lineEdit_dateDay.setEnabled(False)
            self.ui.lineEdit_dateMonth.setEnabled(False)
            self.ui.lineEdit_dateYear.setEnabled(False)
            self.ui.lineEdit_sangAsli_2.setEnabled(True)
            self.ui.lineEdit_sangFari_2.setEnabled(True)
            self.ui.checkBox_viaName.setEnabled(True)

    def viaName(self):
        if self.ui.checkBox_viaName.isChecked():
            self.ui.lineEdit_moteqazi_2.setEnabled(True)
            self.ui.lineEdit_dateDay.setEnabled(False)
            self.ui.lineEdit_dateMonth.setEnabled(False)
            self.ui.lineEdit_dateYear.setEnabled(False)
            self.ui.lineEdit_sangAsli_2.setEnabled(False)
            self.ui.lineEdit_sangFari_2.setEnabled(False)
            self.ui.checkBox_viaDate.setEnabled(False)
            self.ui.lineEdit_sangAsli_2.setText('')
            self.ui.lineEdit_sangFari_2.setText('')
        else:
            self.ui.lineEdit_moteqazi_2.setText('')
            self.ui.lineEdit_moteqazi_2.setEnabled(False)
            self.ui.lineEdit_sangAsli_2.setEnabled(True)
            self.ui.lineEdit_sangFari_2.setEnabled(True)
            self.ui.checkBox_viaDate.setEnabled(True)

    def getUpdateVriable(self):
        try:
            self.sangAsli_1 = self.ui.lineEdit_sangAsli.text()
            self.sangFari_1 = self.ui.lineEdit_sangFari.text()
            self.PL = str(self.sangAsli_1)+"/"+str(self.sangFari_1)
            self.moteqazi = self.ui.lineEdit_moteqazi.text()
            self.bazdid_day   = self.ui.lineEdit_dateDay_2.text()
            self.bazdid_month = self.ui.lineEdit_dateMonth_2.text()
            self.bazdid_year  = self.ui.lineEdit_dateYear_2.text()
            self.bazdid_Saat = self.ui.lineEdit_hour.text()
            self.naghsheBardar = self.ui.comboBox_naghshebardar.currentText()
            self.namayande = self.ui.comboBox_namaiande.currentText()
            self.noeAnjamKar = self.ui.comboBox_noeAnjamKar.currentText()
            self.tozihat = self.ui.textEdit_Tozihat.toPlainText()
        except:
            self.errorM("خطا در ورود اطلاعات")

    def insertdb(self, SD, PL, DW, TB, SB, NB, NM, ML='', TT=''):
        try:
            with sqlite3.connect(self.dbPath) as database:
                BAZDID_DATE = """CREATE TABLE IF NOT EXISTS BAZDID_DATE (id INTEGER      PRIMARY KEY AUTOINCREMENT,sd VARCHAR (20),pl VARCHAR (20), ml TEXT,dw TEXT,tb VARCHAR (20),sb VARCHAR (10),nb TEXT,nm TEXT, tt TEXT,us VARCHAR (72) )"""
                database.execute(BAZDID_DATE)
                TH = self.TimeSabt.strftime("%Y/%m/%d")
                ST = self.TimeSabt.strftime("%H:%M")
                insert = "INSERT INTO BAZDID_DATE(sd, pl, ml, dw, tb, sb, nb, nm, tt, us) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')"\
                    .format(SD, PL, ML, DW, TB, SB, NB, NM, TT, getpass.getuser())
                database.execute(insert)
                database.commit()
                QApplication.processEvents()
                return 1
        except:
            return 0

    def btn_sbt(self):
        self.getUpdateVriable()
        self.dateTime()
        try:
            if self.sangAsli_1 != '':
                if self.sangFari_1 != '':
                    if (self.bazdid_year and self.bazdid_month and self.bazdid_day) != '':
                        self.bazdid_date = str(int(self.bazdid_year)) + "/" + str(int(self.bazdid_month)) + "/" + str(int(self.bazdid_day))
                        if self.bazdid_Saat != '':
                            result = self.insertdb(SD=self.TimeSabt.strftime("%Y/%m/%d"), PL=self.PL, DW=self.noeAnjamKar, TB=self.bazdid_date, SB=self.bazdid_Saat, NB=self.naghsheBardar, NM=self.namayande, ML=self.moteqazi, TT=self.tozihat)
                            if result:
                                self.ui.statusbar.showMessage('با موفقیت ثبت شد')
                                self.btn_New()
                            else:
                                self.errorM('مشکلی در ارتباط با دیتابیس بوجود آمده است!')
                        else:
                            self.errorM('لطفا ساعت بازدید را وارد کنید')
                    else:
                        self.errorM("لطفا تاریخ بازدید را به طور صحیح وارد کنید")
                else:
                    self.errorM('شماره سنگ فرعی باید وارد شود')
            else:
                self.errorM('شماره سنگ اصلی باید وارد شود')
        except:
            self.ui.statusbar.showMessage('خطا در ثبت اطلاعات')
            self.errorM(' خطایی در ثبت اطلاعات بوجود امده است \n این خطا را به مدیر سیستم اطلاع دهید')

    def searcherVariable(self):
        self.sangAsli_2 = self.ui.lineEdit_sangAsli_2.text()
        self.sangFari_2 = self.ui.lineEdit_sangFari_2.text()

    def dbToTableView(self,commandSQL):
        try:
            QApplication.processEvents()
            if QSqlDatabase.contains("qt_sql_default_connection"):
                db = QSqlDatabase.database("qt_sql_default_connection")
            else:
                db = QSqlDatabase.addDatabase("QSQLITE")
                db.setDatabaseName(self.dbPath)
                db.open()
            projectModel = QSqlQueryModel()
            projectModel.setQuery(commandSQL, db)
            projectModel.setHeaderData(0, Qt.Horizontal, 'پلاک')
            projectModel.setHeaderData(1, Qt.Horizontal, 'متقاضی')
            projectModel.setHeaderData(2, Qt.Horizontal, 'نوع انجام کار')
            projectModel.setHeaderData(3, Qt.Horizontal, 'تاریخ بازدید')
            projectModel.setHeaderData(4, Qt.Horizontal, 'ساعت بازدید')
            projectModel.setHeaderData(5, Qt.Horizontal, 'نقشه بردار')
            projectModel.setHeaderData(6, Qt.Horizontal, 'نماینده')
            projectModel.setHeaderData(7, Qt.Horizontal, 'تاریخ ثبت')
            projectModel.setHeaderData(8, Qt.Horizontal, 'توضیحات')
            self.ui.tableView_result.setModel(projectModel)
            self.rowCount = projectModel.rowCount()
            self.tableResult = projectModel
            db.close()
            QApplication.processEvents()
        except:
            self.errorM('مشکل در ارتباط با دیتابیس\n {}')

    def btn_search(self):
        self.TableTitr = ""
        Tr = self.TimeSabt.strftime("%Y/%m/%d")
        Ts = self.TimeSabt.strftime("%H:%M")
        self.ui.pushButton_print.setEnabled(False)
        self.searcherVariable()
        pl = self.sangAsli_2 + "/" + self.sangFari_2
        if self.ui.checkBox_viaDate.isChecked():
            day   = self.ui.lineEdit_dateDay.text()
            month = self.ui.lineEdit_dateMonth.text()
            year  = self.ui.lineEdit_dateYear.text()
            if (year and month and day) != '':
                searchDate = str(int(year))+"/"+str(int(month))+"/"+str(int(day))
                searchDate2 = str(int(year.replace('13', '')))+"/"+str(int(month))+"/"+str(int(day))
                searchDate2_1 = str(int(year.replace('14', '')))+"/"+str(int(month))+"/"+str(int(day))
                searchDate3 = str(int('13'+year))+"/"+str(int(month))+"/"+str(int(day))
                searchDate4 = str(int('14'+year))+"/"+str(int(month))+"/"+str(int(day))
            else:
                searchDate = year+"/"+month+"/"+day
                searchDate2 = year.replace('13', '')+"/"+month+"/"+day
            self.dbToTableView(
                commandSQL="SELECT pl, ml, dw, tb, sb, nb, nm, sd, tt FROM BAZDID_DATE WHERE  (tb='{}' OR tb='{}' OR tb='{}') ".format(
                    searchDate, searchDate2, searchDate2_1, searchDate3, searchDate4, searchDate2_1))
            if self.rowCount <= 0:
                self.ui.statusbar.showMessage(
                    "برای تاریخ {} سابقه ای موجود نیست".format(searchDate))
            else:
                self.TableTitr = f" تمام سوابق ثبت شده موجود برای تاریخ  {searchDate} "
                self.enPrint()
        elif self.ui.checkBox_viaName.isChecked():
            name = self.ui.lineEdit_moteqazi_2.text()
            self.dbToTableView(commandSQL="SELECT pl, ml, dw, tb, sb, nb, nm, sd, tt FROM BAZDID_DATE WHERE  ml LIKE  '%{}%' ".format(name))
            if self.rowCount <= 0:
                self.ui.statusbar.showMessage(
                    "برای نام {} سابقه ای موجود نیست".format(name))
            else:
                self.TableTitr = f" تمام سوابق ثبت شده موجود برای نام  {name} "
                self.enPrint()
        else:
            if self.sangAsli_2 == '' and self.sangFari_2 == '':
                self.dbToTableView(
                    commandSQL="SELECT pl, ml, dw, tb, sb, nb, nm, sd, tt FROM BAZDID_DATE")
                if self.rowCount > 0:
                    self.TableTitr = f" لیست تاریخچه سوابق ثبت شده موجود تا تاریخ {Ts} - {Tr} "
                    self.enPrint()
            elif self.sangAsli_2 != '' and self.sangFari_2 != '' :
                self.dbToTableView(
                    commandSQL="SELECT pl, ml, dw, tb, sb, nb, nm, sd, tt FROM BAZDID_DATE WHERE  pl='{}' ".format(pl))
                if self.rowCount > 0:
                    self.TableTitr = f" لیست تاریخچه سوابق ثبت شده موجود پلاک {pl} تا تاریخ {Ts} - {Tr} "
                    self.enPrint()
                else:
                    self.ui.statusbar.showMessage("برای پلاک {} سابقه ای موجود نیست".format(pl))
            else:
                self.errorM('شماره پلاک به درستی وارد نشده است\n برای بازیابی تمام پلاک ها باید هردو فیلد سنگ اصلی و فرعی خالی باشند و یا پلاک را بطور کامل وارد کنید،\n یا از طریق بخش جستجوی پیشرفته عملیات بازیابی را انجام دهید.')

    def enPrint(self):
        self.ui.pushButton_print.setEnabled(True)

    def dbTOxlsx(self):
        try:
            DeskTop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
            if not os.path.isdir(f'{DeskTop}/Backup'):
                os.mkdir(f'{DeskTop}/Backup')
            Tr = self.TimeSabt.strftime("%Y%m%d%H%M")
            workbook = Workbook('{}/Backup/BackupBazdid_{}.xlsx'.format(DeskTop, Tr))
            worksheet = workbook.add_worksheet()
            with sqlite3.connect(self.dbPath) as conn:
                c = conn.cursor()
                c.execute("select id, pl, ml, dw, tb, sb, nb, nm, sd, tt from BAZDID_DATE")
                mysel = c.execute("select id, pl, ml, dw, tb, sb, nb, nm, sd, tt from BAZDID_DATE ")
                headers = ['ردیف', 'پلاک', 'متقاضی', 'نوع انجام کار', 'تاریخ بازدید', 'ساعت بازدید', 'نقشه بردار',
                           'نماینده', 'تاریخ ثبت', 'توضیحات']
                for i, title in enumerate(headers):
                    worksheet.write(0, i, title)
                for i, row in enumerate(mysel):
                    for j, value in enumerate(row):
                        worksheet.write(i + 1, j, value)
                workbook.close()
                self.errorM(errorText="پشتیبان گیری از دیتابیس با موفقیت انجام شد.", icon='Information')
        except:
            try:
                if not os.path.isdir('./Backup'):
                    os.mkdir('Backup')
                Tr = self.TimeSabt.strftime("%Y%m%d%H%M")
                workbook = Workbook('Backup/BackupBazdid_{}.xlsx'.format(Tr))
                worksheet = workbook.add_worksheet()
                with sqlite3.connect(self.dbPath) as conn:
                    c = conn.cursor()
                    c.execute("select id, pl, ml, dw, tb, sb, nb, nm, sd, tt from BAZDID_DATE")
                    mysel = c.execute("select id, pl, ml, dw, tb, sb, nb, nm, sd, tt from BAZDID_DATE ")
                    headers = ['ردیف', 'پلاک', 'متقاضی', 'نوع انجام کار', 'تاریخ بازدید', 'ساعت بازدید', 'نقشه بردار',
                               'نماینده', 'تاریخ ثبت', 'توضیحات']
                    for i, title in enumerate(headers):
                        worksheet.write(0, i, title)
                    for i, row in enumerate(mysel):
                        for j, value in enumerate(row):
                            worksheet.write(i + 1, j, value)
                    workbook.close()
                    self.errorM(errorText="پشتیبان گیری از دیتابیس با موفقیت انجام شد.", icon='Information')
            except:
                self.errorM("خطا در تهیه پشتیبان از دیتابیس برنامه!")

    def handlePrint(self):
        dialog = QPrintDialog()
        dialog.setWindowFlags(Qt.WindowStaysOnTopHint)
        if dialog.exec_() == QDialog.Accepted:
            self.handlePaintRequest(dialog.printer())
    def handlePreview(self):
        dialog = QPrintPreviewDialog()
        icon = QIcon()
        icon.addPixmap(QPixmap(":/QIcon/Backup/iconn.png"), QIcon.Normal, QIcon.Off)
        dialog.setWindowIcon(icon)
        dialog.setWindowTitle("پیش نمایش چاپ")
        dialog.paintRequested.connect(self.handlePaintRequest)
        dialog.setWindowFlags(Qt.WindowStaysOnTopHint)
        dialog.exec_()
    def handlePaintRequest(self, printer):
        document = QTextDocument()
        document.setPageSize(QSizeF(printer.pageRect().size()))
        cursor = QTextCursor(document)
        tableFormat = QTextTableFormat()
        TableText = QTextCharFormat()
        TableText.setLayoutDirection(Qt.RightToLeft)
        tableFormat.setBackground(QColor('#d3fbf5'))
        tableFormat.setCellPadding(3)
        tableFormat.setCellSpacing(4)
        tableFormat.setLayoutDirection(Qt.RightToLeft)
        tableFormat.setBorderStyle(QTextTableFormat.BorderStyle_Double)
        TitrFormat = QTextCharFormat()
        fontTitr = QFont()
        fontTitr.setBold(True)
        TitrFormat.setFont(fontTitr)
        SotonFormat = QTextCharFormat()
        TitrFormat.setLayoutDirection(Qt.RightToLeft)
        SotonFormat.setFont(fontTitr)
        # SotonFormat.setBackground(QColor('#EEF9C9'))


        cursor.insertText(self.TableTitr+"\n", TitrFormat)
        model = self.ui.tableView_result.model()
        table = cursor.insertTable(model.rowCount()+1, model.columnCount(), tableFormat)
        headers = ['پلاک', 'متقاضی','نوع انجام کار', 'تاریخ بازدید', 'ساعت بازدید', 'نقشه بردار','نماینده','تاریخ ثبت', 'توضیحات']
        self.tableResult.insertRows(10,10)
        for header in reversed(headers):
            cursor.insertText(header,SotonFormat)
            cursor.movePosition(QTextCursor.NextCell)
        for row in range(table.rows()):
            for column in reversed(range(table.columns())):
                cursor.insertText(self.tableResult.data(self.tableResult.index(row,column)),TableText)
                cursor.movePosition(QTextCursor.NextCell)
        cursor.movePosition(QTextCursor.NextBlock)
        cursor.insertText('- سامانه زمانبندی بازدید ثبت ماسال -', TitrFormat)
        # printer.setFullPage(True)
        document.print_(printer)

    def btn_New(self):
        self.ui.lineEdit_sangFari.setText('')
        self.ui.lineEdit_sangAsli.setText('')
        self.ui.textEdit_Tozihat.setText('')
        self.ui.lineEdit_moteqazi.setText('')
        self.ui.lineEdit_dateDay_2.setText('')
        self.ui.lineEdit_dateMonth_2.setText('')
        self.ui.lineEdit_hour.setText('')

    def errorM(self,errorText='مشکلی پیش آمده است !!!', icon=''):
        box = QMessageBox()
        if icon == '':
            box.setIcon(QMessageBox.Warning)
        else:
            box.setIcon(QMessageBox.Information)
        box.setWindowTitle('ارور')
        box.setText(errorText)
        box.setStandardButtons(QMessageBox.Yes)
        buttonY = box.button(QMessageBox.Yes)
        buttonY.setText('       تایید       ')
        box.setStyleSheet("QMessageBox{\n"
                          "background-color:    #d9c9a3    ;\n"
                          "border: 3px solid   #ff0000  ;\n"
                          "border-radius:5px;\n"
                          "}\n"
                          "QLabel{\n"
                          "color:   #ff0000  ;\n"
                          "font: 13pt \"A Arsoo\";\n"
                          "font-weight: bold;\n"
                          "border:no;\n"
                          "}\n"
                          "\n"
                          "QPushButton:hover:!pressed\n"
                          "{\n"
                          "  border: 2px dashed rgb(255, 85, 255);\n"
                          "    background-color:  #e4e7bb ;\n"
                          "    color:  #9804ff ;\n"
                          "}\n"
                          "QPushButton{\n"
                          "background-color:  #a2fdc1 ;\n"
                          "font: 12pt \"A Arsoo\";\n"
                          "font-weight: bold;\n"
                          "    color:  #ff0000 ;\n"
                          "border: 2px solid  #8b00ff ;\n"
                          "border-radius: 8px;\n"
                          "}")
        box.setWindowFlags(box.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        box.exec_()



if __name__ == '__main__':
    run = Bazdid()
