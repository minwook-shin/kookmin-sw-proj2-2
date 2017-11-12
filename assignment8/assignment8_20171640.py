import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout
from math import factorial as fact

numPadList = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', '=',
]

operatorList = [
    '*', '/',
    '+', '-',
    '(', ')',
    'C',
]

constantList = [
    'pi',
    '빛의 이동 속도 (m/s)',
    '소리의 이동 속도 (m/s)',
    '태양과의 평균 거리 (km)',
    '상수 (e)',
]

functionList = [
    'factorial (!)',
    '-> binary',
    'binary -> dec',
    '-> roman',
]


def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r


def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r


def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r


def decToRoman(numStr):
    return 'dec -> Roman'


class Button(QToolButton):
    def __init__(self, text,call):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(call)

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
        self.display.setMaxLength(15)

        # Button Creation and Placement
        numLayout = QGridLayout()
        opLayout = QGridLayout()
        constLayout = QGridLayout()
        funcLayout = QGridLayout()

        buttonGroups = {
            'num': {'buttons': numPadList, 'layout': numLayout, 'columns': 3},
            'op': {'buttons': operatorList, 'layout': opLayout, 'columns': 2},
            'constants': {'buttons': constantList, 'layout': constLayout, 'columns': 1},
            'functions': {'buttons': functionList, 'layout': funcLayout, 'columns': 1},
        }

        for label in buttonGroups.keys():
            r = 0; c = 0
            buttonPad = buttonGroups[label]
            for btnText in buttonPad['buttons']:
                button = Button(btnText, self.button_clicked)
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
        self.setLayout(mainLayout)
        self.setWindowTitle("My Calculator")
        self.init = 0

    def button_clicked(self):
        if self.display.text() == 'Error!':
            self.display.setText('')
        if self.init == 0:
            self.display.setText("")
            self.init += 1
        button = self.sender()
        key = button.text()
        try:
            if key == '=':
                result = str(eval(self.display.text()))
                self.display.setText(result)
            elif key == 'C':
                self.display.setText('0')
                self.init = 0
            elif key == constantList[0]:
                self.display.setText(self.display.text() + '3.141592')
            elif key == constantList[1]:
                self.display.setText(self.display.text() + '3E+8')
            elif key == constantList[2]:
                self.display.setText(self.display.text() + '340')
            elif key == constantList[3]:
                self.display.setText(self.display.text() + '1.5E+8')
            elif key == constantList[4]:
                self.display.setText(self.display.text() + '2.71828')
            elif key == functionList[0]:
                n = self.display.text()
                value = factorial(n)
                self.display.setText(str(value))
            elif key == functionList[1]:
                n = self.display.text()
                value = decToBin(n)
                self.display.setText(str(value))
            elif key == functionList[2]:
                n = self.display.text()
                value = binToDec(n)
                self.display.setText(str(value))
            elif key == functionList[3]:
                n = self.display.text()
                value = decToRoman(n)
                self.display.setText(str(value))
            else:
                self.display.setText(self.display.text() + key)
        except:
            self.display.setText('Error!')
            calc.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
