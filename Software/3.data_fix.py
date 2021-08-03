import os
from datetime import date
import json
from random import random
import numpy as np
from instaloader import Instaloader
from instaloader import Profile
import ast
from time import sleep
import emoji

L = Instaloader()

def create_main(a):
    css = """<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Main</title>
    <link href="https://fonts.googleapis.com/css2?family=Raleway&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://fonts.googleapis.com/css2?family=Muli:wght@900&display=swap" rel="stylesheet">
    </head>
  <style media="screen">
    .container{
      position: absolute;
      top: 120px;
      left: 50px;
      right: 50px;
      bottom: 0px;
      display: inline-block;
      overflow-y: auto;
      overflow-x: hidden;
    }
    .option{
      position: relative;
      width: 90%;
      border-bottom: 1px solid lightgray;
      padding-left: 20px;
      padding-right: 20px;
      padding-top: 30px;
      padding-bottom: 20px;
      font-family: 'Raleway';
      font-weight: 200;
      font-size: 35px;
      display: inline-block;
    }
    .score{
      float: right;
      margin-top: 10px;
      font-family: 'Muli';
      font-size: 20px;
    }
    #up{
      color:#00aede;
    }
    #down{
      color: #ba0404;
    }
    a{
      color: #093652;
      text-decoration:none;
    }
  </style>
  <body>
    <div class="header">
    </div>
    <div class="container">
      <a href="myself.html"><div class="option" id="self">My Self</div></a>\n"""
    main.write(css)
    
    for b in reversed(a):
        if b[1]>0 or b[1] == 0:
            main.write('    <a href="'+str(b[0])+'.html"><div class="option">'+str(b[0])+"<span class='score' id=up>"+str(b[1])+'</span></div></a>\n')
        if b[1]<0:
            main.write('    <a href="'+str(b[0])+'.html"><div class="option">'+str(b[0])+"<span class='score' id=down>"+str(b[1])+'</span></div></a>\n')
    end = """    </div>
\
  </body>
\
</html>"""
    main.write(end)
    main.close()

    return None


