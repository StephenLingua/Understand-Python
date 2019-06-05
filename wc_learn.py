# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sk_learn
   Description： 学习 word cloud
   Author :       stephen
   date：          2019/6/4
-------------------------------------------------
   Change Activity:
                   2019/6/4:
-------------------------------------------------
"""
from lxml import etree, html
import requests
import jieba
from wordcloud import WordCloud
import json
import os

ci_save_name = 'ci.json'
ci_save_path = os.path.join(os.path.abspath('.'), ci_save_name)


def get_songci():
    if os.path.exists(ci_save_path):
        return load_ci()
    else:
        ci_data_list = []
        for ci_url in get_ci_urls():
            print('get url {}'.format(ci_url))
            songci_data = requests.get(url=ci_url).json()
            print(songci_data)
            ci_data_list.extend(songci_data)
        dump_ci(ci_data_list)
        return ci_data_list


def dump_ci(ci_data):
    with open(file=ci_save_path, mode='w') as f:
        json.dump(obj=ci_data, fp=f, indent=2)


def load_ci():
    with open(file=ci_save_path, mode='r') as f:
        ci_data = json.load(f)
    return ci_data


def get_full_url(sub_url):
    usercontent_domain = 'https://raw.githubusercontent.com'
    return usercontent_domain + sub_url


def get_ci_urls():
    songci_url = 'https://github.com/chinese-poetry/chinese-poetry/tree/master/ci'
    resp = requests.get(songci_url).content
    # 得到根节点
    root = html.fromstring(resp)
    # 得到树节点
    t = root.getroottree()
    ci_url_xpath = '//a[starts-with(@title, "ci.song.")]/@href'
    print(t.xpath(ci_url_xpath))
    return [get_full_url(url).replace('blob/', '') for url in t.xpath(ci_url_xpath)]


def generate_wc(ci_dada, name):

    wc = WordCloud(background_color="white",
                   width=1000,
                   height=860,
                   font_path='./font/MicrosoftYaqiHeiBold-2.ttf',
                   margin=2)

    print('generate {} word cloud'.format(name))
    if not ci_dada:
        print('{} not have ci'.format(name))
        return
    wc.generate(ci_dada)
    # plt.figure(num='poet', figsize=(8, 8))  # 创建一个名为astronaut的窗口,并设置大小
    # # p.subplots()
    # # plt.subplot(2, 2, 1)  # 将窗口分为两行两列四个子图，则可显示四幅图片
    # # plt.title('{}'.format(name))  # 第一幅图片标题
    # plt.imshow(wc)  # 绘制第一幅图片
    # # plt.axis('off')  # 不显示坐标尺寸
    # #
    # # plt.imshow(wc)
    # plt.axis("off")
    # # plt.figure()
    # #
    # plt.show()

    wc.to_file('poet_wc/{}.png'.format(name))


def get_wc():
    songci_list = get_songci()
    ci_author_dict = {}
    for ci in songci_list:
        author = ci.get("author")
        ci_paragraphs = ci.get('paragraphs')
        print(author)
        if author not in ci_author_dict.keys():
            ci_author_dict[author] = []
        ci_author_dict[author] += ci_paragraphs

    for name, content in ci_author_dict.items():
        content_cut = []
        for p in content:
            content_cut += jieba.cut(p)
        content_cut_str = ' '.join(content_cut)

        generate_wc(content_cut_str, name)


if __name__ == '__main__':
    # generate_wc(name='陆游')
    get_wc()

# https://raw.githubusercontent.com/chinese-poetry/chinese-poetry/master/ci/ci.song.0.json
# https://raw.githubusercontent.com/chinese-poetry/chinese-poetry/blob/master/ci/ci.song.0.json