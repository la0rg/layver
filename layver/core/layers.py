from PIL import Image
from PIL import ImageDraw

__author__ = 'la0rg'
from selenium import webdriver


class Marker(object):

    def mark_errors(self, filename, coordinate_list):
        im = Image.open("media/{0}".format(filename))
        draw = ImageDraw.Draw(im)

        for obj in coordinate_list:
            draw.line([obj[0]['x'], obj[0]['y'], obj[0]['x'], obj[0]['y']+obj[1]['height']], fill="red", width=3)
            draw.line([obj[0]['x'], obj[0]['y'], obj[0]['x']+obj[1]['width'], obj[0]['y']], fill="red", width=3)
            draw.line([obj[0]['x'], obj[0]['y']+obj[1]['height'], obj[0]['x']+obj[1]['width'], obj[0]['y']+obj[1]['height']], fill="red", width=3)
            draw.line([obj[0]['x']+obj[1]['width'], obj[0]['y'], obj[0]['x']+obj[1]['width'], obj[0]['y']+obj[1]['height']], fill="red", width=3)

        del draw
        im.save("media/marks/mark_errors_screen_{0}.png".format(filename[8:]))
        return "mark_errors_screen_{0}.png".format(filename)


class CoordinateList:

    def __init__(self, browser):
        self.browser = browser
        self.coordinates = []
        self.processing()

    def processing(self):
        list = self.browser.find_elements_by_css_selector("td")
        for item in list:
            self.coordinates.append((item.location, item.size))

    def compare(self, cl, tolerance):
        result = []
        for i in range(0, len(self.coordinates)):
            if abs(self.coordinates[i][0]['x'] - cl.coordinates[i][0]['x']) > tolerance:
                result.append(self.coordinates[i])
            elif abs(self.coordinates[i][0]['y'] - cl.coordinates[i][0]['y']) > tolerance:
                result.append(self.coordinates[i])
        return result



# driver = webdriver.Firefox()
# driver.get("http://nstu.ru/")
# driver1 = webdriver.Ie()
# driver1.get("http://nstu.ru/")
#
#
# cl1 = CoordinateList(driver)
# print(cl1.coordinates)
# cl2 = CoordinateList(driver1)
# print(cl2.coordinates)
#
#
# print(cl1.compare(cl2, 140))
# print(cl2.compare(cl1, 83))
# mark_errors(driver, "firefox", cl1.compare(cl2, 140))
# mark_errors(driver1, "Ie", cl2.compare(cl1, 83))
#
#
# driver.close()
# driver1.close()









