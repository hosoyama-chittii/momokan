# -*- coding: utf-8 -*-
import requests


class SendMessage:
    talk_room_url = "https://notify-api.line.me/api/notify"  # line_notifyのURL
    # token = "MziYe4VeV7HF5yYmwl2Edaa9szYR8jdkHNCWHaBoiAd"  # <--細山宛のLine_notify_token(モモカンセンサーズ)

    token = "ttXyc1VPblGnfnFMGC4FzueOtEfyniLNNGqWM9AehjY"  # <--TDUアイドル研究会宛のLine_notify_token(bish_notifire)

    def send_line(self, message, picture):  # lineにこのファイルのカレントディレクトリにある画像ファイルとself.name、self.commentを送る。

        headers = {"Authorization": "Bearer " + self.token}
        payload = {"message": message}

        if picture == "no_image":
            files = ""
        else:
            files = {"imageFile": open(picture, "rb")}  # バイナリで画像ファイルを開く。対応している形式はPNG/JPEG

        r = requests.post(self.talk_room_url, headers=headers, params=payload, files=files)
