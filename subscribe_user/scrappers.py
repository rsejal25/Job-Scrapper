from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
#from data_layer import *
#from data_layer.Naukri_jobs import Naukri_jobs
from selenium.webdriver.chrome.options import Options
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def sendEmail(toaddr):
 formaddr='nuakrijob@gmail.com'
 msg=MIMEMultipart()
 msg['From']=formaddr
 msg['To']=toaddr
 msg['Subject']='Job portal'
 body='Hello '+toaddr;
 msg.attach(MIMEText(body,'plain'))
 filename="Job_List_File.csv"
 attachment=open('Naukri_File.csv','rb')
 p=MIMEBase('application','octet-stream')
 p.set_payload((attachment).read())
 encoders.encode_base64(p)
 p.add_header('Content-Disposition','attachment;filename="Job_List_File.csv"')
 msg.attach(p)
 s=smtplib.SMTP('smtp.gmail.com',587)
 s.starttls()
 s.login(formaddr,'cuxuqwvfhlkytemg')
 text=msg.as_string()
 s.sendmail(formaddr,toaddr,text)
 s.quit()
 print('sending email')




def webScrapper(job_title,job_location):
 PATH="C:\Program Files (x86)\chromedriver.exe"
 driver=webdriver.Chrome()
 options = webdriver.ChromeOptions()
 options.add_experimental_option('excludeSwitches', ['enable-logging'])
 driver=webdriver.Chrome(options=options)

 print('scapping starts')
 URL='https://www.naukri.com'
 driver.get(URL)
 print('okk started')
 time.sleep(10)
 inputDiv=driver.find_element(By.CLASS_NAME,'qsb')
 inputSubDivs=inputDiv.find_elements(By.CLASS_NAME,'suggestor-input')
 print(len(inputSubDivs))
 inputSubDivs[0].send_keys(job_title)
#value1=input.get_attribute('value')
#print(value1,type(value1))
 time.sleep(5)
 #input2=driver.find_element(By.CLASS_NAME,'suggestor-input')
 inputSubDivs[1].send_keys(job_location)
 time.sleep(5)
 inputSubDivs[1].send_keys(Keys.RETURN)
 time.sleep(5)
 jobs_list=[]
 csv_file=open('Naukri_file.csv','w',encoding='utf-8')
 csv_writer=csv.writer(csv_file)
 csv_writer.writerow(['Job Title','Company Name','Vacancy Link','salary','Experience needed','skills']) 
 x=1
 while x<=1:
  print(driver.title)
  try:
    list1=WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME,"list")))
    #print(next_page,type(next_page))
  except TimeoutException:
    driver.quit()
  #list1=driver.find_elements(By.CLASS_NAME,'list')
  for list2 in list1:
   articles1=list2.find_elements(By.CLASS_NAME,"jobTuple")
   for article1 in articles1:
     headers=article1.find_elements(By.CLASS_NAME,"jobTupleHeader")
     skills=article1.find_element(By.CSS_SELECTOR,"ul.tags.has-description")
     print(type(skills.text))
     skill_lst=skills.text.replace('\n',',')
     print(skill_lst)
     #items=skills.find_elements(By.TAG_NAME,"li")
     descriptions=article1.find_element(By.CSS_SELECTOR,"div.ellipsis.job-description")
     print(descriptions.text)
     total_days_before=article1.find_elements(By.CSS_SELECTOR,"span.fleft.postedDate")
     for header in headers:
      #skills=header.find_element(By.CLASS_NAME,"tags")
      #print(skills,type(skills))
      #items=skills.find_elements(By.TAG_NAME,"li")
      jds=header.find_element(By.TAG_NAME,'ul')
      #location=jds.find_elememt(By)   
      locations=jds.find_element(By.CSS_SELECTOR,"li.fleft.br2.placeHolderLi.location")
      print(locations.text)
      experiences=jds.find_element(By.CSS_SELECTOR,"li.fleft.br2.placeHolderLi.experience")
      salaries=jds.find_element(By.CSS_SELECTOR,"li.fleft.br2.placeHolderLi.salary")
      print(salaries.text,experiences.text)
      infos=header.find_elements(By.CSS_SELECTOR,"div.info.fleft")
      for info in infos:
        anchors=info.find_element(By.CSS_SELECTOR,"a.title.ellipsis")
        vacancy_links=info.find_element(By.CSS_SELECTOR,"a.title.ellipsis")
        print(vacancy_links.get_attribute('href'))
        firms=info.find_element(By.CSS_SELECTOR,"a.subTitle.ellipsis.fleft")
        print(firms.get_attribute('href'))
        #ratings=info.find_element(By.CSS_SELECTOR,'span.starRating.fleft')
        #print(ratings.text)
        #locations=info.find_element(By.CSS_SELECTOR,"li.fleft.br2.placeHolderLi.location")
        #print(locations,len(locations))
        #experiences=info.find_elements(By.CSS_SELECTOR,"li.fleft.br2.placeHolderLi.experience")
        #salaries=info.find_elements(By.CSS_SELECTOR,"li.fleft.br2.placeHolderLi.salary")
        #print(salaries,len(salaries))
        description_link=vacancy_links.get_attribute('href')
        #reviews=info.find_elements(By.CSS_SELECTOR,"a.reviewsCount.ml-5.fleft.blue-text")
        csv_writer.writerow([anchors.get_attribute('text'),firms.get_attribute('text'),description_link,salaries.text,experiences.text,skill_lst])
        #jobs_list.append((anchor.text,firm.text,description_link,skill_list,experience.text,salary.text,location.text,description.text,days_before.text,rating1,review1)) 
        
        #skills=driver.find_element_by_class_name("tags")
        #items=skills.find_elements_by_tag_name("li")
        #skill_list=[]

     
  print("******************************************************************")
  if x<6:
   #next_page=driver.find_element_by_css_selector("a.fright.fs14.btn-secondary.br2").get_attribute('href');
   try:
    next_page=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"a.fright.fs14.btn-secondary.br2")))
    print(next_page,type(next_page))
   except TimeoutException:
    driver.quit()
   #next_page=driver.find_element_by_css_selector("a.fright.fs14.btn-secondary.br2").get_attribute('href');
   driver.get(next_page.get_attribute('href'))
   time.sleep(10)
  x=x+1
 csv_file.close()  
 return None
 #Naukri_jobs.enter_jobs_details(jobs_list)
#print(value2,type(value2))
#list=webScrapper("software developer","Bangalore")
#sendEmail('0701CS191050@uecu.ac.in')




	
#for i in list:
 #print(i)