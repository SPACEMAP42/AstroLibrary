from datetime import datetime
import astrolibrary

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer, Signal, Slot, QDateTime

from opengl_ui import Ui_MainWindow
from space_objects import SpaceObjects

import time


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.simulation_timer = QTimer()
        self.simulation_timer.timeout.connect(self.increase_simulation_time)
        self.simulation_time = QDateTime.currentDateTime()
        self.dateTimeEdit.setDateTime(self.simulation_time)
        self.simulation_unit_time = 100
        self.space_objects = SpaceObjects(spacemap.tle_API.get_recent_tles())

    def increase_simulation_time(self):
        # change_time_by_given_increment()
        self.simulation_time = self.simulation_time.addMSecs(self.simulation_unit_time)

        self.dateTimeEdit.setDateTime(self.simulation_time)
        start = time.time()  # 시작
        coordinates = self.space_objects.position_vector_of_objects_at_moment(
            self.simulation_time.toPython()
        )
        self.openGLWidget.clear_points()
        for coordinate in coordinates:
            self.openGLWidget.add_point(coordinate)
        print(f"propagate: {time.time()-start:.4f} sec")  # 종료와 함께 수행시간 출력
        self.openGLWidget.update()
        # self.update()

    def play_simulation(self):
        if self.simulation_timer.isActive() == False:
            self.simulation_timer.start(self.simulation_unit_time)
        else:
            self.simulation_timer.stop()
        # self.update()


if __name__ == "__main__":
    spacemap = astrolibrary.Client(
        "Y8HSpeoKt+10sYVL7pRJum2lBg8XFfWOu+LVyN0Y26+5l7EO3WXTbGipnlkgkmPi"
    )

    app = QApplication()
    window = MainWindow()

    window.show()
    app.exec()
