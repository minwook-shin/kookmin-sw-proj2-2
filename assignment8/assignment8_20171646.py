from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout

from keypad2 import numPadList, operatorList, constantList, functionList
import calcFunctions
additionalconstantList=[
    "Second",
    "Minutes",
    "Hour",
    "Day"
]
additionalfunctionList=[
    "소수 판정",
    "^^2",
    "8진수",
    "16진수"
]
class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(25)

        # Button Creation and Placement
        numLayout = QGridLayout()
        opLayout = QGridLayout()
        constLayout = QGridLayout()
        funcLayout = QGridLayout()
        additionalcLayout= QGridLayout()
        additionalfLayout=QGridLayout()

        buttonGroups = {
            'num': {'buttons': numPadList, 'layout': numLayout, 'columns': 4},
            'op': {'buttons': operatorList, 'layout': opLayout, 'columns': 3},
            'constants': {'buttons': constantList, 'layout': constLayout, 'columns': 2},
            'functions': {'buttons': functionList, 'layout': funcLayout, 'columns': 2},
            'Additionalf': {'buttons': additionalfunctionList, 'layout': additionalfLayout, 'columns': 1},
            'Additionalc': {'buttons': additionalconstantList, 'layout': additionalcLayout, 'columns': 1}
        }

        for label in buttonGroups.keys():
            r = 0; c = 0
            buttonPad = buttonGroups[label]
            for btnText in buttonPad['buttons']:
                button = Button(btnText, self.buttonClicked)
                buttonPad['layout'].addWidget(button, r, c)
                c += 1
                if c >= buttonPad['columns']:
                    c = 0; r += 1

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)
        mainLayout.addLayout(numLayout, 1, 0)
        mainLayout.addLayout(opLayout, 1, 1)
        mainLayout.addLayout(constLayout, 2, 0)
        mainLayout.addLayout(funcLayout, 2, 1)
        mainLayout.addLayout(additionalcLayout, 3, 0)
        mainLayout.addLayout(additionalfLayout, 3, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")

        self.erasecount=0


    def buttonClicked(self):

        if self.display.text() == 'Error!':
            self.display.setText('')


        button = self.sender()
        key = button.text()

        if key == '=':
            try:
                result = str(eval(self.display.text()))
            except:
                result = 'Error!'
            self.display.setText(result)
            self.erasecount = 1


        elif key == 'C':
            self.display.clear()
        elif key == constantList[0]:
            self.display.setText('3.141592')
        elif key == constantList[1]:
            self.display.setText('3E+8')
        elif key == constantList[2]:
            self.display.setText('340')
        elif key == constantList[3]:
            self.display.setText('1.5E+8')
        elif key == functionList[0]:
            try:
                n = str(eval(self.display.text()))
                value = calcFunctions.factorial(n)
            except:
                value = 'Error!'
            self.display.setText(str(value))
        elif key == functionList[1]:
            n = self.display.text()
            value = calcFunctions.decToBin(n)
            self.display.setText(str(value))
        elif key == functionList[2]:
            n = self.display.text()
            value = calcFunctions.binToDec(n)
            self.display.setText(str(value))
        elif key == functionList[3]:
            n = self.display.text()
            value = calcFunctions.decToRoman(n)
            self.display.setText(str(value))
        elif key == additionalconstantList[0]:
            n = self.display.text()
            if n=='': value=1
            else: value = int(n)
            self.display.setText(str(value))
        elif key == additionalconstantList[1]:
            n = self.display.text()
            if n == '': value = 60
            value = int(n)*60
            self.display.setText(str(value))
        elif key == additionalconstantList[2]:
            n = self.display.text()
            if n == '': value = 3600
            else: value = int(n)*3600
            self.display.setText(str(value))
        elif key == additionalconstantList[3]:
            n = self.display.text()
            if n == '': value=60*3600
            else: value = int(n)*60*3600
            self.display.setText(str(value))
        elif key == additionalfunctionList[0]:
            n = self.display.text()
            try:
                a=int(n)
                value="yes"
                for i in range(2,a):
                    if a%i ==0:
                        value="no"
                        break
            except: value="Error!"
            self.display.setText(str(value))
            self.erasecount=1
        elif key == additionalfunctionList[1]:
            n = self.display.text()
            try: value=float(n)*float(n)
            except: value="Error!"
            self.display.setText(str(value))
        elif key == additionalfunctionList[2]:
            n = self.display.text()
            try: value=oct(int(n))
            except: value="Error!"
            self.display.setText(str(value))
        elif key == additionalfunctionList[3]:
            n = self.display.text()
            try: value=hex(int(n))
            except: value="Error!"

            self.display.setText(str(value))
        else:
            if self.erasecount == 1:
                self.erasecount = 0
                self.display.setText('')
            self.display.setText(self.display.text() + key)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
