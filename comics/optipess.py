import comic_collection

class Optipess(comic_collection.Comic):
    """Bla bla bla
    """
    def __init__(self):
        super().__init__()
        self.title = "Optipess"
        self.url = "https://optipess.com"

    def fetch_comic(self):
        IMG=self.findDivById(self.makeBanner(self.title), self.url, "comic")
        IMG = IMG.replace('<div id="comic">', "")
        IMG = IMG.replace('</div>', "")
        return IMG
