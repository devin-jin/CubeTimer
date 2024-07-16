import time
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QListWidgetItem
import best

# 定时器逻辑类，负责定时器的启动、停止、重置以及时间的更新和历史记录的管理
class TimerLogic:
    def __init__(self):
        # 初始化开始时间、定时器状态和历史记录列表
        self.start_time = None
        self.timer_running = False
        self.history = []

        # 初始化定时器对象，并连接到更新时间的函数
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.ui = None

    # 设置用户界面对象
    def set_ui(self, ui):
        self.ui = ui

    # 切换定时器状态，启动或停止定时器
    def toggle_timer(self):
        if self.timer_running:
            self.stop_timer()
        else:
            self.start_timer()

    # 启动定时器，记录开始时间并启动定时器更新
    def start_timer(self):
        self.start_time = time.time()
        self.timer.start(10)  # 更新间隔为10毫秒
        self.ui.start_button.setText('停止')
        self.timer_running = True

    # 停止定时器，计算并记录流逝时间，更新历史记录
    def stop_timer(self):
        self.timer.stop()
        elapsed_time = time.time() - self.start_time
        self.history.append(elapsed_time)
        self.update_history_list()
        self.update_best()
        self.ui.start_button.setText('开始')
        self.timer_running = False

    # 重置定时器，清除当前时间，显示为0，并重置定时器状态和历史记录
    def reset_timer(self):
        self.timer.stop()
        self.start_time = None
        self.ui.time_label.setText('0.00 秒')
        self.ui.start_button.setText('开始')
        self.timer_running = False
        self.history = []
        self.update_history_list()

    # 更新当前时间显示，根据开始时间计算流逝时间并更新标签文本
    def update_time(self):
        if self.start_time is not None:
            elapsed_time = time.time() - self.start_time
            self.ui.time_label.setText(f'{elapsed_time:.2f} 秒')

    # 更新历史记录列表，清空当前列表并添加新的历史记录
    def update_history_list(self):
        self.ui.history_list.clear()
        for idx, time_val in enumerate(self.history):
            item = QListWidgetItem(f'#{idx + 1}: {time_val:.2f} 秒')
            self.ui.history_list.addItem(item)
    
    def update_best(self):
        bestTime = best.get_best_times(self.history)
        ao5 = best.get_ao5(self.history)
        self.ui.score_label.setText(f'{bestTime:.2f} 秒 {ao5:.2f} 秒')

    def prt(self):
        print(self.history)
        print(1)