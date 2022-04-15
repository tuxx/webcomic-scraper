import comic_collection

class SavageChickens(comic_collection.Comic):
    """Bla bla bla
    """
    def __init__(self):
        super().__init__()
        self.title = "Savage Chickens"
        self.url = "https://www.savagechickens.com/"

    def fetch_comic(self):
        soup = self.getSoupContent(self.url)
        images = soup.findAll('img')
        DONE=0
        for image in images:
            try:
                if "uploads" in image['src']:
                    if image['alt'] != "":
                        if DONE == 0: #Skip the first uploads images with no alt text
                            DONE=1
                            continue

                        if DONE == 1: # Grab 2nd image, we gots the comic boizzz
                            content = f"<a href='{self.url}'><img src='{image['src']}' /></a>"
                            return self.makeBanner(self.title) + content + self.HR
            except:
                pass

