import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create a QVBoxLayout instance
        layout = QVBoxLayout()

        # Create some widgets
        label = QLabel("This is a label")
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")

        # Add widgets to the layout
        layout.addWidget(label)
        layout.addWidget(button1)
        layout.addWidget(button2)

        # Set the layout for the main window
        self.setLayout(layout)

        # Set window title and size
        self.setWindowTitle("Vertical Layout Example")
        self.resize(800,800)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWin = MainWindow()
    mainWin.show()

    sys.exit(app.exec_())
