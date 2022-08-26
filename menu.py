from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout
from intstr import *



app = QApplication([])


main_win = QWidget()
main_win.resize(win_width,win_height)
main_win.setWindowTitle(title_txt)
text1 = QLabel(txt)
text = QLabel(description)
button = QPushButton(btn1)

v_line = QVBoxLayout()
v_line.addWidget(text1, alignment=Qt.AlignLeft)
v_line.addWidget(text, alignment=Qt.AlignCenter) 
v_line.addWidget(button, alignment=Qt.AlignCenter)                  
main_win.setLayout(v_line)
main_win.show()
app.exec_()
