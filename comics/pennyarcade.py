import comic_collection
import requests
import bs4

class PennyArcade(comic_collection.Comic):
    """Bla bla bla
    """
    def __init__(self):
        super().__init__()
        self.title = "Penny Arcade"
        self.url = "https://www.penny-arcade.com/comic"

    def fetch_comic(self):
        valid = True
        try:
            r = requests.get(self.url, timeout=10)
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
            return self.makeBanner(self.title) + RESULT + self.HR
        else:
            return valid
