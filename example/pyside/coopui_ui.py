# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'coopui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateTimeEdit, QDoubleSpinBox,
    QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStatusBar, QTabWidget,
    QTableView, QToolBar, QVBoxLayout, QWidget)

from COOPViewerWidget import COOPViewerWidget

class Ui_COOPViewerClass(object):
    def setupUi(self, COOPViewerClass):
        if not COOPViewerClass.objectName():
            COOPViewerClass.setObjectName(u"COOPViewerClass")
        COOPViewerClass.resize(1131, 924)
        self.centralWidget = QWidget(COOPViewerClass)
        self.centralWidget.setObjectName(u"centralWidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralWidget)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.openglWidget = COOPViewerWidget(self.centralWidget)
        self.openglWidget.setObjectName(u"openglWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openglWidget.sizePolicy().hasHeightForWidth())
        self.openglWidget.setSizePolicy(sizePolicy)
        self.openglWidget.setMinimumSize(QSize(200, 200))

        self.horizontalLayout.addWidget(self.openglWidget)

        self.tabWidget = QTabWidget(self.centralWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setMinimumSize(QSize(400, 0))
        self.tabWidget.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_load_prediction_command = QPushButton(self.groupBox)
        self.pushButton_load_prediction_command.setObjectName(u"pushButton_load_prediction_command")

        self.horizontalLayout_2.addWidget(self.pushButton_load_prediction_command)

        self.horizontalSpacer_2 = QSpacerItem(50, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(50, 16777215))
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.dateTimeEdit_currTime = QDateTimeEdit(self.groupBox_2)
        self.dateTimeEdit_currTime.setObjectName(u"dateTimeEdit_currTime")
        self.dateTimeEdit_currTime.setAlignment(Qt.AlignCenter)
        self.dateTimeEdit_currTime.setDateTime(QDateTime(QDate(2021, 3, 6), QTime(0, 0, 0)))
        self.dateTimeEdit_currTime.setDate(QDate(2021, 3, 6))

        self.horizontalLayout_3.addWidget(self.dateTimeEdit_currTime)

        self.pushButton_go_to_time = QPushButton(self.groupBox_2)
        self.pushButton_go_to_time.setObjectName(u"pushButton_go_to_time")
        self.pushButton_go_to_time.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_3.addWidget(self.pushButton_go_to_time)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_go_to_start = QPushButton(self.groupBox_2)
        self.pushButton_go_to_start.setObjectName(u"pushButton_go_to_start")
        self.pushButton_go_to_start.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_4.addWidget(self.pushButton_go_to_start)

        self.pushButton_rewind = QPushButton(self.groupBox_2)
        self.pushButton_rewind.setObjectName(u"pushButton_rewind")
        self.pushButton_rewind.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_4.addWidget(self.pushButton_rewind)

        self.pushButton_play = QPushButton(self.groupBox_2)
        self.pushButton_play.setObjectName(u"pushButton_play")
        self.pushButton_play.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_4.addWidget(self.pushButton_play)

        self.pushButton_forward = QPushButton(self.groupBox_2)
        self.pushButton_forward.setObjectName(u"pushButton_forward")
        self.pushButton_forward.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_4.addWidget(self.pushButton_forward)

        self.pushButton_go_to_end = QPushButton(self.groupBox_2)
        self.pushButton_go_to_end.setObjectName(u"pushButton_go_to_end")
        self.pushButton_go_to_end.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_4.addWidget(self.pushButton_go_to_end)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.spinBox_stepSize_hour = QSpinBox(self.groupBox_2)
        self.spinBox_stepSize_hour.setObjectName(u"spinBox_stepSize_hour")
        self.spinBox_stepSize_hour.setMaximumSize(QSize(50, 16777215))
        self.spinBox_stepSize_hour.setAlignment(Qt.AlignCenter)
        self.spinBox_stepSize_hour.setMaximum(24)

        self.horizontalLayout_5.addWidget(self.spinBox_stepSize_hour)

        self.spinBox_stepSize_min = QSpinBox(self.groupBox_2)
        self.spinBox_stepSize_min.setObjectName(u"spinBox_stepSize_min")
        self.spinBox_stepSize_min.setMaximumSize(QSize(50, 16777215))
        self.spinBox_stepSize_min.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.spinBox_stepSize_min)

        self.doubleSpinBox_stepSize_sec = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_stepSize_sec.setObjectName(u"doubleSpinBox_stepSize_sec")
        self.doubleSpinBox_stepSize_sec.setMaximumSize(QSize(50, 16777215))
        self.doubleSpinBox_stepSize_sec.setDecimals(1)
        self.doubleSpinBox_stepSize_sec.setMinimum(0.100000000000000)
        self.doubleSpinBox_stepSize_sec.setValue(10.000000000000000)

        self.horizontalLayout_5.addWidget(self.doubleSpinBox_stepSize_sec)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.formLayout = QFormLayout(self.groupBox_3)
        self.formLayout.setSpacing(6)
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setObjectName(u"formLayout")
        self.radioButton_selectPPDB = QRadioButton(self.groupBox_3)
        self.radioButton_selectPPDB.setObjectName(u"radioButton_selectPPDB")
        self.radioButton_selectPPDB.setChecked(True)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.radioButton_selectPPDB)

        self.radioButton_selectTPDB = QRadioButton(self.groupBox_3)
        self.radioButton_selectTPDB.setObjectName(u"radioButton_selectTPDB")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.radioButton_selectTPDB)

        self.radioButton_selectSPDB = QRadioButton(self.groupBox_3)
        self.radioButton_selectSPDB.setObjectName(u"radioButton_selectSPDB")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.radioButton_selectSPDB)

        self.radioButton_selectSafetyEval = QRadioButton(self.groupBox_3)
        self.radioButton_selectSafetyEval.setObjectName(u"radioButton_selectSafetyEval")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.radioButton_selectSafetyEval)

        self.radioButton_selectCN = QRadioButton(self.groupBox_3)
        self.radioButton_selectCN.setObjectName(u"radioButton_selectCN")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.radioButton_selectCN)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.ooiBox = QGroupBox(self.tab)
        self.ooiBox.setObjectName(u"ooiBox")
        self.verticalLayout_3 = QVBoxLayout(self.ooiBox)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_5 = QGroupBox(self.ooiBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_2 = QGridLayout(self.groupBox_5)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.groupBox_5)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.q1_distance = QLineEdit(self.groupBox_5)
        self.q1_distance.setObjectName(u"q1_distance")

        self.gridLayout_2.addWidget(self.q1_distance, 3, 0, 1, 1)

        self.q1_id = QLineEdit(self.groupBox_5)
        self.q1_id.setObjectName(u"q1_id")

        self.gridLayout_2.addWidget(self.q1_id, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.groupBox_5)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 3, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_5)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.ooiBox)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout = QGridLayout(self.groupBox_6)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.q2_distance = QLineEdit(self.groupBox_6)
        self.q2_distance.setObjectName(u"q2_distance")

        self.gridLayout.addWidget(self.q2_distance, 1, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.groupBox_6)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_6)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_6)


        self.verticalLayout.addWidget(self.ooiBox)

        self.q4Box = QGroupBox(self.tab)
        self.q4Box.setObjectName(u"q4Box")
        self.gridLayout_4 = QGridLayout(self.q4Box)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.q4_n = QRadioButton(self.q4Box)
        self.q4_n.setObjectName(u"q4_n")
        self.q4_n.setChecked(True)

        self.gridLayout_4.addWidget(self.q4_n, 0, 1, 1, 1)

        self.q4_c = QRadioButton(self.q4Box)
        self.q4_c.setObjectName(u"q4_c")

        self.gridLayout_4.addWidget(self.q4_c, 0, 3, 1, 1)

        self.q4_b = QRadioButton(self.q4Box)
        self.q4_b.setObjectName(u"q4_b")

        self.gridLayout_4.addWidget(self.q4_b, 0, 2, 1, 1)

        self.checkBox = QCheckBox(self.q4Box)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)

        self.gridLayout_4.addWidget(self.checkBox, 1, 1, 1, 1)

        self.checkBox_2 = QCheckBox(self.q4Box)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setChecked(False)

        self.gridLayout_4.addWidget(self.checkBox_2, 1, 2, 1, 1)


        self.verticalLayout.addWidget(self.q4Box)

        self.label_printStatus = QLabel(self.tab)
        self.label_printStatus.setObjectName(u"label_printStatus")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_printStatus.sizePolicy().hasHeightForWidth())
        self.label_printStatus.setSizePolicy(sizePolicy2)
        self.label_printStatus.setMinimumSize(QSize(400, 10))
        self.label_printStatus.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout.addWidget(self.label_printStatus)

        self.label_summary = QLabel(self.tab)
        self.label_summary.setObjectName(u"label_summary")
        sizePolicy.setHeightForWidth(self.label_summary.sizePolicy().hasHeightForWidth())
        self.label_summary.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_summary)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab, "")
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        self.verticalLayout_6 = QVBoxLayout(self.tab2)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tabWidget.addTab(self.tab2, "")

        self.horizontalLayout.addWidget(self.tabWidget)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.tabWidget_2 = QTabWidget(self.centralWidget)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy3)
        self.tabWidget_2.setMinimumSize(QSize(0, 50))
        self.tabWidget_2.setMaximumSize(QSize(16777215, 200))
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_3 = QGridLayout(self.tab_3)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tableView_TPDBData = QTableView(self.tab_3)
        self.tableView_TPDBData.setObjectName(u"tableView_TPDBData")

        self.gridLayout_3.addWidget(self.tableView_TPDBData, 1, 2, 1, 1)

        self.tableView_PPDBData = QTableView(self.tab_3)
        self.tableView_PPDBData.setObjectName(u"tableView_PPDBData")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tableView_PPDBData.sizePolicy().hasHeightForWidth())
        self.tableView_PPDBData.setSizePolicy(sizePolicy4)
        self.tableView_PPDBData.verticalHeader().setProperty("showSortIndicator", True)

        self.gridLayout_3.addWidget(self.tableView_PPDBData, 1, 1, 1, 1)

        self.label_6 = QLabel(self.tab_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 0, 1, 1, 1)

        self.label_7 = QLabel(self.tab_3)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 0, 2, 1, 1)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget_2.addTab(self.tab_4, "")

        self.verticalLayout_4.addWidget(self.tabWidget_2)

        COOPViewerClass.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(COOPViewerClass)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1131, 22))
        COOPViewerClass.setMenuBar(self.menuBar)
        self.mainToolBar = QToolBar(COOPViewerClass)
        self.mainToolBar.setObjectName(u"mainToolBar")
        COOPViewerClass.addToolBar(Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QStatusBar(COOPViewerClass)
        self.statusBar.setObjectName(u"statusBar")
        COOPViewerClass.setStatusBar(self.statusBar)

        self.retranslateUi(COOPViewerClass)
        self.pushButton_load_prediction_command.clicked.connect(COOPViewerClass.load_prediction_command)
        self.pushButton_play.clicked.connect(COOPViewerClass.play_simulation)
        self.spinBox_stepSize_hour.valueChanged.connect(COOPViewerClass.time_step_changed)
        self.spinBox_stepSize_min.valueChanged.connect(COOPViewerClass.time_step_changed)
        self.doubleSpinBox_stepSize_sec.valueChanged.connect(COOPViewerClass.time_step_changed)
        self.pushButton_forward.clicked.connect(COOPViewerClass.increase_time_by_step)
        self.pushButton_rewind.clicked.connect(COOPViewerClass.decrease_time_by_step)
        self.pushButton_go_to_start.clicked.connect(COOPViewerClass.go_to_start_moment)
        self.pushButton_go_to_end.clicked.connect(COOPViewerClass.go_to_end_moment)
        self.radioButton_selectPPDB.clicked.connect(COOPViewerClass.mode_selection_changed)
        self.radioButton_selectTPDB.clicked.connect(COOPViewerClass.mode_selection_changed)
        self.radioButton_selectSPDB.clicked.connect(COOPViewerClass.mode_selection_changed)
        self.radioButton_selectSafetyEval.clicked.connect(COOPViewerClass.mode_selection_changed)
        self.tableView_PPDBData.doubleClicked.connect(COOPViewerClass.update_PPDB_selection_in_table)
        self.tableView_TPDBData.doubleClicked.connect(COOPViewerClass.update_TPDB_selection_in_table)
        self.pushButton.clicked.connect(COOPViewerClass.objectOfInterest_changed)
        self.pushButton_2.clicked.connect(COOPViewerClass.objectOfInterest_changed)
        self.pushButton.clicked.connect(COOPViewerClass.update_PPDB_n_TPDB_table_Q1)
        self.pushButton_2.clicked.connect(COOPViewerClass.update_PPDB_n_TPDB_table_Q2)
        self.q4_n.clicked.connect(COOPViewerClass.space_center_selection_changed_Q4)
        self.q4_b.clicked.connect(COOPViewerClass.space_center_selection_changed_Q4)
        self.q4_c.clicked.connect(COOPViewerClass.space_center_selection_changed_Q4)
        self.radioButton_selectCN.clicked.connect(COOPViewerClass.mode_selection_changed)
        self.checkBox.clicked.connect(COOPViewerClass.on_all_RSOs)
        self.checkBox_2.clicked.connect(COOPViewerClass.on_criticial_RSOs)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(COOPViewerClass)
    # setupUi

    def retranslateUi(self, COOPViewerClass):
        COOPViewerClass.setWindowTitle(QCoreApplication.translate("COOPViewerClass", u"COOPViewer", None))
        self.groupBox.setTitle(QCoreApplication.translate("COOPViewerClass", u"Load Files", None))
        self.pushButton_load_prediction_command.setText(QCoreApplication.translate("COOPViewerClass", u"1. Load Results", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("COOPViewerClass", u"Control", None))
        self.label.setText(QCoreApplication.translate("COOPViewerClass", u"Time", None))
        self.dateTimeEdit_currTime.setDisplayFormat(QCoreApplication.translate("COOPViewerClass", u"MM-dd-yyyy hh:mm:ss", None))
        self.pushButton_go_to_time.setText(QCoreApplication.translate("COOPViewerClass", u"Go", None))
        self.pushButton_go_to_start.setText(QCoreApplication.translate("COOPViewerClass", u"|\u25c0", None))
        self.pushButton_rewind.setText(QCoreApplication.translate("COOPViewerClass", u"\u25c0\u25c0", None))
        self.pushButton_play.setText(QCoreApplication.translate("COOPViewerClass", u"\u25b6/||", None))
        self.pushButton_forward.setText(QCoreApplication.translate("COOPViewerClass", u"\u25b6\u25b6", None))
        self.pushButton_go_to_end.setText(QCoreApplication.translate("COOPViewerClass", u"\u25b6|", None))
        self.label_2.setText(QCoreApplication.translate("COOPViewerClass", u"Play speed", None))
        self.spinBox_stepSize_hour.setSuffix(QCoreApplication.translate("COOPViewerClass", u" h", None))
        self.spinBox_stepSize_min.setSuffix(QCoreApplication.translate("COOPViewerClass", u" m", None))
        self.doubleSpinBox_stepSize_sec.setSuffix(QCoreApplication.translate("COOPViewerClass", u" s", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("COOPViewerClass", u"COOP Queries", None))
        self.radioButton_selectPPDB.setText(QCoreApplication.translate("COOPViewerClass", u"PPDB", None))
        self.radioButton_selectTPDB.setText(QCoreApplication.translate("COOPViewerClass", u"TPDB", None))
        self.radioButton_selectSPDB.setText(QCoreApplication.translate("COOPViewerClass", u"Q3 [Shortest Path]", None))
        self.radioButton_selectSafetyEval.setText(QCoreApplication.translate("COOPViewerClass", u"Q4 [Safety Evaluation]", None))
        self.radioButton_selectCN.setText(QCoreApplication.translate("COOPViewerClass", u"Q* [Closest Neighbors]", None))
        self.ooiBox.setTitle(QCoreApplication.translate("COOPViewerClass", u"Object of Interest", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("COOPViewerClass", u"Q1.", None))
        self.label_3.setText(QCoreApplication.translate("COOPViewerClass", u"Catalog ID", None))
        self.pushButton.setText(QCoreApplication.translate("COOPViewerClass", u"Submit", None))
        self.label_5.setText(QCoreApplication.translate("COOPViewerClass", u"Cut Off Distance (km)", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("COOPViewerClass", u"Q2.", None))
        self.pushButton_2.setText(QCoreApplication.translate("COOPViewerClass", u"Submit", None))
        self.label_4.setText(QCoreApplication.translate("COOPViewerClass", u"Cut Off Distance (km)", None))
        self.q4Box.setTitle(QCoreApplication.translate("COOPViewerClass", u"Q4. [Select Space Center]", None))
        self.q4_n.setText(QCoreApplication.translate("COOPViewerClass", u"\ub098\ub85c \uc6b0\uc8fc\uc13c\ud130", None))
        self.q4_c.setText(QCoreApplication.translate("COOPViewerClass", u"Cape Canaveral", None))
        self.q4_b.setText(QCoreApplication.translate("COOPViewerClass", u"Boca Chica", None))
        self.checkBox.setText(QCoreApplication.translate("COOPViewerClass", u"All RSOs", None))
        self.checkBox_2.setText(QCoreApplication.translate("COOPViewerClass", u"Critical RSOs", None))
        self.label_printStatus.setText(QCoreApplication.translate("COOPViewerClass", u"Welcome to COOP Program.", None))
        self.label_summary.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("COOPViewerClass", u"Viewer Controller", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), QCoreApplication.translate("COOPViewerClass", u"Tab 2", None))
        self.label_6.setText(QCoreApplication.translate("COOPViewerClass", u"PPDB", None))
        self.label_7.setText(QCoreApplication.translate("COOPViewerClass", u"TPDB", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("COOPViewerClass", u"PPDB & TPDB Data", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("COOPViewerClass", u"Tab 2", None))
    # retranslateUi

