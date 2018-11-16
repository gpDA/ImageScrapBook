# Get example images to test thumbnailing
import requests
import json
import urllib
import os
import re
import shutil


# Use Wikimedia Commons
galleryurl = "https://commons.wikimedia.org/w/api.php?action=query&titles=Commons:Featured_pictures%2FFood_and_drink&format=json&prop=images&imlimit=100"
r = requests.get(galleryurl)

imagenames = []
for imageinfo in r.json()["query"]["pages"]["353686"]["images"]:
    title = imageinfo["title"]
    if title.split(".")[-1] != "svg":
        imagenames.append(imageinfo["title"])

imglist = "|".join(imagenames[:50])
imglist = urllib.parse.quote(imglist)
# list of image urls
urlurl = "https://commons.wikimedia.org/w/api.php?action=query&format=json&prop=imageinfo&titles={}&iiprop=url&iiurlwidth=-1".format(imglist)

urlindex = requests.get(urlurl).json()
pages = urlindex["query"]["pages"]
urls = []
for pageid in pages:
    urls.append(pages[pageid]["imageinfo"][0]["url"])


if not os.path.exists("imgsrc"):
    os.makedirs("imgsrc")
print(len(urls))
for url in urls:
    print("Getting %s" % (url,))
    r = requests.get(url)
    if r.status_code == 200:
        # lets get the filename
        fname = url.split("/")[-1]
        with open("imgsrc/%s" % (fname,), "wb") as f:
            f.write(r.content)
