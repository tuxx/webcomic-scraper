import comic_collection

class BonusContext(comic_collection.Comic):
    """Bla bla bla
    """
    def __init__(self):
        super().__init__()
        self.title = "Bonus Context"
        self.url = "https://bonuscontext.com"

    def fetch_comic(self):
        soup = self.getSoupContent(self.url)
        images = soup.findAll('img')
        for image in images:
            try:
                if image['src'].startswith("/comics/"):
                    content = f"<a href='{self.url}'><img src='{self.url}{image['src']}' /></a>"
                    return self.makeBanner(self.title) + content + self.HR
            except:
                pass
