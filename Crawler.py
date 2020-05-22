import requests
from bs4 import BeautifulSoup
import time

SiteEndings = ['.com', '.net', '.org', '.io', '.uk',
 '.in', '.us', '.biz', '.edu', '.eu', '.co']

def ReadLines():
    with open("linklist.txt", "r") as f:
        Data = f.readlines()
    return Data
skip = False
while True:
    try:
        with open("linklist.txt", "r") as f:
            AllLinks = f.readlines()

        for i in AllLinks:
            AllLinks[AllLinks.index(i)] = i.strip("\n")

        for i in AllLinks:
            if skip == True:
                Data = ReadLines()
                with open("linklist.txt", "r+", encoding="utf-8") as f:
                    try:
                        Data.remove(i + "\n")
                    except:
                        Data.remove(i)
                    for i in Data:
                        f.write(i)
                skip = False
                continue
            SeedLink = i
            response = requests.get(i).text
            soup = BeautifulSoup(response, "html.parser")
            for i in soup.findAll('a'):
                link = i.get('href')
                if link != None:
                    if link.startswith("https://") and link not in AllLinks:
                        print(link)
                        with open("linklist.txt", "a+", encoding="utf-8") as f:
                            f.write(link + "\n")
#                            Data = ReadLines()
#                            f.truncate()
#                            Data.append(link + "\n")
#                            try:
#                                Data.remove(SeedLink + "\n")
#                            except:
#                                try:
#                                    Data.remove(SeedLink)
#                                except:
#                                    pass
#                            for i in Data:
#                                f.write(i)

                    elif link.startswith("http://") and link not in AllLinks:
                        print(link)
#                        Data = ReadLines()
                        with open("linklist.txt", "a+", encoding="utf-8") as f:
                            f.write(link + "\n")
#                            f.truncate()
#                            Data.append(link + "\n")
#                            try:
#                                Data.remove(SeedLink + "\n")
#                            except:
#                                try:
#                                    Data.remove(SeedLink)
#                                except:
#                                    pass
#                            for i in Data:
#                                f.write(i)

                    elif link.startswith("/") and link not in AllLinks:
                        print(link)
                        for i in SiteEndings:
                            if i in SeedLink:
                                LinkBase = SeedLink.split(i)[0] + i

                        
                        link = LinkBase + link
#                        Data = ReadLines()
                        with open("linklist.txt", "a+", encoding="utf-8") as f:
                            f.write(link + "\n")
#                            f.truncate()
#                            Data.append(link + "\n")
#                            try:
#                                Data.remove(SeedLink + "\n")
#                            except:
#                                try:
#                                    Data.remove(SeedLink)
#                                except:
#                                    pass
#                            for i in Data:
#                                f.write(i)

    except Exception as e:
        print(f"error : {e}")
        skip = True
        AllLinks.remove(SeedLink)
        pass