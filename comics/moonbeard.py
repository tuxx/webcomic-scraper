import comic_collection

class Moonbeard(comic_collection.Comic):
    """Bla bla bla
    """
    def __init__(self):
        super().__init__()
        self.title = "Moonbeard"
        self.url = "https://moonbeard.com"

    def fetch_comic(self):
        IMG=self.findDivById(self.makeBanner(self.title), self.url, "comic-1")
        IMG = IMG.replace('<div id="comic-1" class="comicpane">', "")
        IMG = IMG.replace('</div>', "")
        return IMG
