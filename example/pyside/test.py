from datetime import datetime
import astrolibrary

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QAbstractItemView,
    QHeaderView,
    QFileSystemModel,
    QMessageBox,
)
from PySide6.QtCore import (
    QTimer,
    Signal,
    Slot,
    QDateTime,
    Qt,
    QDir,
    QSortFilterProxyModel,
    QRegularExpression,
)
from PySide6.QtGui import QStandardItemModel, QStandardItem

from opengl_ui import Ui_MainWindow
from space_objects import SpaceObjects

import time, os, random, datetime, sys


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
        self.treeViewInit()

    def load_watchercatcher(self):
        self.tableView.resizeRowsToContents()
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)

        NUM_COL_WATCHERCATCHER = 9
        self.watchercatcher_modal.setColumnCount(NUM_COL_WATCHERCATCHER)
        self.watchercatcher_modal.setHeaderData(0, Qt.Horizontal, "Target Satellite")
        self.watchercatcher_modal.setHeaderData(1, Qt.Horizontal, "Site name")
        self.watchercatcher_modal.setHeaderData(2, Qt.Horizontal, "Site Latitude (deg)")
        self.watchercatcher_modal.setHeaderData(
            3, Qt.Horizontal, "Site Longitude (deg)"
        )
        self.watchercatcher_modal.setHeaderData(4, Qt.Horizontal, "Cone Angle (deg)")
        self.watchercatcher_modal.setHeaderData(5, Qt.Horizontal, "Cone Range (Km)")
        self.watchercatcher_modal.setHeaderData(6, Qt.Horizontal, "Interference Angle")
        self.watchercatcher_modal.setHeaderData(7, Qt.Horizontal, "Start Time")
        self.watchercatcher_modal.setHeaderData(8, Qt.Horizontal, "End Time")

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
        header.setSectionResizeMode(7, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(8, QHeaderView.ResizeMode.ResizeToContents)

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
        # print(f"propagate: {time.time()-start:.4f} sec")  # 종료와 함께 수행시간 출력
        start = time.time()  # 시작
        self.openGLWidget.update()
        # print(f"update: {time.time()-start:.4f} sec")  # 종료와 함께 수행시간 출력

    def play_simulation(self):
        if self.simulation_timer.isActive() == False:
            self.simulation_timer.start(self.simulation_unit_time)
        else:
            self.simulation_timer.stop()
        # self.update()

    def treeViewInit(self):
        # archive 디렉토리 경로 설정
        currentPath = QDir.currentPath()
        print(currentPath)
        archivePath = (
            currentPath + "/Archive"
        )  # archivePath = os.path.join(currentPath, "/Archive")

        # QFileSystemModel을 생성하고 루트 경로를 "Archive" 디렉토리로 설정
        model = QFileSystemModel()
        model.setRootPath(archivePath)
        model.setReadOnly(False)

        # QSortFilterProxyModel을 생성하고 원본 모델 설정
        proxyModel = QSortFilterProxyModel()
        proxyModel.setSourceModel(model)

        # 필터 조건 설정
        nameFilter = QRegularExpression("[0-9]?")
        proxyModel.setFilterRegularExpression(nameFilter)
        proxyModel.setFilterKeyColumn(0)

        # treeView를 생성하고 필터된 모델을 설정
        self.treeView.setModel(proxyModel)
        self.treeView.setRootIndex(proxyModel.mapFromSource(model.index(archivePath)))
        self.treeView.setColumnWidth(0, 150)

        # treeView의 doubleClicked 시그널을 슬롯 함수에 연결
        self.treeView.doubleClicked.connect(lambda index: self.onTreeViewDoubleClicked)

    def onTreeViewDoubleClicked(self, index):
        fileIndex = self.treeView.model().mapToSource(index)

        fileInfo = self.treeView.model().sourceModel().fileInfo(fileIndex)

        if fileInfo.isDir():
            self.treeView.expand(index)
        else:
            filePath = self.treeView.model().sourceModel().filePath(fileIndex)

            # 파일로부터 데이터를 추출한 다음, watchercatcher_modal을 채움
            self.loadDataToWatcherCatcher(filePath)

    def loadDataToWatcherCatcher(self, filePath):
        # initial file로 부터 target satellite와 site 정보를 추출
        initialFilePath = filePath.split("/")
        initialFilePath[-1] = "initial.txt"
        initialFilePath = "/".join(initialFilePath)

        try:
            initialData = open(initialFilePath, "r", encoding="UTF8")
        except FileNotFoundError:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error")
            dlg.setText("initial 파일을 찾을 수 없습니다.")
            dlg.move(self.frameGeometry().center() - dlg.frameGeometry().center())
            dlg.exec()
            return

        target = list()
        site = list()
        select = 1
        option = [target, site]
        for line in initialData:
            line = line.replace("\n", "")
            if line == "":
                continue
            elif line == "Target" or line == "Site":
                select = select ^ 1
                continue
            option[select].append(line.split(" ", 1)[1])

        initialData.close()

        # output file로 부터 RFI 관련 데이터 추출
        targetId = list()
        for sat in target:
            targetId.append(sat.split(" ")[1])

        outputData = open(filePath, "r", encoding="UTF8")

        result = list()
        for line in outputData:
            line = line.replace("\n", "")
            if line[0] == "%":
                continue
            data = line.split("\t")
            if len(data) < 15:
                if line[-2] == "0":
                    continue
                ranID = random.choice(targetId)
                data.append(ranID)

            try:
                second = float(data[11])
                second_int = int(second)
                microseconds = int((second - second_int) * 1000000)
                tcaTime = datetime.datetime(
                    int(data[6]),
                    int(data[7]),
                    int(data[8]),
                    int(data[9]),
                    int(data[10]),
                    second_int,
                    microseconds,
                )

                second = float(data[3]) - float(data[4])
                second_int = int(second)
                microseconds = int((second - second_int) * 1000000)
                firstTimeDifference = datetime.timedelta(
                    seconds=second, microseconds=microseconds
                )
                startTime = tcaTime - firstTimeDifference

                second = float(data[5]) - float(data[3])
                second_int = int(second)
                microseconds = int((second - second_int) * 1000000)
                secondTimeDifference = datetime.timedelta(
                    seconds=second, microseconds=microseconds
                )
                endTime = tcaTime + secondTimeDifference

            except IndexError:
                # watchercatcher_modal에서 기존 데이터를 지우고 헤더 데이터를 유지합니다
                self.watchercatcher_modal.removeRows(
                    0, self.watchercatcher_modal.rowCount()
                )
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Error")
                dlg.setText("파일의 형식이 올바르지 않습니다.")
                dlg.move(self.frameGeometry().center() - dlg.frameGeometry().center())
                dlg.exec()
                return

            temp = list()
            temp.append(data[-1])

            for siteData in site[-int(data[0])].split(" "):
                temp.append(siteData)
            temp.append(startTime.strftime("%Y-%m-%d %H:%M:%S.%f"))
            temp.append(endTime.strftime("%Y-%m-%d %H:%M:%S.%f"))
            result.append(temp)

        # Main window에 RFI results 출력
        curr_row = 0
        NUM_COL_WATCHERCATCHER = 9
        for curr_data in result:
            curr_item = QStandardItem(1, NUM_COL_WATCHERCATCHER)
            self.watchercatcher_modal.insertRow(curr_row, curr_item)
            self.watchercatcher_modal.setHeaderData(
                0, Qt.Horizontal, "Target Satellite"
            )
            self.watchercatcher_modal.setHeaderData(1, Qt.Horizontal, "Site name")
            self.watchercatcher_modal.setHeaderData(
                2, Qt.Horizontal, "Site Latitude (deg)"
            )
            self.watchercatcher_modal.setHeaderData(
                3, Qt.Horizontal, "Site Longitude (deg)"
            )
            self.watchercatcher_modal.setHeaderData(
                4, Qt.Horizontal, "Cone Angle (deg)"
            )
            self.watchercatcher_modal.setHeaderData(5, Qt.Horizontal, "Cone Range (Km)")
            self.watchercatcher_modal.setHeaderData(
                6, Qt.Horizontal, "Interference Angle"
            )
            self.watchercatcher_modal.setHeaderData(7, Qt.Horizontal, "Start Time")
            self.watchercatcher_modal.setHeaderData(8, Qt.Horizontal, "End Time")

            targetSatellite = self.watchercatcher_modal.index(curr_row, 0)
            siteName = self.watchercatcher_modal.index(curr_row, 1)
            siteLatitude = self.watchercatcher_modal.index(curr_row, 2)
            siteLongitude = self.watchercatcher_modal.index(curr_row, 3)
            coneAngle = self.watchercatcher_modal.index(curr_row, 4)
            coneRange = self.watchercatcher_modal.index(curr_row, 5)
            interferenceAangle = self.watchercatcher_modal.index(curr_row, 6)
            startTime = self.watchercatcher_modal.index(curr_row, 7)
            endTime = self.watchercatcher_modal.index(curr_row, 8)

            self.watchercatcher_modal.setData(targetSatellite, curr_data[0])
            self.watchercatcher_modal.setData(siteName, curr_data[1])
            self.watchercatcher_modal.setData(siteLatitude, curr_data[2])
            self.watchercatcher_modal.setData(siteLongitude, curr_data[3])
            self.watchercatcher_modal.setData(coneAngle, curr_data[4])
            self.watchercatcher_modal.setData(coneRange, curr_data[5])
            self.watchercatcher_modal.setData(interferenceAangle, curr_data[6])
            self.watchercatcher_modal.setData(startTime, curr_data[7])
            self.watchercatcher_modal.setData(endTime, curr_data[8])

            # temporary code, we can't handle QItem now.
            self.map_row_index_to_watchercatcher[curr_row] = curr_data
            curr_row += 1


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
