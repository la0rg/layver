from django.db import models
from layver.core.DriverManager import DriverManager
from layver.core.layers import CoordinateList, Marker
from layver.core import layers
from layver.core.screen import Screener


class Page(models.Model):
    link = models.CharField(max_length=50)
    browser1 = models.CharField(max_length=15)
    browser2 = models.CharField(max_length=15)


    def make_screenshoots(self):
        screener = Screener(self.link, self.id)
        names = screener.get_sh_pack()

        for name in names:
            screen = Screen()
            screen.image = name
            screen.page = self
            screen.save()

        return names

    def mark_errors(self, browsers, tolerance, names_of_screenshots):
        dict = {
            'ie': DriverManager.ie(),
            'firefox': DriverManager.firefox(),
            'chrome': DriverManager.chrome(),
        }

        driver1 = dict[browsers[0]]
        driver2 = dict[browsers[1]]
        cl1 = CoordinateList(driver1)
        print(cl1.coordinates)
        cl2 = CoordinateList(driver2)
        print(cl2.coordinates)

        compare1 = cl1.compare(cl2, tolerance)
        print(compare1)
        compare2 = cl2.compare(cl1, tolerance)
        print(compare2)
        error_screens = []

        es_name1 = ""
        es_name2 = ""

        #Поиск имен скриншотов с нужных браузеров
        for name in names_of_screenshots:
            if name.find(browsers[0]) != -1:
                es_name1 = name
            elif name.find(browsers[1]) != -1:
                es_name2 = name

        marker = Marker()
        error_screens.append(marker.mark_errors(es_name1, compare1))
        error_screens.append(marker.mark_errors(es_name2, compare2))

        mark_errors = MarkErrors()
        mark_errors.image_browser1 = "marks/" + error_screens[0]
        mark_errors.image_browser2 = "marks/" + error_screens[1]
        mark_errors.page = self
        mark_errors.save()


class Screen(models.Model):
    image = models.ImageField(upload_to='screens/')
    page = models.ForeignKey(Page)


class MarkErrors(models.Model):
    image_browser1 = models.ImageField(upload_to='marks/')
    image_browser2 = models.ImageField(upload_to='marks/')
    page = models.ForeignKey(Page)