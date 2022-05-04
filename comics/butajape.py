import comic_collection

class ButAJape(comic_collection.Comic):
    """Bla bla bla
    """
    def __init__(self):
        super().__init__()
        self.title = "But a Jape"
        self.url = "https://butajape.com/"

    def fetch_comic(self):
        IMG=self.findDivByClass(self.makeBanner(self.title), self.url, "widget widget_mgsisk_webcomic_collection_widget_webcomicmedia")
        return IMG
