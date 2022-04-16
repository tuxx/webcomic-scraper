from comic_collection import ComicCollection
import datetime

date = datetime.datetime.today()
year = date.strftime("%Y")
OUTPUT_FILE="/var/www/comics/index.html"
UPDATED_ON = date.strftime("%d-%m-%Y %H:%M:%S")
LASTUPDATED=f"<center><h3>Last update: {UPDATED_ON}</h3></center>"

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

def main():
    global HTMLHEAD
    my_comics = ComicCollection('comics')
    comics=my_comics.get_all_comics()
    HTMLHEAD+=f"""
    </ul>
    <center>
    <hr style='width:70%;text-align:left;margin-left:0'>
    """
    f = open(OUTPUT_FILE, "w")
    f.write(HTMLHEAD + comics + HTMLFOOT)
    f.close()

if __name__ == '__main__':
    main()
