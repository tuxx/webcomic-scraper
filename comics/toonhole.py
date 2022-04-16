import comic_collection

class Toonhole(comic_collection.Comic):
    """Bla bla bla
    """
    def __init__(self):
        super().__init__()
        self.title = "Toonhole"
        self.url = "https://toonhole.com/"

    def fetch_comic(self):
        soup = self.getSoupContent(self.url)
        images = soup.findAll('img')
        for image in images:
            if "attachment-post-thumbnail" in image['class']:
                if self.year in image['src']:
                    content = f"<a href='{self.url}'><img src='{image['src']}' /></a>"
                    return self.makeBanner(self.title) + content + self.HR
