import bs4
import urllib
import datetime
import requests
import feedparser
import sys

DEBUG=False
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

def dprint(things):
    if DEBUG:
        print(things)

def findImgByClass(BANNER, URL, CLASS, PREPEND_URL=False, DATASRC=False):
    soup = getSoupContent(URL)
    images = soup.findAll('img')
    for image in images:
        try:
            if image['class'] == CLASS:
                if PREPEND_URL and not DATASRC:
                    content = f"<a href='{URL}'><img src='{URL}/{image['src']}' /></a>"
                elif PREPEND_URL and DATASRC:
                    content = f"<a href='{URL}'><img src='{URL}/{image['data-src']}' /></a>"
                else:
                    if DATASRC:
                        content = f"<a href='{URL}'><img src='{image['data-src']}' /></a>"
                    else:
                        content = f"<a href='{URL}'><img src='{image['src']}' /></a>"
                return BANNER + content + HR
        except:
            pass

def findDivById(BANNER, URL, ID, PREPEND_URL=False):
    soup = getSoupContent(URL)
    div = soup.find("div", {"id": ID})
    div=str(div)
    if PREPEND_URL:
        content = f"<a href='{URL}'>{URL}/{div}</a>"
    else:
        content = f"<a href='{URL}'>{div}</a>"

    return BANNER + content + HR

def findDivByClass(BANNER, URL, CLASS):
    soup = getSoupContent(URL)
    div = soup.find("div", {"class": CLASS})
    div=str(div)
    bs=bs4.BeautifulSoup(div, features="html5lib")
    img = bs.find("img")
    content = f"<a href='{URL}'><img src='{img['src']}'/></a>"

    return BANNER + content + HR

def makeBanner(title):
    global INDEX
    anchor=title.replace(" ", "").lower()
    INDEX = INDEX + f"<li><a href='#{anchor}'>{title}</a></li>\n"

    return f"""
<div id="{anchor}"></div>
<h1><a href="#{anchor}">{title}</a> 
<a href="#index">&#x21E7;</a></h1>
"""

def getComicByRss(feedurl, getitem):
    d = feedparser.parse(feedurl)
    content = d['entries'][0]['content'][0]['value']
    return content

def getSoupContent(url):
    req = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'
        }
    )
    url_contents = urllib.request.urlopen(req).read()
    return bs4.BeautifulSoup(url_contents, features="html5lib")


###
### Abstruse Goose
###
def abstrusegoose_fetch():
    title = "Abstruse Goose"
    url = "http://abstrusegoose.com"
    soup = getSoupContent(url)
    images = soup.findAll('img')
    for image in images:
        try:
            if "strips" in image['src']:
                content = f"<a href='{url}'><img src='{image['src']}' /></a>"
                return makeBanner(title) + content + HR
        except:
            pass

###
### Amazing Super Powers
###
def amazingsuperpowers_fetch():
    return findDivById(makeBanner('Amazing Super Powers'), "http://amazingsuperpowers.com", "comic-1")

###
### Bonus Context
###
def bonuscontext_fetch():
    title="Bonus Context"
    url = "https://bonuscontext.com/"
    soup = getSoupContent(url)
    images = soup.findAll('img')
    for image in images:
        try:
            if image['src'].startswith("/comics/"):
                content = f"<a href='{url}'><img src='{url}{image['src']}' /></a>"
                return makeBanner(title) + content + HR
        except:
            pass


###
### CTRL+ALT+DEL
###
def ctrlaltdel_fetch():
    return findImgByClass(makeBanner("Ctrl+Alt+Del"), "https://cad-comic.com", ["comic-display"])

###
### EXPLOSM
###
def cyanidehappiness_fetch():
    title="Cyanide & Happiness"
    url = "https://explosm.net/comics/latest"
    soup = getSoupContent(url)
    for div in soup.findAll('div', {'class':lambda x: x and x.startswith('MainComic__ComicImage')}):
        for image in div.findAll('img'):
            try:
                content = f"<a href='{url}'><img src='{image['src']}' /></a>"
                return makeBanner(title) + content + HR
            except:
                pass


###
### DILBERT
###
def dilbert_fetch():
 return findImgByClass(makeBanner("Dilbert"), "http://dilbert.com", ["img-responsive", "img-comic"])

###
### QWANTZ
###
def dinosaurcomic_fetch():
    return findImgByClass(makeBanner("Dinosaur Comic"), "https://qwantz.com", ["comic"], True)

