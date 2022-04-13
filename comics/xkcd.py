import comic_collection

class XKCD(comic_collection.Comic):
    """Bla bla bla
    """
    def __init__(self):
        super().__init__()
        self.title = "XKCD"
        self.url = "https://xkcd.com"

    def fetch_comic(self):
        IMG=self.findDivById(self.makeBanner(self.title), self.url, "comic")
        IMG = IMG.replace("\"//", "https://")
        IMG = IMG.replace('<div id="comic">', "")
        IMG = IMG.replace('</div>', "")
        return IMG
