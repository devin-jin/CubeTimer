import time
from PyQt5.QtCore import QTimer 
from PyQt5.QtWidgets import QListWidgetItem


class TimerLogic:
    def __init__(self):
        self.start_time = None
        self.timer_running = False
        self.history = []

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.ui = None

    def set_ui(self, ui):
        self.ui = ui

    def toggle_timer(self):
        if self.timer_running:
            self.stop_timer()
        else:
            self.start_timer()

    def start_timer(self):
        self.start_time = time.time()
        self.timer.start(10)  # 更新间隔为10毫秒
        self.ui.start_button.setText('停止')
        self.timer_running = True

    def stop_timer(self):
        self.timer.stop()
        elapsed_time = time.time() - self.start_time
        self.history.append(elapsed_time)
        self.update_history_list()
        self.ui.start_button.setText('开始')
        self.timer_running = False

    def reset_timer(self):
        self.timer.stop()
        self.start_time = None
        self.ui.time_label.setText('0.00 秒')
        self.ui.start_button.setText('开始')
        self.timer_running = False
        self.history = []
        self.update_history_list()

    def update_time(self):
        if self.start_time is not None:
            elapsed_time = time.time() - self.start_time
            self.ui.time_label.setText(f'{elapsed_time:.2f} 秒')

    def update_history_list(self):
        self.ui.history_list.clear()
        for idx, time_val in enumerate(self.history):
            item = QListWidgetItem(f'#{idx + 1}: {time_val:.2f} 秒')
            self.ui.history_list.addItem(item)
