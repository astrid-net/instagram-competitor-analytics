import os
from datetime import datetime
from datetime import date
import json
import numpy as np
import emoji
import spacy
import requests
import pickle
import matplotlib
from instaloader import Instaloader
from instaloader import Post
from sklearn.cluster import KMeans
from collections import Counter
import heapq
import demoji
import emoji
from dateutil.relativedelta import relativedelta
import advertools as adv
from ttp import ttp
import preprocessor
import re
import pandas as pd
from time import sleep

L = Instaloader()


en = spacy.load('en_core_web_sm')
it = spacy.load('it_core_news_sm')
es = spacy.load('es_core_news_sm')
de = spacy.load('de_core_news_sm')
fr = spacy.load('fr_core_news_sm')
languages = [en, it, es, de, fr]
stop_words = []
p = ttp.Parser()


for l in languages:
    for sw in l.Defaults.stop_words:
        stop_words.append(sw)


def like_growth(like_m, like_all):
    X_st = []
    Y_st = []

    X_lt = []
    Y_lt = []

    like_st = np.asarray(like_m)
    like_lt = np.asarray(like_all)

    #Short Term
    n_st = 0
    while True:
        n_st = n_st+1
        if len(like_st)/n_st > 100:
            pass
        else:
            break

    while True:
        if len(like_st)%n_st == 0:
            break
        else:
            like_st = like_st[:-1]
    like_st = like_st.reshape(int(len(like_st)/n_st), n_st)
    for l in reversed(like_st):
        Y_st.append(np.mean(l))
    X_st = [n for n in range(len(Y_st))]

    #Long Term
    n_lt = 0
    while True:
        n_lt = n_lt+1
        if len(like_lt)/n_lt > 100:
            pass
        else:
            break

    while True:
        if len(like_lt)%n_lt == 0:
            break
        else:
            like_lt = like_lt[:-1]
    like_lt = like_lt.reshape(int(len(like_lt)/n_lt), n_lt)
    for l in reversed(like_lt):
        Y_lt.append(np.mean(l))
    X_lt = [n for n in range(len(Y_lt))]

    like_graph_st = [X_st, Y_st]
    like_graph_lt = [X_lt, Y_lt]

    return [like_graph_st, like_graph_lt]


def comment_growth(comment_m, comment_all):
    X_st = []
    Y_st = []

    X_lt = []
    Y_lt = []

    comment_st = np.asarray(comment_m)
    comment_lt = np.asarray(comment_all)

    #Short Term
    n_st = 0
    while True:
        n_st = n_st+1
        if len(comment_st)/n_st > 100:
            pass
        else:
            break

    while True:
        if len(comment_st)%n_st == 0:
            break
        else:
            comment_st = comment_st[:-1]
    comment_st = comment_st.reshape(int(len(comment_st)/n_st), n_st)
    for l in reversed(comment_st):
        Y_st.append(np.mean(l))
    X_st = [n for n in range(len(Y_st))]

    #Long Term
    n_lt = 0
    while True:
        n_lt = n_lt+1
        if len(comment_lt)/n_lt > 100:
            pass
        else:
            break

    while True:
        if len(comment_lt)%n_lt == 0:
            break
        else:
            comment_lt = comment_lt[:-1]
    comment_lt = comment_lt.reshape(int(len(comment_lt)/n_lt), n_lt)
    for l in reversed(comment_lt):
        Y_lt.append(np.mean(l))
    X_lt = [n for n in range(len(Y_lt))]

    comment_graph_st = [X_st, Y_st]
    comment_graph_lt = [X_lt, Y_lt]

    return [comment_graph_st, comment_graph_lt]


