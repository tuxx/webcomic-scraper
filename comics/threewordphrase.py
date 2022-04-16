import comic_collection
import requests

class ThreeWordPhrase(comic_collection.Comic):
    """Bla bla bla
    """
    def __init__(self):
        super().__init__()
        self.title = "Three Word Phrase"
        self.url = "http://threewordphrase.com"

    def fetch_comic(self):
        soup = self.getSoupContent(self.url)
        images = soup.findAll('img')
        for image in images:
            if int(image['width']) >= 900:
                imgurl = f"{self.url}/{image['src']}"
                r = requests.get(imgurl, allow_redirects=True)
                open(f"{self.OUTPUT_DIR}/twp.gif", 'wb').write(r.content)
                content = f"<a href='{self.url}'><img src='/twp.gif' /></a>"
                return self.makeBanner(self.title) + content + self.HR
