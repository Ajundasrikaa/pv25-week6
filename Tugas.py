import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSlider, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor, QPalette

class SliderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Week 6 - F1D022108")
        self.setGeometry(100, 100, 500, 300)

        self.label = QLabel("F1D022108", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Arial", 30))

        self.name_label = QLabel("AJUNDASRIKA ANUGRAHANTI TS", self)
        self.name_label.setAlignment(Qt.AlignCenter)
        self.name_label.setFont(QFont("Arial", 10))

        self.font_slider = QSlider(Qt.Horizontal)
        self.font_slider.setMinimum(20)
        self.font_slider.setMaximum(60)
        self.font_slider.setValue(30)
        self.font_slider.valueChanged.connect(self.update_font_size)

        self.font_color_slider = QSlider(Qt.Horizontal)
        self.font_color_slider.setMinimum(0)
        self.font_color_slider.setMaximum(255)
        self.font_color_slider.setValue(0)
        self.font_color_slider.valueChanged.connect(self.update_font_color)

        self.bg_color_slider = QSlider(Qt.Horizontal)
        self.bg_color_slider.setMinimum(0)
        self.bg_color_slider.setMaximum(255)
        self.bg_color_slider.setValue(255)
        self.bg_color_slider.valueChanged.connect(self.update_bg_color)

        self.font_label = QLabel("Font Size")
        self.font_color_label = QLabel("Font Color (Grayscale)")
        self.bg_color_label = QLabel("Background Color (Grayscale)")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.name_label)

        layout.addWidget(self.font_label)
        layout.addWidget(self.font_slider)

        layout.addWidget(self.font_color_label)
        layout.addWidget(self.font_color_slider)

        layout.addWidget(self.bg_color_label)
        layout.addWidget(self.bg_color_slider)

        self.setLayout(layout)
        self.update_font_color()
        self.update_bg_color()

        slider_style = """
        QSlider::groove:horizontal {
            height: 10px;
            background: #e6f0ff;  
            border-radius: 5px;
        }

        QSlider::handle:horizontal {
            background: #4c8cff; 
            border: 1px solid #777;
            width: 20px;
            margin: -5px 0;
            border-radius: 10px;
        }

        QSlider::sub-page:horizontal {
            background: #b3d7ff;  
            border-radius: 5px;
        }
        """
        self.font_slider.setStyleSheet(slider_style)
        self.font_color_slider.setStyleSheet(slider_style)
        self.bg_color_slider.setStyleSheet(slider_style)

    def update_font_size(self):
        size = self.font_slider.value()
        self.label.setFont(QFont("Arial", size))

    def update_font_color(self):
        val = self.font_color_slider.value()
        color = QColor(val, val, val)
        palette = self.label.palette()
        palette.setColor(QPalette.WindowText, color)
        self.label.setPalette(palette)

    def update_bg_color(self):
        val = self.bg_color_slider.value()
        color = QColor(val, val, val)
        palette = self.label.palette()
        palette.setColor(QPalette.Window, color)
        self.label.setAutoFillBackground(True)
        self.label.setPalette(palette)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SliderApp()
    window.show()
    sys.exit(app.exec_())