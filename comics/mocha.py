import comic_collection
import requests

class Mocha(comic_collection.Comic):
    """Bla bla bla
    """
    def __init__(self):
        super().__init__()
        self.title = "Mocha The Samoyed"
        self.url = "https://www.mochathesamoyed.com"

    def fetch_comic(self):
        soup = self.getSoupContent(self.url)
        images = soup.findAll('img')
        i=0
        for image in images:
            if i < 3:
                i=i+1
                continue
            print(image)
            try:
                imgurl = f"{image['data-image']}"
            except:
                imgurl = f"{image['src']}"
            content = f"<a href='{self.url}'><img src='{imgurl}' /></a>"
            return self.makeBanner(self.title) + content + self.HR
