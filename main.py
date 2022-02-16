from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytube import YouTube

Keyword = input("Paste the Keyword to be searched : ")
link = f'https://www.youtube.com/results?search_query={Keyword}'
driver = webdriver.Chrome("Path to Chromedriver") #Enter path of your chromedrive.exe
driver.maximize_window()

driver.get(link)
time.sleep(1)


#Getting All the URLs in the Page
links = driver.find_elements_by_xpath("//a[@href]")
time.sleep(0.40)

#Looping through the URLs and Printing them
for i in links:
	href = i.get_attribute("href")
	
	try:
		if(len(href)==43):
			yt = YouTube(href)
			print('\n\n')

			print("Video URL: " +href)
			print("Title :", yt.title)
			print("Views :", yt.views)
			print("Duration :", yt.length)
			print("==================================\n")

			with open('YoutubeScrapedList.txt','a') as f:
				f.write("Video URL: " + href + '\n' + "Title: " + yt.title + '\n' + "Views: " + str(yt.views) +'\n' + "Duration: " + str(yt.length) +'\n' + "============================\n")
	
	except:
		print("Video Unavaliable- Automatically Filtered from the List")
  	

driver.quit()





	
