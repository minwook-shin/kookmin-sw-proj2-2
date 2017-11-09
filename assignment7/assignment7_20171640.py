import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout


class Button(QToolButton):
    def __init__(self, text):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.display = QLineEdit("0")
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)
        self.digitButton = [x for x in range(0, 10)]
        for i in range(0, 10):
            self.digitButton[int(i)] = Button(str(i))
            self.digitButton[int(i)].clicked.connect(self.button_clicked)
        self.decButton = Button('.')
        self.decButton.clicked.connect(self.button_clicked)
        self.eqButton = Button('=')
        self.eqButton.clicked.connect(self.button_clicked)
        self.mulButton = Button('*')
        self.mulButton.clicked.connect(self.button_clicked)
        self.divButton = Button('/')
        self.divButton.clicked.connect(self.button_clicked)
        self.addButton = Button('+')
        self.addButton.clicked.connect(self.button_clicked)
        self.subButton = Button('-')
        self.subButton.clicked.connect(self.button_clicked)
        self.lparButton = Button('(')
        self.lparButton.clicked.connect(self.button_clicked)
        self.rparButton = Button(')')
        self.rparButton.clicked.connect(self.button_clicked)
        self.clearButton = Button('C')
        self.clearButton.clicked.connect(self.button_clicked)
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addWidget(self.display, 0, 0, 1, 2)
        numLayout = QGridLayout()
        numLayout.addWidget(self.digitButton[0], 3, 0)
        num = 1
        for i in range(2, -1, -1):
            for j in range(0, 3):
                numLayout.addWidget(self.digitButton[int(num)], int(i), int(j))
                num += 1
        numLayout.addWidget(self.decButton, 3, 1)
        numLayout.addWidget(self.eqButton, 3, 2)
        mainLayout.addLayout(numLayout, 1, 0)
        opLayout = QGridLayout()
        opLayout.addWidget(self.mulButton, 0, 0)
        opLayout.addWidget(self.divButton, 0, 1)
        opLayout.addWidget(self.addButton, 1, 0)
        opLayout.addWidget(self.subButton, 1, 1)
        opLayout.addWidget(self.lparButton, 2, 0)
        opLayout.addWidget(self.rparButton, 2, 1)
        opLayout.addWidget(self.clearButton, 3, 0)
        mainLayout.addLayout(opLayout, 1, 1)
        self.setLayout(mainLayout)
        self.setWindowTitle("My Calculator")
        self.init = 0

    def button_clicked(self):
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
            else:
                self.display.setText(self.display.text() + key)
        except:
            calc.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
