import comic_collection

class FokkeSukke(comic_collection.Comic):
    """Bla bla bla
    """
    def __init__(self):
        super().__init__()
        self.title = "Fokke & Sukke"
        self.url = "https://www.nrc.nl/fokke-sukke/"

    def fetch_comic(self):
        soup = self.getSoupContent(self.url)
        images = soup.findAll('picture')
        for image in images:
            return self.makeBanner(self.title) + str(image) + self.HR
