# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WatcherCatcher.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QDialog, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(900, 681)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 10, 910, 671))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_18)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.targetSatellite = QTableWidget(self.widget)
        if (self.targetSatellite.columnCount() < 2):
            self.targetSatellite.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.targetSatellite.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.targetSatellite.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.targetSatellite.rowCount() < 1):
            self.targetSatellite.setRowCount(1)
        self.targetSatellite.setObjectName(u"targetSatellite")
        self.targetSatellite.setMinimumSize(QSize(200, 0))
        self.targetSatellite.setMaximumSize(QSize(16777215, 200))
        font = QFont()
        font.setPointSize(15)
        font.setBold(False)
        self.targetSatellite.setFont(font)

        self.verticalLayout_6.addWidget(self.targetSatellite)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_19)

        self.targetAddButton = QPushButton(self.widget)
        self.targetAddButton.setObjectName(u"targetAddButton")
        self.targetAddButton.setMaximumSize(QSize(100, 40))

        self.horizontalLayout_3.addWidget(self.targetAddButton, 0, Qt.AlignVCenter)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line)

        self.targetDeleteButton = QPushButton(self.widget)
        self.targetDeleteButton.setObjectName(u"targetDeleteButton")
        self.targetDeleteButton.setMaximumSize(QSize(100, 40))

        self.horizontalLayout_3.addWidget(self.targetDeleteButton, 0, Qt.AlignVCenter)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_20)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.site = QTableWidget(self.widget)
        if (self.site.columnCount() < 6):
            self.site.setColumnCount(6)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.site.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.site.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.site.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.site.setHorizontalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.site.setHorizontalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.site.setHorizontalHeaderItem(5, __qtablewidgetitem7)
        if (self.site.rowCount() < 1):
            self.site.setRowCount(1)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        self.site.setItem(0, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        self.site.setItem(0, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        self.site.setItem(0, 2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        self.site.setItem(0, 3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        self.site.setItem(0, 4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        self.site.setItem(0, 5, __qtablewidgetitem13)
        self.site.setObjectName(u"site")
        self.site.setMinimumSize(QSize(450, 0))
        self.site.setMaximumSize(QSize(16777215, 200))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(235, 235, 235, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        brush3 = QBrush(QColor(192, 192, 192, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush3)
        brush4 = QBrush(QColor(170, 170, 170, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        brush5 = QBrush(QColor(255, 255, 220, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush5)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.site.setPalette(palette)
        self.site.setFont(font)
        self.site.setStyleSheet(u"")
        self.site.setRowCount(1)

        self.verticalLayout_8.addWidget(self.site)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_14)

        self.siteAddButton = QPushButton(self.widget)
        self.siteAddButton.setObjectName(u"siteAddButton")
        self.siteAddButton.setMaximumSize(QSize(100, 40))

        self.horizontalLayout_6.addWidget(self.siteAddButton, 0, Qt.AlignVCenter)

        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_6.addWidget(self.line_2)

        self.siteDeleteButton = QPushButton(self.widget)
        self.siteDeleteButton.setObjectName(u"siteDeleteButton")
        self.siteDeleteButton.setMaximumSize(QSize(100, 40))

        self.horizontalLayout_6.addWidget(self.siteDeleteButton, 0, Qt.AlignVCenter)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_2.addLayout(self.verticalLayout_8)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_21)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")

        self.horizontalLayout_2.addLayout(self.verticalLayout_7)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_22)

        self.startTime = QLabel(self.widget)
        self.startTime.setObjectName(u"startTime")
        self.startTime.setMinimumSize(QSize(150, 30))
        self.startTime.setMaximumSize(QSize(180, 16777215))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(False)
        self.startTime.setFont(font1)

        self.horizontalLayout_24.addWidget(self.startTime)

        self.startTimeInput = QDateTimeEdit(self.widget)
        self.startTimeInput.setObjectName(u"startTimeInput")
        self.startTimeInput.setMinimumSize(QSize(220, 35))
        self.startTimeInput.setMaximumSize(QSize(220, 35))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        self.startTimeInput.setPalette(palette1)
        self.startTimeInput.setCursor(QCursor(Qt.ArrowCursor))
        self.startTimeInput.setStyleSheet(u"")
        self.startTimeInput.setDateTime(QDateTime(QDate(2002, 12, 28), QTime(15, 0, 1)))
        self.startTimeInput.setCurrentSection(QDateTimeEdit.YearSection)
        self.startTimeInput.setCalendarPopup(True)
        self.startTimeInput.setTimeSpec(Qt.UTC)

        self.horizontalLayout_24.addWidget(self.startTimeInput)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_23)


        self.verticalLayout_4.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_24)

        self.entTime = QLabel(self.widget)
        self.entTime.setObjectName(u"entTime")
        self.entTime.setMinimumSize(QSize(150, 30))
        self.entTime.setMaximumSize(QSize(180, 16777215))
        self.entTime.setFont(font1)

        self.horizontalLayout_27.addWidget(self.entTime)

        self.endTimeInput = QDateTimeEdit(self.widget)
        self.endTimeInput.setObjectName(u"endTimeInput")
        self.endTimeInput.setMinimumSize(QSize(220, 35))
        self.endTimeInput.setMaximumSize(QSize(220, 35))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        self.endTimeInput.setPalette(palette2)
        self.endTimeInput.setStyleSheet(u"")
        self.endTimeInput.setDateTime(QDateTime(QDate(2002, 12, 28), QTime(15, 0, 0)))
        self.endTimeInput.setCalendarPopup(True)
        self.endTimeInput.setTimeSpec(Qt.UTC)

        self.horizontalLayout_27.addWidget(self.endTimeInput)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_25)


        self.verticalLayout_4.addLayout(self.horizontalLayout_27)


        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.submitButton = QPushButton(self.widget)
        self.submitButton.setObjectName(u"submitButton")
        self.submitButton.setMinimumSize(QSize(130, 45))
        self.submitButton.setMaximumSize(QSize(130, 45))
        self.submitButton.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.submitButton, 0, Qt.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        ___qtablewidgetitem = self.targetSatellite.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Name", None));
        ___qtablewidgetitem1 = self.targetSatellite.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"NORAD ID", None));
        self.targetAddButton.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.targetDeleteButton.setText(QCoreApplication.translate("Dialog", u"Delete", None))
        ___qtablewidgetitem2 = self.site.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Name", None));
        ___qtablewidgetitem3 = self.site.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Lat", None));
        ___qtablewidgetitem4 = self.site.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"Lon", None));
        ___qtablewidgetitem5 = self.site.horizontalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"Cone Angle(deg)", None));
        ___qtablewidgetitem6 = self.site.horizontalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", u"Cone Range(km)", None));
        ___qtablewidgetitem7 = self.site.horizontalHeaderItem(5)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dialog", u"Interference Angle(deg)", None));

        __sortingEnabled = self.site.isSortingEnabled()
        self.site.setSortingEnabled(False)
        self.site.setSortingEnabled(__sortingEnabled)

        self.siteAddButton.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.siteDeleteButton.setText(QCoreApplication.translate("Dialog", u"Delete", None))
        self.startTime.setText(QCoreApplication.translate("Dialog", u"Start Time(UTC):", None))
        self.entTime.setText(QCoreApplication.translate("Dialog", u"End Time(UTC):", None))
        self.submitButton.setText(QCoreApplication.translate("Dialog", u"Submit", None))
    # retranslateUi

