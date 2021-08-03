import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from time import sleep
import json
import instaloader
from instaloader import Profile
from instaloader import Instaloader
from instaloader import Post
import demoji
from fake_useragent import UserAgent

ig = Instaloader(sleep=True, user_agent = UserAgent().random)

def generate_folder(name):
    try:
        os.mkdir('/home/rootdebian/Scrivania/Hirundo/projects/'+name)
        os.mkdir('/home/rootdebian/Scrivania/Hirundo/projects/'+name+"/public")
        os.mkdir('/home/rootdebian/Scrivania/Hirundo/projects/'+name+"/works")
        os.mkdir('/home/rootdebian/Scrivania/Hirundo/projects/'+name+"/competitor-data")

        ig_name = input('inserisci username cliente: ')
        username = Profile.from_username(ig.context, ig_name)
        user_id = username.userid
        today = str(datetime.today().strftime('%d-%m-%Y'))

        public = open('/home/rootdebian/Scrivania/Hirundo/projects/'+name+'/public/client-data.txt', 'w')
        public.write(str(user_id)+'\n'+today)
        public.close()

        filename = 'competitor-analisys-'+str(datetime.today().strftime('%d-%m-%Y'))+'.html'
        filepath = '/home/rootdebian/Scrivania/Hirundo/projects/'+name+"/works/"+filename
        file = open(filepath, 'w')
        
    except Exception as e:
        print(e)
        print('cliente già inserito. generando il file...')
        ig_name = input('inserisci nome cliente')
        username = Profile.from_username(ig.context, ig_name)
        filename = 'competitor-analisys-'+str(datetime.today().strftime('%d-%m-%Y'))+'.html'
        filepath = '/home/rootdebian/Scrivania/Hirundo/projects/'+name+"/works/"+filename
        file = open(filepath, 'w')

    general_data = [filepath,username.username]
    
    return general_data

def find_competitors(general_data, name):
    ##LOGIN
    options = Options()
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", UserAgent().random)
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get('https://www.instagram.com/accounts/login/')
    sleep(5)
    
    driver.find_element_by_xpath('//input[@name="username"]').send_keys('best_places2k20')
    sleep(1)
    driver.find_element_by_xpath('//input[@name="password"]').send_keys('Polpetta1128')
    sleep(1)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    sleep(3)

    #GOING TO CLIENT ACCOUNT
    username = general_data[1]
    driver.get('https://www.instagram.com/'+username)
    sleep(5)
    driver.find_element_by_xpath('//button[@class="_5f5mN       jIbKX KUBKM      yZn4P   "]').click()

    competitors = []
    sleep(5)
    for i in range(18):
        try:
            span = driver.find_elements_by_xpath('//li[@class="Ckrof"]')
            for s in span:
                competitors.append(s.text.split("\n")[0])
            driver.find_element_by_xpath('//div[@class=" Kf8kP coreSpritePagingChevron    "]').click()
            sleep(2)
        except Exception as e:
            print(e)
            continue
        
    competitors = list(dict.fromkeys(competitors))
    competitor_file = open('/home/rootdebian/Scrivania/Hirundo/projects/'+name+'/public/competitor-list.txt', "w+")
    for c in competitors:
        competitor_file.write(str(c)+'\n')
    competitor_file.close()

    competitor_path = '/home/rootdebian/Scrivania/Hirundo/projects/'+name+'/public/competitor-list.txt'
    return competitor_path

def get_competitor_data(name):
    i = 0
    clist = open('/home/rootdebian/Scrivania/Hirundo/projects/'+name+'/public/competitor-list.txt')

    for c in clist.readlines():
        username = c.replace("\n", "")
        n_tot_comments = 0
        print(username)

        try:
            profile = Profile.from_username(ig.context, username)
        except:
            continue
        usm = profile.username
        
        try:
            os.mkdir('/home/rootdebian/Scrivania/Hirundo/projects/'+name+'/competitor-data/'+usm)
        except Exception as e:
            continue
        

        n_posts = profile.mediacount
        i = 0
        print(usm)

        for post  in profile.get_posts():
            i = i+1
            if post.date > datetime.today()-relativedelta(days=+1) or post.is_sponsored==True:
                continue
            shortcode = post.shortcode
            url = post.url
            like = post.likes
            comment = post.comments
            caption = post.caption
            posttype = post.typename
            date = str(post.date)
                
            if n_tot_comments<8000:
                comments = [c.text for c in post.get_comments()]
            else:
                comments = []
                
            n_tot_comments = n_tot_comments+len(comments)
            print(n_tot_comments)
            struct = {
                'url' : url,
                'type' : posttype,
                'likes' : like,
                'comments' : comment,
                'caption' : caption,
                'date' : date,
                'shortcode':shortcode,
                'comments_text':comments
                }
            with open('/home/rootdebian/Scrivania/Hirundo/projects/'+name+'/competitor-data/'+usm+'/'+str(i)+'.json', 'w') as jsfile:
                json.dump(struct, jsfile)
                jsfile.close()
                
            if i>1800:
                break

    return None

name = input('inserisci nome cliente: ')
#general_data = generate_folder(name)
#find_competitors(general_data, name)
#check = input('premi qualsiasi chiave per confermare la lista competitor')
get_competitor_data(name)
