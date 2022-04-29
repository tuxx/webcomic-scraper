import comic_collection

class Scarecrowbar(comic_collection.Comic):
    """Bla bla bla
    """
    def __init__(self):
        super().__init__()
        self.title = "Scarecrowbar"
        self.url = "https://scarecrow.bar"

    def fetch_comic(self):
        IMG=self.findDivByClass(self.makeBanner(self.title), self.url, "widget widget_mgsisk_webcomic_collection_widget_webcomicmedia")
        return IMG
