import comic_collection

class LitteGamers(comic_collection.Comic):
    """Bla bla bla
    """
    def __init__(self):
        super().__init__()
        self.title = "Little Gamers"
        self.url = "https://little-gamers.com"

    def fetch_comic(self):
        IMG=self.findDivByClass(self.makeBanner(self.title), self.url, "the-actual-comic")
        return IMG
