import urllib3
from bs4 import BeautifulSoup

def get_weapons():
    # change to whatever your url is
    url = "https://roll20.net/compendium/dnd5e/Weapons#toc_15"

    http = urllib3.PoolManager()

    response = http.request('GET', url)
    soup = BeautifulSoup(response.data, 'lxml')

    tbody = soup.find_all('tbody')

    decorator = 35

    # Simple weapons
    print("-" * decorator + "SIMPLE WEAPONS" + "-" * decorator)
    print("WEAPON" + " " * (18 - len("WEAPON")), end="\t")
    print("COST", end="\t")
    print("DAMAGE" + '\t\t\t' + "WEIGHT", end="\t\t")
    print("PROPERTIES")
    for tr in tbody[0].find_all('tr'):
        item = tr.find_all("td")
        # print(str(item[0].string) + str(" " * 30 - len(item[0].string)) + str(item[1].string) + '\t' + str(item[2].string) + '\t' + str(item[3].string))
        print(str(item[0].text.strip()) + " " * (18 - len(item[0].text)), end="\t")
        print(str(item[1].string), end="\t")
        print(str(item[2].string) + '\t\t' + str(item[3].string), end="\t\t")
        print(str(item[4].string))


    # Simple Ranged Weapons
    print("-" * decorator + "SIMPLE RANGED WEAPONS" + "-" * decorator)
    print("WEAPON" + " " * (18 - len("WEAPON")), end="\t")
    print("COST", end="\t")
    print("DAMAGE" + '\t\t\t' + "WEIGHT", end="\t\t")
    print("PROPERTIES")
    for tr in tbody[1].find_all('tr'):
        item = tr.find_all("td")
        # print(str(item[0].string) + str(" " * 30 - len(item[0].string)) + str(item[1].string) + '\t' + str(item[2].string) + '\t' + str(item[3].string))
        print(str(item[0].text.strip()) + " " * (18 - len(item[0].text)), end="\t")
        print(str(item[1].string), end="\t")
        print(str(item[2].string) + '\t\t' + str(item[3].string), end="\t\t")
        print(str(item[4].string))

    # Simple Ranged Weapons
    print("-" * decorator + "MARTIAL WEAPONS" + "-" * decorator)
    print("WEAPON" + " " * (18 - len("WEAPON")), end="\t")
    print("COST", end="\t")
    print("DAMAGE" + '\t\t\t' + "WEIGHT", end="\t\t")
    print("PROPERTIES")
    for tr in tbody[2].find_all('tr'):
        item = tr.find_all("td")
        # print(str(item[0].string) + str(" " * 30 - len(item[0].string)) + str(item[1].string) + '\t' + str(item[2].string) + '\t' + str(item[3].string))
        print(str(item[0].text.strip()) + " " * (18 - len(item[0].text)), end="\t")
        print(str(item[1].string), end="\t")
        print(str(item[2].string) + '\t\t' + str(item[3].string), end="\t\t")
        print(str(item[4].string))


    # Simple Ranged Weapons
    print("-" * decorator + "MARTIAL RANGED WEAPONS" + "-" * decorator)
    print("WEAPON" + " " * (18 - len("WEAPON")), end="\t")
    print("COST", end="\t")
    print("DAMAGE" + '\t\t\t' + "WEIGHT", end="\t\t")
    print("PROPERTIES")
    for tr in tbody[3].find_all('tr'):
        item = tr.find_all("td")
        # print(str(item[0].string) + str(" " * 30 - len(item[0].string)) + str(item[1].string) + '\t' + str(item[2].string) + '\t' + str(item[3].string))
        print(str(item[0].text.strip()) + " " * (18 - len(item[0].text)), end="\t")
        print(str(item[1].string), end="\t")
        print(str(item[2].string) + '\t\t' + str(item[3].string), end="\t\t")
        print(str(item[4].string))
