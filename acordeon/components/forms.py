# -*- coding: latin-1 -*-

from PyQt4.QtGui import QMainWindow, \
    QWidget, QApplication, QLineEdit, QPushButton


class Form(QMainWindow):
    def __init__(self, width=None, height=None, title=None, width_fixed=False):
        super(Form, self).__init__()
        if width is None:
            width = 400
        if height is None:
            height = 600
        self.width_container, self.height_container = width / 2, height
        self.setMinimumSize(width, height)
        if width_fixed:
            self.setMaximumSize(width, height)
        self.setWindowTitle(title)
        # self.center_main_window()

    def center_main_window(self):
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def create_form_gui(self,  id_name):
        self.form_container = QWidget(self)
        self.w = (self.width() - self.width_container) / 2
        self.h = (self.height() - self.height_container) / 2
        self.form_container.setGeometry(self.w, self.h, self.width_container, self.height_container)
        self.form_container.setObjectName(id_name)
    
    def add_input_field(self, name_field, init_x, init_y, width_field, height_field):
        self.input_field = QLineEdit(self.form_container)
        self.spaces_between_fields = 40
        self.init_x, self.init_y = self.spaces_between_fields / 2, 20
        self.width_field, self.height_field = width_field, height_field
        self.input_field.setGeometry(init_x, init_y, self.width_field, self.height_field)
        self.input_field.setPlaceholderText(name_field)

    def add_password_field(self, name_field, init_x, init_y, width_field, height_field):
        self.password_field = QLineEdit(self.form_container)
        self.password_field.setEchoMode(QLineEdit.Password)
        self.spaces_between_fields = 40
        self.init_x, self.init_y = self.spaces_between_fields / 2, 20
        self.width_field, self.height_field = width_field, height_field
        self.password_field.setGeometry(init_x, init_y, self.width_field, self.height_field)
        self.password_field.setPlaceholderText(name_field)

    def add_submit(self, name_field, pos_x, pos_y, width, height):
        self.button_submit = QPushButton(self.form_container)
        self.button_submit.setGeometry(pos_x, pos_y, width, height)
        self.button_submit.setText(name_field)

    def center_widget_form(self):
        self.width_center_form = (self.width() - (self.width_container * 2)) / 2
        self.height_center_form = (self.height() - self.height_container) / 2
        self.form_container.setGeometry(self.width_center_form, self.height_center_form, self.width_container * 2, self.height_container)

    def resizeEvent(self, event):
        self.center_widget_form()

