#SmartTracker.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup as soup
from songline import Sendline
import re
import datetime
import schedule
import requests
import json
import urllib.parse
import sys
from selenium.webdriver.chrome.options import Options

class SmartCovid:
    def __init__(self,token,user,password,time_alarm,member,chromedriverpath):
        self.token = token
        self.user = user
        self.password = password
        self.time_alarm = time_alarm
        self.member = member
        self.r = ''
        self.chromedriverpath = chromedriverpath

    #ส่งรูป
    def sendimage(self,textimage):
        url = "https://notify-api.line.me/api/notify"
        path = 'web_screenshot.png'
        file = {'imageFile':open(path,'rb')}
        data = ({
                'message': textimage
            })
        LINE_HEADERS = {"Authorization":"Bearer "+self.token}
        session = requests.Session()
        r=session.post(url, headers=LINE_HEADERS, files=file, data=data)

    #Screenshot
    def screenweb(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        URL = 'https://news.google.com/covid19/map?hl=th&mid=%2Fm%2F07f1x&gl=TH&ceid=TH%3Ath'
        driver.get(URL)
        S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
        driver.set_window_size(1020,S('Height')) # May need manual adjustment
        driver.find_element_by_tag_name('body').screenshot('web_screenshot.png')
        driver.quit()

    def Smart(self):

        token = self.token
        message = Sendline(token)
        user = self.user #Input Username
        password = self.password #Input Password
        
        opt = webdriver.ChromeOptions()
        opt.add_argument('headless') # Don't open the browser
        opt.add_argument('window-size=1920x1080')
        opt.add_argument("disable-gpu")

        driver = webdriver.Chrome(self.chromedriverpath,options=opt) #webdriver.Chrome('C:\Python37\msedgedriver.exe')
        
        try:
            url = 'https://outsystems.pttgcgroup.com/GcSurvey_Report/Entry.aspx'
            browser = driver.get(url)

            #Click Login
            name = 'OutSystemsUIWeb_wt1$block$wtLogin$OutSystemsUIWeb_wt12$block$wtLogin$wt4'
            elem_search = driver.find_element_by_name(name)
            elem_search.send_keys(Keys.ENTER)
            Lo = True
            while Lo:
                try:
                    name_cancel = 'desktopSsoCancel'
                    elem_cancel = driver.find_element_by_id(name_cancel)
                    elem_cancel.send_keys(Keys.ENTER)
                    Lo = False
                except:
                    pass
            
            #Login User เข้าไป
            
            time.sleep(3)
            name2 = 'loginfmt'
            elem_id = driver.find_element_by_name(name2)
            elem_id.send_keys(user)
            elem_id.send_keys(Keys.ENTER)
            time.sleep(3)
            #ใส่ Password ด้วย
            name3 = 'passwd'
            time.sleep(4)
            elem_pass = driver.find_element_by_name(name3)
            elem_pass.send_keys(password)
            elem_pass.send_keys(Keys.ENTER)
            time.sleep(3)
            elem_yes = driver.find_element_by_id('idSIButton9')
            elem_yes.send_keys(Keys.ENTER)


            time.sleep(5)
            html_data = driver.page_source #ดึง html จากหน้าเว็บ
            data = soup(html_data,'html.parser') #อ่าน html
            

            #---------------------------------------------------
            detect_name = [] #เก็บรายชื่อคนที่ยังไม่ได้ทำ Daily Report
            #โหลด HTML ในหน้านั้นๆ

            for n in range(0,20):

                try:
                    
                    
                    if n == 0:
                                        
                        html_data = driver.page_source
                        data = soup(html_data,'html.parser')
                        daily = data.findAll('span',{'style':'font-weight: bold;'}) #ระบุวันที่
                        mem = data.findAll('span',{'style':'font-size: 14px;'}) #ระบุชื่อ
                        html_check = driver.page_source
                        data_check = soup(html_check,'html.parser')

                        #Listรายชื่อในหน้านั้นๆ
                        list_user = []
                        for i in range(0,len(mem)):
                            if len(mem[i].text) > 5: #เอาคำว่า "บ่าย", "ข้อ7" ออก
                                list_user.append(mem[i].text)
                        

                        #List html status
                        t = []        
                        for i,tag in enumerate(data.find_all(re.compile("^s"))):
                            t.append(str(tag))

                        #Filter only close or check
                        list_name = []
                        for i,name in enumerate(t):
                                if '"fa fa-fw fa-close"' in t[i] or '"fa fa-fw fa-check"' in t[i]:
                                        list_name.append(t[i])

                        # วน For..Loop เพื่อ
                        for i,l in enumerate(list_user):
                                #print(i)
                                j = []
                                count = 0
                                for j in range(0,3):
                                        if '"fa fa-fw fa-close"' in list_name[(i*3)+j]:
                                                count += 1
                                                
                                if count == 3:
                                        detect_name.append(l)

                    else:
                        
                        time.sleep(2)
                        name_nevi = 'wt64_OutSystemsUIWeb_wt2_block_wtContent_wtMainContent_OutSystemsUIWeb_wt128_block_wtContent_RichWidgets_wt113_block_wt28'
                        elem_nevi = driver.find_element_by_id(name_nevi)
                        elem_nevi.send_keys(Keys.ENTER)
                        time.sleep(5)

                        html_data = driver.page_source
                        data = soup(html_data,'html.parser')
                        daily = data.findAll('span',{'style':'font-weight: bold;'}) #ระบุวันที่
                        mem = data.findAll('span',{'style':'font-size: 14px;'}) #ระบุชื่อ
                        html_check = driver.page_source
                        data_check = soup(html_check,'html.parser')
                        
                        #Listรายชื่อในหน้านั้นๆ
                        list_user = []
                        for i in range(0,len(mem)):
                            if len(mem[i].text) > 5: #เอาคำว่า "บ่าย", "ข้อ7" ออก
                                list_user.append(mem[i].text)

                        #List html status
                        t = []        
                        for i,tag in enumerate(data.find_all(re.compile("^s"))):
                            t.append(str(tag))
                            #print(t[i])

                        #Filter only close or check
                        list_name = []
                        for i,name in enumerate(t):
                                if '"fa fa-fw fa-close"' in t[i] or '"fa fa-fw fa-check"' in t[i]:
                                        list_name.append(t[i])

                        # วน For..Loop เพื่อ
                        for i,l in enumerate(list_user):
                                #print(i)
                                j = []
                                count = 0
                                for j in range(0,3):
                                        if '"fa fa-fw fa-close"' in list_name[(i*3)+j]:
                                                count += 1
                                                
                                if count == 3:
                                        detect_name.append(l)

                except:
                    
                    number = len(detect_name)
                    x=datetime.datetime.now()

                    #Follow COVID-19 Situation
                    url_API = "https://covid19.th-stat.com/api/open/today"
                    response = requests.get(url_API)
                    covidreport = response.json()
                    sitcovid = ('\n พบผู้ติดเชื้อเพิ่มขึ้นในประเทศไทย {} คน \n Update: {}'.format(covidreport['NewConfirmed'],covidreport['UpdateDate']))

                    #screenshot
                    #self.screenweb()
                    
                    
                    dmy = time.ctime()[0:len(time.ctime())-5]
                    
                    aaa = ('\n Time & Date : {}\nจำนวนคนที่ยังไม่ทำ Daily Report : {} คน ดังนี้\n'.format(dmy,number))
                   
                    #เก็บค่าจำนวนตัวอักษรเดิม กรณีไม่มีรายชื่อก็ไม่ต้องส่งแผนกนั้น
                    gg = {}
                    lengg = {}
                    for k,v in self.member.items():
                        txt = '\n'+ k + '\n--------------------------\n'
                        gg[k] = txt
                        lengg[k] = len(txt)
                        
                    gg['Other'] = '\nOther\n--------------------------\n'
                    lengg['Other'] = len(gg['Other'])
                    for i in detect_name:
                        for k,v in self.member.items():
                            check = 0
                            if i in v:
                                    gg[k] = gg[k]+ i +'\n'
                                    check = 1
                                    break
                                
                        if check == 0:
                            gg['Other'] = gg['Other']+ i +'\n'
                        
                    

                    #กรณีส่งหมดทุกคนแล้ว
                    if number == 0:
                        message.sendtext('\n Time & Date : {dmy}\nทำ Daily Report ครบทุกคนแล้วครับ')
                        try:
                            self.sendimage(sitcovid)
                        except:
                            pass
                        
                    else:
                        
                        #ส่งเฉพาะแผนกที่มีรายชื่อ 
                        message.sendtext(aaa)
                        for k,v in lengg.items():
                            if len(gg[k]) > v:
                                    message.sendtext(gg[k])

                        try:
                            self.sendimage(sitcovid)
                        except:
                            pass

                        lll = ('\nขอความร่วมมือทำ COVID-19 Daily Report ครับ\n https://outsystems.pttgcgroup.com/GCSurvey/')
                        message.sendtext(lll)

                    driver.quit()
                    Done = False
                    break

        except Exception as e:
            print(e)
            driver.quit()
            Done = True

        return Done

        
    def Smarter(self):
        Lo = True
        self.screenweb()
        while Lo:
            try:
                Lo = self.Smart()
                print(Lo)
            except:
                pass

    def run(self):
        y = input('Now (y/n/reset)?: ').lower()
        if y == 'n':
            print('Start everday at {}'.format(self.time_alarm))
            schedule.every().day.at(self.time_alarm).do(self.Smarter)
            while True:
                schedule.run_pending()
                time.sleep(1)
        elif y == 'reset':
            self.time_alarm = input('time_alarm: ')
            print('Start everday at {}'.format(self.time_alarm))
            schedule.every().day.at(self.time_alarm).do(self.Smarter)
            while True:
                schedule.run_pending()
                time.sleep(1)
        else:
            print('Start now...')
            self.Smarter()
            
 
