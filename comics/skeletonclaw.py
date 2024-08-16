import comic_collection

class SkeletonClaw(comic_collection.Comic):
    """Bla bla bla
    """
    def __init__(self):
        super().__init__()
        self.title = "Skeleton Claw"
        self.url = "https://www.skeletonclaw.com/"

    def fetch_comic(self):
        IMG=self.findDivByClass(self.makeBanner(self.title), self.url, "photo-wrapper-inner")
        return IMG
