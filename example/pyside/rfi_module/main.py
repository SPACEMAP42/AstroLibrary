from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog
from PySide6.QtCore import QDateTime
from rfi_module.WatcherCatcher_ui import Ui_Dialog
import os
from datetime import datetime
import pyproj


class Dialog(QMainWindow, Ui_Dialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(Dialog, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.targetSatellite.setRowCount(0)
        self.site.setRowCount(0)
        self.startTimeInput.setDateTime(QDateTime.currentDateTime())
        self.endTimeInput.setDateTime(QDateTime.currentDateTime())
        self.endTimeInput.setMinimumDateTime(self.startTimeInput.dateTime())
        self.upload_file()
        self.submitButton.clicked.connect(self.submit_button_click)
        self.targetAddButton.clicked.connect(self.target_add_click)
        self.targetDeleteButton.clicked.connect(self.target_delete_click)
        self.siteAddButton.clicked.connect(self.site_add_click)
        self.siteDeleteButton.clicked.connect(self.site_delete_click)
        

    def create_folder(self, dir):
        today_list = str(datetime.today().date()).split("-")
        path = os.getcwd() + dir
        try:
            if not os.path.exists(path):
                os.mkdir(path)
            for date in today_list:
                if not os.path.exists(path + "/" + date):
                    os.mkdir(path + "/" + date)
                path = path + "/" + date
            return path
        except OSError:
            print('Error: Creating directory...')


    def upload_file(self):
        input = open(os.getcwd() + "/config/targets_n_sites.txt", "r")
        lines = input.readlines()
        isTarget = True
        for line in lines:
            line = line.strip()
            
            if(line == "Target"):
                isTarget = True
                continue
            elif(line == "Site"):
                isTarget = False
                continue
            elif(line == ''):
                continue
            else:
                if(isTarget):
                    info = line.split(" ")
                    self.targetSatellite.insertRow(self.targetSatellite.rowCount())
                    for i in range(info.__len__()-1):
                        self.targetSatellite.setItem(int(info[0]),i, QTableWidgetItem(info[i+1]))
                elif(~isTarget):
                    info = line.split(" ")
                    self.site.insertRow(self.site.rowCount())
                    for i in range(info.__len__()-1):
                        self.site.setItem(int(info[0]),i, QTableWidgetItem(info[i+1]))
        input.close()

    def write_new_targets_n_sites_file(self, filepath):
        file = open(filepath, "w")
        file.write("Target\n")
        for i in range(self.targetSatellite.rowCount()):
            data_list = []
            data_list.append(str(i))
            for j in range(self.targetSatellite.columnCount()):
                if(self.targetSatellite.item(i,j) == None):
                    data = ''
                else:
                    data = self.targetSatellite.item(i,j).text()
                data_list.append(data)
            file.write(" ".join(data_list))
            file.write('\n')
        file.write('\n')

        file.write("Site\n")
        for i in range(self.site.rowCount()):
            data_list = []
            data_list.append(str(i))
            for j in range(self.site.columnCount()):
                if(self.site.item(i,j) == None):
                    data = ''
                else:
                    data = self.site.item(i,j).text()
                data_list.append(data)
            file.write(" ".join(data_list))
            file.write('\n')
        file.close()

    def write_rfi_arguments_file(self, input_file_path, result_file_path):
        file = open(result_file_path, "w")
        increment_unit_time = 1
        for i in range(self.site.rowCount()):
            for j in range(self.targetSatellite.rowCount()):
                data_list = []
                data_list.append(str(-1*int(i))) #index
                data_list.append(input_file_path)
                data_list.append(str(self.startTimeInput.date().year()))
                data_list.append(str(self.startTimeInput.date().month()))
                data_list.append(str(self.startTimeInput.date().day()))
                data_list.append(str(self.startTimeInput.time().hour()))
                data_list.append(str(self.startTimeInput.time().minute()))
                data_list.append(str(self.startTimeInput.time().second()))
                data_list.append(str(self.get_window_length()))
                data_list.append(self.site.item(i, 4).text()) #cone length / cone range
                data_list.append(self.site.item(i, 5).text()) #interference angle
                data_list.append(self.site.item(i, 3).text()) #cone angle
                data_list.append(str(increment_unit_time))
                x,y,z = self.convert_lat_lon_to_ecef(float(self.site.item(i,1).text()), float(self.site.item(i,2).text()))
                data_list.append(str(x))
                data_list.append(str(y))
                data_list.append(str(z))
                data_list.append(self.targetSatellite.item(j,1).text()) #norad id
                data_list.append(result_file_path)
                file.write(" ".join(data_list) + "\n")
        file.close()

    def submit_button_click(self):
        dir = '/data'
        input_file_name = 'targets_n_sites'
        result_file_name = 'rfi_arguments'
        idx = 0
        path = self.create_folder(dir)
        input_file_path = '%s/%s_%d.txt'%(path,input_file_name,idx)
        result_file_path = '%s/%s_%d.txt'%(path,result_file_name,idx)
        while os.path.exists(input_file_path):
            idx += 1
            input_file_path = '%s/%s_%d.txt'%(path,input_file_name,idx)
            result_file_path = '%s/%s_%d.txt'%(path,result_file_name,idx)

        self.write_new_targets_n_sites_file(input_file_path)
        self.write_rfi_arguments_file(input_file_path, result_file_path)

    def target_add_click(self):
        self.targetSatellite.insertRow(self.targetSatellite.rowCount())

    def target_delete_click(self):
        self.targetSatellite.removeRow(self.targetSatellite.currentRow())

    def site_add_click(self):
        self.site.insertRow(self.site.rowCount())

    def site_delete_click(self):
        self.site.removeRow(self.site.currentRow())

    def get_window_length(self):
        startTime = datetime.strptime(self.startTimeInput.dateTime().toString("yyyy-MM-dd hh:mm:ss"), "%Y-%m-%d %H:%M:%S")
        endTime = datetime.strptime(self.endTimeInput.dateTime().toString("yyyy-MM-dd hh:mm:ss"), "%Y-%m-%d %H:%M:%S")
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
