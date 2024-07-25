from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MplCanvas(FigureCanvas):
    def __init__(self,  width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)
    
    def clr(self):
        self.axes.clear()

    def plot(self, x, label):
        self.axes.plot(x,label=label)
        self.axes.legend()
        self.draw()

    def label(self):
        self.axes.set_title('history')
        self.axes.set_xlabel('attempt')
        self.axes.set_ylabel('time')
        