from PyQt5.QtCore import Qt

import communication
from home import *

EMERGENCY_STOP_ACTIVE = 'A01001'
EMERGENCY_STOP_INACTIVE = 'A01000'
FEED_RATE_DATA = 'A02'
CYCLE_START_ACTIVE = 'A03001'
CYCLE_START_INACTIVE = 'A03000'
CYCLE_STOP_ACTIVE = 'A04001'
CYCLE_STOP_INACTIVE = 'A04000'
DRV_ACTIVE = 'B01001'
DRV_INACTIVE = 'B01000'
Z_LOCK_ACTIVE = 'B02001'
Z_LOCK_INACTIVE = 'B02000'
DRY_RUN_ACTIVE = 'B03001'
DRY_RUN_INACTIVE = 'B03000'
JOG_ACTIVE = 'B04001'
JOG_INACTIVE = 'B04000'
MDI_ACTIVE = 'B05001'
MDI_INACTIVE = 'B05000'
AUTO_ACTIVE = 'B06001'
AUTO_INACTIVE = 'B06000'
X_ACTIVE = 'B07001'
X_INACTIVE = 'B07000'
Y_ACTIVE = 'B08001'
Y_INACTIVE = 'B08000'
Z_ACTIVE = 'B09001'
Z_INACTIVE = 'B09000'
PLUS_ACTIVE = 'B10001'
PLUS_INACTIVE = 'B10000'
VVV_ACTIVE = 'B11001'
VVV_INACTIVE = 'B11000'
MINUS_ACTIVE = 'B12001'
MINUS_INACTIVE = 'B12000'
NC_REF_ACTIVE = 'C01001'
NC_REF_INACTIVE = 'C01000'
RET_FOR_ACTIVE = 'C02001'
RET_FOR_INACTIVE = 'C02000'
RET_REV_ACTIVE = 'C03001'
RET_REV_INACTIVE = 'C03000'
RET_ON_ACTIVE = 'C04001'
RET_ON_INACTIVE = 'C04000'
PRC_END_ACTIVE = 'D01001'
PRC_END_INACTIVE = 'D01000'
ALM_OVR_ACTIVE = 'D02001'
ALM_OVR_INACTIVE = 'D02000'
ALM_RST_ACTIVE = 'D03001'
ALM_RST_INACTIVE = 'D03000'
LOCK_RST_ACTIVE = 'D04001'
LOCK_RST_INACTIVE = 'D04000'
LASER_ON_ACTIVE = 'E01001'
LASER_ON_INACTIVE = 'E01000'
LASER_READY_ACTIVE = 'E02001'
LASER_READY_INACTIVE = 'E02000'


def clicked_action(send_data):
    communication.write_data(send_data)
    print(send_data)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowFlags(Qt.FramelessWindowHint)
    MainWindow.showFullScreen()
    # Press Alt+F4 to close the window
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    def auto_enablement():
        ui.jogButton.setChecked(False)
        ui.mdiButton.setChecked(False)
        jog_enablement()
        x_jog_movement_enablement()
        y_jog_movement_enablement()
        z_jog_movement_enablement()

    def mdi_enablement():
        ui.jogButton.setChecked(False)
        ui.autoButton.setChecked(False)
        jog_enablement()
        x_jog_movement_enablement()
        y_jog_movement_enablement()
        z_jog_movement_enablement()

    def jog_enablement():
        if ui.jogButton.isChecked():
            ui.xButton.setEnabled(True)
            ui.yButton.setEnabled(True)
            ui.zButton.setEnabled(True)
            ui.mdiButton.setChecked(False)
            ui.autoButton.setChecked(False)
        else:
            ui.xButton.setChecked(False)
            ui.yButton.setChecked(False)
            ui.zButton.setChecked(False)
            ui.xButton.setEnabled(False)
            ui.yButton.setEnabled(False)
            ui.zButton.setEnabled(False)
            ui.plusButton.setEnabled(False)
            ui.vvvButton.setChecked(False)
            ui.vvvButton.setEnabled(False)
            ui.minusButton.setEnabled(False)

    def x_jog_movement_enablement():
        if ui.xButton.isChecked():
            ui.plusButton.setEnabled(True)
            ui.vvvButton.setEnabled(True)
            ui.minusButton.setEnabled(True)
            ui.yButton.setChecked(False)
            ui.zButton.setChecked(False)
        else:
            ui.plusButton.setEnabled(False)
            ui.vvvButton.setChecked(False)
            ui.vvvButton.setEnabled(False)
            ui.minusButton.setEnabled(False)

    def y_jog_movement_enablement():
        if ui.yButton.isChecked():
            ui.plusButton.setEnabled(True)
            ui.vvvButton.setEnabled(True)
            ui.minusButton.setEnabled(True)
            ui.xButton.setChecked(False)
            ui.zButton.setChecked(False)
        else:
            ui.plusButton.setEnabled(False)
            ui.vvvButton.setChecked(False)
            ui.vvvButton.setEnabled(False)
            ui.minusButton.setEnabled(False)

    def z_jog_movement_enablement():
        if ui.zButton.isChecked():
            ui.plusButton.setEnabled(True)
            ui.vvvButton.setEnabled(True)
            ui.minusButton.setEnabled(True)
            ui.yButton.setChecked(False)
            ui.xButton.setChecked(False)
        else:
            ui.plusButton.setEnabled(False)
            ui.vvvButton.setChecked(False)
            ui.vvvButton.setEnabled(False)
            ui.minusButton.setEnabled(False)

    # set up momentary push buttons as by default push buttons have latching action
    # set up push button enablement logic
    jog_enablement()
    x_jog_movement_enablement()
    y_jog_movement_enablement()
    z_jog_movement_enablement()
    ui.jogButton.clicked.connect(lambda: jog_enablement())
    ui.xButton.clicked.connect(lambda: x_jog_movement_enablement())
    ui.yButton.clicked.connect(lambda: y_jog_movement_enablement())
    ui.zButton.clicked.connect(lambda: z_jog_movement_enablement())
    ui.mdiButton.clicked.connect(lambda: mdi_enablement())
    ui.autoButton.clicked.connect(lambda: auto_enablement())
    # communication.connect_ethercat()
    # ui.drvButton.clicked.connect(lambda: drv_clicked())
    MainWindow.show()
    sys.exit(app.exec_())
