import comic_collection

class Wumo(comic_collection.Comic):
    """Bla bla bla
    """
    def __init__(self):
        super().__init__()
        self.title = "Wumo"
        self.url = "https://wumo.com/wumo"

    def fetch_comic(self):
        IMG=self.findDivByClass(self.makeBanner(self.title), self.url, "box-content")
        IMG = IMG.replace("/img", "https://wumo.com/img")
        return IMG
