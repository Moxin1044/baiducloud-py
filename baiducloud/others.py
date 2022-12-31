import requests
import base64


def send_get_json(url, proxy=""):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    if proxy == "":
        return requests.get(url,headers=headers).json()
    else:
        proxies = {
            'http': f'http://{proxy}',
            'https': f'http://{proxy}'
        }
        return requests.get(url, headers=headers, proxies=proxies).json()


def send_post_data(url, data, proxy=""):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }
    if proxy == "":
        return requests.request("POST", url, headers=headers, data=data).json()
    else:
        proxies = {
            'http': f'http://{proxy}',
            'https': f'http://{proxy}'
        }
        return requests.request("POST", url, headers=headers, proxies=proxies, data=data).json()


def get_file_content_as_base64(path):
    """
    获取文件base64编码
    :param path: 文件路径
    :return: base64编码信息
    """
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf8")