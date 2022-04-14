import comic_collection
import requests

class LunarBaboon(comic_collection.Comic):
    """This one does a referer check when including the image in our html. 
       So we download the image and write it to lb.jpg in the web folder.
    """
    def __init__(self):
        super().__init__()
        self.title = "Lunar Baboon"
        self.url = "http://lunarbaboon.com"

    def fetch_comic(self):
        soup = self.getSoupContent(self.url)
        images = soup.findAll('img')
        for image in images:
            try:
                if "/storage/" in image['src']:
                    r = requests.get(self.url+image['src'], allow_redirects=True)
                    open(f"{self.OUTPUT_DIR}/lb.jpg", "wb").write(r.content)
                    content = f"<a href='{self.url}'><img src='/lb.jpg' /></a>"
                    return self.makeBanner(self.title) + content + self.HR
            except:
                pass
