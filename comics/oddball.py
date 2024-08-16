import comic_collection
import bs4

class Oddball(comic_collection.Comic):
    """This comic sometimes has some kind of promotion for a book on the frontpage.
       So if the first page fails to get a comic, we get /page/2
    """
    def __init__(self):
        super().__init__()
        self.title = "Oddball"
        self.url = "https://sarahcandersen.com"

    def get_oddball(self, url):
        soup = self.getSoupContent(url)
        links = soup.findAll('img')
        i=0
        for link in links:
            if i < 2:
                i=i+1
                continue
            if i == 2:
                try:
                    content = f"<a href='{url}'>{link}</a>"
                    return self.makeBanner(self.title) + content + self.HR
                except:
                    pass

    def fetch_comic(self):
        result=self.get_oddball(self.url)
        return result
