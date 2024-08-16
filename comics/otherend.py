import comic_collection
import requests

class TheOtherEnd(comic_collection.Comic):
    """Bla bla bla
    """
    def __init__(self):
        super().__init__()
        self.title = "The Other End"
        self.url = "https://kohney.com/"

    def fetch_comic(self):
        soup = self.getSoupContent(self.url)
        images = soup.findAll('img')
        for image in images:
            try:
                if self.year in image['src']:
                    content = f"<a href='{self.url}'><img src='{image['src']}' /></a>"
                    return self.makeBanner(self.title) + content + self.HR
            except:
                pass
