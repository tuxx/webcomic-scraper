import comic_collection

class Buni(comic_collection.Comic):
    """Bla bla bla
    """
    def __init__(self):
        super().__init__()
        self.title = "Buni"
        self.url = "https://www.bunicomic.com"

    def fetch_comic(self):
        return self.findDivById(self.makeBanner(self.title), self.url, "comic")
