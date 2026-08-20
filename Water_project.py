import sys

from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout)

from PyQt5.QtCore import Qt

class HabitApp(QWidget):
    def __init__(self):
        super().__init__()

        self.water_label = QLabel("Enter amount of water you drank (cups): ", self)
        self.water_amount_input = QLineEdit(self)
        self.advice_button = QPushButton("Get advice", self)
        self.emoji_label = QLabel("💧😊 ")
        self.description_label = QLabel("Getting hydrated enough?")
        self.advice_button.clicked.connect(self.give_advice)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Habit Tracker")
        self.setGeometry(700, 300, 400, 300)

        vbox = QVBoxLayout( )
        vbox.addWidget(self.water_label)
        vbox.addWidget(self.water_amount_input)
        vbox.addWidget(self.advice_button)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.water_label.setAlignment(Qt.AlignCenter)
        self.water_amount_input.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.water_label.setObjectName("water_label")
        self.water_amount_input.setObjectName("water_amount_input")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
        self.advice_button.setObjectName("advice_button")

        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: calibri;          
            }
            QLabel#water_label{
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#water_amount_input{
                font-size: 40px;
            }
            QLabel#emoji_label{
                font-size: 65px;
                font-family: Segoe UI emoji;
            }
            QLabel#description_label{
                font-size: 35px;
                font-family: calibri;
            }
            QPushButton#advice_button{
                font-size: 35px;
                font-weight: bold;
            }
        """)

    def give_advice(self):
        text = self.water_amount_input.text()

        try:
            amount = float(text)

        except ValueError:
            self.emoji_label.setText("⚠️")
            self.description_label.setText("Please enter a valid number!")
            return

        if amount <= 4:
            self.emoji_label.setText("😞")
            self.description_label.setText("Please drink more water!")
        elif amount <= 9:
            self.emoji_label.setText("😄")
            self.description_label.setText("You're doing great, keep it up!")
        elif amount > 10:
            self.emoji_label.setText("😳")
            self.description_label.setText("Chill out dude too much hydration")

        self.water_amount_input.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Habit_app = HabitApp()
    Habit_app.show()
    sys.exit(app.exec_())