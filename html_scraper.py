import mechanize
from bs4 import BeautifulSoup
import urllib2 
import cookielib
import selenium as selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys, getopt

def main(argv):


	# url = argv[0].replace("_", "+")
	# serving_size = argv[1]

	driver = webdriver.Firefox()
	driver.get(argv[0])
	

	#driver = webdriver.PhantomJS()

if __name__ == "__main__":
   main(sys.argv[1:])
