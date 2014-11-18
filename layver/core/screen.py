import os
import PIL
from layver.core.DriverManager import DriverManager
from layver_project import settings

__author__ = 'la0rg'

from selenium import webdriver
import time
from PIL import ImageGrab


class Screener:

    def __init__(self, link, id, sleep=3):
        self.sleep = sleep
        self.link = link
        self.browser = None
        self.filename = None
        self.id = id

    def get_sh_firefox(self):
        self.browser = DriverManager.firefox()
        self.filename = "{0}_sh_firefox.png".format(self.id)
        self.take_screenshoot1()
        return "screens/"+self.filename

    def get_sh_ie(self):
        self.browser = DriverManager.ie()
        self.filename = "{0}_sh_ie.png".format(self.id)
        self.take_screenshoot1()
        return "screens/"+self.filename

    def get_sh_chrome(self):
        self.browser = DriverManager.chrome()

        self.filename = "{0}_sh_chrome.png".format(self.id)
        self.chrome_take_screenshot()
        return "screens/"+self.filename

    def take_screenshoot1(self):
        self.browser.set_window_size(1280, 768)
        self.browser.set_window_position(0, 0)

        self.browser.get(self.link)
        time.sleep(self.sleep)

        self.browser.save_screenshot("media/screens/" + self.filename)

    def chrome_take_screenshot(self):
        self.browser.set_window_size(1280, 768)
        self.browser.set_window_position(0, 0)

        self.browser.get(self.link)
        time.sleep(self.sleep)

        #Получаем данные о странице из браузера
        total_width = self.browser.execute_script("return document.body.offsetWidth")
        total_height = self.browser.execute_script("return document.body.parentNode.scrollHeight")

        viewport_width = self.browser.execute_script("return document.body.clientWidth")
        viewport_height = self.browser.execute_script("return window.innerHeight")

        #Разбить рабочую область браузера на прямоугольники
        rectangles = []

        i = 0
        while i < total_height:
            ii = 0
            top_height = i + viewport_height

            if top_height > total_height:
                top_height = total_height

            while ii < total_width:
                top_width = ii + viewport_width

                if top_width > total_width:
                    top_width = total_width

                rectangles.append((ii, i, top_width, top_height))

                ii = ii + viewport_width

            i = i + viewport_height

        #Загатовка размером сайта
        stitched_image = PIL.Image.new('RGB', (total_width, total_height))
        previous = None
        part = 0
        for rectangle in rectangles:
            #Если это не начало сайта, то скроллим
            if not previous is None:
                self.browser.execute_script("window.scrollTo({0}, {1})".format(rectangle[0], rectangle[1]))
                time.sleep(0.2)

            file_name = "media/tmp/scroll_part_{0}.png".format(part)
            print(file_name)
            print(self.browser.save_screenshot(file_name))

            screenshot = PIL.Image.open(file_name)

            if rectangle[1] + viewport_height > total_height:
                offset = (rectangle[0], total_height - viewport_height)

            else:
                offset = (rectangle[0], rectangle[1])

            stitched_image.paste(screenshot, offset)

            del screenshot

            #os.remove(file_name)

            part += 1
            previous = rectangle

        stitched_image.save("media/screens/" + self.filename)
        return True

    def get_sh_pack(self):
        return [self.get_sh_firefox(), self.get_sh_ie(), self.get_sh_chrome()]


#screener1 = Screener("http://it-om.ru", 1)
#sprint(screener1.get_sh_pack())

