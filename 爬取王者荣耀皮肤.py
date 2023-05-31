# 发送请求
import requests
import os


"""访问英雄主页"""
head={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52"
}
hero_list_url="https://pvp.qq.com/web201605/js/herolist.json"
hero_list_resp=requests.get(hero_list_url,headers=head)
print(hero_list_resp.json())
for h in hero_list_resp.json():
    ename=h.get("ename")
    cname=h.get("cname")
    skin_name=h.get("skin_name")
    skin_name=skin_name.split("|")


    if not os.path.exists(cname):
        os.mkdir(cname)

    # 发送请求
    url=f"https://pvp.qq.com/web201605/herodetail/{ename}.shtml"
    head={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52"
    }
    hero_resp=requests.get(url,headers=head)
    hero_resp.encoding="gbk"

    # 接收服务器响应的图片(皮肤)
    # 保存图片(皮肤)
    for i,n in enumerate(skin_name):
        i+=1
        resp=requests.get(f"http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{ename}/{ename}-bigskin-{i}.jpg",headers=head)

        with open(f"{cname}\{n}.jpg","wb+") as f:
            f.write(resp.content)
            print(f"已下载{n} 的皮肤")
    print("xxxxx")