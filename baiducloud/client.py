import urllib.parse
import json
import requests
import baiducloud.others as others



class baiducloud:
    def __init__(self, api_key, secret_key, proxy=""):
        self.AK = api_key
        self.SK = secret_key
        self.proxy = proxy
        self.url = "https://aip.baidubce.com/oauth/2.0"
        self.access_token = self.Access_token()

    def Access_token(self):
        url = f"{self.url}/token?client_id={self.AK}&client_secret={self.SK}&grant_type=client_credentials"
        response = others.send_get_json(url, self.proxy)
        return response['access_token']

    # 车牌识别
    def orc_license_plate(self,file_path):
        url = "https://aip.baidubce.com/rest/2.0/ocr/v1/license_plate?access_token=" + self.access_token
        payload = "image=" + urllib.parse.quote(baiducloud.operation.get_file_content_as_base64(file_path))
        response = others.send_post_data(url, payload, self.proxy)
        return response

    # 手写文字识别
    def orc_handwriting(self, file_path):
        url = "https://aip.baidubce.com/rest/2.0/ocr/v1/handwriting?access_token=" + self.access_token
        payload = "image=" + urllib.parse.quote(others.get_file_content_as_base64(file_path))
        response = others.send_post_data(url, payload, self.proxy)
        return response

    # 通用文字识别 高精度
    def orc_accurate_basic(self, file_path):
        url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token=" + self.access_token
        payload = "image=" + urllib.parse.quote(others.get_file_content_as_base64(file_path))
        response = others.send_post_data(url, payload, self.proxy)
        return response

    # 通用文字识别
    def orc_general_basic(self, file_path):
        url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=" + self.access_token
        payload = "image=" + urllib.parse.quote(others.get_file_content_as_base64(file_path))
        response = others.send_post_data(url, payload, self.proxy)
        return response

    # 车牌识别 URL版本
    def orc_license_plate_url(self,img_url):
        url = "https://aip.baidubce.com/rest/2.0/ocr/v1/license_plate?access_token=" + self.access_token
        payload = "url="+urllib.parse.quote(img_url)
        response = others.send_post_data(url, payload, self.proxy)
        return response

    # 手写文字识别 URL版本
    def orc_handwriting_url(self,img_url):
        url = "https://aip.baidubce.com/rest/2.0/ocr/v1/handwriting?access_token=" + self.access_token
        payload = "url=" + urllib.parse.quote(img_url)
        response = others.send_post_data(url, payload, self.proxy)
        return response

    # 通用文字识别 高精度 URL版本
    def orc_accurate_basic_url(self,img_url):
        url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token=" + self.access_token
        payload = "url=" + urllib.parse.quote(img_url)
        response = others.send_post_data(url, payload, self.proxy)
        return response

    # 通用文字识别 URL版本
    def orc__general_basic_url(self,img_url):
        url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=" + self.access_token
        payload = "url=" + urllib.parse.quote(img_url)
        response = others.send_post_data(url, payload, self.proxy)
        return response

    # 人脸发现
    def face_detect(self,img_path):
        url = "https://aip.baidubce.com/rest/2.0/face/v3/detect?access_token=" + self.access_token
        payload = json.dumps({
            "image": others.get_file_content_as_base64(img_path),
            "image_type": "BASE64",
            "max_face_num": 100
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json()

    # 人脸对比
    def face_compare(self,img_path, img_path2):
        url = "https://aip.baidubce.com/rest/2.0/face/v3/match?access_token=" + self.access_token
        payload = json.dumps([
            {
                "image": others.get_file_content_as_base64(img_path),
                "image_type": "BASE64"
            },
            {
                "image": others.get_file_content_as_base64(img_path2),
                "image_type": "BASE64"
            }
        ])
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json()

    # 人流量统计
    def person_num(self,img_path):
        url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_num?access_token=" + self.access_token
        payload = "image=" + urllib.parse.quote(others.get_file_content_as_base64(img_path))
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json()

