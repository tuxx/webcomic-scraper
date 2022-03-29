import bs4
import urllib
import datetime
import requests

OUTPUT_DIR="/var/www/comics"
OUTPUT_FILE=f"{OUTPUT_DIR}/index.html"

###
### DATES 'N SHIT
###
date = datetime.date.today()
year = date.strftime("%Y")
date = datetime.datetime.today()

###
### VARIABLES BOIIIII
###
UPDATED_ON = date.strftime("%d-%m-%Y %H:%M:%S")
LASTUPDATED=f"<center><h3>Last update: {UPDATED_ON}</h3></center>"
ENDRESULT=""
HR="<hr style='width:70%;text-align:left;margin-left:0'>"

###
### INDEX
###
INDEX="""
<div id="index"></div>
<h1>Index</h1>
<ul>
"""

###
### HTML HEADER
###
HTMLHEAD=f"""
<!DOCTYPE html>
<html>
<head>
    <title>Comics</title>
    <link rel="stylesheet" href="dark-theme.css">
    <link rel="icon" type="image/png" href="comics.png" />
</head>
<body>
{LASTUPDATED}
<div class="ex1">
"""

###
### HTML FOOTER
###
HTMLFOOT=f"""
{LASTUPDATED}
</center>
</div>
</body>
</html>
"""


def findImgByClass(BANNER, URL, CLASS, PREPEND_URL=False, DATASRC=False):
    soup = getSoupContent(URL)
    images = soup.findAll('img')
    for image in images:
        try:
            if image['class'] == CLASS:
                if PREPEND_URL and not DATASRC:
                    content = f"<a href='{URL}'><img src='{URL}/{image['src']}' /></a>"
                elif PREPEND_URL and DATASRC:
                    #print(image['data-src'])
                    content = f"<a href='{URL}'><img src='{URL}/{image['data-src']}' /></a>"
                else:
                    if DATASRC:
                        #print(image['data-src'])
                        content = f"<a href='{URL}'><img src='{image['data-src']}' /></a>"
                    else:
                        content = f"<a href='{URL}'><img src='{image['src']}' /></a>"
                return BANNER + content + HR
        except:
            pass

def findImgById(BANNER, URL, ID, PREPEND_URL=False):
    soup = getSoupContent(URL)
    div = soup.find("div", {"id": ID})
    div=str(div)
    content = f"<a href='{URL}'>{div}</a>"

    return BANNER + content + HR

def makeBanner(anchor, title):
    global INDEX
    INDEX = INDEX + f"<li><a href='#{anchor}'>{title}</a></li>\n"

    return f"""
<div id="{anchor}"></div>
<h1><a href="#{anchor}">{title}</a> 
<a href="#index">&#x21E7;</a></h1>
"""

def getSoupContent(url):
    req = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )
    url_contents = urllib.request.urlopen(req).read()
    return bs4.BeautifulSoup(url_contents, features="html5lib")

###
### Abstruse Goose
###
url = "http://abstrusegoose.com"
soup = getSoupContent(url)
images = soup.findAll('img')
for image in images:
    try:
        #print(image['src'])
        if "strips" in image['src']:
            content = f"<a href='{url}'><img src='{image['src']}' /></a>"
            ENDRESULT+=makeBanner('goose', 'Abstruse Goose') + content + HR
    except:
        pass

###
### Amazing Super Powers
###
ENDRESULT += findImgById(makeBanner("ASP", "Amazing Super Powers"), "http://amazingsuperpowers.com", "comic-1")

###
### CTRL+ALT+DEL
###
ENDRESULT += findImgByClass(makeBanner("cad", "Ctrl+Alt+Del"), "https://cad-comic.com", ["comic-display"])

###
### EXPLOSM
###
EXPLOSM_BANNER=makeBanner("candh", "Cyanide & Happiness")
url = "https://explosm.net/comics/latest"
soup = getSoupContent(url)
DONE=0
for div in soup.findAll('div', {'class':lambda x: x and x.startswith('MainComic__ComicImage')}):
    if DONE == 1:
        continue

    for image in div.findAll('img'):
        try:
            content = f"<a href='{url}'><img src='{image['src']}' /></a>"
            ENDRESULT+=EXPLOSM_BANNER + content + HR
            DONE=1
        except:
            pass


