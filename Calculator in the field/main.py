from PyQt5 import QtWidgets
from ui import Ui_MainWindow
import algorithm

def res():
    if ui.Number.toPlainText():
        try:
            if algorithm.IsPrime(ui.Field.toPlainText()):
                ui.Answer.setText(f'{ui.Number.toPlainText()}^(-1) in field {ui.Field.toPlainText()} = {algorithm.revers(ui.Number.toPlainText(), ui.Field.toPlainText())}')
            else:
                ui.Answer.setText('!!!Field is not prime!!!')
        except:
            ui.Answer.setText('!!!Make sure that the input is correct!!!')
            
    if ui.Expression.toPlainText():
        try:
            if algorithm.IsPrime(ui.Field.toPlainText()):
                ui.Answer.setText(f'({ui.Expression.toPlainText()}) (mod {ui.Field.toPlainText()}) = {algorithm.counting(ui.Expression.toPlainText(), ui.Field.toPlainText())}')
            else:
                ui.Answer.setText('!!!Field is not prime!!!')
        except:
            ui.Answer.setText('!!!Make sure that the input is correct!!!')

    if ui.Number.toPlainText() and ui.Expression.toPlainText():
        try:
            if algorithm.IsPrime(ui.Field.toPlainText()):
                ui.Answer.setText(f'({ui.Expression.toPlainText()}) (mod {ui.Field.toPlainText()}) = {algorithm.counting(ui.Expression.toPlainText(), ui.Field.toPlainText())} \n{ui.Number.toPlainText()}^(-1) in field {ui.Field.toPlainText()} = {algorithm.revers(ui.Number.toPlainText(), ui.Field.toPlainText())}')
            else:
                ui.Answer.setText('!!!Field is not prime!!!')
        except:
            ui.Answer.setText('!!!Make sure that the input is correct!!!')


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    ui.Enter.clicked.connect(lambda: res())
    sys.exit(app.exec_())