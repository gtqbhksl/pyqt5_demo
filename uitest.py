from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5 import uic


class Stats:
    def __init__(self):
        # 从文件中加载UI定义
        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = uic.loadUi("untitled.ui")

        # 提取要操作的控件
        self.user_name_qwidget = self.ui.lineEdit  # 用户名输入框
        self.password_qwidget = self.ui.lineEdit_2  # 密码输入框
        self.btn1 = self.ui.Button  # 按钮1
        self.btn2 = self.ui.Button_2  # 按钮2
        self.textBrowser = self.ui.textBrowser  # 文本显示区域

        # 绑定信号与槽函数
        self.btn1.clicked.connect(self.login)

    def login(self):
        """登录按钮的槽函数"""
        user_name = self.user_name_qwidget.text()
        password = self.password_qwidget.text()
        if user_name == "admin" and password == "123456":
            self.textBrowser.setText("欢迎%s" % user_name)
            self.textBrowser.repaint()
        else:
            self.textBrowser.setText("用户名或密码错误....请重试")
            self.textBrowser.repaint()

if __name__=='__main__':
    app = QApplication([])
    stats = Stats()
    stats.ui.show()
    app.exec_()

