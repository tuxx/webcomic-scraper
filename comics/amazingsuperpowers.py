import comic_collection

class AmazingSuperPowers(comic_collection.Comic):
    """Bla bla bla
    """
    def __init__(self):
        super().__init__()
        self.title = "Amazing Super Powers"
        self.url = "http://amazingsuperpowers.com"

    def fetch_comic(self):
        return self.findDivById(self.makeBanner(self.title), self.url, "comic-1")