def myself(usm, data):    
    mainp = open('/home/rootdebian/Scrivania/Hirundo/projects/'+name_main+'/works/'+str(date.today())+'-cd/myself.html', 'w')
    url = Profile.from_username(L.context, usm).get_profile_pic_url()
    
    #TYPE POST
    try:
        pic_score = str(data['type_post']['GraphImage'])
    except:
        pic_score = '0'

    try:
        sidecar_score = str(data['type_post']['GraphSidecar'])
    except:
        sidecar_score = '0'

    try:
        video_score = str(data['type_post']['GraphVideo'])
    except:
        video_score = '0'


    #COLORS
    r = str(np.round(data['colors'][0], 3))
    br = str(np.round(data['colors'][1], 3))
    o = str(np.round(data['colors'][2], 3))
    y = str(np.round(data['colors'][3], 3))
    g = str(np.round(data['colors'][4], 3))
    b = str(np.round(data['colors'][5], 3))
    v = str(np.round(data['colors'][6], 3))
    f = str(np.round(data['colors'][7], 3))
    pi = str(np.round(data['colors'][8], 3))
    wh = str(np.round(data['colors'][9], 3))
    bl = str(np.round(data['colors'][10], 3))

    cc = str(np.round(data['colors'][11], 3))
    wc = str(np.round(data['colors'][12], 3))
    
    #BRIGHTNESS
    bright_mean = str(np.round(data['bright_mean'], 3))
    bright_var = str(np.round(data['bright_var'], 3))
    

    #SATURATION
    satur_mean = str(np.round(data['satur_mean'], 3))
    satur_var = str(np.round(data['satur_var'], 3))

    #CAPTION=========ANALYSIS

    #EMOJIS--CAPTION
    emoji_cap_freq = str(np.round(data['caption_analysis'][0], 2))
    for k, i in zip(data['caption_analysis'][1].items(), range(len(data['caption_analysis'][1]))):
        if i == 0:
            try:
                emoji_cap_1 = 'String.fromCodePoint(0x'+str('{:X}'.format(ord(emoji.emojize(':'+str(k[0]).replace(' ', '_')+':'))))+')'
            except Exception as e:
                emoji_cap_1 = "'"+k[0]+"'"
            emoji_f_cap_1 = str(np.round(k[1], 3))
            
        if i == 1:
            try:
                emoji_cap_2 = 'String.fromCodePoint(0x'+str('{:X}'.format(ord(emoji.emojize(':'+str(k[0]).replace(' ', '_')+':'))))+')'
            except:
                emoji_cap_2 = "'"+k[0]+"'"
            emoji_f_cap_2 = str(np.round(k[1], 3))
            
        if i == 2:
            try:
                emoji_cap_3 = 'String.fromCodePoint(0x'+str('{:X}'.format(ord(emoji.emojize(':'+str(k[0]).replace(' ', '_')+':'))))+')'
            except:
                emoji_cap_3 = "'"+k[0]+"'"
            emoji_f_cap_3 = str(np.round(k[1], 3))
            

    #EMOJIS--FAMILY--CAPTION
    for k, i in zip(data['caption_analysis'][2].items(), range(len(data['caption_analysis'][2]))):
        if i == 0:
            emoji_fam_cap_1 = str(k[0])
            emoji_fam_f_cap_1 = str(np.round(k[1], 3))
        if i == 1:
            emoji_fam_cap_2 = str(k[0])
            emoji_fam_f_cap_2 = str(np.round(k[1], 3))       
        if i == 2:
            emoji_fam_cap_3 = str(k[0])
            emoji_fam_f_cap_3 = str(np.round(k[1], 3))
            
    #HASHTAG
    hashtag_freq = str(np.round(data['caption_analysis'][3], 2))
    for k, i in zip(data['caption_analysis'][4].items(), range(len(data['caption_analysis'][4]))):
        if i == 0:
            hashtag_1 = str(k[0])
            hashtag_f_1 = str(np.round(k[1], 3))
        if i == 1:
            hashtag_2 = str(k[0])
            hashtag_f_2 = str(np.round(k[1], 3))      
        if i == 2:
            hashtag_3 = str(k[0])
            hashtag_f_3 = str(np.round(k[1], 3))

    #WORDS
    cap_len = str(np.round(data['caption_analysis'][5], 2))
    
    word_dict= eval(data['caption_analysis'][6])
    w1 = word_dict['word']['0']
    w1_abs_freq = str(word_dict['abs_freq']['0'])
    w1_wtd_freq = str(word_dict['wtd_freq_perc']['0'])
    w1_wtd_freq_cum = str(word_dict['wtd_freq_perc_cum']['0'])

    w2 = word_dict['word']['1']
    w2_abs_freq = str(word_dict['abs_freq']['1'])
    w2_wtd_freq = str(word_dict['wtd_freq_perc']['1'])
    w2_wtd_freq_cum = str(word_dict['wtd_freq_perc_cum']['1'])

    w3 = word_dict['word']['2']
    w3_abs_freq = str(word_dict['abs_freq']['2'])
    w3_wtd_freq = str(word_dict['wtd_freq_perc']['2'])
    w3_wtd_freq_cum = str(word_dict['wtd_freq_perc_cum']['2'])


    #TIMING

    X_month = str(data['month_graph'][0])
    Y_month = str(data['month_graph'][1])

    h1 = str(np.round(data['hours'][0], 0))
    h2 = str(np.round(data['hours'][1], 0))
    h3 = str(np.round(data['hours'][2], 0))


    css = """<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>"""+name_main+"""</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Muli:wght@900&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Raleway&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
  </head>
  <style media="screen">
  .text{
    font-family: 'Raleway', sans-serif;
    font-weight: 200;
    text-align: left;
    color: #093652;
  }
  #title{
    font-size: 60px;
    font-weight: 800;
    text-align: left;
    letter-spacing: 1px;
    line-height: 100px;
  }
  #subtitle{
    font-size: 37px;
    font-weight: 900;
    letter-spacing: 1px;
  }
  #paragraph{
    padding-top: 10px;
    font-size: 23px;
    font-weight: 400;
  }
  .main-pic{
    position: relative;
    width: 180px;
    height: 180px;
    left: 50%;
    margin-left: -90px;
    border-radius: 300px;
    background-color: red;
    background-image: url("""+url+""");
    background-size: cover;
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
    padding-bottom: 20px;
    width: 100%;
  }

  .evidence{
    margin-top: 50px;
    font-family: 'Muli', sans-serif;
    font-weight: 100;
    font-size: 20px;
    color: 	#1685cc;
  }
  #hours{
    text-align: center;
  }
  table.blueTable {
    width: 100%;
    text-align: left;

  }
  table.blueTable td, table.blueTable th {
    padding: 10px 10px;
  }
  table.blueTable tbody td {
    font-size: 18px;
    font-family: 'Raleway', sans-serif;
    padding: 20px;
  }
  table.blueTable thead {
    background: #0f5c8c;
  }
  table.blueTable thead th {
    font-size: 20px;
    font-family: 'Raleway', sans-serif;
    font-weight: bold;
    color: #FFFFFF;
    padding: 20px;
  }

  @media screen and (max-width: 800px){
    #title{
      font-size: 60px;
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
    html="""  </style>
  <body>
    <div class="container">
      <h1 class="text" id="title">"""+usm+"""</h1>
      <div class="main-pic"></div>

      <h2 class="text" id="title">Statistiche Post</h2>
      <h2 class="text" id='subtitle'>Tipologie Più Usate</h2>
      <div class="panel">
        <canvas id="type-post" width="100%" height="70px"></canvas>
      </div>

      <h2 class="text" id='subtitle'>Colori Più Utilizzati</h2>
      <div class="panel">
        <canvas id="colors" width="100%" height="70px"></canvas>
      </div>
      
      <div class="panel" id="bar-colors">
        <table class="blueTable">
          <thead>
            <tr>
            <th>Tipologia Colore</th>
            <th>Presenza</th>
            </tr>
          </thead>
          <tbody>
            <tr>
            <td>Caldi</td><td>"""+wc+"""%</td></tr>
            <tr>
            <td>Freddi</td><td>"""+cc+"""%</td></tr>
            <tr>
            <td>Neutri+</td><td>"""+str(100-float(cc)-float(wc))+"""%</td></tr>
            <tr>
          </tbody>
        </table>
      </div>

      <h2 class="text" id='subtitle'>Features</h2>
      <div class="panel">
        <p class="text" id="paragraph">Brillantezza: <span class="evidence">"""+bright_mean+"""</span> <span style="float: right;">Varianza Brillantezza: <span class="evidence">"""+bright_var+"""</span></span></p>
        <p class="text" id="paragraph">Saturazione: <span class="evidence">"""+satur_mean+"""</span> <span style="float: right;">Varianza Saturazione: <span class="evidence">"""+satur_var+"""</span></span></p>
      </div>

      <h2 class="text" id='title'>Analisi Caption<br></h2>
      <h2 class="text" id='subtitle'>Parole Più Utilizzate</h2>
      <p class="text" id="paragraph">Lunghezza Media Caption: <span class="evidence">"""+cap_len+"""</span></p>
      <div class="panel">
        <table class="blueTable">
          <thead>
            <tr>
            <th>Parola</th>
            <th>Numero</th>
            <th>Freq Pes</th>
            <th>Freq Pes Cum</th>
            </tr>
          </thead>
          <tbody>
            <tr>
            <td>"""+w1+"""</td><td>"""+w1_abs_freq+"""</td><td>"""+w1_wtd_freq+"""</td><td>"""+w1_wtd_freq_cum+"""</td></tr>
            <tr>
            <td>"""+w2+"""</td><td>"""+w2_abs_freq+"""</td><td>"""+w2_wtd_freq+"""</td><td>"""+w2_wtd_freq_cum+"""</td></tr>
            <tr>
            <td>"""+w3+"""</td><td>"""+w3_abs_freq+"""</td><td>"""+w3_wtd_freq+"""</td><td>"""+w3_wtd_freq_cum+"""</td></tr>
            </tr>
          </tbody>
        </table>
      </div>

      <h2 class="text" id='subtitle'>Analisi Emoji</h2>
      <p class="text" id="paragraph">Frequenza Emoji: <span class="evidence">"""+emoji_cap_freq+"""</span></p>
      <div class="panel">
        <canvas id="emoji-most" width="100%" height="40px"></canvas>
      </div>

      <div class="panel">
        <canvas id="emoji-family-most" width="100%" height="40px"></canvas>
      </div>

      <h2 class="text" id='subtitle'>Analisi Hashtag</h2>
      <p class="text" id="paragraph">Frequenza Hashtag: <span class="evidence">"""+hashtag_freq+"""</span></p>
      <div class="panel">
        <canvas id="hashtag-most" width="100%" height="40px"></canvas>
      </div>



      <h2 class="text" id='title'>Statistiche sul Tempo</h2>

      <h2 class="text" id='subtitle'>Post per Mese</h2>
      <div class="panel">
        <canvas id="months" width="100%" height="50px"></canvas>
      </div>

      <div class="panel">
        <p class="text" id="subtitle">Orari Pubblicazioni più frequenti:
          <p class="evidence" id="hours" style="float: 'center'; font-size:45px">"""+h1+"""&nbsp;&nbsp;&nbsp;"""+h2+"""&nbsp;&nbsp;&nbsp;"""+h3+"""</p>
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
      backgroundColor: ['rgb(15, 92, 140)', 'rgb(22, 133, 204)', 'rgb(17, 111, 171)'],
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
  new Chart(document.getElementById('emoji-most'), {
    type: 'horizontalBar',
    data: {
      labels: ["""+emoji_cap_1+""", """+emoji_cap_2+""", """+emoji_cap_3+"""],
      datasets: [
        {
          backgroundColor: ['rgb(15, 92, 140)', 'rgb(22, 133, 204)', 'rgb(15, 92, 140)'],
          data: ["""+emoji_f_cap_1+""", """+emoji_f_cap_2+""", """+emoji_f_cap_3+"""]
        }
      ]
    },
    options: {
        legend: { display: false },
        scales: {
            yAxes: [{
                ticks: {
                    fontSize: 30
                }
            }]
        }
    }
  });
  </script>

  <script>
  new Chart(document.getElementById('emoji-fam-most'), {
    type: 'horizontalBar',
    data: {
      labels: ['"""+emoji_fam_cap_1+"""', '"""+emoji_fam_cap_2+"""', '"""+emoji_fam_cap_3+"""'],
      datasets: [
        {
          backgroundColor: ['rgb(15, 92, 140)', 'rgb(22, 133, 204)', 'rgb(15, 92, 140)'],
          data: ["""+emoji_fam_f_cap_1+""", """+emoji_fam_f_cap_2+""", """+emoji_fam_f_cap_3+"""]
        }
      ]
    },
    options: {
      legend: { display: false },
    }
  });
  </script>

  <script>
  new Chart(document.getElementById('hashtag-most'), {
    type: 'horizontalBar',
    data: {
      labels: ['"""+hashtag_1+"""', '"""+hashtag_2+"""', '"""+hashtag_3+"""'],
      datasets: [
        {
          backgroundColor: ['rgb(15, 92, 140)', 'rgb(22, 133, 204)', 'rgb(15, 92, 140)'],
          data:  ["""+hashtag_f_1+""", """+hashtag_f_2+""", """+hashtag_f_3+"""]
        }
      ]
    },
    options: {
      legend: { display: false },
    }
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

    mainp.write(css)
    mainp.write(html)
    mainp.write(js)
    mainp.close()
    print('ok')
    return None


def pages(name_main, name, competitor, score_like, score_comment, data):
    page = open('/home/rootdebian/Scrivania/Hirundo/projects/'+name_main+'/works/'+str(date.today())+'-cd/'+competitor+'.html', 'w')
    url = Profile.from_username(L.context, competitor).get_profile_pic_url()

    #VARIABILI PREIMPOSTATE
    emoji_cap_1 = ''
    emoji_f_cap_1 = '0'
    emoji_cap_2 = ''
    emoji_f_cap_2 = '0'
    emoji_cap_3 = ''
    emoji_f_cap_3 = '0'
    emoji_fam_cap_1 = ''
    emoji_fam_f_cap_1 = '0'
    emoji_fam_cap_2 = ''
    emoji_fam_f_cap_2 = '0'
    emoji_fam_cap_3 = ''
    emoji_fam_f_cap_3 = '0'
    w1 = ''
    w1_abs_freq = '0'
    w1_wtd_freq = '0'
    w1_wtd_freq_cum = '0'
    w2 = ''
    w2_abs_freq = '0'
    w2_wtd_freq = '0'
    w2_wtd_freq_cum = '0'
    w3 = ''
    w3_abs_freq = '0'
    w3_wtd_freq = '0'
    w3_wtd_freq_cum = '0'
    emoji_comm_1 = ''
    emoji_f_comm_1 = '0'
    emoji_comm_2 = ''
    emoji_f_comm_2 = '0'
    emoji_comm_3 = ''
    emoji_f_comm_3 = '0'
    emoji_fam_comm_1 = ''
    emoji_fam_f_comm_1 = '0'
    emoji_fam_comm_2 = ''
    emoji_fam_f_comm_2 = '0'
    emoji_fam_comm_3 = ''
    emoji_fam_f_comm_3 = '0'
    w1_comm = ''
    w1_comm_abs_freq = '0'
    w1_comm_wtd_freq = '0'
    w1_comm_wtd_freq_cum = '0'
    w2_comm = ''
    w2_comm_abs_freq = '0'
    w2_comm_wtd_freq = '0'
    w2_comm_wtd_freq_cum = '0'
    w3_comm = ''
    w3_comm_abs_freq = '0'
    w3_comm_wtd_freq = '0'
    w3_comm_wtd_freq_cum = '0'

    #LIKE GROWTH
    like_st_score = str(np.round(score_like, 2))
    like_st_graph_X = str(data['like_growth'][0][0])
    like_st_graph_Y = str(data['like_growth'][0][1])

    like_lt_score = str(np.round(np.mean(((data['like_growth'][1][1][-1]+data['like_growth'][1][1][-2]+data['like_growth'][1][1][-3])-(data['like_growth'][1][1][1]+data['like_growth'][1][1][2]+data['like_growth'][1][1][3]))/data['like_growth'][1][1][1]+data['like_growth'][1][1][2]+data['like_growth'][1][1][3])))
    like_lt_graph_X = str(data['like_growth'][1][0])
    like_lt_graph_Y = str(data['like_growth'][1][1])

    #COMMENT GROWTH
    comment_st_score = str(np.round(score_comment, 2))
    comment_st_graph_X = str(data['comment_growth'][0][0])
    comment_st_graph_Y = str(data['comment_growth'][0][1])
    try:
        comment_lt_score = str(np.round(np.mean(((data['comment_growth'][1][1][-1]+data['comment_growth'][1][1][-2]+data['comment_growth'][1][1][-3])-(data['comment_growth'][1][1][1]+data['comment_growth'][1][1][2]+data['comment_growth'][1][1][3]))/data['comment_growth'][1][1][1]+data['comment_growth'][1][1][2]+data['comment_growth'][1][1][3])))
    except:
        comment_lt_score = '0'
        
    comment_lt_graph_X = str(data['comment_growth'][1][0])
    comment_lt_graph_Y = str(data['comment_growth'][1][1])

    #TOP 5 LIKES
    like_dict = {}
    like_b = {}
    like_def = {}

    comm_dict = {}
    comm_b = {}
    comm_def = {}

    for k, v in zip(data['like_growth'][1][0], data['like_growth'][1][1]):
        like_dict.update({k: v})

    i = 0
    for k,v in sorted(like_dict.items(), key=lambda x: x[1], reverse=True):
        like_b.update({k:v})
        i += 1
        if i == 5:
            break

    for k,v in like_b.items():
        for f in os.listdir('/home/rootdebian/Scrivania/Hirundo/projects/'+name_main+'/competitor-data/'+name+'/'):
            if 'DATA' not in f:
                with open('/home/rootdebian/Scrivania/Hirundo/projects/'+name_main+'/competitor-data/'+name+'/'+f) as fi:
                    data_s = json.load(fi)
                    if data_s['likes'] == v:
                        like_def.update({k:data_s['shortcode']})

    for k, v in zip(data['comment_growth'][1][0], data['comment_growth'][1][1]):
        comm_dict.update({k: v})

    i = 0
    for k,v in sorted(comm_dict.items(), key=lambda x: x[1], reverse=True):
        comm_b.update({k:v})
        i += 1
        if i == 5:
            break

    for k,v in comm_b.items():
        for f in os.listdir('/home/rootdebian/Scrivania/Hirundo/projects/'+name_main+'/competitor-data/'+name+'/'):
            if 'DATA' not in f:
                with open('/home/rootdebian/Scrivania/Hirundo/projects/'+name_main+'/competitor-data/'+name+'/'+f) as fi:
                    data_s = json.load(fi)
                    if data_s['comments'] == v:
                        comm_def.update({k:data_s['shortcode']})
                    
    #TYPE POST
    try:
        pic_score = str(data['type_post']['GraphImage'])
    except:
        pic_score = '0'

    try:
        sidecar_score = str(data['type_post']['GraphSidecar'])
    except:
        sidecar_score = '0'

    try:
        video_score = str(data['type_post']['GraphVideo'])
    except:
        video_score = '0'

    #COLORS
    r = str(np.round(np.mean([c[0][0] for c in data['colors']]), 3))
    br = str(np.round(np.mean([c[0][1] for c in data['colors']]), 3))
    o = str(np.round(np.mean([c[0][2] for c in data['colors']]), 3))
    y = str(np.round(np.mean([c[0][3] for c in data['colors']]), 3))
    g = str(np.round(np.mean([c[0][4] for c in data['colors']]), 3))
    b = str(np.round(np.mean([c[0][5] for c in data['colors']]), 3))
    v = str(np.round(np.mean([c[0][6] for c in data['colors']]), 3))
    f = str(np.round(np.mean([c[0][7] for c in data['colors']]), 3))
    pi = str(np.round(np.mean([c[0][8] for c in data['colors']]), 3))
    wh = str(np.round(np.mean([c[0][9] for c in data['colors']]), 3))
    bl = str(np.round(np.mean([c[0][10] for c in data['colors']]), 3))

    cc = np.round(np.mean([c[1][0] for c in data['colors']]), 3)
    wc = np.round(np.mean([c[1][1] for c in data['colors']]), 3)
    
    cc = str(np.round(cc*100, 3))
    wc = str(np.round(wc*100, 3))

    color_script = """<script type='text/javascript'>
  new Chart(document.getElementById('colors'), {
  type: 'doughnut',
  data: {
    labels: ['Rosso', 'Marrone', 'Arancione', 'Giallo', 'Verde', 'Blu', 'Viola', 'Fucsia', 'Rosa', 'Bianco', 'Nero'],
    datasets: [{
      label: 'Colori più presenti',
      backgroundColor: ['rgb(232, 86, 86)', 'rgb(181, 126, 67)', 'rgb(232, 147, 86)', 'rgb(232, 203, 86)', 'rgb(88, 191, 112)', 'rgb(88, 153, 191)', 'rgb(126, 104, 173)', 'rgb(199, 122, 204)', 'rgb(227, 181, 230)', 'rgb(240, 240, 240)', 'rgb(26, 26, 26)'],\
      data: ["""+r+""", """+ br+""", """+ o+""", """+ y+""", """+ g+""", """+ b+""", """+ v+""", """+ f+""", """+ pi+""", """+ wh+""", """+ bl+"""]\
    }]
  },
});
  </script>"""
    
    #BRIGHTNESS
    bright_mean = str(np.round(np.mean([b[4] for b in data['brightness']]), 3))
    bright_var = str(np.round(np.mean([b[3] for b in data['brightness']]), 3))

    #SATURATION
    satur_mean = str(np.round(np.mean([b[4] for b in data['saturation']]), 3))
    satur_var = str(np.round(np.mean([b[3] for b in data['saturation']]), 3))


    #CAPTION=========ANALYSIS

    #EMOJIS--CAPTION
    emoji_cap_freq = str(np.round(data['caption_analysis'][0], 2))
    for k, i in zip(data['caption_analysis'][1].items(), range(len(data['caption_analysis'][1]))):
        if i == 0:
            try:
                emoji_cap_1 = 'String.fromCodePoint(0x'+str('{:X}'.format(ord(emoji.emojize(':'+str(k[0]).replace(' ', '_')+':'))))+')'
            except Exception as e:
                emoji_cap_1 = "'"+k[0]+"'"
            emoji_f_cap_1 = str(np.round(k[1], 3))
            
        if i == 1:
            try:
                emoji_cap_2 = 'String.fromCodePoint(0x'+str('{:X}'.format(ord(emoji.emojize(':'+str(k[0]).replace(' ', '_')+':'))))+')'
            except:
                emoji_cap_2 = "'"+k[0]+"'"
            emoji_f_cap_2 = str(np.round(k[1], 3))
            
        if i == 2:
            try:
                emoji_cap_3 = 'String.fromCodePoint(0x'+str('{:X}'.format(ord(emoji.emojize(':'+str(k[0]).replace(' ', '_')+':'))))+')'
            except:
                emoji_cap_3 = "'"+k[0]+"'"
            emoji_f_cap_3 = str(np.round(k[1], 3))


    #EMOJIS--FAMILY--CAPTION
    for k, i in zip(data['caption_analysis'][2].items(), range(len(data['caption_analysis'][2]))):
        if i == 0:
            emoji_fam_cap_1 = str(k[0])
            emoji_fam_f_cap_1 = str(np.round(k[1], 3))
        if i == 1:
            emoji_fam_cap_2 = str(k[0])
            emoji_fam_f_cap_2 = str(np.round(k[1], 3))       
        if i == 2:
            emoji_fam_cap_3 = str(k[0])
            emoji_fam_f_cap_3 = str(np.round(k[1], 3))
            
    #HASHTAG
    hashtag_freq = str(np.round(data['caption_analysis'][3], 2))
    for k, i in zip(data['caption_analysis'][4].items(), range(len(data['caption_analysis'][4]))):
        if i == 0:
            hashtag_1 = str(k[0])
            hashtag_f_1 = str(np.round(k[1], 3))
        if i == 1:
            hashtag_2 = str(k[0])
            hashtag_f_2 = str(np.round(k[1], 3))      
        if i == 2:
            hashtag_3 = str(k[0])
            hashtag_f_3 = str(np.round(k[1], 3))

    #WORDS
    cap_len = str(np.round(data['caption_analysis'][5], 2))
    
    word_dict= eval(data['caption_analysis'][6])
    w1 = word_dict['word']['0']
    w1_abs_freq = str(np.round(word_dict['abs_freq']['0'], 4))
    w1_wtd_freq = str(np.round(word_dict['wtd_freq_perc']['0'], 4))
    w1_wtd_freq_cum = str(np.round(word_dict['wtd_freq_perc_cum']['0'], 4))

    w2 = word_dict['word']['1']
    w2_abs_freq = str(np.round(word_dict['abs_freq']['1'], 4))
    w2_wtd_freq = str(np.round(word_dict['wtd_freq_perc']['1'], 4))
    w2_wtd_freq_cum = str(np.round(word_dict['wtd_freq_perc_cum']['1'], 4))

    w3 = word_dict['word']['2']
    w3_abs_freq = str(np.round(word_dict['abs_freq']['2'], 4))
    w3_wtd_freq = str(np.round(word_dict['wtd_freq_perc']['2'], 4))
    w3_wtd_freq_cum = str(np.round(word_dict['wtd_freq_perc_cum']['2'], 4))

    #COMMENT=========ANALYSIS
    #COMMENT EMOJI
    emoji_comm_freq  = str(np.round(data['comment_analysis'][0], 2))
    for k, i in zip(data['comment_analysis'][1].items(), range(len(data['comment_analysis'][1]))):
        if i == 0:
            try:
                emoji_comm_1 = 'String.fromCodePoint(0x'+str('{:X}'.format(ord(emoji.emojize(':'+str(k[0]).replace(' ', '_')+':'))))+')'
            except:
                emoji_comm_1 = "'"+k[0]+"'"
            emoji_f_comm_1 = str(np.round(k[1], 3))
            
        if i == 1:
            try:
                emoji_comm_2 = 'String.fromCodePoint(0x'+str('{:X}'.format(ord(emoji.emojize(':'+str(k[0]).replace(' ', '_')+':'))))+')'
            except:
                emoji_comm_2 = "'"+k[0]+"'"
            emoji_f_comm_2 = str(np.round(k[1], 3))
            
        if i == 2:
            try:
                emoji_comm_3 = 'String.fromCodePoint(0x'+str('{:X}'.format(ord(emoji.emojize(':'+str(k[0]).replace(' ', '_')+':'))))+')'
            except:
                emoji_comm_3 = "'"+k[0]+"'"
            emoji_f_comm_3 = str(np.round(k[1], 3))

    for k, i in zip(data['comment_analysis'][2].items(), range(len(data['comment_analysis'][2]))):
        if i == 0:
            emoji_fam_comm_1 = str(k[0])
            emoji_fam_f_comm_1 = str(np.round(k[1], 3))
        if i == 1:
            emoji_fam_comm_2 = str(k[0])
            emoji_fam_f_comm_2 = str(np.round(k[1], 3))       
        if i == 2:
            emoji_fam_comm_3 = str(k[0])
            emoji_fam_f_comm_3 = str(np.round(k[1], 3))

    #COMMENT WORDS
    word_dict_comm= eval(data['comment_analysis'][3])
    w1_comm = word_dict_comm['word']['0']
    w1_comm_abs_freq = str(np.round(word_dict_comm['abs_freq']['0'], 4))
    w1_comm_wtd_freq = str(np.round(word_dict_comm['wtd_freq_perc']['0'], 4))
    w1_comm_wtd_freq_cum = str(np.round(word_dict_comm['wtd_freq_perc_cum']['0'], 4))

    w2_comm = word_dict_comm['word']['1']
    w2_comm_abs_freq = str(np.round(word_dict_comm['abs_freq']['1'], 4))
    w2_comm_wtd_freq = str(np.round(word_dict_comm['wtd_freq_perc']['1'], 4))
    w2_comm_wtd_freq_cum = str(np.round(word_dict_comm['wtd_freq_perc_cum']['1'], 4))

    w3_comm = word_dict_comm['word']['2']
    w3_comm_abs_freq = str(np.round(word_dict_comm['abs_freq']['2'], 4))
    w3_comm_wtd_freq = str(np.round(word_dict_comm['wtd_freq_perc']['2'], 4))
    w3_comm_wtd_freq_cum = str(np.round(word_dict_comm['wtd_freq_perc_cum']['2'], 4))

    #TIMING
    X_year = str(data['timing'][0][0])
    Y_year = str(data['timing'][0][1])

    X_month = str(data['timing'][1][0])
    Y_month = str(data['timing'][1][1])

    h1 = str(np.round(data['timing'][2][0], 0))
    h2 = str(np.round(data['timing'][2][1], 0))
    h3 = str(np.round(data['timing'][2][2], 0))

 
    css = """<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>"""+name+"""</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Muli:wght@900&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Raleway&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@2.9.3"></script>
    <script src="https://cdn.jsdelivr.net/npm/hammerjs@2.0.8"></script>
    <script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-zoom@0.7.7"></script>
  </head>
  <style media="screen">
  .text{
    font-family: 'Raleway', sans-serif;
    font-weight: 200;
    text-align: left;
    color: #093652;
  }
  #title{
    font-size: 60px;
    font-weight: 800;
    text-align: left;
    letter-spacing: 1px;
    line-height: 100px;
  }
  #subtitle{
    font-size: 37px;
    font-weight: 900;
    letter-spacing: 1px;
  }
  #paragraph{
    padding-top: 10px;
    font-size: 23px;
    font-weight: 400;
  }
  .main-pic{
    position: relative;
    width: 180px;
    height: 180px;
    left: 50%;
    margin-left: -90px;
    border-radius: 300px;
    background-color: red;
    background-image: url("""+url+""");
    background-size: cover;
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
    padding-bottom: 20px;
    width: 100%;
  }
canvas {
    -moz-user-select: none;
    -webkit-user-select: none;
    -ms-user-select: none;
    }
  .evidence{
    margin-top: 50px;
    font-family: 'Muli', sans-serif;
    font-weight: 100;
    font-size: 20px;
    color: 	#1685cc;
  }
  #hours{
    text-align: center;
  }
  table.blueTable {
    width: 100%;
    text-align: left;

  }
  table.blueTable td, table.blueTable th {
    padding: 10px 10px;
  }
  table.blueTable tbody td {
    font-size: 18px;
    font-family: 'Raleway', sans-serif;
    padding: 20px;
  }
  table.blueTable thead {
    background: #0f5c8c;
  }
  table.blueTable thead th {
    font-size: 20px;
    font-family: 'Raleway', sans-serif;
    font-weight: bold;
    color: #FFFFFF;
    padding: 20px;
  }

  @media screen and (max-width: 800px){
    #title{
      font-size: 60px;
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
      overflow-x: scroll;
    }
  }
"""
    html1="""  </style>
  <body>
    <div class="container">
      <h1 class="text" id="title">"""+name+"""</h1>
      <div class="main-pic"></div>

      <p class="text" id="paragraph"></p>
      <h2 class="text" id='title'>Crescita Likes</h2>
      <p class="text" id="subtitle">Crescita Breve Termine</p>
      <p class="text" id="paragraph">Crescita Breve Termine: <span class="evidence">"""+like_st_score+"""%</span></p>
      <div class="panel">
        <canvas id="like-growth-st" width="100%" height="70px"></canvas>
      </div>

      <p class="text" id="subtitle">Crescita Lungo Termine</p>
      <p class="text" id="paragraph">Crescita Lungo Termine: <span class="evidence">"""+like_lt_score+"""%</span></p>
      <div class="panel" id="panel-lt">
        <canvas id="like-growth-lt" ></canvas>
      </div>
      <h2 class="text" id='subtitle'>Top 5 Post-Likes</h2>
      <div class="panel">
        <table class="blueTable">
          <thead>
            <tr>
            <th>Numero Post su grafico LT</th>
            <th>Link al Post</th>
            </tr>
          </thead>
          <tbody>
            <tr>
      """

    html2 = """
          </tbody>
        </table>
      </div>
      
      <h2 class="text" id='title'>Crescita Commenti</h2>
      <p class="text" id="subtitle">Crescita Breve Termine</p>
      <p class="text" id="paragraph">Crescita Breve Termine: <span class="evidence">"""+comment_st_score+"""%</span></p>
      <div class="panel">
        <canvas id="comment-growth-st" width="100%" height="70px"></canvas>
      </div>
      <p class="text" id="subtitle">Crescita Lungo Termine</p>
      <p class="text" id="paragraph">Crescita Lungo Termine: <span class="evidence">"""+comment_lt_score+"""%</span></p>
      <div class="panel">
        <canvas id="comment-growth-lt"  height="70px" width = "150%"></canvas>
      </div>

      <h2 class="text" id='subtitle'>Post migliori</h2>
      <div class="panel">
        <table class="blueTable">
          <thead>
            <tr>
            <th>Numero Post su grafico LT</th>
            <th>Link al Post</th>
            </tr>
          </thead>
          <tbody>
            <tr>"""
      
    html3 = """
          </tbody>
        </table>
      </div>

      <h2 class="text" id="title">Statistiche Post</h2>
      <h2 class="text" id='subtitle'>Tipologie Più Usate</h2>

        <canvas id="type-post" width="100%" height="70px"></canvas>

      <h2 class="text" id='subtitle'>Colori Più Utilizzati</h2>
      <div class="panel">
        <canvas id="colors" width="100%" height="70px"></canvas>
      </div>
      <div class="panel">
        <table class="blueTable">
          <thead>
            <tr>
            <th>Tipologia Colore</th>
            <th>Presenza</th>
            </tr>
          </thead>
          <tbody>
            <tr>
            <td>Caldi</td><td>"""+wc+"""%</td></tr>
            <tr>
            <td>Freddi</td><td>"""+cc+"""%</td></tr>
            <tr>
            <td>Neutri+</td><td>"""+str(100-float(cc)-float(wc))+"""%</td></tr>
            <tr>
          </tbody>
        </table>
      </div>

      <h2 class="text" id='subtitle'>Features</h2>
      <div class="panel">
        <p class="text" id="paragraph">Brillantezza: <span class="evidence">"""+bright_mean+"""</span> <span style="float: right;">Varianza Brillantezza: <span class="evidence">"""+bright_var+"""</span></span></p>
        <p class="text" id="paragraph">Saturazione: <span class="evidence">"""+satur_mean+"""</span> <span style="float: right;">Varianza Saturazione: <span class="evidence">"""+satur_var+"""</span></span></p>
      </div>

      <h2 class="text" id='title'>Analisi Caption<br></h2>
      <h2 class="text" id='subtitle'>Parole Più Utilizzate</h2>
      <p class="text" id="paragraph">Lunghezza Media Caption: <span class="evidence">"""+cap_len+"""</span></p>
      <div class="panel">
        <table class="blueTable">
          <thead>
            <tr>
            <th>Parola</th>
            <th>Numero</th>
            <th>Freq Pes</th>
            <th>Freq Pes Cum</th>
            </tr>
          </thead>
          <tbody>
            <tr>
            <td>"""+w1+"""</td><td>"""+w1_abs_freq+"""</td><td>"""+w1_wtd_freq+"""</td><td>"""+w1_wtd_freq_cum+"""</td></tr>
            <tr>
            <td>"""+w2+"""</td><td>"""+w2_abs_freq+"""</td><td>"""+w2_wtd_freq+"""</td><td>"""+w2_wtd_freq_cum+"""</td></tr>
            <tr>
            <td>"""+w3+"""</td><td>"""+w3_abs_freq+"""</td><td>"""+w3_wtd_freq+"""</td><td>"""+w3_wtd_freq_cum+"""</td></tr>
            </tr>
          </tbody>
        </table>
      </div>

      <h2 class="text" id='subtitle'>Analisi Emoji</h2>
      <p class="text" id="paragraph">Frequenza Emoji: <span class="evidence">"""+emoji_cap_freq+"""</span></p>
      <div class="panel">
        <canvas id="emoji-most" width="100%" height="40px"></canvas>
      </div>

      <div class="panel">
        <canvas id="emoji-family-most" width="100%" height="40px"></canvas>
      </div>

      <h2 class="text" id='subtitle'>Analisi Hashtag</h2>
      <p class="text" id="paragraph">Frequenza Hashtag: <span class="evidence">"""+hashtag_freq+"""</span></p>
      <div class="panel">
        <canvas id="hashtag-most" width="100%" height="40px"></canvas>
      </div>

      <h2 class="text" id="title">Analisi Commenti<br></h2>

      <h2 class="text" id='subtitle'>Parole Più Utilizzate</h2>
      <div class="panel">
        <table class="blueTable">
          <thead>
            <tr>
            <th>Parola</th>
            <th>Numero</th>
            <th>Freq Pes</th>
            <th>Freq Pes Cum</th>
            </tr>
          </thead>
          <tbody>
            <tr>
            <td>"""+w1_comm+"""</td><td>"""+w1_comm_abs_freq+"""</td><td>"""+w1_comm_wtd_freq+"""</td><td>"""+w1_comm_wtd_freq_cum+"""</td></tr>
            <tr>
            <td>"""+w2_comm+"""</td><td>"""+w2_comm_abs_freq+"""</td><td>"""+w2_comm_wtd_freq+"""</td><td>"""+w2_comm_wtd_freq_cum+"""</td></tr>
            <tr>
            <td>"""+w3_comm+"""</td><td>"""+w3_comm_abs_freq+"""</td><td>"""+w3_comm_wtd_freq+"""</td><td>"""+w3_comm_wtd_freq_cum+"""</td></tr>
            </tr>
          </tbody>
        </table>
      </div>

      <h2 class="text" id='subtitle'>Analisi Emoji</h2>
      <p class="text" id="paragraph">Frequenza Utilizzo Emoji: <span class="evidence">"""+emoji_comm_freq+"""</span></p>
      <div class="panel">
        <canvas id="emoji-most-comment" width="100%" height="40px"></canvas>
      </div>
      <div class="panel">
        <canvas id="emoji-fam-most-comment" width="100%" height="40px"></canvas>
      </div>


      <h2 class="text" id='title'>Statistiche sul Tempo</h2>

      <h2 class="text" id='subtitle'>Post per Anno</h2>
      <div class="panel">
        <canvas id="years" width="100%" height="50px"></canvas>
      </div>

      <h2 class="text" id='subtitle'>Post per Mese</h2>
      <div class="panel">
        <canvas id="months" width="100%" height="50px"></canvas>
      </div>

      <div class="panel">
        <p class="text" id="subtitle">Orari Pubblicazioni più frequenti:
          <p class="evidence" id="hours" style="float: 'center'; font-size:45px">"""+h1+"""&nbsp;&nbsp;&nbsp;"""+h2+"""&nbsp;&nbsp;&nbsp;"""+h3+"""</p>
        </p>
      </div>
    </div>

  </body>"""

    js = """
  <script>
  new Chart(document.getElementById('like-growth-st'), {
    type: 'line',
    data: {
      labels: """+like_st_graph_X+""",
      datasets: [{
          data: """+like_st_graph_Y+""",
          label: 'Crecita Likes Breve Termine',
          borderColor: 'rgb(22, 133, 204)',
          backgroundColor: 'rgba(22, 133, 204, 0.3)',
        },
      ]
    },
  });
  </script>
  <script>
  new Chart(document.getElementById('like-growth-lt'), {
    type: 'line',
    data: {
      labels: """+like_lt_graph_X+""",
      datasets: [{
          data: """+like_lt_graph_Y+""",
          label: 'Crecita Likes Breve Termine',
          borderColor: 'rgb(22, 133, 204)',
          backgroundColor: 'rgba(22, 133, 204, 0.3)',
        },
      ]
    },
    options: {
        pan: {
            enabled: true,
            mode: "x",
            speed: 1000000000,
            threshold: 10
        },
        zoom: {
            enabled: true,
            drag: false,
            mode: "x",
            speed: 1000000000,
            threshold: 100
        }
    }
  });
  </script>
  <script>
  new Chart(document.getElementById('comment-growth-st'), {
    type: 'line',
    data: {
      labels: """+comment_st_graph_X+""",
      datasets: [{
          data: """+comment_st_graph_Y+""",
          label: 'Crescita Commenti Lungo Termine',
          borderColor: 'rgb(22, 133, 204)',
          backgroundColor: 'rgba(22, 133, 204, 0.3)',
        },
      ]
    },

  });
  </script>
  <script>
  new Chart(document.getElementById('comment-growth-lt'), {
    type: 'line',
    data: {
      labels: """+comment_lt_graph_X+""",
      datasets: [{
          data: """+comment_lt_graph_Y+""",
          label: 'Crescita Commenti Lungo Termine',
          borderColor: 'rgb(22, 133, 204)',
          backgroundColor: 'rgba(22, 133, 204, 0.3)',
        },
      ]
    },
    options: {
        pan: {
            enabled: true,
            mode: "x",
            speed: 1000000000,
            threshold: 10
        },
        zoom: {
            enabled: true,
            drag: false,
            mode: "x",
            speed: 1000000000,
            threshold: 100
        }
    }
  });
  </script>

  <script type='text/javascript'>
  new Chart(document.getElementById('type-post'), {
  type: 'doughnut',
  data: {
    labels: ['Foto', 'Video', 'Sidecar'],
    datasets: [{
      label: 'Population (millions)',
      backgroundColor: ['rgb(15, 92, 140)', 'rgb(22, 133, 204)', 'rgb(17, 111, 171)'],
      data: ["""+pic_score+""", """+video_score+""", """+sidecar_score+"""]
    }]
  },
});
  </script>"""+color_script+"""<script>
  new Chart(document.getElementById('emoji-most'), {
    type: 'horizontalBar',
    data: {
      labels: ["""+emoji_cap_1+""", """+emoji_cap_2+""", """+emoji_cap_3+"""],
      datasets: [
        {
          backgroundColor: ['rgb(15, 92, 140)', 'rgb(22, 133, 204)', 'rgb(15, 92, 140)'],
          data: ["""+emoji_f_cap_1+""", """+emoji_f_cap_2+""", """+emoji_f_cap_3+"""]
        }
      ]
    },
    options: {
        legend: { display: false },
        scales: {
            yAxes: [{
                ticks: {
                    fontSize: 30
                }
            }]
        }
    }
  });
  </script>

  <script>
  new Chart(document.getElementById('emoji-fam-most'), {
    type: 'horizontalBar',
    data: {
      labels: ['"""+emoji_fam_cap_1+"""', '"""+emoji_fam_cap_2+"""', '"""+emoji_fam_cap_3+"""'],
      datasets: [
        {
          backgroundColor: ['rgb(15, 92, 140)', 'rgb(22, 133, 204)', 'rgb(15, 92, 140)'],
          data: ["""+emoji_fam_f_cap_1+""", """+emoji_fam_f_cap_2+""", """+emoji_fam_f_cap_3+"""]
        }
      ]
    },
    options: {
      legend: { display: false },
    }
  });
  </script>

  <script>
  new Chart(document.getElementById('hashtag-most'), {
    type: 'horizontalBar',
    data: {
      labels: ['#"""+hashtag_1+"""', '#"""+hashtag_2+"""', '#"""+hashtag_3+"""'],
      datasets: [
        {
          backgroundColor: ['rgb(15, 92, 140)', 'rgb(22, 133, 204)', 'rgb(15, 92, 140)'],
          data:  ["""+hashtag_f_1+""", """+hashtag_f_2+""", """+hashtag_f_3+"""]
        }
      ]
    },
    options: {
      legend: { display: false },
    }
  });
  </script>


  <script>
  new Chart(document.getElementById('emoji-most-comment'), {
    type: 'horizontalBar',
    data: {
      labels: ["""+emoji_comm_1+""", """+emoji_comm_2+""", """+emoji_comm_3+"""],
      datasets: [
        {
          backgroundColor: ['rgb(15, 92, 140)', 'rgb(22, 133, 204)', 'rgb(15, 92, 140)'],
          data: ["""+emoji_f_comm_1+""", """+emoji_f_comm_2+""", """+emoji_f_comm_3+"""]
        }
      ]
    },
    options: {
        legend: { display: false },
        scales: {
            yAxes: [{
                ticks: {
                    fontSize: 30
                }
            }]
        }
    }
  });
  </script>

  <script>
  new Chart(document.getElementById('emoji-fam-most-comment'), {
    type: 'horizontalBar',
    data: {
      labels: ['"""+emoji_fam_comm_1+"""', '"""+emoji_fam_comm_2+"""', '"""+emoji_fam_comm_3+"""'],
      datasets: [
        {
          backgroundColor: ['rgb(15, 92, 140)', 'rgb(22, 133, 204)', 'rgb(15, 92, 140)'],
          data: ["""+emoji_fam_f_comm_1+""", """+emoji_fam_f_comm_2+""", """+emoji_fam_f_comm_3+"""]
        }
      ]
    },
    options: {
      legend: { display: false },
    }
  });
  </script>

  <script>
  new Chart(document.getElementById('years'), {
      type: 'bar',
      data: {
        labels: """+X_year+""",
        datasets: [
          {
            label: 'Post per Anno',
            backgroundColor: ['rgb(22, 133, 204)', 'rgb(22, 133, 204)', 'rgb(22, 133, 204)', 'rgb(22, 133, 204)', 'rgb(22, 133, 204)', 'rgb(22, 133, 204)', 'rgb(22, 133, 204)', 'rgb(22, 133, 204)', 'rgb(22, 133, 204)', 'rgb(22, 133, 204)'],
            data: """+Y_year+"""
          }
        ]
      },
      options: {
        legend: { display: false },
        title: {
          display: true,
          text: 'Post Pubblicati per Anno'
        }
      }
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
    page.write(html1)
    for k,v in like_def.items():
        page.write('<td>'+str(k)+'</td><td>'+'<a href="https://www.instagram.com/p/'+str(v)+'"> clicca qui </a></td></tr>')
    page.write(html2)
    for k,v in comm_def.items():
        page.write('<td>'+str(k)+'</td><td>'+'<a href="https://www.instagram.com/p/'+str(v)+'"> clicca qui </a></td></tr>')
    page.write(html3)
    page.write(js)
    page.close()
    return None


name_main = 'Alessandro Marino'
usm = 'marketing_espresso'
path = '/home/rootdebian/Scrivania/Hirundo/projects/'+name_main+'/competitor-data/'
#os.mkdir('/home/rootdebian/Scrivania/Hirundo/projects/'+name_main+'/works/'+str(date.today())+'-cd/')
main = open('/home/rootdebian/Scrivania/Hirundo/projects/'+name_main+'/works/'+str(date.today())+'-cd/index.html', 'a')
scores = {}


#=========MAIN=========
for competitor in os.listdir(path):
    print(competitor)
    name = competitor
    like_all = []
    comment_all = []
    n_follow = Profile.from_username(L.context, name).followers
    for f in os.listdir(path+competitor):
        if 'DATA' in f:
            with open(path+competitor+'/'+f) as js:
                data = json.load(js)
                n_reach = np.sum(data['like_growth'][0][1]) + np.sum(data['comment_growth'][0][1])
                score = np.round(n_reach/n_follow, 3)

                if np.sum(data['like_growth'][0][1][0:3]) != 0:
                    score_like = (np.sum(data['like_growth'][0][1][-4:-1])-np.sum(data['like_growth'][0][1][0:3]))/(np.sum(data['like_growth'][0][1][0:3]))
                else:
                    score_like = (np.sum(data['like_growth'][0][1][-4:-1])-np.sum(data['like_growth'][0][1][0:3]))/1

                if np.sum(data['comment_growth'][0][1][0:3]) != 0:
                    score_comment = (np.sum(data['comment_growth'][0][1][-4:-1])-np.sum(data['comment_growth'][0][1][0:3]))/(np.sum(data['comment_growth'][0][1][0:3]))
                else:
                    score_comment = (np.sum(data['comment_growth'][0][1][-4:-1])-np.sum(data['comment_growth'][0][1][0:3]))/1
    #pages(name_main, name, competitor, score_like, score_comment, data)
    scores.update({name: np.round(score, 4)})
    print('ok')
    
a = sorted(scores.items(), key=lambda x: x[1])
create_main(a)
print('finish')

with open('/home/rootdebian/Scrivania/Hirundo/projects/'+name_main+'/BEST_DATA.json') as mainf:
    data = json.load(mainf)
    myself(usm, data)

print('finish')










    

                
                