###
### EXTRA FABULOUS
###
def extrafabulous_fetch():
    title = "Extra Fabulous"
    url = "https://www.reddit.com/r/ExtraFabulousComics"
    soup = getSoupContent(url)
    images = soup.findAll('img')
    for image in images:
        try:
            if "Post image" in image['alt']:
                content = f"<a href='{url}'><img src='{image['src']}' /></a>"
                return makeBanner(title) + content + HR
        except:
            pass


###
### EXOCOMICS
###
def extraordinary_fetch():
    title = "Extra Ordinary"
    url = "https://www.exocomics.com/"
    soup = getSoupContent(url)
    images = soup.findAll('img')
    for image in images:
        try:
            if "image-style-main-comic" in image['class']:
                content = f"<a href='{url}'><img src='https://exocomics.com{image['src']}' /></a>"
                return makeBanner(title) + content + HR
        except:
            pass

###
### LUNAR BABOON
###
def lunarbaboon_fetch():
    title = "Lunar Baboon"
    url = "http://lunarbaboon.com"
    soup = getSoupContent(url)
    images = soup.findAll('img')
    for image in images:
        try:
            if "/storage/" in image['src']:
                img=image['src']
                imgurl = f"{url}{img}"
                
                r = requests.get(imgurl, allow_redirects=True)
                open(f"{OUTPUT_DIR}/lb.jpg", 'wb').write(r.content)
                content = f"<a href='{url}'><img src='/lb.jpg' /></a>"
                return makeBanner(title) + content + HR
        except:
            pass


###
### Loading Artist
def loadingartist_fetch():
    title = "Loading Artist"
    comic = getComicByRss("https://loadingartist.com/index.xml", "aap")
    soup = bs4.BeautifulSoup(comic, features="html5lib")
    images = soup.findAll('img')
    return makeBanner(title) + str(images[0]) + HR

### 
###
### Moonbeard
###
def moonbeard_fetch():
    IMG=findDivById(makeBanner("Moonbeard"), "https://moonbeard.com", "comic-1")
    IMG = IMG.replace('<div id="comic-1" class="comicpane">', "")
    IMG = IMG.replace('</div>', "")
    return IMG

###
### MurderCake
###
def murdercake_fetch():
    IMG=findDivById(makeBanner("Murdercake"), "http://murdercake.com", "comic")
    IMG = IMG.replace('<div id="comic">', "")
    IMG = IMG.replace('</div>', "")
    return IMG

###
### ODDBALL
###
def oddball_fetch():
    title="Oddball"
    url = "https://sarahcandersen.com/"
    soup = getSoupContent(url)
    images = soup.findAll('a')
    for image in images:
        try:
            
            if image['href'][-3:] == "jpg":
                content = f"<a href='{url}'><img src='{image['href']}' /></a>"
                return makeBanner(title) + content + HR
        except:
            pass


###
### OPTIPESS
###
def optipess_fetch():
    IMG=findDivById(makeBanner("Optipess"), "https://optipess.com", "comic")
    IMG = IMG.replace('<div id="comic">', "")
    IMG = IMG.replace('</div>', "")
    return IMG

###
### Pizza Cake
###
def pizzacake_fetch():
    title = "Pizzacake"
    url = "https://pizzacakecomic.com"
    soup = getSoupContent(url)
    images = soup.findAll('img')
    for image in images:
        try:
            if str(image['width']) == "1280":
                content = f"<a href='{url}'><img src='{image['src']}' /></a>"
                return makeBanner(title) + content + HR
        except:
            pass

###
### POORLY DRAWN LINES
###
def poorlydrawnlines_fetch():
    title="Poorly Drawn Lines"
    url = "https://poorlydrawnlines.com/"
    soup = getSoupContent(url)
    images = soup.findAll('img')
    for image in images:
        try:
            if image['class'][0].startswith("wp-image"):
                
                content = f"<a href='{url}'><img src='{image['src']}' /></a>"
                return makeBanner(title) + content + HR
        except:
            pass

###
### PENNY ARCADE
###
def pennyarcade_fetch():
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


###
### RAPH COMIC
###
def raph_fetch():
    return findImgByClass(makeBanner("Raph Comic"), "https://raphcomic.com", ["img-fluid", "lazyload"], True, True)

###
### SAVAGE CHICKENS
###
def savagechickens_fetch():
    title = "Savage Chickens"
    url = "https://www.savagechickens.com/"
    soup = getSoupContent(url)
    images = soup.findAll('img')
    DONE=0
    for image in images:
        try:
            if "uploads" in image['src']:
                if image['alt'] != "":
                    
                    
                    if DONE == 0: #Skip the first uploads images with no alt text
                        DONE=1
                        continue

                    if DONE == 1: # Grab 2nd image, we gots the comic boizzz
                        content = f"<a href='{url}'><img src='{image['src']}' /></a>"
                        return makeBanner(title) + content + HR
        except:
            pass

