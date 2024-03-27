import sys
from PyQt5.Qt import *
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.Qt import QFont
from finder import WeatherFinder
from PyQt5 import QtGui
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from geopy.geocoders import Nominatim
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtWebEngineWidgets
import datetime


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        # ====================начало интерфейса====================================
        self.setGeometry(300, 100, 410, 600)
        self.setWindowIcon(QtGui.QIcon('Icon.png'))
        self.setWindowTitle('Weather')
        self.label = QLabel(self)
        pixmap = QPixmap('Light Sunny.jpg')
        self.label.setPixmap(pixmap)

        if datetime.datetime.now().strftime('%H:%M:%S') >= '18:00:00':
            pixmap = QPixmap('Dark Sunny.jpg')
            self.label.setPixmap(pixmap)

        # создание теней для QPushButton и QLineEdit
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(100)
        self.shadow.setXOffset(2)
        self.shadow.setYOffset(2)

        self.shadow2 = QGraphicsDropShadowEffect()
        self.shadow2.setBlurRadius(100)
        self.shadow2.setXOffset(2)
        self.shadow2.setYOffset(2)

        self.shadow3 = QGraphicsDropShadowEffect()
        self.shadow3.setBlurRadius(100)
        self.shadow3.setXOffset(2)
        self.shadow3.setYOffset(2)

        self.shadow4 = QGraphicsDropShadowEffect()
        self.shadow4.setBlurRadius(100)
        self.shadow4.setXOffset(2)
        self.shadow4.setYOffset(2)

        self.shadow5 = QGraphicsDropShadowEffect()
        self.shadow5.setBlurRadius(100)
        self.shadow5.setXOffset(2)
        self.shadow5.setYOffset(2)

        self.map = QLabel(self)
        self.map.resize(200, 50)
        self.map.move(100, 20)
    # конец создания теней для QPushButton и QLineEdit

    # ====================инициализация кнопки закрытия====================================

        self.clos = QPushButton(self)
        self.clos.move(700, 30)
        self.clos.resize(30, 30)
        self.clos.setStyleSheet("""
                       QPushButton{
                       background: transparent;
                        color: #383838;
                        }
                        """)
        self.clos.setIcon(QIcon('X.png'))
        self.clos.setIconSize(QSize(25, 25))
        self.clos.clicked.connect(self._back)
 
    # ====================инициализация лэйбла города====================================
    
        self.inlabel = QLabel(self)
        self.inlabel.setText("Введите город")
        self.inlabel.resize(205, 50)
        self.inlabel.move(100, 20)
        self.inlabel.setFont(QFont("Verdana", 19))
        self.inlabel.setStyleSheet("""
                QLabel{
                color: #383838}
                """)
        if datetime.datetime.now().strftime('%H:%M:%S') >= '18:00:00':
            self.inlabel.setStyleSheet("""
                            QLabel{
                            color: white}
                            """)

    # ====================инициализация поля ввода====================================

        self.city_line = QLineEdit(self)
        self.city_line.move(50, 70)
        self.city_line.resize(305, 30)
        self.setStyleSheet("""
                QLineEdit{
                border-radius: 8px;} 
                """)
        self.city_line.setGraphicsEffect(self.shadow3)
        self.main_label = QLabel(self)
   
    # ====================инициализация основного поля вывода====================================
    
        self.main_label.setText('')
        self.main_label.move(250, 250)
        self.main_label.setGeometry(205, 330, 250, 200)
        self.main_label.setFont(QFont("Verdana", 21))
        self.main_label.setStyleSheet("""
                        QLabel{
                        color: #383838}
                        """)
        if datetime.datetime.now().strftime('%H:%M:%S') >= '18:00:00':
            self.main_label.setStyleSheet("""
                            QLabel{
                            color: white}
                            """)
   
    # ====================инициализация дополнительного поля вывода====================================
    
        self.main_f_label = QLabel(self)
        self.main_f_label.setText('')
        self.main_f_label.move(250, 250)
        self.main_f_label.setGeometry(410, 50, 300, 200)
        self.main_f_label.setFont(QFont("Verdana", 13))
        self.main_f_label.setStyleSheet("""
                        QLabel{
                        color: #383838}
                        """)
        if datetime.datetime.now().strftime('%H:%M:%S') >= '18:00:00':
            self.main_f_label.setStyleSheet("""
                            QLabel{
                            color: white}
                            """)
    
    # ====================инициализация кнопки ввода====================================
    
        self.btn = QPushButton('Enter', self)
        self.btn.setFont(QFont("Microsoft Sans Serif", 10))
        self.btn.setGeometry(70, 105, 130, 50)
        self.btn.clicked.connect(self.weather)
        self.btn.setGraphicsEffect(self.shadow)
        self.btn.setStyleSheet("""
                       QPushButton{
                       border-radius: 6px;}
                       QPushButton:hover { background-color: #dcecff}
                       QPushButton:!hover { background-color: white }
                        """)
    
    # ====================инициализация кнопки перезапуска====================================
    
        self.reset = QPushButton('Reset', self)
        self.reset.setFont(QFont("Microsoft Sans Serif", 10))
        self.reset.setGeometry(70, 160, 130, 50)
        self.reset.clicked.connect(self.res)
        self.reset.setGraphicsEffect(self.shadow2)
        self.reset.setStyleSheet("""
                               QPushButton{
                               border-radius: 6px;}
                               QPushButton:hover { background-color: #dcecff}
                               QPushButton:!hover { background-color: white }
                                """)
    
    # ====================инициализация кнопки карты====================================
    
        self.maps = QPushButton('Map', self)
        self.maps.setGeometry(205, 105, 130, 50)
        self.maps.setFont(QFont("Microsoft Sans Serif", 10))
        self.maps.clicked.connect(self.openmap)
        self.maps.setGraphicsEffect(self.shadow5)
        self.maps.setStyleSheet("""
                               QPushButton{
                               border-radius: 6px;}
                               QPushButton:hover { background-color: #dcecff}
                               QPushButton:!hover { background-color: white }
                                """)
    
    # ====================инициализация кнопки дополнительной информации====================================
    
        self.lst = QPushButton('Info', self)
        self.lst.setGeometry(205, 160, 130, 50)
        self.lst.setGraphicsEffect(self.shadow4)
        self.lst.clicked.connect(self._expand)
        self.lst.setFont(QFont("Microsoft Sans Serif", 10))
        self.lst.setStyleSheet("""
                               QPushButton{
                               border-radius: 6px;}
                               QPushButton:hover { background-color: #dcecff}
                               QPushButton:!hover { background-color: white }
                                """)

    
    # ====================конец интерфейса====================================
    
    def wallpaper(self, inner):
        if inner == 'Clouds' and datetime.datetime.now().strftime('%H:%M:%S') >= '18:00:00':
            pixmap = QPixmap('d_cloud.jpg')
            self.label.setPixmap(pixmap)

        elif inner == 'Clouds':
            pixmap = QPixmap('l_cloud.jpg')
            self.label.setPixmap(pixmap)

        if inner == 'Clear' and datetime.datetime.now().strftime('%H:%M:%S') >= '18:00:00':
            pixmap = QPixmap('Dark Sunny.jpg')
            self.label.setPixmap(pixmap)
        elif inner == 'Clear':
            pixmap = QPixmap('Light Sunny.jpg')
            self.label.setPixmap(pixmap)

        if inner == 'Snow' and datetime.datetime.now().strftime('%H:%M:%S') >= '18:00:00':
            pixmap = QPixmap('D_Snow.png')
            self.label.setPixmap(pixmap)
        elif inner == 'Snow':
            pixmap = QPixmap('L_Snow.png')
            self.label.setPixmap(pixmap)

        if inner == 'Rain' and datetime.datetime.now().strftime('%H:%M:%S') >= '18:00:00':
            pixmap = QPixmap('D_Rain.jpg')
            self.label.setPixmap(pixmap)
        elif inner == 'Rain':
            pixmap = QPixmap('L_Rain.jpg')
            self.label.setPixmap(pixmap)

        if inner == 'Fog' and datetime.datetime.now().strftime('%H:%M:%S') >= '18:00:00':
            pixmap = QPixmap('D_Fog.jpg')
            self.label.setPixmap(pixmap)
        elif inner == 'Fog':
            pixmap = QPixmap('L_Fog.jpg')
            self.label.setPixmap(pixmap)

        # ====================Смена обоев взависимости от времени и погоды====================================

    def weather(self):
        wr.set_city(self.city_line.text())
        try:
            dat = wr.get_weather()
            self.main_label.setText(dat[0])
            self.main_f_label.setText(dat[1])
            self.wallpaper(dat[2])

        except Exception as ex:
            self.main_f_label.setText('City error. Try again')
            self.main_label.setText('')

    # ====================Проверка на ошибку и выполнения запроса====================================

    def openmap(self):
        Mp.set_city(self.city_line.text())
        Mp.find_city()

    def res(self):
        self.main_f_label.setText('')
        self.main_label.setText('')
        self.city_line.setText('')
        if datetime.datetime.now().strftime('%H:%M:%S') >= '18:00:00':
            pixmap = QPixmap('Dark Sunny.jpg')
            self.label.setPixmap(pixmap)
        else:
            pixmap = QPixmap('Light Sunny.jpg')
        self.label.setPixmap(pixmap)
        Mp.hide()

    def _expand(self):
        for i in range(410, 770 + 1, 11):
            if i:
                self.resize(i, 600)
                self.repaint()

    def _back(self):
        for i in reversed(range(410, 770 + 1, 11)):
            if i:
                self.resize(i, 600)
                self.repaint()

    def sum(self):
        self.sunI.deleteLater()
        self.sunI = None


class MapFind(QtWebEngineWidgets.QWebEngineView):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 100, 1000, 600)

    def set_city(self, city):
        self.city = city

    def find_city(self):
        geolocator = Nominatim(user_agent="Weather")
        location = geolocator.geocode(self.city)
        url = f"https://yandex.ru/pogoda/maps/nowcast?lat={location.latitude}&lon={location.longitude}" \
              f"&via=mmapw&le_Lightning=1"
        self.load(QtCore.QUrl(url))
        self.show()

    # ====================Запуск карты====================================


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wr = WeatherFinder()
    ex = MainWindow()
    Mp = MapFind()
    ex.show()
    sys.exit(app.exec_())
# ====================запуск====================================
