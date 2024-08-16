import comic_collection
import requests

class Sigmund(comic_collection.Comic):
    """This one does a referer check when including the image in our html. 
       So we download the image and write it to lb.jpg in the web folder.
    """
    def __init__(self):
        super().__init__()
        self.title = "Sigmund"
        self.url = "https://sigmund.nl"

    def fetch_comic(self):
        soup = self.getSoupContent(self.url)
        images = soup.findAll('img')
        for image in images:
            try:
                if image['id'] == "strook":
                    r = requests.get(image['src'], allow_redirects=True)
                    open(f"{self.OUTPUT_DIR}/sigmund.gif", "wb").write(r.content)
                    content = f"<a href='{self.url}'><img src='/sigmund.gif' /></a>"
                    return self.makeBanner(self.title) + content + self.HR
            except:
                pass