def caption_analysis(captions):
    #caption lenght
    cap_len = []
    for cap in captions:
        if cap != None:
            cap_len.append(len(cap))
        if cap == None:
            cap_len.append(0)
    cap_len = np.round(np.mean(cap_len), 3)

    
    hashtags = []

    #hashtags
    hashtag = []
    hashtag_most = {}
    captions = list(captions)
    for cap in captions:
        if cap != None:
            for h in p.parse(cap).tags:
                hashtag.append(h)
        if cap == None:
            captions[captions.index(cap)] = ''
    hashtag_freq = np.round(len(hashtag)/len(captions), 3)
    for el, cnt in zip(Counter(hashtag).most_common(), range(3)):
        hashtag_most.update({el[0]: np.round(el[1]/len(hashtag), 3)})

    #emojis
    emoji_count = 0
    emoji_most = {}
    emoji_family_most = {}
    emoji_extract = adv.extract_emoji(captions)
    for n in emoji_extract['emoji_counts']:
        emoji_count = emoji_count + n
    emoji_freq = np.round(emoji_count/len(captions), 3)

    i = 0
    j = 0
    for k,v in emoji_extract['top_emoji_text']:
        if i >2:
            break
        i = i+1
        emoji_most.update({k: np.round(v/emoji_count, 3)})
        
    for k,v in emoji_extract['top_emoji_groups']:
        if j >2:
            break
        j = j+1
        emoji_family_most.update({k: np.round(v/emoji_count, 3)})

    #word
    text_clean = []
    for cap in captions:
        cap = cap.replace('è','e').replace('à', 'a').replace('ò', 'o').replace('é', 'e')
        text_clean.append(re.sub(r'\b\w{1,3}\b', '', preprocessor.clean(cap).replace('/', '').replace('_', '').replace('$', '').replace('%', '').replace('&', '').replace('(', '').replace(')', '').replace('[', '').replace(']', '').replace(',', '').replace('.', '').replace(';', '').replace(':','').replace('!','').replace('?','').replace('-','').replace('"', '').replace("'", "").replace('\n', '').replace('—', '').replace('-', '')))
    words_most = adv.word_frequency(text_clean, rm_words = stop_words, extra_info = True).iloc[[0,1,2], [0, 1, 4, 5]].to_json()

    return [emoji_freq, emoji_most, emoji_family_most, hashtag_freq, hashtag_most, cap_len, words_most]

def comment_analysis(comments):
    #emojis
    emoji_count = 0
    emoji_most = {}
    emoji_family_most = {}
    emoji_extract = adv.extract_emoji(comments)
    for n in emoji_extract['emoji_counts']:
        emoji_count = emoji_count + n
    emoji_freq = np.round(emoji_count/len(captions), 3)

    i = 0
    j = 0
    for k,v in emoji_extract['top_emoji_text']:
        if i >2:
            break
        i = i+1
        emoji_most.update({k: np.round(v/emoji_count, 3)})
        
    for k,v in emoji_extract['top_emoji_groups']:
        if j >2:
            break
        j = j+1
        emoji_family_most.update({k: np.round(v/emoji_count, 3)})

    #word
    text_clean = []
    for cap in comments:
        cap = cap.replace('è','e').replace('à', 'a').replace('ò', 'o').replace('é', 'e')
        text_clean.append(re.sub(r'\b\w{1,3}\b', '', preprocessor.clean(cap).replace('/', '').replace('_', '').replace('$', '').replace('%', '').replace('&', '').replace('(', '').replace(')', '').replace('[', '').replace(']', '').replace(',', '').replace('.', '').replace(';', '').replace(':','').replace('!','').replace('?','').replace('-','').replace('"', '').replace("'", "").replace('\n', '').replace('—', '').replace('-', '')))
    words_most = adv.word_frequency(text_clean, rm_words = stop_words, extra_info = True).iloc[[0,1,2], [0, 1, 4, 5]].to_json()

    return [emoji_freq, emoji_most, emoji_family_most, words_most]