###
### DILBERT
###
DILBERT_BANNER=makeBanner("dilbert", "Dilbert")
ENDRESULT += findImgByClass(DILBERT_BANNER, "http://dilbert.com", ["img-responsive", "img-comic"])

###
### QWANTZ
###
QWANTZ_BANNER=makeBanner("dinosaur", "Dinosaur Comic")
ENDRESULT += findImgByClass(QWANTZ_BANNER, "https://qwantz.com", ["comic"], True)

###
### EXOCOMICS
###
EXOCOMICS_BANNER=makeBanner("extra", "Extra Ordinary")
url = "https://www.exocomics.com/"
soup = getSoupContent(url)
images = soup.findAll('img')
for image in images:
    try:
        if "image-style-main-comic" in image['class']:
            #print(image['src'])
            content = f"<a href='{url}'><img src='https://exocomics.com{image['src']}' /></a>"
            ENDRESULT+=EXOCOMICS_BANNER + content + HR
            DONE=1
    except:
        pass

###
### LUNAR BABOON
###
LUNARBABOON_BANNER=makeBanner("lunarbaboon", "Lunar Baboon")
url = "http://lunarbaboon.com"
soup = getSoupContent(url)
images = soup.findAll('img')
DONE=0
for image in images:
    if DONE == 1:
        continue
    try:
        #print(image['src'])
        if "/storage/" in image['src']:
            img=image['src']
            imgurl = f"{url}{img}"
            #print(f"imgurl: {imgurl}")
            r = requests.get(imgurl, allow_redirects=True)
            open(f"{OUTPUT_DIR}/lb.jpg", 'wb').write(r.content)
            content = f"<a href='{url}'><img src='/lb.jpg' /></a>"
            ENDRESULT+=LUNARBABOON_BANNER + content + HR
            DONE=1
    except:
        pass
###
### Moonbeard
###
MOONBEARD_BANNER=makeBanner("moonbeard", "Moonbeard")
IMG=findImgById(MOONBEARD_BANNER, "https://moonbeard.com", "comic-1")
IMG = IMG.replace('<div id="comic-1" class="comicpane">', "")
IMG = IMG.replace('</div>', "")
ENDRESULT += IMG

###
### MurderCake
###
MURDER_BANNER=makeBanner("murdercake", "Murdercake")
IMG=findImgById(MURDER_BANNER, "http://murdercake.com", "comic")
IMG = IMG.replace('<div id="comic">', "")
IMG = IMG.replace('</div>', "")
ENDRESULT += IMG

###
### ODDBALL
###
ODDBALL_BANNER=makeBanner("oddball", "Oddball")
url = "https://sarahcandersen.com/"
soup = getSoupContent(url)
images = soup.findAll('a')
DONE=0
for image in images:
    if DONE == 1:
        continue
    try:
        #print(image['href'])
        if image['href'][-3:] == "jpg":
            content = f"<a href='{url}'><img src='{image['href']}' /></a>"
            ENDRESULT+=ODDBALL_BANNER + content + HR
            DONE=1
    except:
        pass

###
### OPTIPESS
###
OPTIPESS_BANNER=makeBanner("optipess", "Optipess")
IMG=findImgById(OPTIPESS_BANNER, "https://optipess.com", "comic")
IMG = IMG.replace('<div id="comic">', "")
IMG = IMG.replace('</div>', "")
ENDRESULT += IMG

###
### POORLY DRAWN LINES
###
PDL_BANNER=makeBanner("poorlydrawn", "Poorly Drawn Lines")
url = "https://poorlydrawnlines.com/"
soup = getSoupContent(url)
images = soup.findAll('img')
for image in images:
    try:
        if image['class'][0].startswith("wp-image"):
            #print(image['src'])
            content = f"<a href='{url}'><img src='{image['src']}' /></a>"
            ENDRESULT+=PDL_BANNER + content + HR
            DONE=1
    except:
        pass

###
### PENNY ARCADE
###
def pa_fetch():
    url = "https://www.penny-arcade.com/comic"
    valid = True
    try:
        r = requests.get(url, timeout=10)
    except requests.RequestException as re:
        valid = False

    soup = bs4.BeautifulSoup(r.content, "html.parser")
    panels = soup.find(id="comic-panels")
    div = panels.find_all(class_="comic-panel")

    RESULT="<table cellspacing='0'><tr>"
    for d in div:
        RESULT+=f"<td><img src='{d.img['src']}' /></td>"
    RESULT+="</tr></table>"


    if valid:
        return RESULT
    else:
        return valid

