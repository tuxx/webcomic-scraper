import comic_collection
import bs4

class LoadingArtist(comic_collection.Comic):
    """ Bla bla bla
    """
    def __init__(self):
        super().__init__()
        self.title = "Loading Artist"
        self.url = "https://loadingartist.com/index.xml"

    def fetch_comic(self):
        comic = self.getComicByRss(self.url, "aap")
        soup = bs4.BeautifulSoup(comic, features="html5lib")
        images = soup.findAll('img')
        return self.makeBanner(self.title) + str(images[0]) + self.HR
