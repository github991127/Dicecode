from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QIcon, QImage

import Dicecode
from list_themes import *


class Stats:
    def __init__(self):
        # 从ui文件中加载UI定义,从UI定义中动态创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了.比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('Dicecode.ui')
        self.ui.toolButton_1.clicked.connect(self.handleCalc_delete)
        self.ui.toolButton_2.clicked.connect(self.handleCalc)
        self.ui.toolButton_3.clicked.connect(self.handleCalc_0)

    def handleCalc_delete(self):
        self.ui.textEdit_1.clear()
        self.ui.textEdit_2.clear()

    def handleCalc_0(self):
        self.ui.textEdit_2.clear()
        code = self.ui.textEdit_1.toPlainText()
        code = Dicecode.replacecode_0(code)
        codelist = Dicecode.decode(code)
        len = Dicecode.printimage(codelist)
        for i in range(len + 1):
            name = 'heiji' + str(i + 1) + '.png'
            cursor = self.ui.textEdit_2.textCursor()  # 获取光标
            cursor.insertImage(QImage(name))  # 插入本地图片
            self.ui.textEdit_2.insertPlainText(' ')
            # self.ui.textEdit_2.append("<img src='{}' style='margin-bottom:0'/>".format(name))

    def handleCalc(self):
        self.ui.textEdit_2.clear()
        code = self.ui.textEdit_1.toPlainText()
        code = Dicecode.replacecode(code)
        codelist = Dicecode.decode(code)
        len = Dicecode.printimage(codelist)
        for i in range(len + 1):
            name = 'heiji' + str(i + 1) + '.png'
            cursor = self.ui.textEdit_2.textCursor()  # 获取光标
            cursor.insertImage(QImage(name))  # 插入本地图片
            self.ui.textEdit_2.insertPlainText(' ')
            # self.ui.textEdit_2.append("<img src='{}' style='margin-bottom:0'/>".format(name))


if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon('image.png'))
    apply_stylesheet(app, theme[27], extra=extra, invert_secondary=False)  # 默认dark-False
    w = QWidget()
    w.setWindowIcon(QIcon('image.png'))
    stats = Stats()
    stats.ui.show()
    app.exec_()
