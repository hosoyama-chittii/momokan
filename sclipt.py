# -*- coding: utf-8 -*-
from NotifyToLine import SendMessage  # mod.pyのMemberクラスの呼び込み
from MonitorWebPages import MonitorBishHP

# インスタンス化
monitor = MonitorBishHP()
notify = SendMessage()

with open("/home/shoma/Documents/workfiles/momokan/TopNews.txt", 'r') as file:
    top_news = file.read()

if monitor.is_changed_for_top_news() == True:
    notify.send_line(
        "\n" +
        "\n" + "BiSH official siteに更新はありません"+
        "\n" +
        "\n" + "---------------------------------------" +
        "\n" + "***最新情報***"
        "\n" + top_news +
        "\n" + monitor.url,
        "/home/shoma/Documents/workfiles/momokan/pictures/no_update.jpg")
else:
    notify.send_line(
        "\n" +
        "\n" + "BiSH official siteに更新がありました" +
        "\n" +
        "\n" + "---------------------------------------" +
        "\n" + "***最新情報***"
        "\n" + top_news +
        "\n" + monitor.url,
        "/home/shoma/Documents/workfiles/momokan/pictures/updated.jpg")

# 更新されたトップニュースを保存
monitor.save_top_news()
