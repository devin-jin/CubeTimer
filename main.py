import sys
import time
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

    def toggle_timer(self):
        if self.timer_running:
            self.stop_timer()
        else:
            self.start_timer()

    def start_timer(self):
        self.start_time = time.time()
        self.timer.start(10)  # 更新间隔为10毫秒
        self.start_button.setText('停止')
        self.timer_running = True

    def stop_timer(self):
        self.timer.stop()
        elapsed_time = time.time() - self.start_time
        self.history.append(elapsed_time)
        self.update_history_list()
        self.start_button.setText('开始')
        self.timer_running = False

    def reset_timer(self):
        self.timer.stop()
        self.start_time = None
        self.time_label.setText('0.00 秒')
        self.start_button.setText('开始')
        self.timer_running = False
        self.history = []
        self.update_history_list()

    def update_time(self):
        if self.start_time is not None:
            elapsed_time = time.time() - self.start_time
            self.time_label.setText(f'{elapsed_time:.2f} 秒')

    def update_history_list(self):
        self.history_list.clear()
        for idx, time_val in enumerate(self.history):
            item = QListWidgetItem(f'#{idx + 1}: {time_val:.2f} 秒')
            self.history_list.addItem(item)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.toggle_timer()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TimerApp()
    ex.show()
    sys.exit(app.exec_())
