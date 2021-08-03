import os
from datetime import datetime
from datetime import date
import instaloader
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
from instaloader import Profile
from instaloader import Post
import json
import numpy as np
import emoji
import spacy
from io import StringIO
import requests
import pickle
import matplotlib
from math import sqrt
from instaloader import Instaloader
from instaloader import Post
from sklearn.cluster import KMeans
from collections import Counter
import heapq
import demoji
from PIL import Image
from dateutil.relativedelta import relativedelta
from fake_useragent import UserAgent
from urllib.request import urlopen

ig = Instaloader(sleep=True, user_agent = UserAgent().random)

color_classifier = pickle.load(open('/home/rootdebian/Scrivania/Hirundo/competitor-analysis/colorclassifier.pkl', 'rb'))
color_cluster = KMeans(n_clusters = 3, random_state=0, max_iter=300, n_init=1 )

def select_best(like_all, comment_all):
    best = 0
    pos = 0
    positions = []
    scores = []
    
    for l,c,n in zip(like_all, comment_all, range(len(like_all))):
        val = c+l

        if val>best:
            best = val
            pos = n
            
    limit = best-(best*30)/100

    for l,c,n in zip(like_all, comment_all, range(len(like_all))):
        val = c+l

        if val>limit:
            scores.append(val)
            positions.append(n)

    bests = [list(positions), list(scores)]
    return bests

def url_to_matrix(u, c):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)

    try:
        im = Image.open(urlopen(u))
        im = im.resize((150, 150))
    except Exception as e:
        try:
            driver.get('https://www.instagram.com/p/'+c)
            sleep(10)
            tag = driver.find_element_by_xpath('//img[@class="_8jZFn"]')
            u = tag.get_attribute('src')
            im = Image.open(urlopen(u))
            im = im.resize((150, 150))
            print('occhei')
        except Exception as ex:
            sleep(10)
            tag = driver.find_element_by_xpath('//video[@class="tWeCl"]')
            u = tag.get_attribute('poster')
            r = requests.get(u, headers=UserAgent().random)
            im = Image.open(urlopen(u))
                
    return np.asarray(im)

def find_colors(mat, colors_gen):
    r = 0
    br = 0
    o = 0
    y = 0
    g = 0
    b = 0
    v = 0
    f = 0
    pi = 0
    black = 0
    white = 0

    

    color_cluster.fit_predict(mat.reshape(22500, 3))
    
    for co in color_cluster.cluster_centers_:
        p = color_classifier.predict([co])

        if p == 0:
            r = 1
        if p == 1:
            br = 1
        if p == 2:
            o = 1
        if p == 3:
            y = 1
        if p == 4:
            g = 1
        if p == 5:
            b = 1
        if p == 6:
            v = 1
        if p == 7:
            f = 1
        if p == 8:
            pi = 1
        if p == 9:
            white = 1
        if p==10:
            black= 1
    cc = r+br+o+y+f
    wc = g+b+v+pi
            
    colors = np.array([r,br,o,y,g,b,v,f,pi,white,black])
    colors_gen[0].append(r)
    colors_gen[1].append(br)
    colors_gen[2].append(o)
    colors_gen[3].append(y)
    colors_gen[4].append(g)
    colors_gen[5].append(b)
    colors_gen[6].append(v)
    colors_gen[7].append(f)
    colors_gen[8].append(pi)
    colors_gen[9].append(white)
    colors_gen[10].append(black)
    colors_gen[11].append(cc)
    colors_gen[12].append(wc)
    colors_features = np.array([cc, wc])
    color = np.array([(colors)/np.sum(colors), (colors_features)/np.sum(colors)])
    color = [list(color[0]), list(color[1])]
    return color

