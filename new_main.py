
######################################################################################################
##
##  Software Created By - GNLabs
##  Software fully written in purely Python
##
######################################################################################################


#--------------- Imported Modules ---------------------
from PyQt5 import QtCore, QtGui, QtWidgets
from graphics import resource
import sys, re, time
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QApplication, QSystemTrayIcon
from database import get_items_list, get_data
from bill import bill_save_into_txt
from print_dialog import run

save_data = {}
max_limit = 0


#----------------- BiLLeRR Main Window ----------------
class Ui_MainWindow(object):

    #----------------- SetupUI -------------------
    def setupUi(self, MainWindow):
        
        #################################################################
        ## ---------------------- Main Window ---------------------------
        #################################################################
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)

        # Central Widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")

        # Setting layout in Central Widgets
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_window = QtWidgets.QFrame(self.centralwidget)
        self.main_window.setStyleSheet("QFrame{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 20px;\n"
"}")
        self.main_window.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_window.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_window.setObjectName("main_window")

        # Setting Layout for Main Window
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main_window)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")



        #################################################################
        ## ---------------------- MENU BAR ------------------------------
        #################################################################
        self.menu_bar = QtWidgets.QFrame(self.main_window)
        self.menu_bar.setMinimumSize(QtCore.QSize(0, 45))
        self.menu_bar.setMaximumSize(QtCore.QSize(16777215, 45))
        self.menu_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_bar.setObjectName("menu_bar")

        # Setting Layout in Menu Bar
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.menu_bar)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")

        # BiLLeRR Icon
        self.billerr_icon = QtWidgets.QLabel(self.menu_bar)
        self.billerr_icon.setMinimumSize(QtCore.QSize(45, 32))
        self.billerr_icon.setMaximumSize(QtCore.QSize(45, 32))
        self.billerr_icon.setStyleSheet("QLabel {\n"
"    image: url(:/Upper Menu Icons/BiLLeRR_icon.png);\n"
"}")
        self.billerr_icon.setText("")
        self.billerr_icon.setObjectName("billerr_icon")

        # Setting Layout for BiLLeRR Icon 
        self.horizontalLayout_10.addWidget(self.billerr_icon)
        self.billerr_txt = QtWidgets.QLabel(self.menu_bar)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)

        # Biller Text
        self.billerr_txt.setFont(font)
        self.billerr_txt.setStyleSheet("")
        self.billerr_txt.setObjectName("billerr_txt")
        self.horizontalLayout_10.addWidget(self.billerr_txt)

        # User Button Settings and Layouts
        self.user_btn = QtWidgets.QFrame(self.menu_bar)
        self.user_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.user_btn.setMaximumSize(QtCore.QSize(160, 40))
        self.user_btn.setStyleSheet("QFrame {\n"
"    background-color: rgb(245, 245, 245);\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"    background-color: rgba(0, 0, 0, 20);\n"
"}")
        self.user_btn.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.user_btn.setFrameShadow(QtWidgets.QFrame.Raised)
        self.user_btn.setObjectName("user_btn")

        # Layout For User Button
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.user_btn)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")

        # User Icon
        self.user_icon = QtWidgets.QPushButton(self.user_btn)
        self.user_icon.setMinimumSize(QtCore.QSize(50, 40))
        self.user_icon.setMaximumSize(QtCore.QSize(50, 40))
        self.user_icon.setStyleSheet("QPushButton {\n"
"    image: url(:/Upper Menu Icons/user.png);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    image: url(:/Upper Menu Icons/user_hover.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(10, 10, 10, 30);\n"
"}")
        self.user_icon.setText("")
        self.user_icon.setObjectName("user_icon")
        self.horizontalLayout_7.addWidget(self.user_icon)

        # User Text
        self.user_txt = QtWidgets.QPushButton(self.user_btn)
        self.user_txt.setMinimumSize(QtCore.QSize(0, 40))
        self.user_txt.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.user_txt.setFont(font)
        self.user_txt.setStyleSheet("QPushButton {\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    padding-left: 5px;\n"
"    text-align: left;\n"
"    border-top-left-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    border-top-right-radius: 20px;\n"
"    border-bottom-right-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0, 0, 0, 40);\n"
"}")
        self.user_txt.setObjectName("user_txt")

        # Layout For User Icon and Text
        self.horizontalLayout_7.addWidget(self.user_txt)
        self.horizontalLayout_10.addWidget(self.user_btn)

        # End Spacing in Menu Bar
        self.right_spacing = QtWidgets.QFrame(self.menu_bar)
        self.right_spacing.setMinimumSize(QtCore.QSize(20, 40))
        self.right_spacing.setMaximumSize(QtCore.QSize(20, 40))
        self.right_spacing.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right_spacing.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_spacing.setObjectName("right_spacing")
        self.horizontalLayout_10.addWidget(self.right_spacing)
        self.verticalLayout_2.addWidget(self.menu_bar)


        ###############################################################
        # ---------------------- MAIN FRAME ---------------------------
        ###############################################################
        self.main_frame = QtWidgets.QFrame(self.main_window)
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")

        # Layout for Main Frame
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main_frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")


        ################################################################
        # ---------------------- TOGGLE MENU ---------------------------
        ################################################################
        self.toggle_menu = QtWidgets.QFrame(self.main_frame)
        self.toggle_menu.setMinimumSize(QtCore.QSize(60, 0))
        self.toggle_menu.setMaximumSize(QtCore.QSize(60, 16777215))
        self.toggle_menu.setStyleSheet("QFrame{\n"
"    border-radius: 0px;\n"
"    border-top-right-radius: 30px;\n"
"    background-color: rgb(85, 85, 255);\n"
"}")
        self.toggle_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.toggle_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.toggle_menu.setObjectName("toggle_menu")
        

        # Layout For Toggle Menu
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.toggle_menu)
        self.verticalLayout_9.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_9.setObjectName("verticalLayout_9")


        # First Button in Toggle Menu
        ##################################################################
        self.toggle_menu_1_btn = QtWidgets.QFrame(self.toggle_menu)
        self.toggle_menu_1_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.toggle_menu_1_btn.setMaximumSize(QtCore.QSize(16777215, 50))
        self.toggle_menu_1_btn.setStyleSheet("QFrame:hover {\n"
"    background-color: rgba(255, 255, 255, 30);\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"")
        self.toggle_menu_1_btn.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.toggle_menu_1_btn.setFrameShadow(QtWidgets.QFrame.Raised)
        self.toggle_menu_1_btn.setObjectName("toggle_menu_1_btn")

        # Layout For 1st Toggle Menu Button
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.toggle_menu_1_btn)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        # Control Center Button Icon
        self.control_center_icon = QtWidgets.QPushButton(self.toggle_menu_1_btn)
        self.control_center_icon.setMinimumSize(QtCore.QSize(60, 40))
        self.control_center_icon.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.control_center_icon.setFont(font)
        self.control_center_icon.setStyleSheet("QPushButton {\n"
"    image: url(:/Toggle Menu Icons/control_center.png);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: 1px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    image: url(:/Toggle Menu Icons/control_center_hover.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(245, 245, 245, 40);\n"
"}")
        self.control_center_icon.setText("")
        self.control_center_icon.setIconSize(QtCore.QSize(32, 32))
        self.control_center_icon.setObjectName("control_center_icon")
        self.horizontalLayout_5.addWidget(self.control_center_icon)

        # Control Center Button Text
        self.control_center_txt = QtWidgets.QPushButton(self.toggle_menu_1_btn)
        self.control_center_txt.setMinimumSize(QtCore.QSize(0, 40))
        self.control_center_txt.setMaximumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.control_center_txt.setFont(font)
        self.control_center_txt.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.control_center_txt.setAutoFillBackground(False)
        self.control_center_txt.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    padding-left: 5px;\n"
