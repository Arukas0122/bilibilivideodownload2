import json
import re
import time
import requests
import os

headers = {
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER',
           "Referer": "https://www.bilibili.com/"}

CurrentPath = os.getcwd()

#pyinstaller -F -i tubiao.ico wenjian.py 图标打包命令参考

def send_request(url):
    # 请求数据
    response = requests.get(url=url, headers=headers)
    return response


def uid_download():
    uid = input("输入用户的uid：")
    yema = int(input("输入视频总页数："))
    for j in range(1, yema + 1):
        html = 'https://api.bilibili.com/x/space/arc/search?mid=%s&ps=30&tid=0&pn=%s&keyword=&order=pubdate&jsonp=jsonp' % (
            uid, j)
        html_data = send_request(html).text
        for i in range(0, 30):
            bv_data = json.loads(html_data)
            bv = bv_data['data']['list']['vlist'][i]['bvid']
            video_html = 'https://www.bilibili.com/video/%s' % (bv)
            video_html_data = send_request(video_html).text
            p = re.findall('<span class="cur-page">(.*?)</span>', video_html_data)
            if p != []:
                pv = p[0]
                vn = int(pv.split('/')[1].split(')')[0])
                print('该BV号共有%s个视频' % (vn))
            else:
                print("该BV号只有一个视频")
            shipinxiazai = r'you-get --playlist -c  {dizhi}\cookies.sqlite ' + video_html
            shipinxiazai1=shipinxiazai.format(dizhi=CurrentPath)
            #print(shipinxiazai1)
            os.system(shipinxiazai1)
    time.sleep(1)


def bv_download():
    bvnumber = input("输入BV号：")
    video_html = 'https://www.bilibili.com/video/%s' % (bvnumber)
    video_html_data = send_request(video_html).text
    p = re.findall('<span class="cur-page">(.*?)</span>', video_html_data)
    if p != []:
        pv = p[0]
        vn = int(pv.split('/')[1].split(')')[0])
        print('共有%s个视频' % (vn))
    else:
        print("该BV号只有一个视频")
    shipinxiazai = r'you-get --playlist -c  {dizhi}\cookies.sqlite ' + video_html
    shipinxiazai1 = shipinxiazai.format(dizhi=CurrentPath)
    os.system(shipinxiazai1)
    time.sleep(1)


def download():
    lianjie = input("请输入视频链接：")
    shipinxiazai = r'you-get --playlist -c  {dizhi}\cookies.sqlite ' + lianjie
    shipinxiazai1 = shipinxiazai.format(dizhi=CurrentPath)
    os.system(shipinxiazai1)
    time.sleep(1)


def showInfo():
    print("-" * 40)
    print("    猪猪视频下载  v1.24 2021.7.28")
    print("1.根据用户UID与视频页数下载")
    print("2.根据BV号下载")
    print("3.根据链接解析下载")
    print("4.退出系统\n")
    print("124版更新日志\n"
          "@该版本需要搭配python的you-get包进行使用\n"
          "@cookie同目录运行\n"
          "@移除了him")
    print('-' * 40)


while True:
    showInfo()
    key = int(input("输入所需的功能："))
    if key == 1:
        uid_download()
    elif key == 2:
        bv_download()
    elif key == 3:
        download()
    elif key == 4:
        break
    else:
        print("输入有误！请重新输入。")