def saturationn(mat, satur_mean, satur_var):
    sat_value = np.array([])
    sat_h = 0
    sat_m = 0
    sat_l = 0

    for px in mat.reshape(22500, 3)*255:
        sat_value = np.append(sat_value,matplotlib.colors.rgb_to_hsv(px)[1])
            
    sat_mean = np.mean(sat_value)
    satur_mean.append(sat_mean)

    if sat_mean<0.33:
        sat_l = 1
    if 0.66>sat_mean>0.33:
        sat_m = 1
    if sat_mean>0.66:
        sat_h = 1
        
    sat_var = np.var(sat_value)
    satur_var.append(sat_var)

    saturation = [sat_h, sat_m, sat_l, sat_var, sat_mean]

    return saturation

def brightnesss(mat, bright_mean, bright_var):
    bri_value = np.array([])
    bri_h = 0
    bri_m = 0
    bri_l = 0

    for px in mat.reshape(22500, 3)*255:
        bri_value = np.append(bri_value, sqrt(0.299*(px[0]**2) + 0.587*(px[1]**2) + 0.114*(px[2]**2))/255)

    bri_mean = np.mean(bri_value)
    bright_mean.append(bri_value)
    
    if bri_mean<0.33:
        bri_l = 1
    if 0.66>bri_mean>0.33:
        bri_m = 1
    if bri_mean>0.66:
        bri_h = 1
    
    
    bri_var = np.var(bri_value)
    bright_var.append(bri_var)

    brightness = [bri_h, bri_m, bri_l, bri_var, bri_mean]

    return brightness

#def pad(brightn, satur):
    #p = 0.69*brightn[-1] + 0.22*satur[-1]
    #a = -0.31*brightn[-1] + 0.60*satur[-1]
    #d = -0.76*brightn[-1] + 0.32*satur[-1]

    #pad = [p,a,d]
    #return pad

def myself_stats(colors_gen, bright_mean_gen, bright_var_gen, satur_mean_gen, satur_var_gen, path):
    for competitor in os.listdir(path):
        with open(path+competitor+'/DATA.json', 'r') as fi:
            data = json.load(fi)
            
            colors_gen[0].append(np.round(np.mean([c[0][0] for c in data['colors']]), 3))
            colors_gen[1].append(np.round(np.mean([c[0][1] for c in data['colors']]), 3))
            colors_gen[2].append(np.round(np.mean([c[0][2] for c in data['colors']]), 3))
            colors_gen[3].append(np.round(np.mean([c[0][3] for c in data['colors']]), 3))
            colors_gen[4].append(np.round(np.mean([c[0][4] for c in data['colors']]), 3))
            colors_gen[5].append(np.round(np.mean([c[0][5] for c in data['colors']]), 3))
            colors_gen[6].append(np.round(np.mean([c[0][6] for c in data['colors']]), 3))
            colors_gen[7].append(np.round(np.mean([c[0][7] for c in data['colors']]), 3))
            colors_gen[8].append(np.round(np.mean([c[0][8] for c in data['colors']]), 3))
            colors_gen[9].append(np.round(np.mean([c[0][9] for c in data['colors']]), 3))
            colors_gen[10].append(np.round(np.mean([c[0][10] for c in data['colors']]), 3))

            colors_gen[11].append(np.round(np.mean([c[1][0] for c in data['colors']]), 3)*100)
            colors_gen[12].append(np.round(np.mean([c[1][1] for c in data['colors']]), 3)*100)
            
            #BRIGHTNESS
            bright_mean_gen.append(np.round(np.mean([b[4] for b in data['brightness']]), 3))
            bright_var_gen.append(np.round(np.mean([b[3] for b in data['brightness']]), 3))

            #SATURATION
            satur_mean_gen.append(np.round(np.mean([b[4] for b in data['saturation']]), 3))
            satur_var_gen.append(np.round(np.mean([b[3] for b in data['saturation']]), 3))
    return None

colors_gen = [[],[],[],[],[],[],[],[],[],[],[], [], []]
bright_mean_gen = []
bright_var_gen = []
satur_mean_gen = []
satur_var_gen = []


name = 'Alessandro Marino'
path = '/home/rootdebian/Scrivania/Hirundo/projects/'+name+'/competitor-data/'

