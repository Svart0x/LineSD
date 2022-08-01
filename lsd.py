#######################
# Created by: Svart0x #
#######################



from PyQt6 import QtCore, QtGui, QtWidgets
import urllib.request, urllib.error
import sys, os

basedir = os.path.dirname(__file__)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(583, 239)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("iconLineStickerApp.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QWidget {\n"
"\n"
"background : #565656\n"
"\n"
"}")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedKingdom))
        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(220, 150, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(os.path.join(basedir, "dl_btn.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(MainWindow)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 30, 403, 49))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.explanationLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.explanationLabel.setFont(font)
        self.explanationLabel.setObjectName("explanationLabel")
        self.gridLayout.addWidget(self.explanationLabel, 0, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.stickerIDInput = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.stickerIDInput.setFont(font)
        self.stickerIDInput.setStyleSheet("QlineEdit\n"
"{\n"
"color : white\n"
"\n"
"}")
        self.stickerIDInput.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhPreferNumbers)
        self.stickerIDInput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.stickerIDInput.setObjectName("stickerIDInput")
        self.gridLayout.addWidget(self.stickerIDInput, 1, 1, 1, 1)

        # CREATION DE LA PROGRESSBAR
        self.progressBar = QtWidgets.QProgressBar(MainWindow)
        self.progressBar.setGeometry(QtCore.QRect(80, 100, 441, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.Download) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Line Sticker Downloader - Made Possible By Svart0x"))
        self.pushButton.setText(_translate("MainWindow", "Download"))
        self.explanationLabel.setText(_translate("MainWindow", "Please enter in the box below the Line Sticker ID"))
        self.label.setText(_translate("MainWindow", "Line Sticker ID :"))

    def Handle_Progress(self, blocknum, blocksize, totalsize):
 
        ## calculate the progress
        readed_data = int(blocknum) * int(blocksize)
        self.progressBar.setValue(0)

        if totalsize > 0:
            download_percentage = readed_data * 100 / totalsize
            self.progressBar.setValue(int(download_percentage))
            QtWidgets.QApplication.processEvents()

    def Download(self):
        
        inputID = self.stickerIDInput.text()
        #hurl = f'http://dl.stickershop.line.naver.jp/products/0/0/1/{inputID}/iphone/stickerpack@2x.zip'
        # specify the url of the file which is to be downloaded
        down_url = f'http://dl.stickershop.line.naver.jp/products/0/0/1/{inputID}/iphone/stickerpack@2x.zip' # specify download url here
        down_url2 = f'http://dl.stickershop.line.naver.jp/products/0/0/1/{inputID}/iphone/stickers@2x.zip' # specify download url here

        # specify save location where the file is to be saved
        #save_loc = f'{inputID}.zip'
        save_loc = os.path.expanduser("~/Downloads/" + inputID + ".zip")
 
        

        # Downloading using urllib
        try:
            req = urllib.request.urlretrieve(down_url,save_loc, self.Handle_Progress)

        except urllib.error.HTTPError as e:
            if e.code == 404:
                urllib.request.urlretrieve(down_url2,save_loc, self.Handle_Progress)
            else:
                print('HTTPError: {}'.format(e.code))
        except urllib.error.URLError as e:
                # Not an HTTP-specific error (e.g. connection refused)
                # ...
            print('URLError: {}'.format(e.reason))
        '''else:
            # 200
            # ...
            print('good')'''


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
