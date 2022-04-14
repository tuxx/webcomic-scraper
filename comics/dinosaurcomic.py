import comic_collection

class DinosaurComic(comic_collection.Comic):
    """Bla bla bla
    """
    def __init__(self):
        super().__init__()
        self.title = "Dinosaur Comic"
        self.url = "https://qwantz.com"

    def fetch_comic(self):
        return self.findImgByClass(self.makeBanner(self.title), self.url, ["comic"], True)
