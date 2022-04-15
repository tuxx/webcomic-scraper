import comic_collection

class PoorlyDrawnLines(comic_collection.Comic):
    """Bla bla bla
    """
    def __init__(self):
        super().__init__()
        self.title = "Poorly Drawn Lines"
        self.url = "https://poorlydrawnlines.com"

    def fetch_comic(self):
        soup = self.getSoupContent(self.url)
        images = soup.findAll('img')
        for image in images:
            try:
                if image['class'][0].startswith("wp-image"):
                    content = f"<a href='{self.url}'><img src='{image['src']}' /></a>"
                    return self.makeBanner(self.title) + content + self.HR
            except:
                pass
