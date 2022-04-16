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
        self.url2 = f"{self.url}/page/2"

    def get_oddball(self, url):
        soup = self.getSoupContent(url)
        links = soup.findAll('a')
        for link in links:
            try:
                if link['href'][-3:] == "jpg":
                    content = f"<a href='{url}'><img src='{link['href']}' /></a>"
                    return self.makeBanner(self.title) + content + self.HR
            except:
                pass

    def fetch_comic(self):
        result=self.get_oddball(self.url)
        if result is None:
            result=self.get_oddball(self.url2)
        return result
