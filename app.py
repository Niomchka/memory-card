from PyQt6.QtWidgets import QApplication
from random import choice, shuffle


app = QApplication([])

from main_window import *
from menu_window import *

class Question():
    def __init__(self, text, answer, wrong1, wrong2, wrong3):
        self.text = text
        self.answer = answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

        self.actual = True
        self.count_asked = 0
        self.count_correct = 0

    def got_right(self):
        self.count_asked += 1
        self.count_correct += 1
    def got_wrong(self):
        self.count_asked += 1

q1 = Question('Яблуко', 'apple', 'application', 'pineapple', 'apply')
q2 = Question('Дім', 'house', 'horse', 'hurry', 'hour')
q3 = Question('Миша', 'mouse', 'malus', 'muse', 'museum')
q4 = Question('Число', 'number', 'digit', 'amount', 'summary')
q5 = Question("Ключі", "keys", "kind", "king", "kiss")
q6 = Question("Квітка", "flower", "face", "fail", "fall")

qestion_list = [q1, q2, q3, q4, q5, q6]

current_qestion = None
radio_list = [radio_btn_1, radio_btn_2, radio_btn_3, radio_btn_4]


def new_question():
    global current_qestion
    current_qestion = choice(qestion_list)

    qestion_text.setText(current_qestion.text)

    shuffle(radio_list)
    radio_list[0].setText(current_qestion.answer)
    radio_list[1].setText(current_qestion.wrong1)
    radio_list[2].setText(current_qestion.wrong2)
    radio_list[3].setText(current_qestion.wrong3)
new_question()



def check_result():
    if radio_list[0].isChecked():
        result_text.setText("Правильно")
    else:
        result_text.setText("Неправильно")

    radio_group.setExclusive(False)
    for btn in radio_list:
        btn.setChecked(False)
    radio_group.setExclusive(True)

def change_box():
    correct_text.setText(radio_list[0].text())
    if next_btn.text() == "Відповісти":
        radio_box.hide()
        answer_box.show()
        next_btn.setText("Наступне питання")
        check_result()
    elif next_btn.text() == "Наступне питання":
        radio_box.show()
        answer_box.hide()
        next_btn.setText("Відповісти")
        new_question()

next_btn.clicked.connect(change_box)

def show_menu():
    main_win.hide()
    menu_win.show()

menu_btn.clicked.connect(show_menu)

def hide_menu():
    main_win.show()
    menu_win.hide()

menu_back_btn.clicked.connect(hide_menu)

def add_qestion():
    new_text = menu_qestion_edit.text()
    new_answer = menu_answer_edit.text()
    new_wrong_1 = menu_wrong1_answer_edit.text()
    new_wrong_2 = menu_wrong2_answer_edit.text()
    new_wrong_3 = menu_wrong3_answer_edit.text()

    new_q = Question(new_text, new_answer, new_wrong_1, new_wrong_2, new_wrong_3)

    qestion_list.append(new_q)
    clear_menu()

menu_add_qestion_btn.clicked.connect(add_qestion)

def clear_menu():
    menu_qestion_edit.clear()
    menu_answer_edit.clear()
    menu_wrong1_answer_edit.clear()
    menu_wrong2_answer_edit.clear()
    menu_wrong3_answer_edit.clear()

menu_clear_btn.clicked.connect(clear_menu)

main_win.show()
app.exec()