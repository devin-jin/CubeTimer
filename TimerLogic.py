import time
from PyQt5.QtCore import QTimer,Qt
from PyQt5.QtWidgets import QListWidgetItem
from history import history
from dfQt import PandasModel

# 定时器逻辑类，负责定时器的启动、停止、重置以及时间的更新和历史记录的管理
class TimerLogic:
    def __init__(self):
        # 初始化开始时间、定时器状态和历史记录列表
        self.start_time = None
        self.timer_running = False

        # 初始化定时器对象，并连接到更新时间的函数
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.ui = None
        self.history = history()

    # 设置用户界面对象
    def num2str(self,num):
        return f"{num:.2f}"
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
        self.timer.start(1)  # 更新间隔为1毫秒
        self.ui.start_button.setText('停止')
        self.timer_running = True

    # 停止定时器，计算并记录流逝时间，更新历史记录
    def stop_timer(self):
        self.timer.stop()
        elapsed_time = time.time() - self.start_time
        self.update(elapsed_time)
        self.ui.start_button.setText('开始')
        self.timer_running = False

    # 重置定时器，清除当前时间，显示为0，并重置定时器状态和历史记录
    def reset_timer(self):
        self.timer.stop()
        self.start_time = 0
        self.ui.time_label.setText(self.num2str(self.start_time))
        self.ui.start_button.setText('开始')
        self.timer_running = False
        self.history.clr()

    # 更新当前时间显示，根据开始时间计算流逝时间并更新标签文本
    def update_time(self):
        if self.start_time is not None:
            elapsed_time = time.time() - self.start_time
            self.ui.time_label.setText(self.num2str(elapsed_time))
    def update(self,time):
        self.update_history(time)
        self.update_best()
        self.update_gragh()
    def update_best(self):
        strBest="best:"+self.num2str(self.history.best(0))+"\nao5:"+self.num2str(self.history.best(1))+"\nao12:"+self.num2str(self.history.best(2))
        self.ui.best_label.setText(strBest)
    # 更新历史记录列表，清空当前列表并添加新的历史记录
    def update_history(self,time):
        self.history.append(time)
        self.history.updateDf()
        self.model=PandasModel(self.history.df_h)
        self.ui.table.setModel(self.model)

    def update_gragh(self):
        self.ui.graph_canvas.plot(self.history.df_h.time)
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.logic.toggle_timer()

    

