import comic_collection

class Swordscomic(comic_collection.Comic):
    """Bla bla bla
    """
    def __init__(self):
        super().__init__()
        self.title = "Swords Comic"
        self.url = "https://swordscomic.com"

    def fetch_comic(self):
        IMG=self.findDivByClass(self.makeBanner(self.title), self.url, "page-image-wrapper", True)
        return IMG
