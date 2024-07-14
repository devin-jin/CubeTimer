import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QListWidget, QListWidgetItem
from PyQt5.QtCore import QTimer, Qt

class TimerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.start_time = None
        self.timer_running = False
        self.history = []

    def initUI(self):
        self.setWindowTitle('计时器')
        self.setGeometry(800, 800, 800, 800)

        main_layout = QVBoxLayout()
        main_layout.setSpacing(20)  # 设置垂直间隔

        # 时间显示部分
        self.time_label = QLabel('0.00 秒', self)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 100px;")
        main_layout.addWidget(self.time_label, alignment=Qt.AlignCenter)

        # 按钮布局
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)  # 设置水平间隔

        self.start_button = QPushButton('开始', self)
        self.start_button.clicked.connect(self.toggle_timer)
        button_layout.addWidget(self.start_button)

        self.reset_button = QPushButton('重置', self)
        self.reset_button.clicked.connect(self.reset_timer)
        button_layout.addWidget(self.reset_button)

        main_layout.addLayout(button_layout)

        # 历史记录部分
        self.history_list = QListWidget(self)
        main_layout.addWidget(self.history_list)

        self.setLayout(main_layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TimerApp()
    ex.show()
    sys.exit(app.exec_())
