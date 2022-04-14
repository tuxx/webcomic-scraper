import inspect
import os
import pkgutil
import bs4
import urllib
import requests
import feedparser


class Comic(object):
    def __init__(self):
        self.description = 'UNKNOWN'
        self.HR="<hr style='width:70%;text-align:left;margin-left:0'>"
        self.index="""
        <div id="index"></div>
        <h1>Index</h1>
        <ul>
        """
        self.OUTPUT_DIR="/var/www/comics"

    def getSoupContent(self, url):
        req = urllib.request.Request(
            url,
            data=None,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'
            }
        )
        url_contents = urllib.request.urlopen(req).read()
        return bs4.BeautifulSoup(url_contents, features="html5lib")

    def makeBanner(self, title):
        anchor=title.replace(" ", "").lower()
        self.index = self.index + f"<li><a href='#{anchor}'>{title}</a></li>\n"
        return f"""
    <div id="{anchor}"></div>
    <h1><a href="#{anchor}">{title}</a> 
    <a href="#index">&#x21E7;</a></h1>
    """
    def getComicByRss(self, feedurl, getitem):
        d = feedparser.parse(feedurl)
        content = d['entries'][0]['content'][0]['value']
        return content

    def findImgByClass(self, BANNER, URL, CLASS, PREPEND_URL=False, DATASRC=False):
        soup = self.getSoupContent(URL)
        images = soup.findAll('img')
        for image in images:
            try:
                if image['class'] == CLASS:
                    if PREPEND_URL and not DATASRC:
                        content = f"<a href='{URL}'><img src='{URL}/{image['src']}' /></a>"
                    elif PREPEND_URL and DATASRC:
                        content = f"<a href='{URL}'><img src='{URL}/{image['data-src']}' /></a>"
                    else:
                        if DATASRC:
                            content = f"<a href='{URL}'><img src='{image['data-src']}' /></a>"
                        else:
                            content = f"<a href='{URL}'><img src='{image['src']}' /></a>"
                    return BANNER + content + self.HR
            except:
                pass

    def findDivById(self, BANNER, URL, ID, PREPEND_URL=False):
        soup = self.getSoupContent(URL)
        div = soup.find("div", {"id": ID})
        div=str(div)
        if PREPEND_URL:
            content = f"<a href='{URL}'>{URL}/{div}</a>"
        else:
            content = f"<a href='{URL}'>{div}</a>"

        return BANNER + content + self.HR

    def findDivByClass(BANNER, URL, CLASS):
        soup = self.getSoupContent(URL)
        div = soup.find("div", {"class": CLASS})
        div=str(div)
        bs=bs4.BeautifulSoup(div, features="html5lib")
        img = bs.find("img")
        content = f"<a href='{URL}'><img src='{img['src']}'/></a>"

        return BANNER + content + self.HR

    def perform_operation(self, argument):
        """The method that we expect all comics to implement. This is the
        method that our framework will call
        """
        raise NotImplementedError


class ComicCollection(object):
    def __init__(self, comic_package):
        self.comic_package = comic_package
        self.reload_comics()


    def reload_comics(self):
        self.comics = []
        self.seen_paths = []
        print()
        print(f'Looking for comics under directory {self.comic_package}')
        self.walk_package(self.comic_package)


    def get_all_comics(self):
        ENDRESULT=""
        for comic in self.comics:
            print(comic.fetch_comic())

        return ENDRESULT

    def walk_package(self, package):
        imported_package = __import__(package, fromlist=['blah'])

        for _, comicname, ispkg in pkgutil.iter_modules(imported_package.__path__, imported_package.__name__ + '.'):
            if not ispkg:
                comic_module = __import__(comicname, fromlist=['blah'])
                clsmembers = inspect.getmembers(comic_module, inspect.isclass)
                for (_, c) in clsmembers:
                    # Only add classes that are a sub class of Comic, but NOT Comic itself
                    if issubclass(c, Comic) and (c is not Comic):
                        print(f'    Found comic class: {c.__module__}.{c.__name__}')
                        self.comics.append(c())


        # Now that we have looked at all the modules in the current package, start looking
        # recursively for additional modules in sub packages
        all_current_paths = []
        if isinstance(imported_package.__path__, str):
            all_current_paths.append(imported_package.__path__)
        else:
            all_current_paths.extend([x for x in imported_package.__path__])

        for pkg_path in all_current_paths:
            if pkg_path not in self.seen_paths:
                self.seen_paths.append(pkg_path)

                # Get all sub directory of the current package path directory
                child_pkgs = [p for p in os.listdir(pkg_path) if os.path.isdir(os.path.join(pkg_path, p))]

                # For each sub directory, apply the walk_package method recursively
                for child_pkg in child_pkgs:
                    self.walk_package(package + '.' + child_pkg)

