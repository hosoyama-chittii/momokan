# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup


class MonitorBishHP():
    # BiSHのHPのURL。このURLをスクレイピングする。
    url = "https://www.bish.tokyo/news/"

    def __init__(self):
        # URLにアクセスする。 戻り値にはアクセスした結果やHTMLなどが入ったinstanceが帰る。
        instance = urllib.request.urlopen(self.url)

        # instanceからHTMLを取り出して、BeautifulSoupで扱えるようにパースする。
        self.soup = BeautifulSoup(instance, "html.parser")

        # CSSセレクターを使って指定した場所のtextを表示する。アクセスしたURL先の一番上のニュースの内容を変数に格納。
        self.url_data = self.soup.select_one("a").get("herf")
        self.top_news = self.soup.select_one("h2").string
        self.top_news_url = self.soup.select_one("a").string

    # 現在のスクレイピング先のURLのh2タグの中身を出力
    def print_top_news(self):
        print(str(self.top_news))

    # スクレイピングした内容をファイルに上書き保存する。
    def save_top_news(self):
        # 実行時のトップニュースをtxtファイルで保存
        with open("/home/shoma/Documents/workfiles/momokan/TopNews.txt", 'w') as file:  # ファイル名をself.read_start_timeとしファイルを作る。'w'は開いたファイルにデータを上書きする。
            file.write(str(self.top_news))

    # 現在のスクレイピング先のURLのh2タグの中身と前回分と差を確認
    def is_changed_for_top_news(self):
        # 過去のトップニュースを読み込む
        with open("/home/shoma/Documents/workfiles/momokan/TopNews.txt", 'r') as file:
            self.top_news_txt = file.read()

        print("実行時のトップニュース"+":"+self.top_news)
        print("過去のトップニュース"+":"+self.top_news_txt)

        # 実行時のトップニュースと過去のトップニュースの差があればfalseを返す
        return self.top_news == self.top_news_txt
