import sys

from PySide6.QtWidgets import (
    QAbstractSpinBox,
    QApplication,
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QSlider,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)
from PySide6.QtCore import QTimer, Qt


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Lesson 5")

        self.counter = 0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timer_method)

        self.spin_box = QSpinBox()
        self.spin_box.setRange(0, 10000)
        self.spin_box.setReadOnly(True)
        self.spin_box.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spin_box.setStyleSheet("QSpinBox { background-color: lightgray; }")

        self.slider_spin_box = QSpinBox()
        self.slider_spin_box.setRange(0, 10000)
        self.slider_spin_box.setReadOnly(True)
        self.slider_spin_box.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.slider_spin_box.setStyleSheet("QSpinBox { background-color: lightgray; }")

        self.slider = QSlider(Qt.Orientation.Vertical)
        self.slider.setRange(0, 255)
        self.slider.valueChanged.connect(self.slider_method)

        self.toggle_button = QPushButton("Start")
        self.toggle_button.setCheckable(True)
        self.toggle_button.toggled.connect(self.button_method)

        controls_layout = QVBoxLayout()
        controls_layout.addWidget(self.spin_box)
        controls_layout.addWidget(self.toggle_button)

        slider_layout = QVBoxLayout()
        slider_layout.addWidget(self.slider_spin_box)
        slider_layout.addWidget(self.slider, alignment=Qt.AlignmentFlag.AlignHCenter)

        layout = QHBoxLayout()
        layout.addLayout(controls_layout)
        layout.addLayout(slider_layout)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def button_method(self, checked: bool) -> None:
        self.toggle_button.setText("Stop" if checked else "Start")
        if checked:
            self.timer.start(10)
        else:
            self.timer.stop()

    def timer_method(self):
        self.counter += 1
        self.spin_box.setValue(self.counter)
        if self.counter == 500:
            self.timer.stop()
            self.button.setChecked(False)

    def slider_method(self):
        value = self.slider.value()
        self.slider_spin_box.setValue(value)


def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
