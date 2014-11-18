__author__ = 'la0rg'
from selenium import webdriver


class DriverManager(object):

    firefox_driver = None
    ie_driver = None
    chrome_driver = None

    @classmethod
    def firefox(cls):
        if cls.firefox_driver is not None:
            return cls.firefox_driver
        else:
            cls.firefox_driver = webdriver.Firefox()
            return cls.firefox_driver

    @classmethod
    def ie(cls):
        if cls.ie_driver is not None:
            return cls.ie_driver
        else:
            cls.ie_driver = webdriver.Ie()
            return cls.ie_driver

    @classmethod
    def chrome(cls):
        if cls.chrome_driver is not None:
            return cls.chrome_driver
        else:
            options = webdriver.ChromeOptions()
            options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
            cls.chrome_driver = webdriver.Chrome(chrome_options=options)
            return cls.chrome_driver

    @classmethod
    def close_browsers(cls):
        if cls.firefox_driver is not None:
            cls.firefox_driver.close()
        if cls.ie_driver is not None:
            cls.ie_driver.close()
        if cls.chrome_driver is not None:
            cls.chrome_driver.close()
        cls.firefox_driver = None
        cls.ie_driver = None
        cls.chrome_driver = None