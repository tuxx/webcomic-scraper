import comic_collection

class TheyCanTalk(comic_collection.Comic):
    """Bla bla bla
    """
    def __init__(self):
        super().__init__()
        self.title = "They Can Talk"
        self.url = "https://theycantalk.com"

    def fetch_comic(self):
        soup = self.getSoupContent(self.url)
        images = soup.findAll('img')
        for image in images:
            content = f"<a href='{self.url}'><img src='{image['src']}' /></a>"
            return self.makeBanner(self.title) + content + self.HR