"    text-align: left;\n"
"    border: 1px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(245, 245, 245, 40);\n"
"}")
        self.control_center_txt.setFlat(False)
        self.control_center_txt.setObjectName("control_center_txt")
        self.horizontalLayout_5.addWidget(self.control_center_txt)
        self.verticalLayout_9.addWidget(self.toggle_menu_1_btn)


        # Second Button in Toggle Menu
        ##################################################################
        self.toggle_menu_2_btn = QtWidgets.QFrame(self.toggle_menu)
        self.toggle_menu_2_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.toggle_menu_2_btn.setMaximumSize(QtCore.QSize(16777215, 50))
        self.toggle_menu_2_btn.setStyleSheet("QFrame:hover {\n"
"    background-color: rgba(255, 255, 255, 30);\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"")
        self.toggle_menu_2_btn.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.toggle_menu_2_btn.setFrameShadow(QtWidgets.QFrame.Raised)
        self.toggle_menu_2_btn.setObjectName("toggle_menu_2_btn")

        # Layout for 2nd Button in Toggle Menu
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.toggle_menu_2_btn)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        # Help Button Icon
        self.help_icon = QtWidgets.QPushButton(self.toggle_menu_2_btn)
        self.help_icon.setMinimumSize(QtCore.QSize(60, 40))
        self.help_icon.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.help_icon.setFont(font)
        self.help_icon.setStyleSheet("QPushButton {\n"
"    image: url(:/Toggle Menu Icons/help.png);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: 1px;\n"
"}    \n"
"\n"
"QPushButton:hover {\n"
"    image: url(:/Toggle Menu Icons/help_hover.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(245, 245, 245, 40);\n"
"}")
        self.help_icon.setText("")
        self.help_icon.setIconSize(QtCore.QSize(32, 32))
        self.help_icon.setObjectName("help_icon")
        self.horizontalLayout_6.addWidget(self.help_icon)

        # Help Button Text
        self.help_txt = QtWidgets.QPushButton(self.toggle_menu_2_btn)
        self.help_txt.setMinimumSize(QtCore.QSize(0, 40))
        self.help_txt.setMaximumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.help_txt.setFont(font)
        self.help_txt.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.help_txt.setAutoFillBackground(False)
        self.help_txt.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    padding-left: 5px;\n"
