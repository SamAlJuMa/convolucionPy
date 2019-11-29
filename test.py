from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton
from main import Ui_MainWindow
from conv import makeConv, perConv
import numpy as np
import sys
import matplotlib.pyplot as plt


def setX(center, sgnList):
    x = []
    for i in range(1, len(sgnList)+1):
        x.append((center-i)*-1)
    return x


def grafSgn(x, y):

    # setting the axes at the centre
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.set_xticks(x)

    # plot the function
    plt.stem(x, y)

    # show the plot
    plt.show()


class Dialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(Dialog, self).__init__(*args, **kwargs)
        self.setFixedSize(400, 200)


def createErrorMessage():
    d = QDialog()
    l1 = QLabel("Aún Faltan Datos", d)
    l1.move(50, 30)
    d.setWindowTitle("Dialog")
    d.exec_()


class mywindow(QtWidgets.QMainWindow):

    def __init__(self):

        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        with open("styles.css") as f:
            self.setStyleSheet(f.read())

        # connecting the clicked signal with btnClicked slot
        self.ui.textBtn.clicked.connect(self.getData)
        self.ui.textBtn_2.clicked.connect(self.getData2)
        self.ui.convBtn.clicked.connect(self.convFinita)
        self.ui.convBtn_2.clicked.connect(self.convPer)
        self.ui.convBtn_3.clicked.connect(self.convCir)

    def getData(self):
        # Obtener muestras y centro
        sgnString = self.ui.sgn.toPlainText()
        center = self.ui.centerText.text()

        if (sgnString == "" or center == ""):
            createErrorMessage()

        else:
            # Casteo de variables
            sgnString = str(sgnString)
            center = int(str(center))

            # Convertir muestras a lista de python
            sgnList = sgnString.split(",")
            for i in range(len(sgnList)):
                sgnList[i] = float(eval(sgnList[i]))

            if(self.ui.per1.isChecked()):
                center = len(sgnList)+center
                sgnList = sgnList+sgnList+sgnList

            # Definir eje x
            x = setX(center, sgnList)

            # Graficar
            grafSgn(x, sgnList)

    def getData2(self):
        # Obtener muestras y centro
        sgnString = self.ui.sgn_2.toPlainText()
        center = self.ui.centerText_2.text()

        if (sgnString == "" or center == ""):
            createErrorMessage()

        else:
            # Casteo de variables
            sgnString = str(sgnString)
            center = int(str(center))

            # Convertir muestras a lista de python
            sgnList = sgnString.split(",")
            for i in range(len(sgnList)):
                sgnList[i] = float(eval(sgnList[i]))

            if(self.ui.per2.isChecked()):
                center = len(sgnList)+center
                sgnList = sgnList+sgnList+sgnList

            # Definir eje x
            x = setX(center, sgnList)

            # Graficar
            grafSgn(x, sgnList)

    def convFinita(self):
        sgn1String = self.ui.sgn.toPlainText()
        sgn2String = self.ui.sgn_2.toPlainText()

        sgn1String = str(sgn1String)
        sgn2String = str(sgn2String)

        center1 = self.ui.centerText.text()
        center2 = self.ui.centerText_2.text()

        if (sgn1String == "" or sgn2String == "" or center1 == "" or center2 == ""):
            createErrorMessage()
        else:
            center1 = int(str(center1))
            center2 = int(str(center2))
            center = center1+center2-1
            sgn1List = sgn1String.split(",")
            sgn2List = sgn2String.split(",")

            for i in range(len(sgn1List)):
                sgn1List[i] = float(eval(sgn1List[i]))

            for i in range(len(sgn2List)):
                sgn2List[i] = float(eval(sgn2List[i]))

            convSgn = makeConv(sgn1List, sgn2List)
            x = setX(center, convSgn)

            self.ui.sgn_3.setText(str(convSgn))
            self.ui.posCent.setText(str(center))
            self.ui.ePosCent.setText(str(convSgn[center-1]))
            grafSgn(x, convSgn)

    def convPer(self):
        sgn1String = self.ui.sgn.toPlainText()
        sgn2String = self.ui.sgn_2.toPlainText()

        sgn1String = str(sgn1String)
        sgn2String = str(sgn2String)

        center1 = self.ui.centerText.text()
        center2 = self.ui.centerText_2.text()

        if (sgn1String == "" or sgn2String == "" or center1 == "" or center2 == ""):
            createErrorMessage()
        elif(self.ui.per2.isChecked() or self.ui.per1.isChecked()):
            sgn1List = sgn1String.split(",")
            sgn2List = sgn2String.split(",")

            center1 = int(str(center1))
            center2 = int(str(center2))
            center = center1+center2-1

            for i in range(len(sgn1List)):
                sgn1List[i] = float(eval(sgn1List[i]))

            for i in range(len(sgn2List)):
                sgn2List[i] = float(eval(sgn2List[i]))

            sgnPer = []
            sgnFin = []
            if(self.ui.per1.isChecked()):
                sgnPer = sgn1List
                sgnFin = sgn2List
            elif(self.ui.per2.isChecked()):
                sgnPer = sgn2List
                sgnFin = sgn1List

            convSgn = perConv(sgnPer, sgnFin)
            center = center+len(convSgn)
            convSgn = convSgn+convSgn+convSgn
            x = setX(center, convSgn)
            self.ui.sgn_3.setText(str(convSgn))
            self.ui.posCent.setText(str(center))
            self.ui.ePosCent.setText(str(convSgn[center-1]))
            grafSgn(x, convSgn)

    def convCir(self):
        sgn1String = self.ui.sgn.toPlainText()
        sgn2String = self.ui.sgn_2.toPlainText()

        sgn1String = str(sgn1String)
        sgn2String = str(sgn2String)

        center1 = self.ui.centerText.text()
        center2 = self.ui.centerText_2.text()

        if (sgn1String == "" or sgn2String == "" or center1 == "" or center2 == ""):
            createErrorMessage()

        else:
            sgn1List = sgn1String.split(",")
            sgn2List = sgn2String.split(",")

            center1 = int(str(center1))
            center2 = int(str(center2))
            center = center1+center2-1

            for i in range(len(sgn1List)):
                sgn1List[i] = float(eval(sgn1List[i]))

            for i in range(len(sgn2List)):
                sgn2List[i] = float(eval(sgn2List[i]))

            if len(sgn1List) >= len(sgn2List):
                convSgn = perConv(sgn1List, sgn2List)
            else:
                convSgn = perConv(sgn2List, sgn1List)
            center = center+len(convSgn)
            convSgn = convSgn+convSgn+convSgn
            x = setX(center, convSgn)
            self.ui.sgn_3.setText(str(convSgn))
            self.ui.posCent.setText(str(center))
            self.ui.ePosCent.setText(str(convSgn[center-1]))
            grafSgn(x, convSgn)


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
