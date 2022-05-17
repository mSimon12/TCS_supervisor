from re import U
import sys
from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw
from main_design import Ui_main


class Interface(qtw.QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_main()
        self.ui.setupUi(self)
        
        self.ui.gen_button.clicked.connect(self.generate)
        
    def generate(self):
        
        self.ui.label.setText('Already generated')
        print("Hallo")

    
if __name__ == "__main__":
    app = qtw.QApplication([])
    
    main_win = Interface()
    main_win.show()
    sys.exit(app.exec_())