i = 0
for competitor in os.listdir(path):
    
    print(competitor)
    print('==============================')
    i += 1

    if i<38:
        continue
    url = np.array([])
    codes = np.array([])
    typepost = np.array([])
    like_all = []
    comment_all = []
    time = np.array([])
    
    for f in os.listdir(path+competitor):
        if 'DATA' in f:
            continue
        try:
            with open(path+competitor+'/'+f) as js:
                data = json.load(js)
                like_all.append(data['likes'])
                comment_all.append(data['comments'])
                typepost = np.append(typepost, data['type'])
                time = np.append(time, data['date'])
        except Exception as e:
            print(e)
            break

    typepost = Counter(typepost)
    bests = select_best(like_all, comment_all)
    best_url = []
    best_c = []

    for b in bests[0]:
        pathf = path+competitor+'/'+str(b)+'.json'
        with open(pathf) as js:
            data = json.load(js)
            best_url.append(data['url'])
            best_c.append(data['shortcode'])
    
    colors = []
    satur = []
    brightn = []
    
    for u, c in zip(best_url, best_c):
        try:
            mat = url_to_matrix(u, c)
            colors.extend([find_colors(mat, colors_gen)])
            satur.extend([saturationn(mat, satur_mean, satur_var)])
            brightn.extend([brightnesss(mat, bright_mean, bright_var)])
        except Exception as e:
            print(e, u)
            continue
        
    picture_features = {
        'type_post': typepost,
        'colors':colors,
        'saturation':satur,
        'brightness':brightn,
        'best_pictures': bests[0]
        }
    with open(path+competitor+'/DATA.json', 'r') as j:
        old_data = json.load(j)
        data = old_data.update(picture_features)
        print(data, 'ok', old_data)
    with open(path+competitor+'/DATA.json', 'w') as j:
        json.dump(old_data, j)
        j.close()
    print('ok')

myself_stats(colors_gen, bright_mean_gen, bright_var_gen, satur_mean_gen, satur_var_gen, path)

colors_gen[0] = np.round(np.mean(colors_gen[0]), 3)
colors_gen[1] = np.round(np.mean(colors_gen[1]), 3)
colors_gen[2] = np.round(np.mean(colors_gen[2]), 3)
colors_gen[3] = np.round(np.mean(colors_gen[3]), 3)
colors_gen[4] = np.round(np.mean(colors_gen[4]), 3)
colors_gen[5] = np.round(np.mean(colors_gen[5]), 3)
colors_gen[6] = np.round(np.mean(colors_gen[6]), 3)
colors_gen[7] = np.round(np.mean(colors_gen[7]), 3)
colors_gen[8] = np.round(np.mean(colors_gen[8]), 3)
colors_gen[9] = np.round(np.mean(colors_gen[9]), 3)
colors_gen[10] = np.round(np.mean(colors_gen[10]), 3)
colors_gen[11] = np.round(np.mean(colors_gen[11]), 3)
colors_gen[12] = np.round(np.mean(colors_gen[12]), 3)

bright_mean_gen = np.round(np.mean(bright_mean_gen), 3)
bright_var_gen = np.round(np.mean(bright_var_gen), 3)
satur_mean_gen = np.round(np.mean(satur_mean_gen), 3)
satur_var_gen = np.round(np.mean(satur_var_gen), 3)

best_pic_features = {
    'colors': colors_gen,
    'bright_mean': bright_mean_gen,
    'bright_var': bright_var_gen,
    'satur_mean': satur_mean_gen,
    'satur_var': satur_var_gen
    }

with open('/home/rootdebian/Scrivania/Hirundo/projects/'+name+'/BEST_DATA.json', 'r') as mainf:
    old_data = json.load(mainf)
    data = old_data.update(best_pic_features)
with open('/home/rootdebian/Scrivania/Hirundo/projects/'+name+'/BEST_DATA.json', 'w') as mainf:
    json.dump(old_data, mainf)
    mainf.close()
