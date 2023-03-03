from PyQt5 import QtWidgets
from ui import Ui_MainWindow
import algorithm.py
import art

def res():
    pic = art.text2art('LidCode')
    if not ui.textV.toPlainText():
        try:
            if ui.matrixG.isChecked() == True:
                ui.textOut.setText(f'{pic}\n{lab1.enter_G(ui.textEnter.toPlainText())}')
            elif ui.matrixH.isChecked() == True:
                ui.textOut.setText(f'{pic}\n{lab1.enter_H(ui.textEnter.toPlainText())}')
            else:
                ui.textOut.setText('!!!Select the matrix type!!!')
        except:
            ui.textOut.setText('!!!Make sure that the input is correct!!!')
    else:
        try:
            if ui.matrixG.isChecked() == True:
                ui.textOut.setText(f'{pic}\n{lab1.enter_G(ui.textEnter.toPlainText())}{lab1.enter_VG(ui.textEnter.toPlainText(), ui.textV.toPlainText())}')
            elif ui.matrixH.isChecked() == True:
                ui.textOut.setText(f'{pic}\n{lab1.enter_H(ui.textEnter.toPlainText())}{lab1.enter_VH(ui.textEnter.toPlainText(), ui.textV.toPlainText())}')
            else:
                ui.textOut.setText('!!!Select the matrix type!!!')
        except:
            ui.textOut.setText('!!!Make sure that the input is correct!!!')

def check():
    if ui.matrixG.isChecked() == True:
        ui.textV.setText('0 1 0 1 0 0 0 1')

    elif ui.matrixH.isChecked() == True:
        ui.textV.setText('0 1 1 1 0 0 0 1')


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    ui.textEnter.setText('1 0 1 1 1 1 0 0\n0 1 1 1 0 1 0 0\n0 0 1 1 1 0 1 0\n0 0 0 1 1 1 0 1')
    ui.textV.setText('1 0 0 0 0 1 0 0')

    # ui.matrixG.clicked.connect(lambda: check())
    # ui.matrixH.clicked.connect(lambda: check())
    ui.enter.clicked.connect(lambda: res())
    sys.exit(app.exec_())
