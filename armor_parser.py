import urllib3
from bs4 import BeautifulSoup

decorator = 40


def get_armor():
    # change to whatever your url is
    url = "https://roll20.net/compendium/dnd5e/Armor#content"

    http = urllib3.PoolManager()

    response = http.request('GET', url)
    soup = BeautifulSoup(response.data, 'lxml')

    tbody = soup.find_all('tbody')

    # Simple weapons
    print("-" * decorator + "LIGHT ARMOR" + "-" * decorator)
    print_head()
    for tr in tbody[0].find_all('tr'):
        item = tr.find_all("td")
        # print(str(item[0].string) + str(" " * 30 - len(item[0].string)) + str(item[1].string) + '\t' + str(item[2].string) + '\t' + str(item[3].string))
        print(str(item[0].text.strip()) + " " *
              (18 - len(item[0].text)), end="\t")
        print(str(item[1].string) + " " *
              (15 - len(item[1].text)), end='\t')
        print(str(item[2].string) + " " *
              (30 - len(item[2].text)), end='\t')
        print(str(item[3].string), end="\t\t")
        print(str(item[4].string) + " " *
              (15 - len(item[4].text)), end='\t')
        print(str(item[5].string))

    # Simple Ranged Weapons
    print("-" * decorator + "MEDIUM ARMOR" + "-" * decorator)
    print_head()
    for tr in tbody[1].find_all('tr'):
        item = tr.find_all("td")
        # print(str(item[0].string) + str(" " * 30 - len(item[0].string)) + str(item[1].string) + '\t' + str(item[2].string) + '\t' + str(item[3].string))
        print(str(item[0].text.strip()) + " " *
              (18 - len(item[0].text)), end="\t")
        print(str(item[1].string) + " " *
              (15 - len(item[1].text)), end='\t')
        print(str(item[2].string) + " " *
              (30 - len(item[2].text)), end='\t')
        print(str(item[3].string), end="\t\t")
        print(str(item[4].string) + " " *
              (15 - len(item[4].text)), end='\t')
        print(str(item[5].string))

    # Simple Ranged Weapons
    print("-" * decorator + "HEAVY ARMOR" + "-" * decorator)
    print_head()
    for tr in tbody[2].find_all('tr'):
        item = tr.find_all("td")
        # print(str(item[0].string) + str(" " * 30 - len(item[0].string)) + str(item[1].string) + '\t' + str(item[2].string) + '\t' + str(item[3].string))
        print(str(item[0].text.strip()) + " " *
              (18 - len(item[0].text)), end="\t")
        print(str(item[1].string) + " " *
              (15 - len(item[1].text)), end='\t')
        print(str(item[2].string) + " " *
              (30 - len(item[2].text)), end='\t')
        print(str(item[3].string), end="\t\t")
        print(str(item[4].string) + " " *
              (15 - len(item[4].text)), end='\t')
        print(str(item[5].string))

    # Simple Ranged Weapons
    print("-" * decorator + "SHIELD" + "-" * decorator)
    print_head()
    for tr in tbody[3].find_all('tr'):
        item = tr.find_all("td")
        # print(str(item[0].string) + str(" " * 30 - len(item[0].string)) + str(item[1].string) + '\t' + str(item[2].string) + '\t' + str(item[3].string))
        print(str(item[0].text.strip()) + " " *
              (18 - len(item[0].text)), end="\t")
        print(str(item[1].string) + " " *
              (15 - len(item[1].text)), end='\t')
        print(str(item[2].string) + " " *
              (30 - len(item[2].text)), end='\t')
        print(str(item[3].string), end="\t\t")
        print(str(item[4].string) + " " *
              (15 - len(item[4].text)), end='\t')
        print(str(item[5].string))


def print_head():
    print("ARMOR" + " " * (18 - len("ARMOR")), end="\t")
    print("COST", end="\t\t")
    print("ARMOR CLASS", end='\t\t\t')
    print("STRENTH", end="\t\t")
    print("STEALTH", end="\t\t")
    print("WEIGHT")
