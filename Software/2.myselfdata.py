import os
from datetime import date
import json
from random import random
import numpy as np
from instaloader import Instaloader
from instaloader import Profile
from sklearn.cluster import KMeans
from datetime import datetime
import emoji, demoji, spacy
from collections import Counter
import numpy as np

L = Instaloader()
en = spacy.load('en_core_web_sm')
it = spacy.load('it_core_news_sm')
es = spacy.load('es_core_news_sm')
de = spacy.load('de_core_news_sm')
fr = spacy.load('fr_core_news_sm')
languages = [en, it, es, de, fr]
stop_words = []


for l in languages:
    for sw in l.Defaults.stop_words:
        stop_words.append(sw)


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


def get_data(data, colors_gen, bright_mean_gen, bright_var_gen, satur_mean_gen, satur_var_gen):
    url = Profile.from_username(L.context, usm).get_profile_pic_url()

    #COLORS
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

    return colors_gen, bright_mean_gen, bright_var_gen, satur_mean_gen, satur_var_gen

def myself(name_main, colors_gen, bright_mean_gen, bright_var_gen, satur_mean_gen, satur_var_gen, h_gen,month_graph_gen):
    os.mkdir('/home/rootdebian/Scrivania/Hirundo/projects/'+name_main+'/works/data-cd/')
    page = open('/home/rootdebian/Scrivania/Hirundo/projects/'+name_main+'/works/data-cd/myself.html', 'w')


    #TYPE POST
    pic_score = str(Counter(type_post_gen)['GraphImage'])
    sidecar_score = str(Counter(type_post_gen)['GraphSidecar'])
    video_score = str(Counter(type_post_gen)['GraphVideo'])

    #COLORS
    r = str(np.round(np.mean(colors_gen[0]), 3))
    br = str(np.round(np.mean(colors_gen[1]), 3))
    o = str(np.round(np.mean(colors_gen[2]), 3))
    y = str(np.round(np.mean(colors_gen[3]), 3))
    g = str(np.round(np.mean(colors_gen[4]), 3))
    b = str(np.round(np.mean(colors_gen[5]), 3))
    v = str(np.round(np.mean(colors_gen[6]), 3))
    f = str(np.round(np.mean(colors_gen[7]), 3))
    pi = str(np.round(np.mean(colors_gen[8]), 3))
    wh = str(np.round(np.mean(colors_gen[9]), 3))
    bl = str(np.round(np.mean(colors_gen[10]), 3))

    cc = str(np.round(np.mean(colors_gen[11]), 3))
    wc = str(np.round(np.mean(colors_gen[12]), 3))

    
    #BRIGHTNESS
    bright_mean = str(np.round(np.mean(bright_mean_gen), 3))
    bright_var = str(np.round(np.mean(bright_var_gen), 3))

    #SATURATION
    satur_mean = str(np.round(np.mean(satur_mean_gen), 3))
    satur_var = str(np.round(np.mean(satur_var_gen), 3))


    #TIMING
    X_month = str(month_graph_gen[0])
    Y_month = str(month_graph_gen[1])

    h1 = str(np.round(h_gen[0], 0)).replace('[', '').replace(']', '').replace('.', '')
    h2 = str(np.round(h_gen[1], 0))
    h3 = str(np.round(h_gen[2], 0))

    css = """<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Migliori Features</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Muli:wght@900&display=swap" rel="stylesheet">
    <link href='https://fonts.googleapis.com/css?family=Raleway' rel='stylesheet'>
  </head>
  <style media="screen">
  .text{
    font-family: 'Raleway';
    font-weight: 200;
    text-align: left;
  }
  #title{
    font-size: 70px;
    letter-spacing: 1px;
    text-align: center;
  }
  #subtitle{
    font-size: 50px;
  }
  #paragraph{
    font-size: 30px;
    font-weight: 300;
  }
  .container{
    position: absolute;
    width: 800px;
    padding-bottom: 30px;
    top: 100px;
    left: 50%;
    margin-left: -420px;
    display: inline-block;
  }

  .panel{
    position: relative;
    padding-bottom: 10px;
    width: 100%;
  }
  #bar-colors{
    padding-top: 80px;
    padding-bottom: 40px;
  }
  .bar{
    position: relative;
    height: 100%;
    display: inline-block;
    text-align: center;
    font-size: 20px;
    font-family: 'Raleway';
    font-weight: 300;
  }
  #warm{
    width: """+wc+"""%;
    background-color: #e85656;
    color: #e85656;
  }
  #cold{
    width: """+cc+"""%;
    background-color: #6eb2d4;
    color: #6eb2d4;
    left: -5px;
  }
  .cold-warm{
    width: 100%;
    height: 10px;
    background-color: #e8e8e8;
  }
  .evidence{
    margin-top: 10px;
    font-family: 'Muli';
    font-size: 30px;
    color: 	#1685cc;
  }
  #hours{
    text-align: center;
  }
  @media screen and (max-width: 800px){
    #title{
      font-size: 60px;
      text-align: left;
    }
    #subtitle{
      font-size: 40px;
    }
    #paragraph{
      font-size: 20px;
    }
    .container{
      width: 98%;
      margin-left: 0;
      left: 1%;
    }
    .panel{
      width: 100%;
    }
  }
"""
    html="""</style>
  <body>
    <div class='container'>
      <h1 class='text' id='title'>Migliori Features</h1>
      <h2 class='text' id='subtitle'>Tipologia Post Più Usate</h2>

        <canvas id='type-post' width='100%' height='70px'></canvas>

      <h2 class='text' id='subtitle'>Post-Colori Più Utilizzati</h2>
      <div class='panel'>
        <canvas id='colors' width='100%' height='70px'></canvas>
      </div>
      <div class='panel' id='bar-colors'>
        <div class='cold-warm'>
          <div class='bar' id='warm'><span style='position: relative; top: -30px;'>caldi</span></div>
          <div class='bar' id='cold'><span style='position: relative; top: -30px;'>freddi</span></div>
        </div>
      </div>

      <h2 class='text' id='subtitle'>Post-Statistiche Foto</h2>
      <div class='panel'>
        <p class='text' id='paragraph'>Brillantezza: <span class='evidence'>"""+bright_mean+"""</span> <span style='float: right;'>Varianza Brillantezza: <span class='evidence'>"""+bright_var+"""</span></span></p>
        <p class='text' id='paragraph'>Saturazione: <span class='evidence'>"""+satur_mean+"""</span> <span style='float: right;'>Varianza Saturazione: <span class='evidence'>"""+satur_var+"""</span></span></p>
      </div>


      <h2 class='text' id='subtitle'>Statistiche sul Tempo</h2>

      <div class='panel'>
        <canvas id='months' width='100%' height='50px'></canvas>
      </div>

      <div class='panel'>
        <p class='text' id='subtitle'>Orari di Pubblicazione più frequenti:
          <p class='evidence' id='hours' style='float: 'center'; font-size:45px'>"""+h1+"""&nbsp;&nbsp;&nbsp;"""+h2+"""&nbsp;&nbsp;&nbsp;"""+h3+"""</p>
        </p>
      </div>
    </div>

  </body>"""

    js = """
  <script type='text/javascript'>
  new Chart(document.getElementById('type-post'), {
  type: 'doughnut',
  data: {
    labels: ['Foto', 'Video', 'Sidecar'],
    datasets: [{
      label: 'Population (millions)',
      backgroundColor: ['rgb(15, 92, 140)', 'rgb(22, 133, 204)', 'rgb(15, 92, 140)'],
      data: ["""+pic_score+""", """+video_score+""", """+sidecar_score+"""]
    }]
  },
});
  </script>
  <script type='text/javascript'>
  new Chart(document.getElementById('colors'), {
  type: 'doughnut',
  data: {
    labels: ['Rosso', 'Marrone', 'Arancione', 'Giallo', 'Verde', 'Blu', 'Viola', 'Fucsia', 'Rosa', 'Bianco', 'Nero'],
    datasets: [{
      label: 'Colori più presenti',
      backgroundColor: ['rgb(232, 86, 86)', 'rgb(181, 126, 67)', 'rgb(232, 147, 86)', 'rgb(232, 203, 86)', 'rgb(88, 191, 112)', 'rgb(88, 153, 191)', 'rgb(126, 104, 173)', 'rgb(199, 122, 204)', 'rgb(227, 181, 230)', 'rgb(240, 240, 240)', 'rgb(26, 26, 26)'],
      data: ["""+r+""", """+ br+""", """+ o+""", """+ y+""", """+ g+""", """+ b+""", """+ v+""", """+ f+""", """+ pi+""", """+ wh+""", """+ bl+"""]
    }]
  },
});
  </script>



<script>
new Chart(document.getElementById('months'), {
    type: 'bar',
    data: {
      labels: """+X_month+""",
      datasets: [
        {
          label: 'Post per Mese',
          backgroundColor: ['rgb(22, 133, 204)', 'rgb(22, 133, 204)', 'rgb(22, 133, 204)', 'rgb(22, 133, 204)', 'rgb(22, 133, 204)', 'rgb(22, 133, 204)', 'rgb(22, 133, 204)', 'rgb(22, 133, 204)', 'rgb(22, 133, 204)', 'rgb(22, 133, 204)', 'rgb(22, 133, 204)', 'rgb(22, 133, 204)'],
          data: """+Y_month+"""
        }
      ]
    },
    options: {
      legend: { display: false },
      title: {
        display: true,
        text: 'Post Pubblicati per Mese'
      }
    }
});
</script>
</html>"""
    page.write(css)
    page.write(html)
    page.write(js)
    page.close()

    return None
    


