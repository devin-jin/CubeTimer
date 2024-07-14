
import time
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QListWidget, QListWidgetItem
from PyQt5.QtCore import QTimer, Qt

def toggle_timer(timer):
    if timer.timer_running:
        timer.stop_timer()
    else:
        timer.start_timer()

def start_timer(timer):
    timer.start_time = time.time()
    timer.timer.start(10)  # 更新间隔为10毫秒
    timer.start_button.setText('停止')
    timer.timer_running = True

def stop_timer(timer):
    timer.timer.stop()
    elapsed_time = time.time() - timer.start_time
    timer.history.append(elapsed_time)
    timer.update_history_list()
    timer.start_button.setText('开始')
    timer.timer_running = False

def reset_timer(timer):
    timer.timer.stop()
    timer.start_time = None
    timer.time_label.setText('0.00 秒')
    timer.start_button.setText('开始')
    timer.timer_running = False
    timer.history = []
    timer.update_history_list()

def update_time(timer):
    if timer.start_time is not None:
        elapsed_time = time.time() - timer.start_time
        timer.time_label.setText(f'{elapsed_time:.2f} 秒')

def update_history_list(timer):
    timer.history_list.clear()
    for idx, time_val in enumerate(timer.history):
        item = QListWidgetItem(f'#{idx + 1}: {time_val:.2f} 秒')
        timer.history_list.addItem(item)

def keyPressEvent(timer, event):
    if event.key() == Qt.Key_Space:
        timer.toggle_timer()