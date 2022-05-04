import comic_collection

class WereOutOfCornflakes(comic_collection.Comic):
    """Bla bla bla
    """
    def __init__(self):
        super().__init__()
        self.title = "We're Out Of Cornflakes"
        self.url = "https://wereoutofcornflakes.com"

    def fetch_comic(self):
        IMG=self.findDivById(self.makeBanner(self.title), self.url, "comic")
        return IMG
