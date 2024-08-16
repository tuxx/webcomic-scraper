import comic_collection
import requests

class DaveContra(comic_collection.Comic):
    """Bla bla bla
    """
    def __init__(self):
        super().__init__()
        self.title = "Dave Contra"
        self.url = "https://davecontra.com"

    def fetch_comic(self):
        IMG=self.findDivByClass(self.makeBanner(self.title), self.url, "summary-thumbnail-outer-container")
        return IMG
