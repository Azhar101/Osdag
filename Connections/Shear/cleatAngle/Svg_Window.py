'''
Created on Oct 20, 2016

@author: USER
'''
from PyQt4 import QtSvg, QtGui
import sys
import shutil


class SvgWindow(object):

    def call_svgwindow(self, filename, view, folder):
        self.folder = folder
        self.svgWidget = QtSvg.QSvgWidget()
        # self.svgWidget.renderer().load(filename)

        self.label = QtGui.QLabel(self.svgWidget)
        self.label.setFrameShape(QtGui.QFrame.Box)
        self.label.setFrameShadow(QtGui.QFrame.Plain)
        self.label.setPixmap(QtGui.QPixmap(filename))
        self.label.setScaledContents(True)

        self.gridlayout = QtGui.QGridLayout(self.svgWidget)
        self.gridlayout.addWidget(self.label, 0, 0, 1, 3)
        spaceritem = QtGui.QSpacerItem(260,20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spaceritem, 1, 0, 1, 1)

        self.horizontallayout = QtGui.QHBoxLayout()
        self.gridlayout.addLayout(self.horizontallayout, 1, 1, 1, 1)
        spaceritem2 = QtGui.QSpacerItem(260, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spaceritem2, 1, 2, 1, 1)
        self.svgWidget.setFixedSize(1100, 900)

        # spaceritem1 = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        # self.horizontallayout.addItem(spaceritem1)

        self.btn_save_png = QtGui.QPushButton('Save as PNG', self.svgWidget)
        self.btn_save_png.setToolTip('Saves 2D Image as PNG')
        self.btn_save_png.resize(self.btn_save_png.sizeHint())
        self.btn_save_svg = QtGui.QPushButton('Save as SVG', self.svgWidget)
        self.btn_save_svg.setToolTip('Saves 2D Image as SVG')
        self.btn_save_svg.resize(self.btn_save_svg.sizeHint())

        self.horizontallayout.addWidget(self.btn_save_png)
        self.horizontallayout.addWidget(self.btn_save_svg)

        myfont = QtGui.QFont()
        myfont.setBold(True)
        myfont.setPointSize(10)
        myfont.setFamily("Arial")
        self.btn_save_png.setFont(myfont)
        self.btn_save_svg.setFont(myfont)
        self.svgWidget.setWindowTitle('2D View')
        self.svgWidget.show()

        self.btn_save_png.clicked.connect(lambda: self.save_2d_image_png_names(view))
        self.btn_save_svg.clicked.connect(lambda: self.save_2d_image_svg_names(view))

    def save_2d_image_png_names(self, view):
        #         view = self.go_to_open_svg(view)
        # self.btn_save.clicked.connect(view)

        if view == "Front":
            png_image_path = self.folder + "/images_html/cleatFront.png"
            shutil.copyfile(png_image_path, str(QtGui.QFileDialog.getSaveFileName(None, "Save File As", self.folder + "/", "PNG (*.png)")))
        elif view == "Side":
            png_image_path = self.folder + "/images_html/cleatSide.png"
            shutil.copyfile(png_image_path, str(QtGui.QFileDialog.getSaveFileName(None, "Save File As", self.folder + "/", "PNG (*.png)")))
        else:
            png_image_path = self.folder + "/images_html/cleatTop.png"
            shutil.copyfile(png_image_path, str(QtGui.QFileDialog.getSaveFileName(None, "Save File As", self.folder + "/", "PNG (*.png)")))

        QtGui.QMessageBox.about(None, 'Information', "Image Saved")


    def save_2d_image_svg_names(self, view):
        #         view = self.go_to_open_svg(view)
        # self.btn_save.clicked.connect(view)

        if view == "Front":
            png_image_path = self.folder + "/images_html/cleatFront.svg"
            shutil.copyfile(png_image_path, str(QtGui.QFileDialog.getSaveFileName(None, "Save File As", self.folder + "/", "SVG (*.svg)")))
        elif view == "Side":
            png_image_path = self.folder + "/images_html/cleatSide.svg"
            shutil.copyfile(png_image_path, str(QtGui.QFileDialog.getSaveFileName(None, "Save File As", self.folder + "/", "SVG (*.svg)")))
        else:
            png_image_path = self.folder + "/images_html/cleatTop.svg"
            shutil.copyfile(png_image_path, str(QtGui.QFileDialog.getSaveFileName(None, "Save File As", self.folder + "/", "SVG (*.svg)")))

        QtGui.QMessageBox.about(None, 'Information', "Image Saved")


def main():
    app = QtGui.QApplication(sys.argv)
    ex = SvgWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
