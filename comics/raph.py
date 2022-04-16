import comic_collection

class Raph(comic_collection.Comic):
    """Bla bla bla
    """
    def __init__(self):
        super().__init__()
        self.title = "Raph Comic"
        self.url = "https://raphcomic.com"

    def fetch_comic(self):
        return self.findImgByClass(self.makeBanner(self.title), self.url, ["img-fluid", "lazyload"], True, True)