"    text-align: left;\n"
"    border: 1px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 40);\n"
"}")
        self.help_txt.setFlat(False)
        self.help_txt.setObjectName("help_txt")
        self.horizontalLayout_6.addWidget(self.help_txt)
        self.verticalLayout_9.addWidget(self.toggle_menu_2_btn)


        # Toggle Menu 3rd Button
        ##################################################################
        self.toggle_menu_3_btn = QtWidgets.QFrame(self.toggle_menu)
        self.toggle_menu_3_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.toggle_menu_3_btn.setMaximumSize(QtCore.QSize(16777215, 50))
        self.toggle_menu_3_btn.setStyleSheet("QFrame:hover {\n"
"    background-color: rgba(255, 255, 255, 30);\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"")
        self.toggle_menu_3_btn.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.toggle_menu_3_btn.setFrameShadow(QtWidgets.QFrame.Raised)
        self.toggle_menu_3_btn.setObjectName("toggle_menu_3_btn")

        # Layout for third Button
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.toggle_menu_3_btn)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")

        # Logout Icon
        self.logout_icon = QtWidgets.QPushButton(self.toggle_menu_3_btn)
        self.logout_icon.setMinimumSize(QtCore.QSize(60, 40))
        self.logout_icon.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.logout_icon.setFont(font)
        self.logout_icon.setStyleSheet("QPushButton {\n"
"    image: url(:/Toggle Menu Icons/logout.png);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: 1px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(245, 245, 245, 40);\n"
"}")
        self.logout_icon.setText("")
        self.logout_icon.setIconSize(QtCore.QSize(32, 32))
        self.logout_icon.setObjectName("logout_icon")
        self.horizontalLayout_9.addWidget(self.logout_icon)

        # Logout Text
        self.logout_txt = QtWidgets.QPushButton(self.toggle_menu_3_btn)
        self.logout_txt.setMinimumSize(QtCore.QSize(0, 40))
        self.logout_txt.setMaximumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.logout_txt.setFont(font)
        self.logout_txt.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.logout_txt.setAutoFillBackground(False)
        self.logout_txt.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    padding-left: 5px;\n"
