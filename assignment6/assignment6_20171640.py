import pickle
import sys

from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication, QLabel,
                             QComboBox, QTextEdit, QLineEdit)


class ScoreDB(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):

        name_label = QLabel("Name:")
        self.name_line = QLineEdit()
        age_label = QLabel("Age:")
        self.age_line = QLineEdit()
        score_label = QLabel("Score:")
        self.score_line = QLineEdit()
        amount_label = QLabel("Amount:")
        self.amount_line = QLineEdit()
        key_label = QLabel("Key:")
        self.key_combo = QComboBox()
        self.key_combo.addItem("Name")
        self.key_combo.addItem("Age")
        self.key_combo.addItem("Score")
        add_button = QPushButton("Add")
        add_button.clicked.connect(self.add_clicked)
        del_button = QPushButton("Del")
        del_button.clicked.connect(self.del_clicked)
        find_button = QPushButton("Find")
        find_button.clicked.connect(self.find_clicked)
        inc_button = QPushButton("Inc")
        inc_button.clicked.connect(self.inc_clicked)
        show_button = QPushButton("Show")
        show_button.clicked.connect(self.show_clicked)
        result_label = QLabel("Result:")
        self.output = QTextEdit()

        h_box1 = QHBoxLayout()
        h_box2 = QHBoxLayout()
        h_box3 = QHBoxLayout()
        h_box4 = QHBoxLayout()
        h_box5 = QHBoxLayout()
        h_box1.addWidget(name_label)
        h_box1.addWidget(self.name_line)
        h_box1.addWidget(age_label)
        h_box1.addWidget(self.age_line)
        h_box1.addWidget(score_label)
        h_box1.addWidget(self.score_line)
        h_box2.addStretch()
        h_box2.addWidget(amount_label)
        h_box2.addWidget(self.amount_line)
        h_box2.addWidget(key_label)
        h_box2.addWidget(self.key_combo)
        h_box3.addStretch()
        h_box3.addWidget(add_button)
        h_box3.addWidget(del_button)
        h_box3.addWidget(find_button)
        h_box3.addWidget(inc_button)
        h_box3.addWidget(show_button)
        h_box4.addWidget(result_label)
        h_box5.addWidget(self.output)

        v_box = QVBoxLayout()
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box3)
        v_box.addLayout(h_box4)
        v_box.addLayout(h_box5)

        self.setLayout(v_box)
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

    def add_clicked(self):
        name = self.name_line.text()
        age = int(self.age_line.text())
        score = int(self.score_line.text())
        record = {'Name': name, 'Age': age, 'Score': score}
        self.scoredb += [record]
        self.showScoreDB()

    def del_clicked(self):
        del_name = self.name_line.text()
        self.scoredb[:] = [x for x in self.scoredb if x["Name"] != del_name]
        self.showScoreDB()

    def find_clicked(self):
        find_name = self.name_line.text()
        find_message = ""
        for x in self.scoredb:
            if x["Name"] == find_name:
                for y in sorted(x):
                    find_message += y + "=" + str(x[y]) + "\t"
                find_message += "\n"
        self.output.setText(find_message)

    def inc_clicked(self):
        inc_name = self.name_line.text()
        inc_score = int(self.amount_line.text())
        for x in self.scoredb:
            if x["Name"] == inc_name:
                x["Score"] += inc_score
        self.showScoreDB()

    def show_clicked(self):
        self.showScoreDB()

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
        key_sort = str(self.key_combo.currentText())
        show_message = ""
        key_sort = "Name" if not key_sort else key_sort

        for x in sorted(self.scoredb, key=lambda person: person[key_sort]):
            for y in sorted(x):
                show_message += y + "=" + str(x[y]) + "\t"
            show_message += "\n"
        self.output.setText(show_message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
