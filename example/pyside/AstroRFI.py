from datetime import datetime
from rfi_module import main

from astrolibrary.data.tle import TLE
from astrolibrary.data.rfi_time_interval import RfiTimeInterval
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
    QDateTime,
    Qt,
    QDir,
    QSortFilterProxyModel,
    QRegularExpression,
)
from PySide6.QtGui import QStandardItemModel, QStandardItem

from opengl_ui import Ui_MainWindow
from space_objects import SpaceObjects

from datetime import datetime
import time, random, datetime, re
import os


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.space_objects = SpaceObjects([])
        self.watchercatcher_modal = QStandardItemModel()

        self.simulation_timer = QTimer()
        self.simulation_timer.timeout.connect(self.increase_simulation_time)
        self.simulation_time = QDateTime.currentDateTime()
        self.dateTimeEdit.setDateTime(self.simulation_time)
        self.simulation_unit_time = 100

        self.map_row_index_to_watchercatcher = dict()

        self.load_watchercatcher()
        self.treeViewInit()
        self.rfiButton.clicked.connect(self.rfi_exe)

    def rfi_exe(self):
        path = os.path.dirname(os.path.abspath(__file__))  # 현재 파일 경로
        self.rfi = main.Dialog()
        self.rfi.init(path)  # dialog 모달로 현재 파일 경로 전달
        self.rfi.show()

    def load_watchercatcher(self):
        self.tableView.resizeRowsToContents()
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)

        NUM_COL_WATCHERCATCHER = 10
        self.watchercatcher_modal.setColumnCount(NUM_COL_WATCHERCATCHER)
        self.watchercatcher_modal.setHeaderData(0, Qt.Horizontal, "Target Satellite")
        self.watchercatcher_modal.setHeaderData(1, Qt.Horizontal, "Site name")
        self.watchercatcher_modal.setHeaderData(2, Qt.Horizontal, "Site Latitude (deg)")
        self.watchercatcher_modal.setHeaderData(3, Qt.Horizontal, "Site Longitude (deg)")
        self.watchercatcher_modal.setHeaderData(4, Qt.Horizontal, "Start Time")
        self.watchercatcher_modal.setHeaderData(5, Qt.Horizontal, "End Time")
        self.watchercatcher_modal.setHeaderData(6, Qt.Horizontal, "Cone Angle (deg)")
        self.watchercatcher_modal.setHeaderData(7, Qt.Horizontal, "Cone Range (Km)")
        self.watchercatcher_modal.setHeaderData(8, Qt.Horizontal, "Interference Angle")
        self.watchercatcher_modal.setHeaderData(9, Qt.Horizontal, "Min Angle")

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
        archivePath = currentPath + "/data"

        # QFileSystemModel을 생성하고 루트 경로를 "Archive" 디렉토리로 설정
        model = QFileSystemModel()
        model.setRootPath(archivePath)
        model.setReadOnly(False)

        # QSortFilterProxyModel을 생성하고 원본 모델 설정
        proxyModel = QSortFilterProxyModel()
        proxyModel.setSourceModel(model)

        # 필터 조건 설정
        nameFilter = QRegularExpression("")
        proxyModel.setFilterRegularExpression(nameFilter)
        # proxyModel.setRecursiveFilteringEnabled(True)
        proxyModel.setFilterKeyColumn(0)

        # treeView를 생성하고 필터된 모델을 설정
        self.treeView.setModel(proxyModel)
        self.treeView.setRootIndex(proxyModel.mapFromSource(model.index(archivePath)))
        self.treeView.setColumnWidth(0, 300)

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

    def __get_recent_TLE_file_path(self, file_path):
        # TLE 데이터를 추출하여 opengl_ui에 rendering
        tle_file_path = file_path.split("/")
        tle_file_path[-1] = "recent.tle"
        return "/".join(tle_file_path)

    def __load_TLE_data(self, tle_file_path):
        try:
            tle_data = open(tle_file_path, "r", encoding="UTF8")
            return tle_data.read()
        except FileNotFoundError:
            self.__handle_error("TLE 파일을 찾을 수 없습니다.")
            return None

    def __handle_error(self, message):
        self.watchercatcher_modal.removeRows(0, self.watchercatcher_modal.rowCount())
        self.space_objects = SpaceObjects([])
        self.change_simulation_time()
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Error")
        dlg.setText(message)
        dlg.move(self.frameGeometry().center() - dlg.frameGeometry().center())
        dlg.exec()

    def __parse_TLE_data(self, tles):
        tle_list = list()
        lines = tles.split("\n")

        for i in range(0, len(lines), 3):
            tle_dict = dict()
            tle_dict["name"] = lines[i].split(" ", 1)[1]
            tle_dict["firstLine"] = lines[i + 1]
            tle_dict["secondLine"] = lines[i + 2]
            tle = TLE(tle_dict)
            tle_list.append(tle)

        return tle_list

    def __get_target_and_site_file_path(self, file_path):
        target_and_site_file_path = file_path.split("/")
        pattern = r"rfi_result_\d+\.txt"
        if not bool(re.fullmatch(pattern, target_and_site_file_path[-1])):
            self.__handle_error("RFI 결과 파일명이 올바르지 않습니다.")
            return None

        index = target_and_site_file_path[-1].split(".")[0].split("_")[-1]
        target_and_site_file_path[-1] = f"targets_n_sites_{index}.txt"
        return "/".join(target_and_site_file_path)

    def __load_target_and_site_data(self, target_and_site_file_path):
        try:
            target_and_site_data = open(target_and_site_file_path, "r", encoding="UTF8")
            return target_and_site_data
        except FileNotFoundError:
            self.__handle_error("RFI 결과 파일과 대응되는 입력 파일을 찾을 수 없습니다.")
            return None

    def __extract_target_and_site_data(self, target_and_site_data):
        target = list()
        site = list()
        select = 1
        option = [target, site]
        for line in target_and_site_data:
            line = line.replace("\n", "")
            if line == "":
                continue
            elif line == "Target" or line == "Site":
                select = select ^ 1
                continue
            option[select].append(line.split(" ", 1)[1])

        target_and_site_data.close()
        return target, site

    # sample data에 random id를 부여하는 함수
    # 추후 실제 데이터를 불러올 경우 함수가 수정되어야 함
    def __extract_rfi_result_data(self, rfi_result, target, site):
        target_id = [sat.split(" ")[1] for sat in target]

        rfi_list = list()
        for line in rfi_result:
            line = line.replace("\n", "")
            if line[0] == "%":
                continue
            data = line.split("\t")
            if len(data) < 15:
                if line[-2] == "0":
                    continue
                ran_id = random.choice(target_id)
                data.append(ran_id)

            try:
                second = float(data[11])
                second_int = int(second)
                microseconds = int((second - second_int) * 1000000)
                tca_time = datetime.datetime(
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
                start_to_tca_time_diffrence = datetime.timedelta(
                    seconds=second, microseconds=microseconds
                )
                start_time = tca_time - start_to_tca_time_diffrence

                second = float(data[5]) - float(data[3])
                second_int = int(second)
                microseconds = int((second - second_int) * 1000000)
                tca_to_end_time_diffrence = datetime.timedelta(
                    seconds=second, microseconds=microseconds
                )
                end_time = tca_time + tca_to_end_time_diffrence

            except IndexError:
                self.__handle_error("파일의 형식이 올바르지 않습니다.")
                return None

            rfi_dict = dict()
            rfi_dict["targetSatellite"] = data[-1]
            rfi_dict["siteName"] = site[-int(data[0])].split(" ")[0]
            rfi_dict["siteLatitude"] = site[-int(data[0])].split(" ")[1]
            rfi_dict["siteLongitude"] = site[-int(data[0])].split(" ")[2]
            rfi_dict["startTime"] = start_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-4]
            rfi_dict["endTime"] = end_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-4]
            rfi_dict["coneAngle"] = site[-int(data[0])].split(" ")[3]
            rfi_dict["coneRange"] = site[-int(data[0])].split(" ")[4]
            rfi_dict["interferenceAngle"] = site[-int(data[0])].split(" ")[5]
            rfi_dict["minAngle"] = data[-2]

            rfi = RfiTimeInterval(rfi_dict)
            rfi_list.append(rfi)

        return rfi_list
    
    def show_rfi_results(self, rfi_list):
        NUM_COL_WATCHERCATCHER = 10

        for idx, rfi in rfi_list:
            item = QStandardItem(1, NUM_COL_WATCHERCATCHER)
            self.watchercatcher_modal.insertRow(idx, item)
            self.watchercatcher_modal.setHeaderData(0, Qt.Horizontal, "Target Satellite")
            self.watchercatcher_modal.setHeaderData(1, Qt.Horizontal, "Site name")
            self.watchercatcher_modal.setHeaderData(2, Qt.Horizontal, "Site Latitude (deg)")
            self.watchercatcher_modal.setHeaderData(3, Qt.Horizontal, "Site Longitude (deg)")
            self.watchercatcher_modal.setHeaderData(4, Qt.Horizontal, "Start Time")
            self.watchercatcher_modal.setHeaderData(5, Qt.Horizontal, "End Time")
            self.watchercatcher_modal.setHeaderData(6, Qt.Horizontal, "Cone Angle (deg)")
            self.watchercatcher_modal.setHeaderData(7, Qt.Horizontal, "Cone Range (Km)")
            self.watchercatcher_modal.setHeaderData(8, Qt.Horizontal, "Interference Angle")
            self.watchercatcher_modal.setHeaderData(9, Qt.Horizontal, "Min Angle")

            target_satellite = self.watchercatcher_modal.index(idx, 0)
            site_name = self.watchercatcher_modal.index(idx, 1)
            site_latitude = self.watchercatcher_modal.index(idx, 2)
            site_longitude = self.watchercatcher_modal.index(idx, 3)
            cone_angle = self.watchercatcher_modal.index(idx, 4)
            cone_range = self.watchercatcher_modal.index(idx, 5)
            interference_angle = self.watchercatcher_modal.index(idx, 6)
            start_time = self.watchercatcher_modal.index(idx, 7)
            end_time = self.watchercatcher_modal.index(idx, 8)
            min_angle = self.watchercatcher_modal.index(idx, 9)

            self.watchercatcher_modal.setData(target_satellite, rfi.target_satellite)
            self.watchercatcher_modal.setData(site_name, rfi.site_name)
            self.watchercatcher_modal.setData(site_latitude, rfi.site_latitude)
            self.watchercatcher_modal.setData(site_longitude, rfi.site_longitude)
            self.watchercatcher_modal.setData(cone_angle, rfi.cone_angle)
            self.watchercatcher_modal.setData(cone_range, rfi.cone_range)
            self.watchercatcher_modal.setData(interference_angle, rfi.interference_angle)
            self.watchercatcher_modal.setData(start_time, rfi.start_time)
            self.watchercatcher_modal.setData(end_time, rfi.end_time)
            self.watchercatcher_modal.setData(min_angle, rfi.min_angle)

            self.map_row_index_to_watchercatcher[idx] = rfi

    def loadDataToWatcherCatcher(self, file_path):
        tle_file_path = self.__get_recent_TLE_file_path(file_path)
        tle_data = self.__load_TLE_data(tle_file_path)
        if tle_data is None:
            return

        tle_list = self.__parse_TLE_data(tle_data)
        self.space_objects = SpaceObjects(tle_list)
        self.change_simulation_time()

        target_and_site_file_path = self.__get_target_and_site_file_path(file_path)
        target_and_site_data = self.__load_target_and_site_data(
            target_and_site_file_path
        )
        if target_and_site_data is None:
            return
        target, site = self.__extract_target_and_site_data(target_and_site_data)

        rfi_result_data = open(file_path, "r", encoding="UTF8")
        rfi_list = self.__extract_rfi_result_data(rfi_result_data, target, site)
        rfi_result_data.close()

        self.show_rfi_results(rfi_list)


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