PENNY=pa_fetch()
if not pa_fetch:
    print("Penny arcade failed bruh")
else:
    PENNY_BANNER=makeBanner("pennyarcade", "Penny Arcade")
    ENDRESULT+=PENNY_BANNER + PENNY + HR

###
### RAPH COMIC
###
RAPH_BANNER=makeBanner("raphcomic", "Raph Comic")
ENDRESULT += findImgByClass(RAPH_BANNER, "https://raphcomic.com", ["img-fluid", "lazyload"], True, True)

###
### SAVAGE CHICKENS
###
SC_BANNER=makeBanner("savagechickens", "Savage chickens")
url = "https://www.savagechickens.com/"
soup = getSoupContent(url)
images = soup.findAll('img')
DONE=0
for image in images:
    if DONE == 2:
        continue
    try:
        if "uploads" in image['src']:
            if image['alt'] != "":
                #print(image['src'])
                #print(image['alt'])
                if DONE == 0: #Skip the first uploads images with no alt text
                    DONE=1
                    continue

                if DONE == 1: # Grab 2nd image, we gots the comic boizzz
                    content = f"<a href='{url}'><img src='{image['src']}' /></a>"
                    ENDRESULT+=SC_BANNER + content + HR
                #    print("Adding savage chicken")
                    DONE=2
    except:
        pass

###
### smbc
###
smbc_banner=makeBanner("smbc", "SMBC")
url = "http://smbc-comics.com"
soup = getSoupContent(url)
div = soup.find("div", {"id": "cc-comicbody"})
sep = '/>'
div = str(div).split(sep, 1)[0]
content = f"<a href='{url}'>{div}/></a>"
content = content.replace('<div id="cc-comicbody">', "")
ENDRESULT+=smbc_banner + content + HR

###
### THREE WORD PHRASE
###
TWF_BANNER=makeBanner("threewordphrase", "Three Word Phrase")
url = "http://threewordphrase.com"
soup = getSoupContent(url)
images = soup.findAll('img')
DONE=0
for image in images:
    if DONE == 1:
        continue
    if int(image['width']) >= 900:
        imgurl = f"{url}/{image['src']}"
        #print(f"imgurl: {imgurl}")
        r = requests.get(imgurl, allow_redirects=True)
        open(f"{OUTPUT_DIR}/twp.gif", 'wb').write(r.content)
        #print("Wrote file.")

        content = f"<a href='{url}'><img src='/twp.gif' /></a>"
        ENDRESULT+=TWF_BANNER + content + HR
        DONE=1

###
### TOONHOLE
###
TOONHOLE_BANNER=makeBanner("toonhole", "Toonhole")
url = "https://toonhole.com/"
soup = getSoupContent(url)
images = soup.findAll('img')
DONE=0
for image in images:
    if DONE == 1:
        continue
    try:
        if "attachment-post-thumbnail" in image['class']:
            if year in image['src']:
                content = f"<a href='{url}'><img src='{image['src']}' /></a>"
                ENDRESULT+=TOONHOLE_BANNER + content + HR
                DONE=1
    except:
        pass

###
### War And Peas
###
WAP_BANNER=makeBanner("warandpeas", "War and Peas")
url = "https://warandpeas.com/"
soup = getSoupContent(url)
images = soup.findAll('img')
DONE=0
for image in images:
    if DONE == 1:
        continue
    try:
        if year in image['src']:
            content = f"<a href='{url}'><img src='{image['src']}' /></a>"
            ENDRESULT+=WAP_BANNER + content + HR
            DONE=1
    except:
        pass
###
### XKCD.COM
###
XKCDCOM_BANNER=makeBanner("xkcd", "XKCD")
IMG=findImgById(XKCDCOM_BANNER, "https://xkcd.com", "comic")
IMG = IMG.replace("\"//", "https://")
IMG = IMG.replace('<div id="comic">', "")
IMG = IMG.replace('</div>', "")
ENDRESULT += IMG

###
### WRITE HTML FILE
###
HTMLHEAD+=INDEX + f"""
</ul>
<center>
{HR}
"""

f = open(OUTPUT_FILE, "w")
f.write(HTMLHEAD + ENDRESULT + HTMLFOOT)
f.close()
