from selenium import webdriver
import requests
import os
import urllib.request
from urllib.request import urlopen
from xvfbwrapper import Xvfb
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def create_dir(fname): 
    global filename 
    filename=fname
    if not os.path.isdir(filename):
        os.mkdir(filename)
    os.chdir(filename)
    print(filename)

def download(link):
   
    driver.get(link)
    name=driver.find_element_by_xpath('/html/body/div[2]/h2').text
    title=name.split(' - ')[0]
    print(title)
    l=driver.find_element_by_xpath('/html/body/div[2]/div[6]/a')
    getmp3=l.get_attribute('href')
    urllib.request.urlretrieve(getmp3,filename+'/'+str(title)+'.mp3')
    

def scrap(page):

    display = Xvfb()#Hide the browser
    display.start()  
    if page==tp:
        driver.quit()
        display.stop()
    get_url='https://pagalworld.me/files/11735/Bollywood%20Top%20Mp3%20Songs%202017/position/'+str(page)+'.html'
    url = urlopen(get_url)
    content = url.read()
    
    chromedriver_loc = '/home/ninjakx/Downloads/chromedriver' # enter path of chromedriver
    global driver
    driver = webdriver.Chrome(executable_path=chromedriver_loc)
    driver.get(get_url)
    if page==1:
        
        total_pages=driver.find_element_by_xpath('//*[@id="genreMorePageLinks"]/center/center/b').text
    
        tp=total_pages.split(' ')[3]
    print(tp)
    for i in range(10):
        s='//*[@id="genreMoreList"]/ul/li['+str(i+1)+']/b/a'
        st=driver.find_element_by_xpath(s)
        std=st.get_attribute('href')
        print(std)
        download(std)
        driver.get(get_url) 
    print(page)

'''global directory
directory='/home/raj/auth_user/'
fname=str(input("Enter filename : "))
create_dir(directory+fname) #create directory
'''  

global page
page=0
while(page<=13):
    page+=1
    scrap(page)

