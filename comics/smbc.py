import comic_collection

class SMBC(comic_collection.Comic):
    """Bla bla bla
    """
    def __init__(self):
        super().__init__()
        self.title = "SMBC"
        self.url = "http://smbc-comics.com"

    def fetch_comic(self):
        soup = self.getSoupContent(self.url)
        div = soup.find("div", {"id": "cc-comicbody"})
        sep = '/>'
        div = str(div).split(sep, 1)[0]
        content = f"<a href='{self.url}'>{div}/></a>"
        content = content.replace('<div id="cc-comicbody">', "")
        return self.makeBanner(self.title) + content + self.HR
