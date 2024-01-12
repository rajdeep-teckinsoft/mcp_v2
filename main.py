from PyQt5.QtCore import Qt

import communication
from home import *
from time import sleep

MOMENTARY_SWITCH_ON_TIME_SEC = 0.2

# 1st column of keys
CYCLE_START_ACTIVE = 1
CYCLE_START_INACTIVE = 2

# 2nd column of keys
CYCLE_STOP_ACTIVE = 3
CYCLE_STOP_INACTIVE = 4

# 3rd column of keys
DRV_ACTIVE = '5'
DRV_INACTIVE = '6'
JOG_ACTIVE = 7
JOG_INACTIVE = 8
X_ACTIVE = 9
X_INACTIVE = 10
PLUS_ACTIVE = 11
PLUS_INACTIVE = 12

# 4th column of keys
Z_LOCK_ACTIVE = 13
Z_LOCK_INACTIVE = 14
MDI_ACTIVE = 15
MDI_INACTIVE = 16
Y_ACTIVE = 17
Y_INACTIVE = 18
VVV_ACTIVE = 19
VVV_INACTIVE = 20

# 5th column of keys
DRY_RUN_ACTIVE = 21
DRY_RUN_INACTIVE = 22
AUTO_ACTIVE = 23
AUTO_INACTIVE = 24
Z_ACTIVE = 25
Z_INACTIVE = 26
MINUS_ACTIVE = 27
MINUS_INACTIVE = 28

# 6th column of keys
NC_REF_ACTIVE = 29
NC_REF_INACTIVE = 30
NC_OFF_ACTIVE = 31
NC_OFF_INACTIVE = 32
RET_FOR_ACTIVE = 33
RET_FOR_INACTIVE = 34
RET_REV_ACTIVE = 35
RET_REV_INACTIVE = 36

# 7th column of keys
PRC_END_ACTIVE = 37
PRC_END_INACTIVE = 38
ALM_OVR_ACTIVE = 39
ALM_OVR_INACTIVE = 40
ALM_RST_ACTIVE = 41
ALM_RST_INACTIVE = 42
LOCK_RST_ACTIVE = 43
LOCK_RST_INACTIVE = 44

# 8th column of keys
LASER_ON_ACTIVE = 45
LASER_ON_INACTIVE = 46

serial_connected = False