"    text-align: left;\n"
"    border: 1px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(245, 245, 245, 40);\n"
"}")
        self.logout_txt.setFlat(False)
        self.logout_txt.setObjectName("logout_txt")
        self.horizontalLayout_9.addWidget(self.logout_txt)
        self.verticalLayout_9.addWidget(self.toggle_menu_3_btn)
        self.horizontalLayout.addWidget(self.toggle_menu)


        # Main Frame
        ##################################################################
        self.main_content = QtWidgets.QFrame(self.main_frame)
        self.main_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_content.setObjectName("main_content")

        # Layout For Main Content
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.main_content)
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")


        ##################################################################
        # --------------------- STACK WIDGET -----------------------------
        ##################################################################
        self.stackedWidget = QtWidgets.QStackedWidget(self.main_content)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stackedWidget.setObjectName("stackedWidget")


        # PAge 1
        ##################################################################
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setEnabled(True)
        self.page_1.setObjectName("page_1")

        # Layout For 1st Page
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_1)
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.working_area = QtWidgets.QFrame(self.page_1)
        self.working_area.setEnabled(True)
        self.working_area.setStyleSheet("QFrame{\n"
"    border-radius: 35px;\n"
"    background-color: rgb(235, 235, 235);\n"
"}")
        self.working_area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.working_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.working_area.setObjectName("working_area")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.working_area)
        self.verticalLayout_5.setObjectName("verticalLayout_5")


        ####################################################################
        # ----------------------- Item List Frame --------------------------
        ####################################################################
        self.items_list_frame = QtWidgets.QFrame(self.working_area)
        self.items_list_frame.setMaximumSize(QtCore.QSize(16777215, 25))
        self.items_list_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.items_list_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.items_list_frame.setObjectName("items_list_frame")

        # Layout For Item List Frame
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.items_list_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.items_list_lbl = QtWidgets.QLabel(self.items_list_frame)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.items_list_lbl.setFont(font)
        self.items_list_lbl.setStyleSheet("QLabel{\n"
"    padding-left: 25px;\n"
"}")
        self.items_list_lbl.setObjectName("items_list_lbl")
        self.horizontalLayout_2.addWidget(self.items_list_lbl)
        self.verticalLayout_5.addWidget(self.items_list_frame)

        # Item List Table Area
        self.item_list_tbl_area = QtWidgets.QFrame(self.working_area)
        self.item_list_tbl_area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.item_list_tbl_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.item_list_tbl_area.setObjectName("item_list_tbl_area")

        # Layout for Item List TAble Area
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.item_list_tbl_area)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        # Item List Table Frame
        self.item_list_tbl_frame = QtWidgets.QFrame(self.item_list_tbl_area)
        self.item_list_tbl_frame.setMinimumSize(QtCore.QSize(0, 280))
        self.item_list_tbl_frame.setStyleSheet("QFrame{\n"
"    border-radius: 40px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.item_list_tbl_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.item_list_tbl_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.item_list_tbl_frame.setObjectName("item_list_tbl_frame")

        # Layout For Item Table Frame
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.item_list_tbl_frame)
        self.verticalLayout_7.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")

        # ITems List Text
        self.item_list_tbl = QtWidgets.QTableWidget(self.item_list_tbl_frame)
        self.item_list_tbl.setStyleSheet("QHeaderView::section {\n"
"    background-color: rgb(235, 235, 235);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border-top: 1px solid #fffff8;\n"
"}\n"
"\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border-left: 1px solid #fffff8;\n"
"}")
        self.item_list_tbl.setLineWidth(2)
        self.item_list_tbl.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.item_list_tbl.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.item_list_tbl.setTabKeyNavigation(False)
        self.item_list_tbl.setProperty("showDropIndicator", True)
        self.item_list_tbl.setShowGrid(True)
        self.item_list_tbl.setCornerButtonEnabled(True)
        self.item_list_tbl.setObjectName("item_list_tbl")


        # Show Data In Table
        ##################################################################
        self.show_item_list()

        item = QtWidgets.QTableWidgetItem()
        self.item_list_tbl.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.item_list_tbl.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.item_list_tbl.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.item_list_tbl.setHorizontalHeaderItem(3, item)

        header = self.item_list_tbl.horizontalHeader()

        # Resize Column To Content Feature   
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)

        # Layout For Customizing Table
        self.verticalLayout_7.addWidget(self.item_list_tbl)
        self.verticalLayout_6.addWidget(self.item_list_tbl_frame)
        self.verticalLayout_5.addWidget(self.item_list_tbl_area)


        ##################################################################
        # ----------------- Input Panel And Review Frame -----------------
        ##################################################################
        self.inpanel_review_frame = QtWidgets.QFrame(self.working_area)
        self.inpanel_review_frame.setMaximumSize(QtCore.QSize(16777215, 25))
        self.inpanel_review_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.inpanel_review_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inpanel_review_frame.setObjectName("inpanel_review_frame")

        # Layout For Inpanel and review Frame
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.inpanel_review_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(9)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")


        # Input Panel Text
        ##################################################################
        self.inpanel_lbl = QtWidgets.QLabel(self.inpanel_review_frame)
        self.inpanel_lbl.setMinimumSize(QtCore.QSize(400, 0))
        self.inpanel_lbl.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(10)
        self.inpanel_lbl.setFont(font)
        self.inpanel_lbl.setStyleSheet("QLabel{\n"
"    padding-left: 25px;\n"
"}")
        self.inpanel_lbl.setObjectName("inpanel_lbl")
        self.horizontalLayout_3.addWidget(self.inpanel_lbl)

        # Review Text
        ##################################################################
        self.review_lbl = QtWidgets.QLabel(self.inpanel_review_frame)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(10)
        self.review_lbl.setFont(font)
        self.review_lbl.setStyleSheet("QLabel{\n"
"    padding-left: 25px;\n"
"}")
        self.review_lbl.setObjectName("review_lbl")
        self.horizontalLayout_3.addWidget(self.review_lbl)
        self.verticalLayout_5.addWidget(self.inpanel_review_frame)


        ##################################################################
        # ----------------------- INput Panel Area -----------------------
        ##################################################################
        self.inpanel_review_area = QtWidgets.QFrame(self.working_area)
        self.inpanel_review_area.setMaximumSize(QtCore.QSize(16777215, 250))
        self.inpanel_review_area.setMinimumSize(QtCore.QSize(0, 250))
        self.inpanel_review_area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.inpanel_review_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inpanel_review_area.setObjectName("inpanel_review_area")

        # Layout For Input 
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.inpanel_review_area)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(9)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        # Input Panel Frame
        ##################################################################
        self.inpanel_frame = QtWidgets.QFrame(self.inpanel_review_area)
        self.inpanel_frame.setMinimumSize(QtCore.QSize(300, 0))
        self.inpanel_frame.setMaximumSize(QtCore.QSize(400, 16777215))
        self.inpanel_frame.setStyleSheet("QFrame{\n"
"    border-radius: 40px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    padding-top: 15px;\n"
"    padding-left: 5px;\n"
"}")
        self.inpanel_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.inpanel_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inpanel_frame.setObjectName("inpanel_frame")

        # Form Layout
        self.formLayout = QtWidgets.QFormLayout(self.inpanel_frame)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setSpacing(9)
        self.formLayout.setObjectName("formLayout")


        # Item Code INput
        ##################################################################
        self.itm_code_input = QtWidgets.QLineEdit(self.inpanel_frame)
        self.itm_code_input.setMinimumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.itm_code_input.setFont(font)
        self.itm_code_input.setStyleSheet("QLineEdit{\n"
"    border: 1.4px solid black;\n"
"    border-radius: 4px;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid black;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid blue;\n"
"}")
        self.itm_code_input.setObjectName("itm_code_input")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.itm_code_input)


        # Item Quantity INput
        ##################################################################
        self.qnty_input = QtWidgets.QLineEdit(self.inpanel_frame)
        self.qnty_input.setMinimumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.qnty_input.setFont(font)
        self.qnty_input.setStyleSheet("QLineEdit{\n"
"    border: 1.4px solid black;\n"
"    border-radius: 4px;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid black;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid blue;\n"
"}")
        self.qnty_input.setObjectName("qnty_input")
        self.qnty_input.editingFinished.connect(self.check_and_save_input_data)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.qnty_input)


        # Print Bill Button
        ##################################################################
        self.printbill_btn = QtWidgets.QPushButton(self.inpanel_frame)
        self.printbill_btn.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.printbill_btn.setFont(font)
        self.printbill_btn.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(21, 144, 255);\n"
