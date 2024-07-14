import sys 
from PyQt5.QtWidgets import QApplication
from TimerUI import TimerUI
from TimerLogic import TimerLogic
if __name__ == '__main__':


    app = QApplication(sys.argv)
    logic = TimerLogic()
    ui = TimerUI(logic)
    logic.set_ui(ui)
    ui.show()
    sys.exit(app.exec_())
