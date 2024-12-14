# coding:utf-8

import sys
from autoClickUI import Ui_MainWindow  # UI方面的模块

import autoClick

from PySide6.QtWidgets import QApplication, QMainWindow



"""
利用ui转py的那个设置文件，
有一个类，这个类只是一个普通的类，继承于object，
它的关键是这个类的setupUi方法，这个方法需要传入QMainWindow类型的对象
调用这个函数会对传入的那个对象进行ui的设置。
"""


class Mymainwindow(QMainWindow,autoClick.AutoClick):
    """
    这个类继承于QMainWindow，因此它包含QMainWindow的属性和方法，
    因此可以在该类的初始化函数中，实例化autoClickUI.Ui_MainWindow这个类
    把自身作为参数调用这个setupui函数，实现对这个类的ui设置
    """

    def __init__(self, parent=None):
        """
        :param parent: 没有父类
        注意，在后续函数中改变ui中控件的值会直接影响其真实反应，并且要读取控件的值只能从ui中获取
        """
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


    def startMouseClickslot(self):
        """
为什么能够在这里定义槽函数呢？
首先在autoClickUI中连接的槽函数是MainWindow.startMouseClickslot,是在setup中连接的，
其中的MainWindow是setup函数的输入，在这个类中调用setup传入的参数是这个类myMainWindow本身(由于myMainWindow继承于QMainWindow,因此这个赋值是没问题的)
因此对于类而言，在setup中提到的startMouseClickslot就是本类中的方法，在本类中定义这个槽函数就理所应当了
"""
        print("鼠标连点槽函数开始")
        self.mouse_click(
            self.ui.mouseClickTime.value(),
            self.ui.mouseLeftorRight.currentText(),
            self.ui.mouseClickInv.value())
        # print(self.ui.mouseClickTime.value())
        # print(self.ui.mouseLeftorRight.currentText())
        # print(self.ui.mouseClickInv.value())
        # print(1)

    def startKeyClickslot(self):
        print("键盘连按槽函数开始")
        self.key(
            self.ui.keyChar.text(),
            self.ui.keyClickTime.value(),
            self.ui.keyClickInv.value())

# 槽函数
#     def queryWeather(self):
#         cityName = self.ui.comboBox.currentText()
#         cityCode = self.getCode(cityName)
#
#         r = requests.get("http://t.weather.sojson.com/api/weather/city/{}".format(cityCode))
#
#         print(r.json())
#
#         if r.json().get('status') == 200:
#             weatherMsg = '城市：{}\n日期：{}\n天气：{}\nPM 2.5：{} {}\n温度：{}\n湿度：{}\n风力：{}\n\n{}'.format(
#                 r.json()['cityInfo']['city'],
#                 r.json()['data']['forecast'][0]['ymd'],
#                 r.json()['data']['forecast'][0]['type'],
#                 int(r.json()['data']['pm25']),
#                 r.json()['data']['quality'],
#                 r.json()['data']['wendu'],
#                 r.json()['data']['shidu'],
#                 r.json()['data']['forecast'][0]['fl'],
#                 r.json()['data']['forecast'][0]['notice'],
#             )
#         else:
#             weatherMsg = '天气查询失败，请稍后再试！'
#
#         self.ui.textEdit.setText(weatherMsg)
#
#     def getCode(self, cityName):
#         cityDict = {"北京": "101010100",
#                     "上海": "101020100",
#                     "天津": "101030100"}
#
#         return cityDict.get(cityName, '101010100')
#
#     def clearText(self):
#         self.ui.textEdit.clear()


if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    myWin = Mymainwindow()
    myWin.show()
    print(dir(myWin))
    sys.exit(myapp.exec())
