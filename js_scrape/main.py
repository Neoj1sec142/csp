import mechanize
import urllib3
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchAttributeException
from selenium.webdriver.common.keys import Keys
import os
import re


br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(False)
br.addheaders = [('User-agent', 'Firefox')]

browser = webdriver.Firefox('js-scrape')
browser.get("https//www.applebees.com")
