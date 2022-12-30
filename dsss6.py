import sys  # System-specific parameters and functions

from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QAction,
                             QFileDialog, QGridLayout, QVBoxLayout, QMessageBox)

import pyqtgraph as pg
import json
import imageio.v2 as io
from PyQt5.QtCore import Qt


# Preparing the environment for the image:
class Interface(QWidget):
    def __init__(self):
        super().__init__()  # super() is used to refer the superclass from the subclass.

        # Initialize a QGridLayout
        self.l = QGridLayout(self)
        print(type(self.l))
        # Create an ImageView inside the central widget
        self.imv = pg.ImageView()
        self.l.addWidget(self.imv)
        self.setAcceptDrops(True)


# Let's define our widget
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        ## Run the function to set defaults
        self.set_defaults()
        # Creating a CentralWidget
        w = QWidget(self)
        self.setCentralWidget(
            w)  # QMainWindow takes ownership of the widget pointer and deletes it at the appropriate time.
        self.mainLayout = QVBoxLayout()
        w.setLayout(self.mainLayout)
        self.statusBar()

        # setting the minimum size
        self.setMinimumSize(250, 300)  # images of 256x256+space for buttons
        # self.setMaximumSize(1920, 1080)

        openFile = QAction('File', self)
        openFile.setShortcut('Ctrl+F')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.open)

        saveFile = QAction("&Save File", self)
        saveFile.setShortcut("Ctrl+S")
        saveFile.setStatusTip('Save File')
        saveFile.triggered.connect(self.save)

        menubar = self.menuBar()
        menubar.addAction(openFile)
        w.addAction(saveFile)
        ####------- IMAGE WIDGET  +++++++++++++++++++++++++++++  -------####
        self.imageViewer = Interface()
        self.mainLayout.addWidget(self.imageViewer)

        ####------- Make the layout look better -------####
        self.mainLayout.addStretch(1)

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.set_image(file_path)

            event.accept()
        else:
            event.ignore()

    def set_image(self, file_path):
        self.im = io.imread(file_path)
        self.imageViewer.imv.setImage(self.im)

    def set_defaults(self):  ## Set default values for the application
        # Settings for the window:
        self.status = self.statusBar()
        self.setAcceptDrops(True)  # enables drop events

        # Initialize the variable containing the image
        self.im = None

        ## Load the settings from the json file
        with open("C:/Users/rshru/OneDrive/Desktop/DSSS/6/settings.json", "r") as jsonfile:
            self.options = json.load(jsonfile)

        ## Set window options (width, height)
        width = self.options["defaults"]["width"]
        height = self.options["defaults"]["height"]
        self.resize(width, height)
        self.setWindowTitle(self.options["defaults"]["window title"])

    def clearItems(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)
                else:
                    self.clearItems(item.layout())

    ### Clear layouts inside layouts
    def clearLayouts(self, layout):
        self.clearItems(layout)
        for i in reversed(range(layout.count())):
            layout_item = layout.itemAt(i)
            self.clearItems(layout_item.layout())
            layout.removeItem(layout_item)

    ## Function to open and load an image
    def open(self):
        home_dir = "C:/Users/rshru/OneDrive/Desktop/DSSS/6"
        fn, _ = QFileDialog.getOpenFileName(self, filter="*.png *.jpg", directory=home_dir)

        if fn:
            self.status.showMessage(fn)
            self.im = io.imread(fn)
            self.imageViewer.imv.setImage(self.im)
            QMessageBox.information(self,
                                    "file loaded",
                                    "Image succesfully loaded!")
        else:
            QMessageBox.critical(self,
                                 "Error!",
                                 "Something went wrong!")

    ## Function to save an image
    def save(self):
        home_dir = "C:/Users/rshru/OneDrive/Desktop/DSSS/6"
        fn, _ = QFileDialog.getSaveFileName(self, filter="*.png *.jpg", directory=home_dir)
        msg = QMessageBox()

        if fn:
            self.status.showMessage(fn)
            value = self.imageViewer.imv.getImageItem()
            io.imwrite(fn, value.image)
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setWindowTitle("Info")
            msg.setText("Image was saved successfully!")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            returnValue = msg.exec()
        else:
            msg.setIcon(QMessageBox.Critical)
            msg.setDefaultButton(QMessageBox.Retry)
            msg.setWindowTitle("Error")
            msg.setText("Error trying to save the image!")
            msg.setInformativeText("Image could not be saved")
            returnValue = msg.exec()


def main():
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
