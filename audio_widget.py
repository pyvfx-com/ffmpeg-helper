import sys
import librosa
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import librosa.display


class AudioWaveformVisualizer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Audio Waveform Visualizer")
        self.setGeometry(100, 100, 900, 200)

        # Create layout and widgets
        layout = QVBoxLayout()


        # Matplotlib figure and canvas
        self.figure = plt.Figure(figsize=(8, 3))
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        # Set the layout for the QWidget
        self.setLayout(layout)
        self.load_audio_file()

    def load_audio_file(self):
        audio_file = "/home/rion/dev/ffmpeg-helper/audio/relaxing_guitar_loop.wav"

        if audio_file:
            # Load the audio file using librosa
            y, sr = librosa.load(audio_file, sr=None)

            # Clear the previous plot
            self.figure.clear()

            # Create a new axis to plot the waveform
            ax = self.figure.add_subplot(111)
            librosa.display.waveshow(y, sr=sr, ax=ax, color='#302842')

            # Set plot titles and labels
            ax.set_title("Audio Waveform")
            ax.set_xlabel("Time (s)")
            ax.set_ylabel("Amplitude")
            ax.grid(True)

            # Redraw the canvas
            self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AudioWaveformVisualizer()
    window.show()
    sys.exit(app.exec_())
