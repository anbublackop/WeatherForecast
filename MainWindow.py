# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
from pprint import pprint
import requests, json, CalculateForecast
from pprint import pprint

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(802, 601)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 801, 71))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 160, 801, 231))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.weather1 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.weather1.setStyleSheet(_fromUtf8("background-color: rgb(85, 170, 255);\n"
"color: white;\n"
"border-radius: 5px;\n"
"margin: 1px;"))
        self.weather1.setAlignment(QtCore.Qt.AlignCenter)
        self.weather1.setObjectName(_fromUtf8("weather1"))
        self.horizontalLayout_3.addWidget(self.weather1)
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 390, 801, 161))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.weather2 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.weather2.setStyleSheet(_fromUtf8("background-color: rgb(85, 170, 255);\n"
"color: white;\n"
"border-radius: 5px;\n"
"margin: 1px;"))
        self.weather2.setAlignment(QtCore.Qt.AlignCenter)
        self.weather2.setObjectName(_fromUtf8("weather2"))
        self.horizontalLayout_4.addWidget(self.weather2)
        self.weather3 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.weather3.setStyleSheet(_fromUtf8("background-color: rgb(85, 170, 255);\n"
"color: white;\n"
"border-radius: 5px;\n"
"margin: 1px;"))
        self.weather3.setAlignment(QtCore.Qt.AlignCenter)
        self.weather3.setObjectName(_fromUtf8("weather3"))
        self.horizontalLayout_4.addWidget(self.weather3)
        self.weather4 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.weather4.setStyleSheet(_fromUtf8("background-color: rgb(85, 170, 255);\n"
"color: white;\n"
"border-radius: 5px;\n"
"margin: 1px;"))
        self.weather4.setAlignment(QtCore.Qt.AlignCenter)
        self.weather4.setObjectName(_fromUtf8("weather4"))
        self.horizontalLayout_4.addWidget(self.weather4)
        self.weather5 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.weather5.setStyleSheet(_fromUtf8("background-color: rgb(85, 170, 255);\n"
"color: white;\n"
"border-radius: 5px;\n"
"margin: 1px;"))
        self.weather5.setAlignment(QtCore.Qt.AlignCenter)
        self.weather5.setObjectName(_fromUtf8("weather5"))
        self.horizontalLayout_4.addWidget(self.weather5)
        self.weather6 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.weather6.setStyleSheet(_fromUtf8("background-color: rgb(85, 170, 255);\n"
"color: white;\n"
"border-radius: 5px;\n"
"margin: 1px;"))
        self.weather6.setAlignment(QtCore.Qt.AlignCenter)
        self.weather6.setObjectName(_fromUtf8("weather6"))
        self.horizontalLayout_4.addWidget(self.weather6)
        self.weather7 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.weather7.setStyleSheet(_fromUtf8("background-color: rgb(85, 170, 255);\n"
"color: white;\n"
"border-radius: 5px;\n"
"margin: 1px;"))
        self.weather7.setAlignment(QtCore.Qt.AlignCenter)
        self.weather7.setObjectName(_fromUtf8("weather7"))
        self.horizontalLayout_4.addWidget(self.weather7)
        self.weather8 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.weather8.setStyleSheet(_fromUtf8("background-color: rgb(85, 170, 255);\n"
"color: white;\n"
"border-radius: 5px;\n"
"margin: 1px;"))
        self.weather8.setAlignment(QtCore.Qt.AlignCenter)
        self.weather8.setObjectName(_fromUtf8("weather8"))
        self.horizontalLayout_4.addWidget(self.weather8)
        self.weather9 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.weather9.setStyleSheet(_fromUtf8("background-color: rgb(85, 170, 255);\n"
"color: white;\n"
"border-radius: 5px;\n"
"margin: 1px;"))
        self.weather9.setAlignment(QtCore.Qt.AlignCenter)
        self.weather9.setObjectName(_fromUtf8("weather9"))
        self.horizontalLayout_4.addWidget(self.weather9)
        self.weather10 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.weather10.setStyleSheet(_fromUtf8("background-color: rgb(85, 170, 255);\n"
"color: white;\n"
"border-radius: 5px;\n"
"margin: 1px;"))
        self.weather10.setAlignment(QtCore.Qt.AlignCenter)
        self.weather10.setObjectName(_fromUtf8("weather10"))
        self.horizontalLayout_4.addWidget(self.weather10)
        self.horizontalLayoutWidget_4 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 90, 801, 71))
        self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.WeatherButton = QtGui.QPushButton(self.horizontalLayoutWidget_4)
        self.WeatherButton.setDefault(False)
        self.WeatherButton.setFlat(False)
        self.WeatherButton.setObjectName(_fromUtf8("WeatherButton"))
        self.horizontalLayout_5.addWidget(self.WeatherButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.result = ''
        self.codes, self.dates, self.days, self.highs, self.lows, self.texts = [],[],[],[],[],[]
        self.home()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "City", None))
        self.label_2.setText(_translate("MainWindow", "Province/State/Country", None))
        self.weather1.setText(_translate("MainWindow", "Weather1", None))
        self.weather2.setText(_translate("MainWindow", "Weather2", None))
        self.weather3.setText(_translate("MainWindow", "Weather3", None))
        self.weather4.setText(_translate("MainWindow", "Weather4", None))
        self.weather5.setText(_translate("MainWindow", "Weather5", None))
        self.weather6.setText(_translate("MainWindow", "Weather6", None))
        self.weather7.setText(_translate("MainWindow", "Weather7", None))
        self.weather8.setText(_translate("MainWindow", "Weather8", None))
        self.weather9.setText(_translate("MainWindow", "Weather9", None))
        self.weather10.setText(_translate("MainWindow", "Weather10", None))
        self.WeatherButton.setText(_translate("MainWindow", "Show me the forecast", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))


    def home(self):
        self.WeatherButton.clicked.connect(self.showResults)

    def showResults(self):
        result = CalculateForecast.Weather.ShowMeTheWeather(CalculateForecast.Weather(), str(self.lineEdit.text()), str(self.lineEdit_2.text()))
        
        forecast = result["results"]["channel"]["item"]["forecast"]
        pprint (forecast)
        for day in range(len(forecast)):
            self.codes.append(forecast[day]["code"])
            self.dates.append(forecast[day]["date"])
            self.days.append(forecast[day]["day"])
            self.highs.append(forecast[day]["high"])
            self.lows.append(forecast[day]["low"])
            self.texts.append(forecast[day]["text"])

        self.weather1.setStyleSheet(_fromUtf8("font-size: 20px;\n"
            "color: white;\n"
            "border-radius: 5px;\n"
            "margin: 1px;\n"
            "background-color: rgb(85, 170, 255);"))    
        self.weather1.setText("Code: "+self.codes[0]+"\n"+"Date: "+self.dates[0]+"\n"+"Day: "+self.days[0]+"\n"+"High: "+self.highs[0]+"\n"+"Low: "+self.lows[0]+"\n"+"Weather: "+self.texts[0])
        self.weather2.setText(self.codes[1]+"\n"+self.dates[1]+"\n"+self.days[1]+"\n"+self.highs[1]+"\n"+self.lows[1]+"\n"+self.texts[1])
        self.weather3.setText(self.codes[2]+"\n"+self.dates[2]+"\n"+self.days[2]+"\n"+self.highs[2]+"\n"+self.lows[2]+"\n"+self.texts[2])
        self.weather4.setText(self.codes[3]+"\n"+self.dates[3]+"\n"+self.days[3]+"\n"+self.highs[3]+"\n"+self.lows[3]+"\n"+self.texts[3])
        self.weather5.setText(self.codes[4]+"\n"+self.dates[4]+"\n"+self.days[4]+"\n"+self.highs[4]+"\n"+self.lows[4]+"\n"+self.texts[4])
        self.weather6.setText(self.codes[5]+"\n"+self.dates[5]+"\n"+self.days[5]+"\n"+self.highs[5]+"\n"+self.lows[5]+"\n"+self.texts[5])
        self.weather7.setText(self.codes[6]+"\n"+self.dates[6]+"\n"+self.days[6]+"\n"+self.highs[6]+"\n"+self.lows[6]+"\n"+self.texts[6])
        self.weather8.setText(self.codes[7]+"\n"+self.dates[7]+"\n"+self.days[7]+"\n"+self.highs[7]+"\n"+self.lows[7]+"\n"+self.texts[7])
        self.weather9.setText(self.codes[8]+"\n"+self.dates[8]+"\n"+self.days[8]+"\n"+self.highs[8]+"\n"+self.lows[8]+"\n"+self.texts[8])
        self.weather10.setText(self.codes[9]+"\n"+self.dates[9]+"\n"+self.days[9]+"\n"+self.highs[9]+"\n"+self.lows[9]+"\n"+self.texts[9])



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

