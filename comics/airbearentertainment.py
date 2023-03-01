import comic_collection
import requests

class AirBearEntertainment(comic_collection.Comic):
    """Bla bla bla
    """
    def __init__(self):
        super().__init__()
        self.title = "Air Bear Entertainment"
        self.url = "http://airbearentertainment.com/"

    def fetch_comic(self):
        soup = self.getSoupContent(self.url)
        images = soup.findAll('img')
        for image in images:
            try:
                if "comic_stripped_live_images" in image['src']:
                    imgurl = f"{self.url}{image['src']}"
                    r = requests.get(imgurl, allow_redirects=True)
                    open(f"{self.OUTPUT_DIR}/abe.jpg", 'wb').write(r.content)
                    content = f"<a href='{self.url}'><img src='/abe.jpg' /></a>"
                    print(content)
                    return self.makeBanner(self.title) + content + self.HR
            except:
                pass
