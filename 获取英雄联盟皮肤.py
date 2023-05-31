import os.path
import json

import requests

head = {
    #每个人的代理都不一样，如果需要更改，请在浏览器-》F12->网络->标头-》user-agent里面获取
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52"
}

hero_url = "https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?ts=2791949"
hero_url_resp = requests.get(hero_url, headers=head)
for hero in hero_url_resp.json().get("hero"):
    heroId = hero.get("heroId")
    name1 = hero.get("name")
    if not os.path.exists(name1):
        os.mkdir(name1)

    skin_url = f"https://game.gtimg.cn/images/lol/act/img/js/hero/{heroId}.js?ts=2791955"
    skin_url_resp = requests.get(skin_url, headers=head)
    for skin in skin_url_resp.json().get("skins"):
        skinId = skin.get("skinId")
        name2 = skin.get("name")

        url = f"https://game.gtimg.cn/images/lol/act/img/skin/big{skinId}.jpg"
        url_resp = requests.get(url, headers=head)
        with open(f"{name1}/{name2}.jpg", 'wb+') as f:
            f.write(url_resp.content)
            print(f"已下载{name2}的皮肤")

    print("xxxxxxxxxxxxxx")
