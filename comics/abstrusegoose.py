import comic_collection

class AbstruseGoose(comic_collection.Comic):
    """Bla bla bla
    """
    def __init__(self):
        super().__init__()
        self.title = "Abstruse Goose"
        self.url = "http://abstrusegoose.com"

    def fetch_comic(self):
        soup = self.getSoupContent(self.url)
        images = soup.findAll('img')
        for image in images:
            try:
                if "strips" in image['src']:
                    content = f"<a href='{self.url}'><img src='{image['src']}' /></a>"
                    return self.makeBanner(self.title) + content + self.HR
            except:
                pass
