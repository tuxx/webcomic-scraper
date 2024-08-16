import comic_collection

class ComicLicious(comic_collection.Comic):
    """Bla bla bla
    """
    def __init__(self):
        super().__init__()
        self.title = "Comic Licious"
        self.url = "https://comicskingdom.com/comiclicious/"

    def fetch_comic(self):
        IMG=self.findDivById(self.makeBanner(self.title), self.url, "theComicImage")
        return IMG
