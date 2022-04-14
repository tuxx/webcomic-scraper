import comic_collection

class CyanideAndHappiness(comic_collection.Comic):
    """Bla bla bla
    """
    def __init__(self):
        super().__init__()
        self.title = "Cyanide & Happiness"
        self.url = "https://explosm.net/comics/latest"

    def fetch_comic(self):
        soup = self.getSoupContent(self.url)
        for div in soup.findAll('div', {'class':lambda x: x and x.startswith('MainComic__ComicImage')}):
            for image in div.findAll('img'):
                try:
                    content = f"<a href='{self.url}'><img src='{image['src']}' /></a>"
                    return self.makeBanner(self.title) + content + self.HR
                except:
                    pass