"    border: 1px;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 2px solid black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid blue;\n"
"    color: blue;\n"
"}")
        self.printbill_btn.setObjectName("printbill_btn")
        self.printbill_btn.clicked.connect(self.print_bill)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.printbill_btn)
        self.horizontalLayout_4.addWidget(self.inpanel_frame)

        # Cancel Order Button
        ##################################################################
        self.Cancel_order_btn = QtWidgets.QPushButton(self.inpanel_frame)
        self.Cancel_order_btn.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Cancel_order_btn.setFont(font)
        self.Cancel_order_btn.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(21, 144, 255);\n"
"    border: 1px;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 2px solid black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid blue;\n"
"    color: blue;\n"
"}")
        self.Cancel_order_btn.setObjectName("order_cancel_btn")
        self.Cancel_order_btn.clicked.connect(self.cancel_order)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Cancel_order_btn)
        self.horizontalLayout_4.addWidget(self.inpanel_frame)


        ##################################################################
        # ---------------------- Review Area ---------------------------
        ##################################################################
        self.review_area = QtWidgets.QFrame(self.inpanel_review_area)
        self.review_area.setStyleSheet("QFrame{\n"
"    border-radius: 40px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.review_area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.review_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.review_area.setObjectName("review_area")

        # Layout For Review Area
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.review_area)
        self.verticalLayout_8.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")

        # Review Table
        ##################################################################
        self.review_tbl = QtWidgets.QTableWidget(self.review_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.review_tbl.sizePolicy().hasHeightForWidth())
        self.review_tbl.setSizePolicy(sizePolicy)
        self.review_tbl.setStyleSheet("QHeaderView::section {\n"
"    background-color: rgb(235, 235, 235);\n"
"    border-radius: 8px;\n"
"    padding-right: 2px;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border-top: 1px solid #fffff8;\n"
"}\n"
"\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border-left: 1px solid #fffff8;\n"
"}")
        self.review_tbl.setObjectName("review_tbl")
        self.review_tbl.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setUnderline(False)
        item.setFont(font)

        # Show Review Items in Review Table
        self.t_r = self.show_selected_item_list()

        # Layout For Table With Data
        self.review_tbl.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.review_tbl.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.review_tbl.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.review_tbl.setHorizontalHeaderItem(3, item)

        header = self.review_tbl.horizontalHeader()

        # Resize Column To Content Feature   
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)


        self.review_tbl.horizontalHeader().setDefaultSectionSize(90)
        self.verticalLayout_8.addWidget(self.review_tbl)


        self.frame = QtWidgets.QFrame(self.review_area)
        self.frame.setMinimumSize(QtCore.QSize(0, 20))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setStyleSheet("QLabel{\n"
"    background-color: rgb(240, 240, 240);\n"
"    border-radius: 8px;\n"
"}")
        self.frame.setObjectName("frame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"    padding-left: 25px;\n"
"}")
        self.label.setObjectName("label")
        self.horizontalLayout_8.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setMinimumSize(QtCore.QSize(30, 0))
        self.label_2.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_8.addWidget(self.label_2)
        self.verticalLayout_8.addWidget(self.frame)
        self.horizontalLayout_4.addWidget(self.review_area)
        self.verticalLayout_5.addWidget(self.inpanel_review_area)
        self.verticalLayout_4.addWidget(self.working_area)
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.main_content)
        self.verticalLayout_2.addWidget(self.main_frame)
        self.verticalLayout.addWidget(self.main_window)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # All Connection Defined here
        self.itm_code_input.editingFinished.connect(self.enter_pressed)
        self.qnty_input.editingFinished.connect(self.qnty_enter_pressed)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.billerr_txt.setText(_translate("MainWindow", "BiLLeRR"))
        self.user_txt.setText(_translate("MainWindow", "Username"))
        self.control_center_txt.setText(_translate("MainWindow", "Control Center"))
        self.help_txt.setText(_translate("MainWindow", "Help"))
        self.logout_txt.setText(_translate("MainWindow", "Logout"))
        self.items_list_lbl.setText(_translate("MainWindow", "ITEMS LIST"))
        item = self.item_list_tbl.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Item Code"))
        item = self.item_list_tbl.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Item Name"))
        item = self.item_list_tbl.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Item Rate"))
        item = self.item_list_tbl.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Item Type"))
        self.inpanel_lbl.setText(_translate("MainWindow", "INPUT PANEL"))
        self.review_lbl.setText(_translate("MainWindow", "REVIEW"))
        self.itm_code_input.setPlaceholderText(_translate("MainWindow", "Item Code"))
        self.qnty_input.setPlaceholderText(_translate("MainWindow", "Quantity"))
        self.printbill_btn.setText(_translate("MainWindow", "Print Bill"))
        self.Cancel_order_btn.setText(_translate("MainWindow", "Cancel Order"))
        item = self.review_tbl.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Item Code"))
        item = self.review_tbl.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Item Name"))
        item = self.review_tbl.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Item Quantity"))
        item = self.review_tbl.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Item Rate"))
        self.label.setText(_translate("MainWindow", "You have to Pay -"))
        self.label_2.setText(_translate("MainWindow", "₹"))
        

    # Change line Edit when Enter is pressed
    def enter_pressed(self):
        self.qnty_input.setFocus()
        
        
    def qnty_enter_pressed(self):
        self.itm_code_input.setFocus()
        self.itm_code_input.clear()
        self.qnty_input.clear()
        t_r = self.show_selected_item_list()
        self.retranslate(t_r)


    def cancel_order(self):
        self.itm_code_input.setFocus()
        self.itm_code_input.clear()
        self.qnty_input.clear()
        save_data.clear()
        self.show_selected_item_list()
        self.retranslate(0)
        self.cancel_order_dialog()


    # Error Message
    def error(self, text):
        global max_limit
        if max_limit == 1:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Error!")
                msg.setInformativeText(text)
                msg.setWindowTitle("Error")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.exec_()
                save_data.clear()
                self.show_selected_item_list()
        elif max_limit >= 2:
                max_limit = 0
        

    def cancel_order_dialog(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setInformativeText('Order Canceled Successfully!')
        msg.setWindowTitle("Order Canceled!")
        msg.exec_()
        

    # Table Creation
    def show_item_list(self):

        row, col, data = get_items_list()
        
        #Row count
        self.item_list_tbl.setRowCount(row)
        
        #Column count
        self.item_list_tbl.setColumnCount(col)
        
        header_lbl = []
        for r, items in enumerate(data):
                header_lbl.append(f'  {r+1}')
                self.item_list_tbl.setVerticalHeaderLabels(header_lbl)
                for c, itm_d in enumerate(items):
                        self.item_list_tbl.setItem(r, c, QTableWidgetItem(str(itm_d)))
                c = 0


    def show_selected_item_list(self):

        # Row Count
        self.review_tbl.setRowCount(0)
        
        # Column Count
        self.review_tbl.setColumnCount(4)

        # Show review
        total_rate = 0
        row = 0
        header_lbl = []
        for r, items in enumerate(save_data.items()):
                row += 1
                self.review_tbl.insertRow(r)
                header_lbl.append(f'  {r+1}')
                self.review_tbl.setVerticalHeaderLabels(header_lbl)
                for c, data in enumerate(items[1]):
                        self.review_tbl.setItem(r, c, QTableWidgetItem(str(data)))
                        if c == 3:
                                total_rate += int(data)
        return total_rate

        
        
    def retranslate(self, t_r):
        _translate = QtCore.QCoreApplication.translate
        self.label_2.setText(_translate("MainWindow", f"₹ {float(t_r)}"))

    def print_bill(self):
        cus_n = 'Pankaj'
        cus_phn = '9519519519'
        bill_save_into_txt(save_data, cus_n, cus_phn)
        run()


    def check_and_save_input_data(self):
        global max_limit
        max_limit += 1
        regex = re.compile("[@_!#$%^&*()<>?/\\|}{~:',.;`₹]")
        ask = self.itm_code_input.text()
        if (not ask):
                text = 'Please Enter Item Code!'
                self.error(text)
        elif (ask.isspace() == True):
                text = 'Please Enter code Properly!!'
                self.error(text)
        elif (ask.isalpha() == True):
                text = 'Please Enter code Properly!!'
                self.error(text)
        elif (regex.search(ask)):
                text = 'Please Enter code Properly!!'
                self.error(text)
        else:
                data = []
                ask = int(ask)
                qnty = self.qnty_input.text()
                if (not qnty):
                        qnty = 1
                try:
                        g_data = get_data(ask)
                        lst_pos = 0
                        for item in g_data[0]:
                                data.append(str(item))
                                lst_pos += 1
                                if lst_pos == 2:
                                        data.append(str(qnty))
                                elif lst_pos == 3:
                                        data.pop()
                                        data.append(str(item * int(qnty)))

                        data.pop()
                        save_data[ask] = data
                        print(save_data)
                except:
                        text = 'Please Enter code Properly!!'
                        self.error(text)



class Main_Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        icon = QtGui.QIcon('graphics/BiLLeRR_icon.png')
        self.setWindowIcon(icon)
        self.setWindowTitle('BiLLeRR v1.0.0')
        self.show()




def BiLLeRR_app():
    app = QApplication(sys.argv)
    window = Main_Window()
    window.show()
    sys.exit(app.exec_())


BiLLeRR_app()

