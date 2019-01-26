
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QAction, QListWidget, QAbstractButton, QAbstractItemView, QMessageBox,QFocusFrame,QAbstractItemDelegate,QComboBox
from select_players import fetch_batsmen,fetch_bowler,fetch_allRounders,fetch_wicketKeeper,fetch_points
from value_role import player_value,check_role
from save_open import saving_team,opening_team,items_combobox
from retrieve import fetch_points_2,rr




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        width=1140
        height=900
        MainWindow.setFixedSize ( width,height )
        MainWindow.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(240,255,240);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(161, 81, 791, 211))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.bat_lab = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.bat_lab.setFont(font)
        self.bat_lab.setObjectName("bat_lab")
        self.horizontalLayout.addWidget(self.bat_lab)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.bow_lab = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.bow_lab.setFont(font)
        self.bow_lab.setObjectName("bow_lab")
        self.horizontalLayout.addWidget(self.bow_lab)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.wk_lab = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.wk_lab.setFont(font)
        self.wk_lab.setObjectName("wk_lab")
        self.horizontalLayout.addWidget(self.wk_lab)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.ar_lab = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.ar_lab.setFont(font)
        self.ar_lab.setObjectName("ar_lab")
        self.horizontalLayout.addWidget(self.ar_lab)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.points_avail = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.points_avail.setFont(font)
        self.points_avail.setObjectName("points_avail")
        self.horizontalLayout_2.addWidget(self.points_avail)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.points = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.points.setFont(font)
        self.points.setObjectName("points")
        self.horizontalLayout_2.addWidget(self.points)
        self.points_used_lab = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.points_used_lab.setFont(font)
        self.points_used_lab.setObjectName("points_used")
        self.horizontalLayout_2.addWidget(self.points_used_lab)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(160, 330, 791, 401))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.bat_rb = QtWidgets.QRadioButton(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.bat_rb.setFont(font)
        self.bat_rb.setObjectName("bat_rb")
        self.horizontalLayout_4.addWidget(self.bat_rb)
        self.bow_rb = QtWidgets.QRadioButton(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.bow_rb.setFont(font)
        self.bow_rb.setObjectName("bow_rb")
        self.horizontalLayout_4.addWidget(self.bow_rb)
        self.ar_rb = QtWidgets.QRadioButton(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.ar_rb.setFont(font)
        self.ar_rb.setObjectName("ar_rb")
        self.horizontalLayout_4.addWidget(self.ar_rb)
        self.wk_rb = QtWidgets.QRadioButton(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.wk_rb.setFont(font)
        self.wk_rb.setObjectName("wk_rb")
        self.horizontalLayout_4.addWidget(self.wk_rb)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.list_1 = QtWidgets.QListWidget(self.widget1)
        self.list_1.setObjectName("list_1")
        self.verticalLayout_2.addWidget(self.list_1)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.label_10 = QtWidgets.QLabel(self.widget1)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.team_name = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.team_name.setFont(font)
        self.team_name.setObjectName("team_name")
        self.horizontalLayout_5.addWidget(self.team_name)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.list_2 = QtWidgets.QListWidget(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(10)
        self.list_2.setFont(font)
        self.list_2.setObjectName("list_2")
        self.verticalLayout_3.addWidget(self.list_2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.label.raise_()
        self.label.raise_()
        self.list_1.raise_()
        self.label_6.raise_()
        self.team_name.raise_()
        self.list_2.raise_()
        self.label_10.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1117, 26))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.new_team = QtWidgets.QAction(MainWindow)
        self.new_team.setObjectName("new_team")
        self.open_team = QtWidgets.QAction(MainWindow)
        self.open_team.setObjectName("open_team")
        self.save_team = QtWidgets.QAction(MainWindow)
        self.save_team.setObjectName("save_team")
        self.eval_team = QtWidgets.QAction(MainWindow)
        self.eval_team.setObjectName("eval_team")
        self.menuManage_Teams.addAction(self.new_team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.open_team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.save_team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.eval_team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())
        self.wk_lab.setStyleSheet("color: rgb(255, 0, 0)")
        self.bat_lab.setStyleSheet("color: rgb(255, 0, 0)")
        self.bow_lab.setStyleSheet("color: rgb(255, 0, 0)")
        self.ar_lab.setStyleSheet("color: rgb(255, 0, 0)")
        self.points_avail.setStyleSheet("color: rgb(255, 0, 0)")
        self.points_used_lab.setStyleSheet("color: rgb(252, 0, 0)")
        self.list_1.setStyleSheet("color: rgb(139,69,19)")
        self.list_2.setStyleSheet("color: rgb(28, 170, 104)")
        self.team_name.setStyleSheet("color: rgb(28, 170, 104)")
        self.bat_rb.setStyleSheet("color: rgb(124, 137, 255)")
        self.bow_rb.setStyleSheet("color: rgb(124, 137, 255)")
        self.ar_rb.setStyleSheet("color: rgb(124, 137, 255)")
        self.wk_rb.setStyleSheet("color: rgb(124, 137, 255)")
        self.menuManage_Teams.setStyleSheet("color: rgb(139,69,19)")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fantasy Cricket"))
        MainWindow.setWindowIcon(QtGui.QIcon("Icon.png"))
        self.label.setText(_translate("MainWindow", "                                                                                     Your Selections"))
        self.label_2.setText(_translate("MainWindow", "   Batsmen(BAT)  "))
        self.bat_lab.setText(_translate("MainWindow", "##"))
        self.label_3.setText(_translate("MainWindow", "Bowlers(BOW)  "))
        self.bow_lab.setText(_translate("MainWindow", "##"))
        self.label_5.setText(_translate("MainWindow", "Wicket-keeper(WK)  "))
        self.wk_lab.setText(_translate("MainWindow", "##"))
        self.label_4.setText(_translate("MainWindow", "Allrounders(AR)  "))
        self.ar_lab.setText(_translate("MainWindow", "##"))
        self.label_7.setText(_translate("MainWindow", "   Points Available"))
        self.points_avail.setText(_translate("MainWindow", "####"))
        self.points.setText(_translate("MainWindow", "Points Used"))
        self.points_used_lab.setText(_translate("MainWindow", "####"))
        self.bat_rb.setText(_translate("MainWindow", "BAT"))
        self.bow_rb.setText(_translate("MainWindow", "BOW"))
        self.ar_rb.setText(_translate("MainWindow", "AR"))
        self.wk_rb.setText(_translate("MainWindow", "WK"))
        self.label_10.setText(_translate("MainWindow", "        >           "))
        self.label_6.setText(_translate("MainWindow", "Team Name"))
        self.team_name.setText(_translate("MainWindow", "Team"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.new_team.setText(_translate("MainWindow", "New Team"))
        self.new_team.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.open_team.setText(_translate("MainWindow", "Open Team"))
        self.open_team.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.save_team.setText(_translate("MainWindow", "Save Team"))
        self.save_team.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.eval_team.setText(_translate("MainWindow", "Evaluate Team"))



class Window( Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        QtWidgets.QMainWindow.__init__(self, parent )
        self.setupUi(self)



        self.new_team.triggered.connect(self.new_teamf)

        self.list_1.itemClicked.connect(self.removelist1)
        self.list_2.itemClicked.connect ( self.removelist2 )

        self.open_team.triggered.connect(self.open_teamf)
        self.save_team.triggered.connect(self.save_teamf)

        self.eval_team.triggered.connect(self.eval_teamf)


        self.list_1.itemClicked.connect ( self.update_labels )
        self.list_2.itemClicked.connect(self.update_labels)


    @QtCore.pyqtSlot()
    def new_teamf(self):
        text, result=QInputDialog.getText(self,'Team','Enter name of your Team')
        if result== True:
            self.team_name.setText(str(text))

        self.list_2.clear()
        self.update_labels()

        set_points=1000
        self.points_avail.setText (  str ( set_points ) )

        self.bat_rb.toggled.connect ( self.select_batsmen )
        self.bow_rb.toggled.connect(self.select_bowlers)
        self.ar_rb.toggled.connect(self.select_allRounders)
        self.wk_rb.toggled.connect(self.select_wicketKeeper)

    def update_labels(self):
        try:
            points = 1000
            points_used = 0
            batsmen = 0
            bowlers = 0
            wicket_keeper = 0
            allRounders = 0

            for x in range ( self.list_2.count () ):
                name = self.list_2.item ( x ).text ()

                used_points = fetch_points ( name )

                player_role = check_role ( name )

                points_used = points_used + used_points

                points = points - used_points

                if points_used > 1000:
                    self.exceed ()
                    points_used = points_used - used_points
                    points = points + used_points
                    QMessageBox.information ( self, "Message", "There are no enough Points" )
                else:
                    self.reselect ()
                    if player_role == "BAT":
                        batsmen = batsmen + 1

                    if player_role == "BWL":
                        bowlers = bowlers + 1

                    if player_role == "AR":
                        allRounders = allRounders + 1

                    if player_role == "WK":
                        wicket_keeper = wicket_keeper + 1
                        if wicket_keeper>1:
                            QMessageBox.information ( self, "Message", "In a team two wk should not be selected" )

            self.points_used_lab.setText ( str ( points_used ) )
            self.points_avail.setText ( str ( points ) )
            self.bat_lab.setText ( str ( batsmen ) )
            self.bow_lab.setText ( str ( bowlers ) )
            self.ar_lab.setText ( str ( allRounders ) )
            self.wk_lab.setText ( str ( wicket_keeper ) )

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format ( type ( ex ).__name__, ex.args )
            print (  message  )

    def exceed(self):
        self.list_1.setEnabled(False)
        h=self.list_2.count()
        s=h-1
        t=self.list_2.item(s).text()
        self.list_2.takeItem(s)
        print("the current index is  {} and text {}".format(s,t))
        self.list_1.addItem(t)
        print("the removed and added {}".format(t))
    def reselect(self):
        self.list_1.setEnabled(True)


    def select_batsmen(self):
        batsmen = fetch_batsmen()
        self.update_list(batsmen)


    def select_bowlers(self):
        bowler = fetch_bowler()
        a=self.update_list(bowler)



    def select_allRounders(self):
        all_rounder = fetch_allRounders()
        self.update_list(all_rounder)



    def select_wicketKeeper(self):
        wicket_keeper = fetch_wicketKeeper()
        self.update_list(wicket_keeper)

    def update_list(self, data):
        self.list_1.clear()
        for item in data:
            name_1 = item[0] # get name from left list

            # compare name_1 with all names on list_2

            found = False # default value before comparing name_1 with list_2

            for x in range(self.list_2.count()):
                name_2 = self.list_2.item(x).text() # get name from right list

                if name_1 == name_2:
                    found = True # found name_1 on list_2
                    break # you don't have to compare with other names from list_2
            # if not found this name on list_2 then you can add to list_1
            if not found:
                self.list_1.addItem(*item)

    def removelist1(self, item):
        self.list_1.takeItem(self.list_1.row(item))
        self.list_2.addItem(item.text())

    def removelist2(self, item):
        self.list_2.takeItem(self.list_2.row(item))
        self.list_1.addItem(item.text())

    def open_teamf(self):
        try:
            teams=items_combobox()
            list=[]
            for i in teams:
                list.append(*i)
            con_tup = tuple ( list )
            items = con_tup
            item, ok = QInputDialog.getItem ( self, "select input dialog", "Open a Team", items, 0, False )
            if ok and item:
                players_in_team=opening_team(item)
                self.list_2.clear()
                for i in players_in_team:
                    self.list_2.addItem(*i)
                    self.update_labels()

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format ( type ( ex ).__name__, ex.args )
            print(message)

    def save_teamf(self):
        try:
            q=self.wk_lab.text()
            check=q
            if check=="##":
                QMessageBox.information ( self, "Message",
                                          "Please create a team to save" )

            if int(check)!=1:
                QMessageBox.information ( self, "Message", "Game logic is not followed.Check Wicket Keeper" )
            else:
                teamName = self.team_name.text ()
                for x in range ( self.list_2.count () ):
                    player_name = self.list_2.item ( x ).text ()
                    value = player_value ( player_name )
                    g = saving_team ( teamName, player_name, value )
                QMessageBox.information ( self, "Message", "Your Team is saved" )

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format ( type ( ex ).__name__, ex.args )
            print ( "sel {}".format ( message ) )


    def eval_teamf(self):
        try:

            self.s=SecondWindow()
            self.s.show()

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format ( type ( ex ).__name__, ex.args )
            print ( message )


class Ui_Dilaog(object):
    def setupUi1(self, Dilaog):
        Dilaog.setObjectName("Dilaog")
        height=725
        width=802
        Dilaog.setFixedSize(height,width)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dilaog.sizePolicy().hasHeightForWidth())
        Dilaog.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        Dilaog.setFont(font)
        #Dilaog.setSizeGripEnabled(False)
        self.cal_score = QtWidgets.QPushButton(Dilaog)
        self.cal_score.setGeometry(QtCore.QRect(270, 710, 161, 41))
        self.cal_score.setObjectName("cal_score")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dilaog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 9, 741, 71))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.line = QtWidgets.QFrame(Dilaog)
        self.line.setGeometry(QtCore.QRect(-10, 150, 761, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.widget = QtWidgets.QWidget(Dilaog)
        self.widget.setGeometry(QtCore.QRect(40, 80, 631, 61))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.team_cb = QtWidgets.QComboBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.team_cb.sizePolicy().hasHeightForWidth())
        self.team_cb.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.team_cb.setFont(font)
        self.team_cb.setCurrentText("")
        self.team_cb.setDuplicatesEnabled(False)
        self.team_cb.setObjectName("team_cb")
        self.horizontalLayout.addWidget(self.team_cb)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.match_cb = QtWidgets.QComboBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.match_cb.sizePolicy().hasHeightForWidth())
        self.match_cb.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.match_cb.setFont(font)
        self.match_cb.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.match_cb.setCurrentText("")
        self.match_cb.setMaxVisibleItems(11)
        self.match_cb.setObjectName("match_cb")
        self.horizontalLayout.addWidget(self.match_cb)
        spacerItem2 = QtWidgets.QSpacerItem(68, 56, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.widget1 = QtWidgets.QWidget(Dilaog)
        self.widget1.setGeometry(QtCore.QRect(40, 210, 621, 471))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.elist_1 = QtWidgets.QListWidget(self.widget1)
        self.elist_1.setObjectName("elist_1")
        self.horizontalLayout_2.addWidget(self.elist_1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.elist_2 = QtWidgets.QListWidget(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.elist_2.sizePolicy().hasHeightForWidth())
        self.elist_2.setSizePolicy(sizePolicy)
        self.elist_2.setObjectName("elist_2")
        self.horizontalLayout_2.addWidget(self.elist_2)
        self.widget2 = QtWidgets.QWidget(Dilaog)
        self.widget2.setGeometry(QtCore.QRect(41, 180, 621, 31))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget2)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem4 = QtWidgets.QSpacerItem(128, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.label_3 = QtWidgets.QLabel(self.widget2)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.cal_score.raise_()
        self.verticalLayoutWidget.raise_()
        self.elist_1.raise_()
        self.team_cb.raise_()
        self.match_cb.raise_()
        self.line.raise_()
        Dilaog.setStyleSheet("background-color:rgb(255,250,240)")
        Dilaog.setWindowIcon(QtGui.QIcon("evaluate.png"))
        self.retranslateUi(Dilaog)
        QtCore.QMetaObject.connectSlotsByName(Dilaog)

    def retranslateUi(self, Dilaog):
        _translate = QtCore.QCoreApplication.translate
        Dilaog.setWindowTitle(_translate("Dilaog", "Evaluate Score "))
        self.cal_score.setText(_translate("Dilaog", "Calculate Score"))
        self.label.setText(_translate("Dilaog", "Evaluate the perforamnce of your Fantasy Team"))
        self.label_2.setText(_translate("Dilaog", "     Players"))
        self.label_3.setText(_translate("Dilaog", "Points"))

class SecondWindow(Ui_Dilaog,QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.setupUi1(self)
        try:
            self.team_cb.activated.connect(self.team_names)
            self.cal_score.clicked.connect(self.score)

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format ( type ( ex ).__name__, ex.args )
            print (  message  )

        get_teams = items_combobox ()
        for i in get_teams:
            self.team_cb.addItem ( "{}".format ( *i ) )

        for i in range(1,5):
            self.match_cb.addItem("Match {}".format(i))


    @QtCore.pyqtSlot()
    def team_names(self):
        try:
            indx = self.team_cb.currentIndex ()
            item = self.team_cb.currentText ()
            players=opening_team(item)
            self.elist_1.clear()
            self.elist_2.clear()
            self.points_list=[]
            for x in players:
                self.elist_1.addItem(*x)
                h=fetch_points_2(*x)
                g=int(h)
                self.points_list.append(g)

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format ( type ( ex ).__name__, ex.args )
            print ( message )

    def score(self):
        try:
            a=self.elist_2.count()
            if a<1:
                get_points=self.points_list
                for j in get_points:
                    con_str=str(j)
                    self.elist_2.addItem(con_str)
                self.elist_2.addItem("The Total Points are  {} ".format(sum(self.points_list)))

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format ( type ( ex ).__name__, ex.args )
            print (  message  )


if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    w=Window()
    w.show()
    sys.exit(app.exec_())




