from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MplCanvas(FigureCanvas):
    def __init__(self,  width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

    def plot(self, x):
        y = [1,2,3,4,5,6,7,8,9,10]
        z=[1,2,3,4,5,6,7,8,9,10]
        self.axes.plot(y,z)
        self.axes.plot(x)
        