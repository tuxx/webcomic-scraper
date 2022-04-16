import comic_collection

class Dilbert(comic_collection.Comic):
    """Bla bla bla
    """
    def __init__(self):
        super().__init__()
        self.title = "Dilbert"
        self.url = "http://dilbert.com"

    def fetch_comic(self):
        return self.findImgByClass(self.makeBanner(self.title), self.url, ["img-responsive", "img-comic"])
