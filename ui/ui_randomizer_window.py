# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'randomizer_window.ui'
#
# Created: Thu May 24 13:24:52 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 534)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.seed = QtGui.QLineEdit(self.centralwidget)
        self.seed.setObjectName("seed")
        self.gridLayout.addWidget(self.seed, 2, 1, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.clean_iso_path = QtGui.QLineEdit(self.centralwidget)
        self.clean_iso_path.setObjectName("clean_iso_path")
        self.gridLayout.addWidget(self.clean_iso_path, 0, 1, 1, 1)
        self.output_folder = QtGui.QLineEdit(self.centralwidget)
        self.output_folder.setObjectName("output_folder")
        self.gridLayout.addWidget(self.output_folder, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.clean_iso_path_browse_button = QtGui.QPushButton(self.centralwidget)
        self.clean_iso_path_browse_button.setObjectName("clean_iso_path_browse_button")
        self.gridLayout.addWidget(self.clean_iso_path_browse_button, 0, 2, 1, 1)
        self.output_folder_browse_button = QtGui.QPushButton(self.centralwidget)
        self.output_folder_browse_button.setObjectName("output_folder_browse_button")
        self.gridLayout.addWidget(self.output_folder_browse_button, 1, 2, 1, 1)
        self.generate_seed_button = QtGui.QPushButton(self.centralwidget)
        self.generate_seed_button.setObjectName("generate_seed_button")
        self.gridLayout.addWidget(self.generate_seed_button, 2, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.progression_treasure_charts = QtGui.QCheckBox(self.groupBox)
        self.progression_treasure_charts.setObjectName("progression_treasure_charts")
        self.gridLayout_2.addWidget(self.progression_treasure_charts, 4, 1, 1, 1)
        self.progression_platforms_rafts = QtGui.QCheckBox(self.groupBox)
        self.progression_platforms_rafts.setObjectName("progression_platforms_rafts")
        self.gridLayout_2.addWidget(self.progression_platforms_rafts, 2, 0, 1, 1)
        self.progression_sidequests = QtGui.QCheckBox(self.groupBox)
        self.progression_sidequests.setObjectName("progression_sidequests")
        self.gridLayout_2.addWidget(self.progression_sidequests, 1, 0, 1, 1)
        self.progression_minigames = QtGui.QCheckBox(self.groupBox)
        self.progression_minigames.setObjectName("progression_minigames")
        self.gridLayout_2.addWidget(self.progression_minigames, 1, 1, 1, 1)
        self.progression_dungeons = QtGui.QCheckBox(self.groupBox)
        self.progression_dungeons.setChecked(True)
        self.progression_dungeons.setObjectName("progression_dungeons")
        self.gridLayout_2.addWidget(self.progression_dungeons, 0, 0, 1, 1)
        self.progression_submarines = QtGui.QCheckBox(self.groupBox)
        self.progression_submarines.setChecked(False)
        self.progression_submarines.setObjectName("progression_submarines")
        self.gridLayout_2.addWidget(self.progression_submarines, 2, 1, 1, 1)
        self.progression_triforce_charts = QtGui.QCheckBox(self.groupBox)
        self.progression_triforce_charts.setObjectName("progression_triforce_charts")
        self.gridLayout_2.addWidget(self.progression_triforce_charts, 4, 0, 1, 1)
        self.progression_misc = QtGui.QCheckBox(self.groupBox)
        self.progression_misc.setEnabled(False)
        self.progression_misc.setChecked(True)
        self.progression_misc.setObjectName("progression_misc")
        self.gridLayout_2.addWidget(self.progression_misc, 5, 1, 1, 1)
        self.progression_expensive_purchases = QtGui.QCheckBox(self.groupBox)
        self.progression_expensive_purchases.setChecked(True)
        self.progression_expensive_purchases.setObjectName("progression_expensive_purchases")
        self.gridLayout_2.addWidget(self.progression_expensive_purchases, 5, 0, 1, 1)
        self.progression_secret_caves = QtGui.QCheckBox(self.groupBox)
        self.progression_secret_caves.setChecked(True)
        self.progression_secret_caves.setObjectName("progression_secret_caves")
        self.gridLayout_2.addWidget(self.progression_secret_caves, 0, 1, 1, 1)
        self.progression_eye_reef_chests = QtGui.QCheckBox(self.groupBox)
        self.progression_eye_reef_chests.setObjectName("progression_eye_reef_chests")
        self.gridLayout_2.addWidget(self.progression_eye_reef_chests, 3, 0, 1, 1)
        self.progression_big_octos = QtGui.QCheckBox(self.groupBox)
        self.progression_big_octos.setChecked(True)
        self.progression_big_octos.setObjectName("progression_big_octos")
        self.gridLayout_2.addWidget(self.progression_big_octos, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.randomize_charts = QtGui.QCheckBox(self.groupBox_3)
        self.randomize_charts.setChecked(True)
        self.randomize_charts.setObjectName("randomize_charts")
        self.horizontalLayout_3.addWidget(self.randomize_charts)
        self.randomize_starting_island = QtGui.QCheckBox(self.groupBox_3)
        self.randomize_starting_island.setObjectName("randomize_starting_island")
        self.horizontalLayout_3.addWidget(self.randomize_starting_island)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.swift_sail = QtGui.QCheckBox(self.groupBox_2)
        self.swift_sail.setChecked(True)
        self.swift_sail.setObjectName("swift_sail")
        self.horizontalLayout_2.addWidget(self.swift_sail)
        self.instant_text_boxes = QtGui.QCheckBox(self.groupBox_2)
        self.instant_text_boxes.setChecked(True)
        self.instant_text_boxes.setObjectName("instant_text_boxes")
        self.horizontalLayout_2.addWidget(self.instant_text_boxes)
        self.reveal_full_sea_chart = QtGui.QCheckBox(self.groupBox_2)
        self.reveal_full_sea_chart.setChecked(True)
        self.reveal_full_sea_chart.setObjectName("reveal_full_sea_chart")
        self.horizontalLayout_2.addWidget(self.reveal_full_sea_chart)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.option_description = QtGui.QLabel(self.centralwidget)
        self.option_description.setMinimumSize(QtCore.QSize(0, 32))
        self.option_description.setText("")
        self.option_description.setWordWrap(True)
        self.option_description.setObjectName("option_description")
        self.verticalLayout.addWidget(self.option_description)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.about_button = QtGui.QPushButton(self.centralwidget)
        self.about_button.setObjectName("about_button")
        self.horizontalLayout.addWidget(self.about_button)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.randomize_button = QtGui.QPushButton(self.centralwidget)
        self.randomize_button.setObjectName("randomize_button")
        self.horizontalLayout.addWidget(self.randomize_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Wind Waker Randomizer", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Clean WW ISO", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Output Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Seed (optional)", None, QtGui.QApplication.UnicodeUTF8))
        self.clean_iso_path_browse_button.setText(QtGui.QApplication.translate("MainWindow", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.output_folder_browse_button.setText(QtGui.QApplication.translate("MainWindow", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.generate_seed_button.setText(QtGui.QApplication.translate("MainWindow", "New seed", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Where Should Progress Items Appear?", None, QtGui.QApplication.UnicodeUTF8))
        self.progression_treasure_charts.setText(QtGui.QApplication.translate("MainWindow", "Sunken Treasure (From Treasure Charts)", None, QtGui.QApplication.UnicodeUTF8))
        self.progression_platforms_rafts.setText(QtGui.QApplication.translate("MainWindow", "Lookout Platforms and Rafts", None, QtGui.QApplication.UnicodeUTF8))
        self.progression_sidequests.setText(QtGui.QApplication.translate("MainWindow", "Sidequests", None, QtGui.QApplication.UnicodeUTF8))
        self.progression_minigames.setText(QtGui.QApplication.translate("MainWindow", "Minigames", None, QtGui.QApplication.UnicodeUTF8))
        self.progression_dungeons.setText(QtGui.QApplication.translate("MainWindow", "Dungeons", None, QtGui.QApplication.UnicodeUTF8))
        self.progression_submarines.setText(QtGui.QApplication.translate("MainWindow", "Submarines", None, QtGui.QApplication.UnicodeUTF8))
        self.progression_triforce_charts.setText(QtGui.QApplication.translate("MainWindow", "Sunken Treasure (From Triforce Charts)", None, QtGui.QApplication.UnicodeUTF8))
        self.progression_misc.setText(QtGui.QApplication.translate("MainWindow", "Everywhere Else", None, QtGui.QApplication.UnicodeUTF8))
        self.progression_expensive_purchases.setText(QtGui.QApplication.translate("MainWindow", "Expensive Purchases", None, QtGui.QApplication.UnicodeUTF8))
        self.progression_secret_caves.setText(QtGui.QApplication.translate("MainWindow", "Secret Caves", None, QtGui.QApplication.UnicodeUTF8))
        self.progression_eye_reef_chests.setText(QtGui.QApplication.translate("MainWindow", "Eye Reef Chests", None, QtGui.QApplication.UnicodeUTF8))
        self.progression_big_octos.setText(QtGui.QApplication.translate("MainWindow", "Big Octos", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Additional Randomization Options", None, QtGui.QApplication.UnicodeUTF8))
        self.randomize_charts.setText(QtGui.QApplication.translate("MainWindow", "Randomize Charts", None, QtGui.QApplication.UnicodeUTF8))
        self.randomize_starting_island.setText(QtGui.QApplication.translate("MainWindow", "Randomize Starting Island", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Convenience Tweaks", None, QtGui.QApplication.UnicodeUTF8))
        self.swift_sail.setText(QtGui.QApplication.translate("MainWindow", "Swift Sail", None, QtGui.QApplication.UnicodeUTF8))
        self.instant_text_boxes.setText(QtGui.QApplication.translate("MainWindow", "Instant Text Boxes", None, QtGui.QApplication.UnicodeUTF8))
        self.reveal_full_sea_chart.setText(QtGui.QApplication.translate("MainWindow", "Reveal Full Sea Chart", None, QtGui.QApplication.UnicodeUTF8))
        self.about_button.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.randomize_button.setText(QtGui.QApplication.translate("MainWindow", "Randomize", None, QtGui.QApplication.UnicodeUTF8))

