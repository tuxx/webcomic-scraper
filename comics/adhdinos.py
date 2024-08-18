import comic_collection
import instaloader
import requests

class Adhdinos(comic_collection.Comic):
    """Bla bla bla
    """
    def __init__(self):
        super().__init__()
        self.title = "adhdinos"
        self.url = "https://www.instagram.com/adhdinos"
        self.instagram_username = "adhdinos"

    def fetch_comic(self):
        loader = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(loader.context, self.instagram_username)
        latest_post = next(profile.get_posts())
        r = requests.get(latest_post.url, allow_redirects=True)
        open(f"{self.OUTPUT_DIR}/adhdinos.jpg", 'wb').write(r.content)
        content = f'<a href="{self.url}"><img src="/adhdinos.jpg" /></a>'
        return self.makeBanner(self.title) + content + self.HR