type_post_gen = []
colors_gen = [[], [], [], [], [], [], [], [], [], [], [], [], []]
caption_gen = []
bright_mean_gen = []
bright_var_gen = []
satur_mean_gen = []
satur_var_gen = []
hour_gen = []
model = KMeans(n_clusters = 3, random_state=0, max_iter=300, n_init=1 )
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

name_main = input('Inserisci il nome utente: ')
usm = input('Inserisci il nick di instagram: ')
path = '/home/rootdebian/Scrivania/Hirundo/projects/'+name_main+'/competitor-data/'

for competitor in os.listdir(path):
    for f in os.listdir(path+competitor):
        if 'DATA' in f:
            with open(path+competitor+'/'+f) as js:
                print(competitor)
                data = json.load(js)
                get_data(data, colors_gen, bright_mean_gen, bright_var_gen, satur_mean_gen, satur_var_gen)

for competitor in os.listdir(path):
    like_all = []
    comment_all = []

    for i in range(len(os.listdir(path+competitor))):
        try:
            with open(path+competitor+'/'+str(i+1)+'.json') as js:
                data = json.load(js)

                like_all.append(data['likes'])
                comment_all.append(data['comments'])
        except:
            continue
        
    bests = select_best(like_all, comment_all)
    for b in bests[0]:
        pathf = path+competitor+'/'+str(b)+'.json'
        with open(pathf) as js:
            data = json.load(js)
            date = datetime.strptime(data['date'], '%Y-%m-%d %H:%M:%S')
            type_post_gen.append(data['type'])
                
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

            hour_gen.append(date.hour)
            caption_gen.append(data['caption'])

month_graph_gen = [['j', 'f', 'm', 'a', 'm', 'j', 'j', 'a', 's', 'o', 'n', 'd'], [jen, fe, mar, apr, may, jun, jul, ag, sep, oc, nov, dec]]
model.fit_predict(np.asarray(hour_gen).reshape(-1, 1))
h_gen = np.round(model.cluster_centers_, 0)
myself(name_main, colors_gen, bright_mean_gen, bright_var_gen, satur_mean_gen, satur_var_gen, h_gen,month_graph_gen)
