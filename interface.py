from main import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(481, 293)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleCB = QtWidgets.QCheckBox(self.centralwidget)
        self.titleCB.setGeometry(QtCore.QRect(50, 40, 82, 23))
        self.titleCB.setObjectName("titleCB")
        self.noteCB = QtWidgets.QCheckBox(self.centralwidget)
        self.noteCB.setGeometry(QtCore.QRect(200, 40, 82, 23))
        self.noteCB.setObjectName("noteCB")
        self.genreCB = QtWidgets.QCheckBox(self.centralwidget)
        self.genreCB.setGeometry(QtCore.QRect(340, 40, 82, 23))
        self.genreCB.setObjectName("genreCB")
        self.castingCB = QtWidgets.QCheckBox(self.centralwidget)
        self.castingCB.setGeometry(QtCore.QRect(260, 80, 82, 21))
        self.castingCB.setObjectName("castingCB")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 121, 17))
        self.label.setObjectName("label")
        self.jaroCB = QtWidgets.QCheckBox(self.centralwidget)
        self.jaroCB.setGeometry(QtCore.QRect(40, 150, 82, 23))
        self.jaroCB.setObjectName("jaroCB")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 161, 17))
        self.label_2.setObjectName("label_2")
        self.keyCB = QtWidgets.QCheckBox(self.centralwidget)
        self.keyCB.setGeometry(QtCore.QRect(90, 80, 82, 23))
        self.keyCB.setObjectName("keyCB")
        self.levCB = QtWidgets.QCheckBox(self.centralwidget)
        self.levCB.setGeometry(QtCore.QRect(140, 150, 101, 23))
        self.levCB.setObjectName("levCB")
        self.ngramCB = QtWidgets.QCheckBox(self.centralwidget)
        self.ngramCB.setGeometry(QtCore.QRect(260, 150, 82, 23))
        self.ngramCB.setObjectName("ngramCB")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 180, 181, 17))
        self.label_3.setObjectName("label_3")
        self.jaroPond = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.jaroPond.setGeometry(QtCore.QRect(40, 200, 62, 26))
        self.jaroPond.setObjectName("jaroPond")
        self.levPond = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.levPond.setGeometry(QtCore.QRect(140, 200, 62, 26))
        self.levPond.setObjectName("levPond")
        self.ngramPond = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.ngramPond.setGeometry(QtCore.QRect(250, 200, 62, 26))
        self.ngramPond.setObjectName("ngramPond")
        self.nSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.nSpinBox.setGeometry(QtCore.QRect(330, 150, 45, 26))
        self.nSpinBox.setObjectName("nSpinBox")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(330, 240, 80, 25))
        self.submit.setObjectName("submit")
        self.titleCB.raise_()
        self.noteCB.raise_()
        self.genreCB.raise_()
        self.castingCB.raise_()
        self.label.raise_()
        self.jaroCB.raise_()
        self.label_2.raise_()
        self.keyCB.raise_()
        self.ngramCB.raise_()
        self.levCB.raise_()
        self.label_3.raise_()
        self.jaroPond.raise_()
        self.levPond.raise_()
        self.ngramPond.raise_()
        self.nSpinBox.raise_()
        self.submit.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titleCB.setText(_translate("MainWindow", "Title"))
        self.noteCB.setText(_translate("MainWindow", "Note"))
        self.genreCB.setText(_translate("MainWindow", "Genre"))
        self.castingCB.setText(_translate("MainWindow", "Casting"))
        self.keyCB.setText(_translate("MainWindow", "Key"))
        self.propertyCBlist = []
        self.propertyCBlist.append(self.titleCB)
        self.propertyCBlist.append(self.noteCB)
        self.propertyCBlist.append(self.genreCB)
        self.propertyCBlist.append(self.castingCB)
        self.propertyCBlist.append(self.keyCB)
        self.label.setText(_translate("MainWindow", "Choose a property"))
        self.jaroCB.setText(_translate("MainWindow", "Jaro"))
        self.label_2.setText(_translate("MainWindow", "Choose a similarity mesure "))
        self.levCB.setText(_translate("MainWindow", "Levenshtein"))
        self.ngramCB.setText(_translate("MainWindow", "Jaccard"))
        self.label_3.setText(_translate("MainWindow", "Choose a ponderation"))
        self.similarityCBlist = []
        self.similarityCBlist.append(self.jaroCB)
        self.similarityCBlist.append(self.levCB)
        self.similarityCBlist.append(self.ngramCB)
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.submit.clicked.connect(self.start)

    def getChoosenProperties(self):
        chosenProperties = []
        for cb in self.propertyCBlist:
            if cb.isChecked():
                chosenProperties.append(cb.text())
        return chosenProperties

    def getPonderation(self, methodeName):
        if methodeName == "Levenshtein":
            return round(self.levPond.value(), 3)
        elif methodeName == "Jaro":
            return round(self.jaroPond.value(), 3)
        elif methodeName == "Jaccard":
            return round(self.ngramPond.value(), 3)

    def getChoosenSimilarityMethod(self):
        choosenSimilarityMethod = []
        for cb in self.similarityCBlist:
            if cb.isChecked():
                choosenSimilarityMethod.append("{}:{}".format(cb.text(), self.getPonderation(cb.text())))
        return choosenSimilarityMethod

    def start(self):

        list = self.getChoosenProperties()
        seuil = round(self.nSpinBox.value(), 3)
        lists = self.getChoosenSimilarityMethod()
        for i in self.getChoosenProperties():
            if "Note" == i:
                function_has_note(lists, seuil)
            elif "Title" == i:
                function_has_title(lists, seuil)
            elif "Key" == i:
                function_has_key(lists, seuil)
            elif "Genre" == i:
                function_has_genre(lists, seuil)
            elif "Casting" == i:
                function_has_casting(lists)
            else:
                print("unknown property")
            print(self.getChoosenSimilarityMethod())
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())