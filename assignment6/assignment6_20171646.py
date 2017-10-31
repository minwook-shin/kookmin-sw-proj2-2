import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication, QLabel,
                             QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    def __init__(self):
        super().__init__()

        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()
        self.initUI()

    def initUI(self):
        namelabel = QLabel("Name:")
        self.editname = QLineEdit(self)
        agelabel = QLabel("Age:")
        self.editage = QLineEdit()
        scorelabel = QLabel("Score:", self)
        self.editscore = QLineEdit()
        amountlabel = QLabel("Amount:", self)
        self.editamount = QLineEdit()
        keylabel = QLabel("Key:")
        self.keycombo = QComboBox()
        self.keycombo.addItem("Age")
        self.keycombo.addItem("Score")
        addbutton = QPushButton("Add")
        delbutton = QPushButton("Del")
        findbutton = QPushButton("Find")
        incbutton = QPushButton("Inc")
        showbutton = QPushButton("Show")
        self.texts = QTextEdit(self)
        list = self.scoredb
        self.texts.setText(self.listtostring(list))
        self.keycombo.activated[str].connect(self.buttonClicked)

        hbox = QHBoxLayout()
        hbox.addWidget(namelabel)
        hbox.addWidget(self.editname)
        hbox.addWidget(agelabel)
        hbox.addWidget(self.editage)
        hbox.addWidget(scorelabel)
        hbox.addWidget(self.editscore)
        hbox.addWidget(amountlabel)
        hbox.addWidget(self.editamount)
        hbox.addWidget(keylabel)
        hbox.addWidget(self.keycombo)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(addbutton)
        hbox2.addWidget(delbutton)
        hbox2.addWidget(findbutton)
        hbox2.addWidget(incbutton)
        hbox2.addWidget(showbutton)
        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.texts)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        self.setLayout(vbox)

        addbutton.clicked.connect(self.buttonClicked)
        delbutton.clicked.connect(self.buttonClicked)
        findbutton.clicked.connect(self.buttonClicked)
        incbutton.clicked.connect(self.buttonClicked)
        showbutton.clicked.connect(self.buttonClicked)

        self.setGeometry(300, 300, 1000, 300)
        self.setWindowTitle('Assignment6')
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        name = self.editname.text()
        age = self.editage.text()
        score = self.editscore.text()
        amount = self.editamount.text()
        text = self.texts
        if sender.text() == "Add":
            self.scoredb.append({"Name": name, "Age": age, "Score": score})
            self.writeScoreDB()
            self.texts.setText(self.listtostring(self.scoredb))
        elif sender.text() == "Del":
            for p in self.scoredb:
                if p["Name"] == name:
                    self.scoredb.remove(p)
            self.writeScoreDB()
            self.texts.setText(self.listtostring(self.scoredb))
        elif sender.text() == "Find":
            s = ""
            for p in self.scoredb:
                if p["Name"] == name:
                    for j in p:
                        s += j + " = " + str(p[j]) + "   "
                    s += "\n"
            self.texts.setText(s)
        elif sender.text() == "Inc":
            for p in self.scoredb:
                if p["Name"] == name:
                    p["Score"] += int(amount)
                    count=1
            if count==1:
                self.writeScoreDB()
                self.texts.setText(self.listtostring(self.scoredb))
        elif sender.text() == "Show":
            s = ""
            keyname = self.keycombo.currentText()
            for p in sorted(self.scoredb, key=lambda x: x[keyname]):
                for j in p:
                    s += str(j) + "=" + str(p[j]) + "\t"
                s += "\n"
            self.texts.setText(s)

    def listtostring(self, list):
        s = ""
        for i in range(len(list)):
            for p in list[i]:
                s += p + " = " + str(list[i][p]) + "\t"
            s += "\n"
        return s

    def closeEvent(self, event):

        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb = pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
