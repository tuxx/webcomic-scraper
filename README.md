# Table of Contents
- [Description](#description)
- [Install](#install)
- [Todo](#todo)
  * [Work In Progress](#work-in-progress)
  * [Nice 2 haves](#nice-2-haves)
  * [Probably never gonna happen](#probably-never-gonna-happen)
  * [General life todo](#general-life-todo)
- [Toons to add](#toons-to-add)
  * [Instagram toons](#instagram-toons)

# Description
HTML scraping script that gets some online web comics and displays them on a single page, because i am lazy.

# Install
- Copy `web/` files to your webserver folder.
- edit `config.py` and set the correct webserver folder.
- `pip install -r requirements.txt`
- `python main.py`

# Todo

## Donezell Washington
- [x] Make all current comics as plugins in the comics/ directory 
- [x] Actually output HTML (currently it just prints the scraped html)
- [x] Discard old.py
- [x] Config parser so that `OUTPUT_FILE` and `OUTPUT_DIR` are not defined in 2 files.
- [x] Do not stop when one comic fails to scrape, just ignore that comic.
- [x] Make instagram scraper for instagram comics
  - [ ] Add the instagram scraping to [comic_collection.py](comic_collection.py) instead of [this](comics/adhdinos.py) and [that](comics/davidskaufjord.py)

## To be done
- [ ] Make it possible to scrape 1 comic for testing purposes
- [ ] Add index generator
- [ ] Check when a comic has been updated and display that (or put it on the top of the page, so you dont have to scroll so much)

## General life todo
- [x] Drink beer
- [x] Raise hell
- [x] Pet dogs

## Instagram toons

- ~~https://www.instagram.com/adhdinos/~~
- ~~https://instagram.com/davidskaufjord/~~
- https://www.instagram.com/theghostofaprilhill/
- https://www.instagram.com/nathanwpylestrangeplanet/
- https://www.instagram.com/thelifeofsharks/
- https://www.instagram.com/system32comics/
- https://www.instagram.com/club.cryptid/
