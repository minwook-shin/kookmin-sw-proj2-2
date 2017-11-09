from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout
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

        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        self.erasecount=0

        self.digitButton = []
        for i in range(10):
            self.digitButton.append(Button(str(i),self.Buttonclicked))
        self.decButton = Button('.',self.Buttonclicked)
        self.eqButton = Button('=',self.Buttonclicked)
        self.mulButton = Button('*',self.Buttonclicked)
        self.divButton = Button('/',self.Buttonclicked)
        self.addButton = Button('+',self.Buttonclicked)
        self.subButton = Button('-',self.Buttonclicked)
        self.lparButton = Button('(',self.Buttonclicked)
        self.rparButton = Button(')',self.Buttonclicked)
        self.clearButton = Button('C',self.Buttonclicked)

        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)

        numLayout = QGridLayout()
        count=1

        for i in range(2,-1,-1):
            for j in range(3):
                numLayout.addWidget(self.digitButton[count],i,j)
                count+=1

        numLayout.addWidget(self.digitButton[0], 3, 0)
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
    def Buttonclicked(self):
        try:
            button =self.sender()
            key= button.text()
            if self.erasecount==1:
                self.display.setText("")
                self.erasecount=0
            if key == "=":
                result = str(eval(self.display.text()))
                self.display.setText(result)
                self.erasecount=1
            elif key== "C":
                self.display.setText("")
            else:
                self.display.setText(self.display.text() +key)
        except:
            self.display.setText(self.display.text())


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
