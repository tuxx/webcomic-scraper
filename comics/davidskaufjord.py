import comic_collection
import instaloader
import requests

class Davidskaufjord(comic_collection.Comic):
    """Bla bla bla
    """
    def __init__(self):
        super().__init__()
        self.title = "David Skaufjord"
        self.url = "https://www.instagram.com/davidskaufjord"
        self.instagram_username = "davidskaufjord"

    def fetch_comic(self):
        loader = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(loader.context, self.instagram_username)
        latest_post = next(profile.get_posts())

        # Check if the latest post is a carousel (multiple images)
        if latest_post.typename == 'GraphSidecar':
          # If it's a carousel, iterate through all media in the post
          last_image_url = latest_post.get_sidecar_nodes()[-1].display_url
        else:
          # If it's a single image/video post, just get the single URL
          image_urls = [latest_post.url]

        if last_image_url:
              r = requests.get(last_image_url, allow_redirects=True)
              open(f"{self.OUTPUT_DIR}/david.jpg", 'wb').write(r.content)
              content = f"<a href='{self.url}'><img src='/david.jpg' /></a>"
        else:
            content = f"<a href='{self.url}'>"
            # Print all the image URLs
            for idx, url in enumerate(image_urls, start=1):
              r = requests.get(url, allow_redirects=True)
              open(f"{self.OUTPUT_DIR}/david{idx}.jpg", 'wb').write(r.content)
              content += f"<img src='/david{idx}.jpg' />"
            content += f"</a>"

        return self.makeBanner(self.title) + content + self.HR
