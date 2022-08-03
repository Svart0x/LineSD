#######################
# Created by: Svart0x #
#######################



from turtle import title
from PyQt6 import QtCore, QtGui, QtWidgets
import PyQt6
from PyQt6.QtGui import QPixmap, QScreen
import sys,os
import urllib.request, urllib.error
import requests
from bs4 import BeautifulSoup
import re

basedir = os.path.dirname(__file__)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        MainWindow.resize(612, 694)
        font = QtGui.QFont()
        font.setPointSize(1)
        MainWindow.setFont(font)
        #icon = QtGui.QIcon()
        #icon.addPixmap(QtGui.QPixmap("icon.icns"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        #MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedKingdom))
        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(220, 620, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(os.path.join(basedir, "dl_btn.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(MainWindow)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 30, 469, 62))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.explanationLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
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
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.stickerIDInput = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
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


        self.progressBar = QtWidgets.QProgressBar(MainWindow)
        self.progressBar.setGeometry(QtCore.QRect(80, 540, 441, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.checkStickerButton = QtWidgets.QPushButton(MainWindow)
        self.checkStickerButton.setGeometry(QtCore.QRect(220, 110, 164, 31))


        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)


        self.checkStickerButton.setFont(font)
        self.checkStickerButton.setObjectName("checkStickerButton")
        self.stickerPackDescription = QtWidgets.QLabel(MainWindow)
        self.stickerPackDescription.setGeometry(QtCore.QRect(60, 160, 481, 53))


        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)


        self.stickerPackDescription.setFont(font)
        self.stickerPackDescription.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.stickerPackDescription.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.stickerPackDescription.setIndent(-1)
        self.stickerPackDescription.setObjectName("stickerPackDescription")


        """self.stickerImage = QtWidgets.QGraphicsView(MainWindow)
        self.stickerImage.setGeometry(QtCore.QRect(160, 250, 271, 211))
        self.stickerImage.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.stickerImage.setObjectName("stickerImage")"""

        self.stickerImage = QtWidgets.QLabel(MainWindow)
        #self.stickerImage.setGeometry(160, 250, 271, 211)
        self.stickerImage.setGeometry(160, 250, 240, 240)



        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.Download) # type: ignore
        self.checkStickerButton.clicked.connect(self.checkButtonClicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Line Sticker Downloader - Made By Svart0x"))
        self.pushButton.setText(_translate("MainWindow", "Download"))
        self.explanationLabel.setText(_translate("MainWindow", "Please enter in the box below the Line Sticker ID"))
        self.label.setText(_translate("MainWindow", "Line Stickers Pack ID :"))
        #self.stickerImage.setText(_translate("MainWindow", "IMAGE HERE"))
        self.checkStickerButton.setText(_translate("MainWindow", "Check Sticker Pack"))
        self.stickerPackDescription.setText(_translate("MainWindow", "TextLabel"))

      
        
    def checkButtonClicked(self):
        inputID = self.stickerIDInput.text()
        page = requests.get(f"https://store.line.me/stickershop/product/{inputID}/en")
        imageTag = f"https://stickershop.line-scdn.net/stickershop/v1/product/{inputID}/LINEStorePC/main.png"
        parsedPAge = BeautifulSoup(page.content, 'lxml')
        path3 = R"${TEMP}" + inputID + ".png"

        #save_loc = os.path.expanduser("~/Downloads/" + inputID + ".png")
        save_loc = os.path.expanduser(path3)
        

        
        titleTag = parsedPAge.find('p', {'class':'mdCMN38Item01Ttl'})
        title = titleTag.contents[0]
        title2 = title.text
        #print(title2)
                          
        self.stickerPackDescription.setText(title2)

        reqImg = urllib.request.urlretrieve(imageTag,save_loc)

        pixmap = QPixmap(os.path.expanduser(path3))
        self.stickerImage.show()
        self.stickerImage.setPixmap(pixmap)
        


    def Handle_Progress(self, blocknum, blocksize, totalsize):
    
        ## calculate the progress #####################
        readed_data = int(blocknum) * int(blocksize) ##
        self.progressBar.setValue(0)                 ##
        ###############################################

        if totalsize > 0:
            download_percentage = readed_data * 100 / totalsize
            self.progressBar.setValue(int(download_percentage))
            QtWidgets.QApplication.processEvents()

    def Download(self):
        
        
        inputID = self.stickerIDInput.text()
        page = requests.get(f"https://store.line.me/stickershop/product/{inputID}/en")
        parsedPAge = BeautifulSoup(page.content, 'lxml')
        titleTag = parsedPAge.find('p', {'class':'mdCMN38Item01Ttl'})
        title = titleTag.contents[0]
        title2 = title.text
        #print(title2)

        down_url = f'http://dl.stickershop.line.naver.jp/products/0/0/1/{inputID}/iphone/stickerpack@2x.zip' 
        down_url2 = f'http://dl.stickershop.line.naver.jp/products/0/0/1/{inputID}/iphone/stickers@2x.zip' 

        save_loc = os.path.expanduser("~/Downloads/" + inputID + ".zip")
 
        
        try:
            req = urllib.request.urlretrieve(down_url,save_loc, self.Handle_Progress)

        except urllib.error.HTTPError as e:
            if e.code == 404:
                urllib.request.urlretrieve(down_url2,save_loc, self.Handle_Progress)
            else:
                print('HTTPError: {}'.format(e.code))
        except urllib.error.URLError as e:
                # Not an HTTP-specific error (e.g. connection refused)
                
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
