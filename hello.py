#!/usr/bin/env python

import flask
from flask import request
from flask import make_response
import selenium as selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys, getopt

# Create the application.
app = flask.Flask(__name__)


@app.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index.html')


@app.route('/getIndeedInfo', methods=['POST'])
def getIndeedInfo():

	job = request.json['job']
	location = request.json['location']
	#driver = webdriver.Firefox()
	driver = webdriver.PhantomJS()
	driver.get("http://www.indeed.com/jobs?q="+job+"&l="+location+"&utm_source=publisher&utm_medium=organic_listings&utm_campaign=affiliate")
	resultsCol = driver.find_element_by_id("resultsCol")
	links = resultsCol.find_elements_by_tag_name("a")
	links[2].click() #first job result
	response = {}
	response["link"] = links[2].get_attribute("href")
	response["jobTitle"] = driver.find_element_by_css_selector(".jobtitle").get_attribute("innerHTML")
	response["company"] = driver.find_element_by_css_selector(".company").get_attribute("innerHTML")
	response["summary"] = driver.find_element_by_css_selector(".snip").get_attribute("innerHTML")
	response["location"] = driver.find_element_by_css_selector(".location").get_attribute("innerHTML")



	return flask.jsonify(**response)


if __name__ == '__main__':
    app.debug=True
    app.run()