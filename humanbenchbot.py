#!/usr/bin/env python3
# coding: utf-8

from selenium import webdriver
from time import sleep
import sys

def start_browser():
    global browser
    browser = webdriver.Firefox()
    browser.get('http://www.humanbenchmark.com/tests/reactiontime')

def green():
    try:
        #elem = browser.find_element_by_class_name('view-go') #speed?
        elem = browser.find_element_by_css_selector('div.view-go')
        return (True, elem)
    except:
        return (False, None)

def run_loop(times):
    clicked = 0
    while clicked < times:
        green_status, elem = green()
        if green_status:
            elem.click()
            clicked += 1
        
def main():
    start_browser()
    if len(sys.argv) > 1:
        run_loop(int(sys.argv[1]))
    else:
        times = ''
        while not times:
            times = int(input('How many times should the clicker run?\n'))
        run_loop(times)

if __name__ == '__main__':
    sys.exit(main())