from bs4 import BeautifulSoup as bs
import requests
import csv

link = requests.get("https://liquipedia.net/dota2/Portal:Statistics/Player_earnings")
root = bs(link.content, "html.parser")

flag_ls = [(element["alt"]) for element in root.find_all('img', alt= True) if element["alt"] != "" if element["alt"] != "Logo"]

print(len(flag_ls))

link = requests.get("https://liquipedia.net/dota2/Special:Ask/-5B-5BConcept:Player-20earnings-5D-5D/-3FHas-20name/-3FHas-20nationality/-3FHas-20earnings/-3FHas-20id/mainlabel%3D/limit%3D500/order%3Ddesc/sort%3Dhas-20earnings/offset%3D500/format%3Dtemplate/link%3Dnone/searchlabel%3D...-20further-20results/default%3DNo-20more-20players-20with-20earnings/template%3DPortal-20statistics-20player-20earnings-20table-200-2D100-2Frow/introtemplate%3DPortal-20statistics-20player-20earnings-20table-2Fintro/outrotemplate%3DPortal-20statistics-20player-20earnings-20table-2Foutro")
root = bs(link.content, "html.parser")

flag_ls.extend([(element["alt"]) for element in root.find_all('img', alt= True) if element["alt"] != "" if element["alt"] != "Logo"])

print(len(flag_ls))

link = requests.get("https://liquipedia.net/dota2/index.php?title=Special:Ask&limit=500&offset=1000&q=%5B%5BConcept%3APlayer+earnings%5D%5D&p=mainlabel%3D%2Fformat%3Dtemplate%2Flink%3Dnone%2Fsearchlabel%3D...-20further-20results%2Fdefault%3DNo-20more-20players-20with-20earnings%2Ftemplate%3DPortal-20statistics-20player-20earnings-20table-200-2D100-2Frow%2Fintrotemplate%3DPortal-20statistics-20player-20earnings-20table-2Fintro%2Foutrotemplate%3DPortal-20statistics-20player-20earnings-20table-2Foutro&po=%3FHas+name%0A%3FHas+nationality%0A%3FHas+earnings%0A%3FHas+id%0A&sort=has+earnings&order=desc&eq=no#search")
root = bs(link.content, "html.parser")

flag_ls.extend([(element["alt"]) for element in root.find_all('img', alt= True) if element["alt"] != "" if element["alt"] != "Logo"])

print(len(flag_ls))

with open("flags.csv", "w", encoding="UTF8", newline="") as f:
    writer = csv.writer(f)

    for name in flag_ls:
        writer.writerow([name])

