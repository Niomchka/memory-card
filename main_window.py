from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QRadioButton, QGroupBox, QButtonGroup, QLabel

main_win = QWidget()


main_win.resize(800, 600)
main_win.setWindowTitle("Memory Card")

main_v_line = QVBoxLayout()

menu_btn = QPushButton("Меню.")
qestion_text = QLabel("Питання")

radio_box = QGroupBox("Варіанти Відповіді")

radio_group = QButtonGroup()

radio_btn_1 = QRadioButton("нянянян")
radio_btn_2 = QRadioButton("2")
radio_btn_3 = QRadioButton("Якась відповідь")
radio_btn_4 = QRadioButton("Ще щось")

radio_group.addButton(radio_btn_1)
radio_group.addButton(radio_btn_2)
radio_group.addButton(radio_btn_3)
radio_group.addButton(radio_btn_4)



box_v_line = QVBoxLayout()
box_h_line_1 = QHBoxLayout()
box_h_line_2 = QHBoxLayout()

box_h_line_1.addWidget(radio_btn_1)
box_h_line_1.addWidget(radio_btn_2)
box_h_line_2.addWidget(radio_btn_3)
box_h_line_2.addWidget(radio_btn_4)

box_v_line.addLayout(box_h_line_1)
box_v_line.addLayout(box_h_line_2)

radio_box.setLayout(box_v_line)

answer_box = QGroupBox()

answer_line = QVBoxLayout()

result_text = QLabel("dsfs")
correct_text = QLabel("текст правильної відповіді")

answer_line.addWidget(result_text)
answer_line.addWidget(correct_text)

answer_box.setLayout(answer_line)


next_btn = QPushButton("Відповісти")

main_v_line.addWidget(menu_btn)
main_v_line.addWidget(qestion_text)
main_v_line.addWidget(radio_box)
main_v_line.addWidget(answer_box)
main_v_line.addWidget(next_btn)

answer_box.hide()

main_win.setLayout(main_v_line)