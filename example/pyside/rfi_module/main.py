from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog
from PySide6.QtCore import QDateTime
from rfi_module.WatcherCatcher_ui import Ui_Dialog
import os, sys
from datetime import datetime
import pyproj
import subprocess


class Dialog(QMainWindow, Ui_Dialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(Dialog, self).__init__(*args, **kwargs)
        self.current_path = os.path.dirname(os.path.abspath(__file__))

    def init(self, path):
        self.current_path = path  # path 를 실행파일 경로로 변경
        self.setupUi(self)
        self.targetSatellite.setRowCount(0)
        self.site.setRowCount(0)
        self.startTimeInput.setDateTime(QDateTime.currentDateTime())
        self.endTimeInput.setDateTime(QDateTime.currentDateTime())
        self.endTimeInput.setMinimumDateTime(self.startTimeInput.dateTime())
        self.upload_file(path)  # 실행파일 (AstroRFI.py 경로 전달)
        self.submitButton.clicked.connect(self.submit_button_click)
        self.targetAddButton.clicked.connect(self.target_add_click)
        self.targetDeleteButton.clicked.connect(self.target_delete_click)
        self.siteAddButton.clicked.connect(self.site_add_click)
        self.siteDeleteButton.clicked.connect(self.site_delete_click)

    def create_folder(self, dir):
        today_list = str(datetime.today().date()).split("-")
        path = self.current_path + dir  # 현재 파일이 있는 위치에 directory 를 만든다.
        try:
            if not os.path.exists(path):  # 파라미터로 받은 dir(여기서는 data) 폴더가 존재하지 않으면 만든다.
                os.mkdir(path)
            for (
                date
            ) in today_list:  # today_list = [연도, 월, 일] 이고 연도부터 폴더가 있는지 확인하고 없으면 만든다.
                if not os.path.exists(path + "/" + date):
                    os.mkdir(path + "/" + date)
                path = path + "/" + date  # 경로/연도/월/일 폴더로 하나씩 들어간다.
            return path  # path =경로/연도/월/일
        except OSError:
            print("Error: Creating directory...")

    def upload_file(self, path):
        input = open(
            path + "/config/targets_n_sites.txt", "r"
        )  # 파라미터로 받은 path 에 있는 config 폴더의 파일을 오픈 => 실행파일이 있는 위치에 있는 config 폴더
        lines = input.readlines()
        isTarget = True
        for line in lines:  # Target / Site 에 따라 각각 테이블에 정보를 저장
            line = line.strip()
            if line == "Target":
                isTarget = True
                continue
            elif line == "Site":
                isTarget = False
                continue
            elif line == "":
                continue
            else:
                if isTarget:
                    info = line.split(" ")
                    self.targetSatellite.insertRow(self.targetSatellite.rowCount())
                    for i in range(info.__len__() - 1):
                        self.targetSatellite.setItem(
                            int(info[0]), i, QTableWidgetItem(info[i + 1])
                        )
                elif ~isTarget:
                    info = line.split(" ")
                    self.site.insertRow(self.site.rowCount())
                    for i in range(info.__len__() - 1):
                        self.site.setItem(
                            int(info[0]), i, QTableWidgetItem(info[i + 1])
                        )
        input.close()

    def write_new_targets_n_sites_file(
        self, filepath
    ):  # 초기 파일에서 불러온 후 수정한 테이블의 값을 새로운 파일에 기록하는 함수
        # filepath 는 file 이름을 포함한 파일 경로 => ~/targets_n_sites_idx.txt
        file = open(filepath, "w")
        file.write("Target\n")
        for i in range(self.targetSatellite.rowCount()):
            data_list = []
            data_list.append(str(i))
            for j in range(self.targetSatellite.columnCount()):
                if self.targetSatellite.item(i, j) == None:
                    data = ""
                else:
                    data = self.targetSatellite.item(i, j).text()
                data_list.append(data)
            file.write(" ".join(data_list))
            file.write("\n")
        file.write("\n")

        file.write("Site\n")
        for i in range(self.site.rowCount()):
            data_list = []
            data_list.append(str(i))
            for j in range(self.site.columnCount()):
                if self.site.item(i, j) == None:
                    data = ""
                else:
                    data = self.site.item(i, j).text()
                data_list.append(data)
            file.write(" ".join(data_list))
            file.write("\n")
        file.close()

    def write_rfi_arguments_file(
        self, argument_file_path, result_file_path
    ):  # 결과를 저장하는 함수 => rfi_arguments_idx.txt
        file = open(argument_file_path, "w")
        increment_unit_time = 1
        for i in range(self.site.rowCount()):  # site x target
            for j in range(self.targetSatellite.rowCount()):
                data_list = []
                data_list.append(str(-1 * int(i)))  # index
                data_list.append(argument_file_path)
                data_list.append(str(self.startTimeInput.date().year()))
                data_list.append(str(self.startTimeInput.date().month()))
                data_list.append(str(self.startTimeInput.date().day()))
                data_list.append(str(self.startTimeInput.time().hour()))
                data_list.append(str(self.startTimeInput.time().minute()))
                data_list.append(str(self.startTimeInput.time().second()))
                data_list.append(str(self.get_window_length()))
                data_list.append(
                    self.site.item(i, 4).text()
                )  # cone length / cone range
                data_list.append(self.site.item(i, 5).text())  # interference angle
                data_list.append(self.site.item(i, 3).text())  # cone angle
                data_list.append(str(increment_unit_time))
                x, y, z = self.convert_lat_lon_to_ecef(
                    float(self.site.item(i, 1).text()),
                    float(self.site.item(i, 2).text()),
                )
                data_list.append(str(x))
                data_list.append(str(y))
                data_list.append(str(z))
                data_list.append(self.targetSatellite.item(j, 1).text())  # norad id
                data_list.append(result_file_path)
                file.write(" ".join(data_list) + "\n")
        file.close()

    def submit_button_click(self):
        data_dir = "/data"

        input_file_name = "targets_n_sites"
        argument_file_name = "rfi_arguments"
        result_file_name = "rfi_result"
        idx = 0
        today_path = self.create_folder(data_dir)
        print(today_path)
        input_file_path = "%s/%s_%d.txt" % (today_path, input_file_name, idx)
        argument_file_path = "%s/%s_%d.txt" % (today_path, argument_file_name, idx)
        result_file_path = "%s/%s_%d.txt" % (today_path, result_file_name, idx)

        while os.path.exists(input_file_path):  # 파일 이름에 index 붙이는 과정
            idx += 1
            input_file_path = "%s/%s_%d.txt" % (today_path, input_file_name, idx)
            argument_file_path = "%s/%s_%d.txt" % (today_path, argument_file_name, idx)
            result_file_path = "%s/%s_%d.txt" % (today_path, result_file_name, idx)

        self.write_new_targets_n_sites_file(input_file_path)
        self.write_rfi_arguments_file(argument_file_path, result_file_path)

    def execute_rfi(self, today_path, input_file_path, result_file_path):
        engine_dir = self.current_path + "/engine/"
        prediction_command = today_path + "/COMMAND.txt"
        # WACASURFACE_RFI
        coop_engine = engine_dir + "/COOP.exe"
        subprocess.call(
            [
                engine_dir + "/AstroRFI",
                input_file_path,
                result_file_path,
                engine_dir,
            ]
        )

    def target_add_click(self):
        self.targetSatellite.insertRow(self.targetSatellite.rowCount())

    def target_delete_click(self):
        self.targetSatellite.removeRow(self.targetSatellite.currentRow())

    def site_add_click(self):
        self.site.insertRow(self.site.rowCount())

    def site_delete_click(self):
        self.site.removeRow(self.site.currentRow())

    def get_window_length(self):
        startTime = datetime.strptime(
            self.startTimeInput.dateTime().toString("yyyy-MM-dd hh:mm:ss"),
            "%Y-%m-%d %H:%M:%S",
        )
        endTime = datetime.strptime(
            self.endTimeInput.dateTime().toString("yyyy-MM-dd hh:mm:ss"),
            "%Y-%m-%d %H:%M:%S",
        )
        interval = int((endTime - startTime).total_seconds())
        return interval

    def convert_lat_lon_to_ecef(self, latitude, longitude):
        # WGS84 좌표계와 ECEF 좌표계 간의 변환을 위한 프로젝션 생성
        wgs84 = pyproj.Proj(proj="latlong", datum="WGS84", ellps="WGS84")
        ecef = pyproj.Proj(proj="geocent", datum="WGS84", ellps="WGS84")

        # WGS84 좌표를 ECEF 좌표로 변환
        x, y, z = pyproj.transform(wgs84, ecef, longitude, latitude, 0, radians=False)

        return x, y, z


if __name__ == "__main__":
    app = QApplication()
    window = Dialog()
    window.show()
    app.exec()