def clicked_action(send_data):
    if serial_connected:
        communication.write_data(send_data)
    if __debug__:
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

    # set up UI logics--------------------------------------------------
    def auto_ui_logic():
        ui.jogButton.setChecked(False)
        ui.mdiButton.setChecked(False)
        jog_ui_logic()
        x_jog_ui_logic()
        y_jog_ui_logic()
        z_jog_ui_logic()

    def mdi_ui_logic():
        ui.jogButton.setChecked(False)
        ui.autoButton.setChecked(False)
        jog_ui_logic()
        x_jog_ui_logic()
        y_jog_ui_logic()
        z_jog_ui_logic()

    def jog_ui_logic():
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

    def x_jog_ui_logic():
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

    def y_jog_ui_logic():
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

    def z_jog_ui_logic():
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


    jog_ui_logic()
    x_jog_ui_logic()
    y_jog_ui_logic()
    z_jog_ui_logic()
    ui.jogButton.clicked.connect(lambda: jog_ui_logic())
    ui.xButton.clicked.connect(lambda: x_jog_ui_logic())
    ui.yButton.clicked.connect(lambda: y_jog_ui_logic())
    ui.zButton.clicked.connect(lambda: z_jog_ui_logic())
    ui.mdiButton.clicked.connect(lambda: mdi_ui_logic())
    ui.autoButton.clicked.connect(lambda: auto_ui_logic())

    # set up push button functions---------------------------------------
    serial_connected = communication.connect_ethercat()
    if __debug__:
        if serial_connected:
            print("Serial is connected")
        else:
            print("Serial is not connected. Please check!")

    def cycle_start_function():
        clicked_action(CYCLE_START_ACTIVE)
        sleep(MOMENTARY_SWITCH_ON_TIME_SEC)
        clicked_action(CYCLE_START_INACTIVE)

    def cycle_stop_function():
        clicked_action(CYCLE_STOP_ACTIVE)
        sleep(MOMENTARY_SWITCH_ON_TIME_SEC)
        clicked_action(CYCLE_STOP_INACTIVE)

    def drv_function():
        if ui.drvButton.isChecked():
            clicked_action(DRV_ACTIVE)
        else:
            clicked_action(DRV_INACTIVE)

    def z_lock_function():
        if ui.zLockButton.isChecked():
            clicked_action(Z_LOCK_ACTIVE)
        else:
            clicked_action(Z_LOCK_INACTIVE)

    def dry_run_function():
        if ui.dryRunButton.isChecked():
            clicked_action(DRY_RUN_ACTIVE)
        else:
            clicked_action(DRY_RUN_INACTIVE)

    def jog_function():
        if ui.jogButton.isChecked():
            clicked_action(JOG_ACTIVE)
        else:
            clicked_action(JOG_INACTIVE)

    def mdi_function():
        if ui.mdiButton.isChecked():
            clicked_action(MDI_ACTIVE)
        else:
            clicked_action(MDI_INACTIVE)

    def auto_function():
        if ui.autoButton.isChecked():
            clicked_action(AUTO_ACTIVE)
        else:
            clicked_action(AUTO_INACTIVE)

    def x_jog_function():
        if ui.xButton.isChecked():
            clicked_action(X_ACTIVE)
        else:
            clicked_action(X_INACTIVE)

    def y_jog_function():
        if ui.yButton.isChecked():
            clicked_action(Y_ACTIVE)
        else:
            clicked_action(Y_INACTIVE)

    def z_jog_function():
        if ui.zButton.isChecked():
            clicked_action(Z_ACTIVE)
        else:
            clicked_action(Z_INACTIVE)

    def plus_jog_function():
        clicked_action(PLUS_ACTIVE)
        sleep(MOMENTARY_SWITCH_ON_TIME_SEC)
        clicked_action(PLUS_INACTIVE)

    def minus_jog_function():
        clicked_action(MINUS_ACTIVE)
        sleep(MOMENTARY_SWITCH_ON_TIME_SEC)
        clicked_action(MINUS_INACTIVE)

    def vvv_jog_function():
        if ui.vvvButton.isChecked():
            clicked_action(VVV_ACTIVE)
        else:
            clicked_action(VVV_INACTIVE)

    def nc_ref_function():
        if ui.ncRefButton.isChecked():
            clicked_action(NC_REF_ACTIVE)
        else:
            clicked_action(NC_REF_INACTIVE)

    def nc_offset_function():
        if ui.ncOffsetButton.isChecked():
            clicked_action(NC_OFF_ACTIVE)
        else:
            clicked_action(NC_OFF_INACTIVE)

    def ret_for_function():
        clicked_action(RET_FOR_ACTIVE)
        sleep(MOMENTARY_SWITCH_ON_TIME_SEC)
        clicked_action(RET_FOR_INACTIVE)

    def ret_rev_function():
        clicked_action(RET_REV_ACTIVE)
        sleep(MOMENTARY_SWITCH_ON_TIME_SEC)
        clicked_action(RET_REV_INACTIVE)

    def prc_end_function():
        clicked_action(PRC_END_ACTIVE)
        sleep(MOMENTARY_SWITCH_ON_TIME_SEC)
        clicked_action(PRC_END_INACTIVE)

    def alm_ovr_function():
        clicked_action(ALM_OVR_ACTIVE)
        sleep(MOMENTARY_SWITCH_ON_TIME_SEC)
        clicked_action(ALM_OVR_INACTIVE)

    def alm_rst_function():
        clicked_action(ALM_RST_ACTIVE)
        sleep(MOMENTARY_SWITCH_ON_TIME_SEC)
        clicked_action(ALM_RST_INACTIVE)

    def lock_rst_function():
        clicked_action(LOCK_RST_ACTIVE)
        sleep(MOMENTARY_SWITCH_ON_TIME_SEC)
        clicked_action(LOCK_RST_INACTIVE)

    def laser_on_function():
        if ui.laserOnButton.isChecked():
            clicked_action(LASER_ON_ACTIVE)
        else:
            clicked_action(LASER_ON_INACTIVE)

    ui.cycleStartButton.clicked.connect(lambda: cycle_start_function())
    ui.cycleStopButton.clicked.connect(lambda: cycle_stop_function())
    ui.drvButton.clicked.connect(lambda: drv_function())
    ui.zLockButton.clicked.connect(lambda: z_lock_function())
    ui.dryRunButton.clicked.connect(lambda: dry_run_function())
    ui.jogButton.clicked.connect(lambda: jog_function())
    ui.mdiButton.clicked.connect(lambda: mdi_function())
    ui.autoButton.clicked.connect(lambda: auto_function())
    ui.xButton.clicked.connect(lambda: x_jog_function())
    ui.yButton.clicked.connect(lambda: y_jog_function())
    ui.zButton.clicked.connect(lambda: z_jog_function())
    ui.plusButton.clicked.connect(lambda: plus_jog_function())
    ui.vvvButton.clicked.connect(lambda: vvv_jog_function())
    ui.minusButton.clicked.connect(lambda: minus_jog_function())
    ui.ncRefButton.clicked.connect(lambda: nc_ref_function())
    ui.ncOffsetButton.clicked.connect(lambda: nc_offset_function())
    ui.retForButton.clicked.connect(lambda: ret_for_function())
    ui.retRevButton.clicked.connect(lambda: ret_rev_function())
    ui.prcEndButton.clicked.connect(lambda: prc_end_function())
    ui.almOvrButton.clicked.connect(lambda: alm_ovr_function())
    ui.almRstButton.clicked.connect(lambda: alm_rst_function())
    ui.lockRstButton.clicked.connect(lambda: lock_rst_function())
    ui.laserOnButton.clicked.connect(lambda: laser_on_function())

    MainWindow.show()
    sys.exit(app.exec_())