def timefunct(time):
    model = KMeans(n_clusters = 3, random_state=0, max_iter=300, n_init=1 )
    hour = np.array([])
    
    y2020 = 0
    y2019 = 0
    y2018 = 0
    y2017 = 0
    y2016 = 0
    y2015 = 0
    y2014 = 0
    y2013 = 0
    y2012 = 0
    y2011 = 0
    
    jen = 0
    fe = 0
    mar = 0
    apr = 0
    may = 0
    jun = 0
    jul = 0
    ag = 0
    sep = 0
    oc = 0
    nov = 0
    dec = 0
    
    for d in time:
        date = datetime.strptime(d, '%Y-%m-%d %H:%M:%S')
        if date.year == 2020:
            y2020 += 1
        if date.year == 2019:
            y2019 += 1
        if date.year == 2018:
            y2018 += 1
        if date.year == 2017:
            y2017 += 1
        if date.year == 2016:
            y2016 += 1
        if date.year == 2015:
            y2015 += 1
        if date.year == 2014:
            y2014 += 1
        if date.year == 2013:
            y2013 += 1
        if date.year == 2012:
            y2012 += 1
        if date.year == 2011:
            y2011 += 1

        if date.month == 1:
            jen += 1
        if date.month == 2:
            fe += 1
        if date.month == 3:
            mar += 1
        if date.month == 4:
            apr += 1
        if date.month == 5:
            may += 1
        if date.month == 6:
            jun += 1
        if date.month == 7:
            jul += 1
        if date.month == 8:
            ag += 1
        if date.month == 9:
            sep += 1
        if date.month == 10:
            oc += 1
        if date.month == 11:
            nov += 1
        if date.month == 12:
            dec += 1

        hour = np.append(hour, date.hour)

    year_graph = [['2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'], [y2011, y2012, y2013, y2014, y2015, y2016, y2017, y2018, y2019, y2020]]
    month_graph = [['j', 'f', 'm', 'a', 'm', 'j', 'j', 'a', 's', 'o', 'n', 'd'], [jen, fe, mar, apr, may, jun, jul, ag, sep, oc, nov, dec]]

    model.fit_predict(hour.reshape(-1, 1))
    hours = model.cluster_centers_
    h = [float(t) for t in hours]
    
    times = [year_graph, month_graph, h]

    return times

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



name = input('inserisci il nome: ')
path = '/home/rootdebian/Scrivania/Hirundo/projects/'+name+'/competitor-data/'
now = datetime.now()
st = now-relativedelta(months=+3)

type_post_gen = []
caption_gen = []
time_gen = []
count_best = 0

for competitor in os.listdir(path):
    print(competitor)
    print('==============================')
    like_m = []
    like_all = []
    comment_m = []
    comment_all = []
    captions = np.array([])
    comments = np.array([])
    time = np.array([])
    n_comments = 0

    n = len(os.listdir(path+competitor)) - 1


    for f in range(n):
        try:
            with open(path+competitor+'/'+str(f)+'.json') as js:
                data = json.load(js)
                postdate = datetime.strptime(data['date'], '%Y-%m-%d %H:%M:%S')
                if now > postdate > st:
                    like_m.append(data['likes'])
                    comment_m.append(data['comments'])
                like_all.append(data['likes'])
                comment_all.append(data['comments'])
                time = np.append(time, data['date'])
                captions = np.append(captions, data['caption'])
                if n_comments>50000:
                    continue
                for c in data['comments_text']:
                    if len(c)>0:
                        comments = np.append(comments, c)
                        n_comments = n_comments+len(c)
        except Exception as e:
            continue

    n_st = [i for i in range(len(like_m))]
    n_lt = [i for i in range(len(like_all))]
    like_graphs = [[n_st, like_m[::-1]], [n_lt, like_all[::-1]]]
    comment_graphs = [[n_st, comment_m[::-1]], [n_lt, comment_all[::-1]]]

    
    times = timefunct(time)
    best_url = []
    best_c = []

    caption_an = caption_analysis(captions)
    comments_an = comment_analysis(comments)
    
    general_data = {
        'like_growth': like_graphs,
        'comment_growth': comment_graphs,
        'caption_analysis': caption_an,
        'comment_analysis': comments_an,
        'timing': times,
        'last_modify': str(date.today())
        }
    
    with open(path+competitor+'/DATA.json', 'w') as f:
            json.dump(general_data, f)
            f.close()

    print('done')

    best = select_best(like_all, comment_all)
    count_best += len(best[0])
    print(count_best)
    for b in best[0]:
        try:
            with open(path+competitor+'/'+str(b)+'.json') as js:
                data = json.load(js)
                type_post_gen.append(data['type'])
                caption_gen.append(data['caption'])
                time_gen.append(data['date'])
        except Exception as e:
            print(e)
print('ok')
type_post = Counter(type_post_gen)
    
caption = caption_gen
caption_an = caption_analysis(caption)

time = time_gen
time = timefunct(time)
month_graph_gen = time[1]
hours_gen = time[2]

best_data = {
    'caption_analysis': caption_an,
    'type_post': type_post,
    'month_graph': month_graph_gen,
    'hours': hours_gen
    }

with open('/home/rootdebian/Scrivania/Hirundo/projects/'+name+'/BEST_DATA.json', 'w') as j:
    json.dump(best_data, j)
    j.close()
            
