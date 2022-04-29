import comic_collection

class Conspiracyofbirds(comic_collection.Comic):
    """Bla bla bla
    """
    def __init__(self):
        super().__init__()
        self.title = "Conspiracy of Birds"
        self.url = "https://www.conspiracyofbirds.com/"

    def fetch_comic(self):
        IMG=self.findDivByClass(self.makeBanner(self.title), self.url, "separator")
        return IMG
