from datetime import datetime
import astrolibrary

from PySide6.QtWidgets import QApplication, QMainWindow, QAbstractItemView, QHeaderView
from PySide6.QtCore import QTimer, Signal, Slot, QDateTime, Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem

from opengl_ui import Ui_MainWindow
from space_objects import SpaceObjects

import time


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.astro_client = astrolibrary.Client(
            "Y8HSpeoKt+10sYVL7pRJum2lBg8XFfWOu+LVyN0Y26+5l7EO3WXTbGipnlkgkmPi"
        )
        self.space_objects = SpaceObjects(self.astro_client.tle_API.get_recent_tles())
        self.watchercatcher_modal = QStandardItemModel()

        self.simulation_timer = QTimer()
        self.simulation_timer.timeout.connect(self.increase_simulation_time)
        self.simulation_time = QDateTime.currentDateTime()
        self.dateTimeEdit.setDateTime(self.simulation_time)
        self.simulation_unit_time = 100

        self.map_row_index_to_watchercatcher = dict()

        self.load_watchercatcher()

    def load_watchercatcher(self):
        status_list = self.astro_client.watcher_catcher_API.get_requests_status_list()

        result = []
        for status in status_list["data"]:
            result.append(
                self.astro_client.watcher_catcher_API.get_predicted_result(
                    status["_id"]
                )
            )
        print(result)
        self.tableView.resizeRowsToContents()
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)

        NUM_COL_WATCHERCATCHER = 7
        self.watchercatcher_modal.setColumnCount(NUM_COL_WATCHERCATCHER)
        self.watchercatcher_modal.setHeaderData(0, Qt.Horizontal, "Apex Latitude (deg)")
        self.watchercatcher_modal.setHeaderData(
            1, Qt.Horizontal, "Apex Longitude (deg)"
        )
        self.watchercatcher_modal.setHeaderData(2, Qt.Horizontal, "Cone Range (km)")
        self.watchercatcher_modal.setHeaderData(
            3, Qt.Horizontal, "Cone Field of View (deg)"
        )
        self.watchercatcher_modal.setHeaderData(
            4, Qt.Horizontal, "Start Time of Timeline"
        )
        self.watchercatcher_modal.setHeaderData(
            5, Qt.Horizontal, "End Time of Timeline"
        )
        self.watchercatcher_modal.setHeaderData(
            6, Qt.Horizontal, "Downloaded Time Interval"
        )

        self.tableView.setModel(self.watchercatcher_modal)
        self.tableView.setEditTriggers(QAbstractItemView.EditTrigger().NoEditTriggers)

        header = self.tableView.horizontalHeader()

        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(6, QHeaderView.ResizeMode.ResizeToContents)

        curr_row = 0
        for curr_data in result:
            curr_item = QStandardItem(1, NUM_COL_WATCHERCATCHER)
            self.watchercatcher_modal.insertRow(curr_row, curr_item)

            apex_latitude_index = self.watchercatcher_modal.index(curr_row, 0)
            apex_longitude_index = self.watchercatcher_modal.index(curr_row, 1)
            cone_range_index = self.watchercatcher_modal.index(curr_row, 2)
            cone_field_of_view_index = self.watchercatcher_modal.index(curr_row, 3)
            start_time_of_timeline_index = self.watchercatcher_modal.index(curr_row, 4)
            end_time_of_timelin_index = self.watchercatcher_modal.index(curr_row, 5)
            downloaded_time_of_used_TLE_index = self.watchercatcher_modal.index(
                curr_row, 6
            )
            watching_time_interval_index = self.watchercatcher_modal.index(curr_row, 7)

            self.watchercatcher_modal.setData(
                apex_latitude_index, curr_data.apex_latitude
            )
            self.watchercatcher_modal.setData(
                apex_longitude_index, curr_data.apex_longitude
            )
            self.watchercatcher_modal.setData(cone_range_index, curr_data.cone_range)
            self.watchercatcher_modal.setData(
                cone_field_of_view_index, curr_data.cone_field_of_view
            )
            self.watchercatcher_modal.setData(
                start_time_of_timeline_index, curr_data.start_time_of_timeline
            )
            self.watchercatcher_modal.setData(
                end_time_of_timelin_index, curr_data.end_time_of_timeline
            )
            self.watchercatcher_modal.setData(
                downloaded_time_of_used_TLE_index, curr_data.downloaded_time_of_used_TLE
            )
            self.watchercatcher_modal.setData(
                watching_time_interval_index, curr_data.watching_time_interval
            )

            # temporary code, we can't handle QItem now.
            self.map_row_index_to_watchercatcher[curr_row] = curr_data
            curr_row += 1

    def update_watchercatcher_selection_in_table(self, selected_row):
        print(selected_row.row())
        row = selected_row.row()
        print(self.map_row_index_to_watchercatcher[row])
        

    def increase_simulation_time(self):
        # change_time_by_given_increment()
        self.simulation_time = self.simulation_time.addMSecs(self.simulation_unit_time)
        self.dateTimeEdit.setDateTime(self.simulation_time)
        self.update_simulation_time()
        # self.update()

    def change_simulation_time(self):
        self.simulation_time = self.dateTimeEdit.dateTime()
        self.update_simulation_time()

    def update_simulation_time(self):
        start = time.time()  # 시작
        coordinates = self.space_objects.position_vector_of_objects_at_moment(
            self.simulation_time.toPython()
        )
        self.openGLWidget.clear_points()
        for coordinate in coordinates:
            self.openGLWidget.add_point(coordinate)
        print(f"propagate: {time.time()-start:.4f} sec")  # 종료와 함께 수행시간 출력
        start = time.time()  # 시작
        self.openGLWidget.update()
        print(f"update: {time.time()-start:.4f} sec")  # 종료와 함께 수행시간 출력

    def play_simulation(self):
        if self.simulation_timer.isActive() == False:
            self.simulation_timer.start(self.simulation_unit_time)
        else:
            self.simulation_timer.stop()
        # self.update()


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()

    window.show()
    app.exec()
