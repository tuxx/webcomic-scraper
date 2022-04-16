import comic_collection

class CtrlAltDel(comic_collection.Comic):
    """Bla bla bla
    """
    def __init__(self):
        super().__init__()
        self.title = "Ctrl+Alt+Del"
        self.url = "https://cad-comic.com"

    def fetch_comic(self):
        return self.findImgByClass(self.makeBanner(self.title), self.url, ["comic-display"])