###
### SIGMUND
###
def sigmund_fetch():
    title = "Sigmund"
    url = "http://sigmund.nl"
    soup = getSoupContent(url)
    images = soup.findAll('img')
    for image in images:
        try:
            if image['id'] == "strook":
                r = requests.get(image['src'], allow_redirects=True)
                open(f"{OUTPUT_DIR}/sigmund.gif", 'wb').write(r.content)
                content = f"<a href='{url}'><img src='/sigmund.gif' /></a>"
                return makeBanner(title) + content + HR
        except:
            pass


###
### smbc
###
def smbc_fetch():
    title="SMBC"
    url = "http://smbc-comics.com"
    soup = getSoupContent(url)
    div = soup.find("div", {"id": "cc-comicbody"})
    sep = '/>'
    div = str(div).split(sep, 1)[0]
    content = f"<a href='{url}'>{div}/></a>"
    content = content.replace('<div id="cc-comicbody">', "")
    return makeBanner(title) + content + HR

###
### THEYCANTALK
###
def theycantalk_fetch():
    title = "They Can Talk"
    url = "https://theycantalk.com"
    soup = getSoupContent(url)
    images = soup.findAll('img')
    for image in images:
        content = f"<a href='{url}'><img src='{image['src']}' /></a>"
        return makeBanner(title) + content + HR

###
### THREE WORD PHRASE
###
def threewordphrase_fetch():
    title = "Three Word Phrase"
    url = "http://threewordphrase.com"
    soup = getSoupContent(url)
    images = soup.findAll('img')
    for image in images:
        if int(image['width']) >= 900:
            imgurl = f"{url}/{image['src']}"
            r = requests.get(imgurl, allow_redirects=True)
            open(f"{OUTPUT_DIR}/twp.gif", 'wb').write(r.content)
            content = f"<a href='{url}'><img src='/twp.gif' /></a>"
            return makeBanner(title) + content + HR

###
### TOONHOLE
###
def toonhole_fetch():
    title="Toonhole"
    url = "https://toonhole.com/"
    soup = getSoupContent(url)
    images = soup.findAll('img')
    for image in images:
        try:
            if "attachment-post-thumbnail" in image['class']:
                if year in image['src']:
                    content = f"<a href='{url}'><img src='{image['src']}' /></a>"
                    return makeBanner(title) + content + HR
        except:
            pass

###
### War And Peas
###
def warandpeas_fetch():
    title = "War And Peas"
    url = "https://warandpeas.com/"
    soup = getSoupContent(url)
    images = soup.findAll('img')
    for image in images:
        try:
            if year in image['src']:
                content = f"<a href='{url}'><img src='{image['src']}' /></a>"
                return makeBanner(title) + content + HR
        except:
            pass

###
### Wumo
###
def wumo_fetch():
    IMG=findDivByClass(makeBanner("Wumo"), "https://wumo.com/wumo", "box-content")
    IMG = IMG.replace("/img", "https://wumo.com/img")
    return IMG

###
### XKCD.COM
###
def xkcd_fetch():
    IMG=findDivById(makeBanner("XKCD"), "https://xkcd.com", "comic")
    IMG = IMG.replace("\"//", "https://")
    IMG = IMG.replace('<div id="comic">', "")
    IMG = IMG.replace('</div>', "")
    return IMG

def _inspect_tasks():
    return { f[0].replace("_fetch", ""): f[1]
        for f in inspect.getmembers(sys.modules['__main__'], inspect.isfunction)
        if f[0].endswith('_fetch')
    }

def fetch_all():
    dprint("Fetching all comics!")
    ENDRESULT=""
    comics=_inspect_tasks()
    for key in comics:
        dprint(f"Fetching {key}..")
        ENDRESULT+=str(globals()[key+"_fetch"]())

    return ENDRESULT

def fetch_one(name):
    dprint(f"Fetch one comic: {name}")
    return globals()[name+"_fetch"]()


if len(sys.argv) > 1: # Fetch only one comic and output to test.html
    ENDRESULT += fetch_one(sys.argv[1])
    OUTPUT_FILE = f"{OUTPUT_DIR}/test.html"
else: # Fetch all comics
    ENDRESULT += fetch_all()


###
### WRITE HTML FILE
###
HTMLHEAD+=INDEX + f"""
</ul>
<center>
{HR}
"""

dprint(f"Outputting to {OUTPUT_FILE}")
f = open(OUTPUT_FILE, "w")
f.write(HTMLHEAD + ENDRESULT + HTMLFOOT)
f.close()
