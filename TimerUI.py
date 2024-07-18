from PyQt5.QtWidgets import  QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QListWidget,QTableView
from PyQt5.QtCore import Qt


class TimerUI(QWidget):
    def __init__(self, logic):
        super().__init__()

        self.logic = logic
        self.initUI()

    def initUI(self):
        self.setWindowTitle('计时器')
        self.setGeometry(200, 100, 1000,1000)

        main_layout = QHBoxLayout()
        main_layout.setSpacing(10)  # 设置垂直间隔

        show_layout = QVBoxLayout()
        show_layout.setSpacing(10)  # 设置垂直间隔

        # 时间显示部分
        self.time_label = QLabel('0.00', self)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 150px;")
        show_layout.addWidget(self.time_label, alignment=Qt.AlignCenter)

        # 按钮布局
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)  # 设置水平间隔

        self.start_button = QPushButton('开始', self)
        self.start_button.clicked.connect(self.logic.toggle_timer)
        self.start_button.setStyleSheet("font-size: 30px;")
        button_layout.addWidget(self.start_button)

        self.reset_button = QPushButton('重置', self)
        self.reset_button.clicked.connect(self.logic.reset_timer)
        self.reset_button.setStyleSheet("font-size: 30px;")
        button_layout.addWidget(self.reset_button)

        show_layout.addLayout(button_layout)

        self.score_label = QLabel('best: NaN    ao5: NaN    ao12: NaN', self)
        self.score_label.setAlignment(Qt.AlignCenter)
        self.score_label.setStyleSheet("font-size: 20px;")
        show_layout.addWidget(self.score_label, alignment=Qt.AlignCenter)

        self.table = QTableView()
        self.table.setStyleSheet("font-size: 20px;")
        show_layout.addWidget(self.table, alignment=Qt.AlignCenter)

        main_layout.addLayout(show_layout)
        


        # 历史记录部分
        self.history_list = QListWidget(self)
        main_layout.addWidget(self.history_list)
        self.history_list.setStyleSheet("font-size: 30px;")
        self.setLayout(main_layout)


