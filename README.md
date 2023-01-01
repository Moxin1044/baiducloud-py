# 百度智能云 API调用PythonSDK

这是一个用于百度云部分开放AI功能的Python库。主要为ORC功能，可以对各种图像文件进行文字识别，包括车牌、手写文字、通用文字、人脸发现、人脸比对和人流量统计等。

更多的功能大家可以提出，后续会慢慢开发这个库。

使用这个库，你可以很方便地调用百度云OCR API，并将识别结果以json的形式返回。你可以根据自己的需要来使用不同的API，以获得更精确或更快速的识别结果。

此外，这个库还提供了URL版本的文字识别功能，可以直接对网络图片进行识别。

# 使用方法

## 1.安装库

使用pip安装：

```bash
pip install baiducloud
```

## 2.准备API Key和Secret Key

在使用百度云OCR API之前，你需要去百度云控制台申请API Key和Secret Key。

地址：https://console.bce.baidu.com/ai/#/ai/ocr/overview/index

## 3.初始化baiducloud类

在你的代码中导入baiducloud类，并使用API Key和Secret Key初始化它：

```python
from baiducloud import baiducloud

api_key = "your_api_key"
secret_key = "your_secret_key"

bc = baiducloud(api_key, secret_key)
```

## 4.使用Python开发你的程序

### 例子1.车牌识别

```python
result = bc.orc_license_plate("image.jpg")
print(result)
```

返回结果是一个json

### 例子2.使用URL版本的文字识别

```python
result = bc.orc_license_plate_url("https://example.com/image.jpg")
print(result)
```

**注意：使用URL版本的文字识别方法时，你需要确保图片URL是可以公开访问的。**

### 例子3.使用人脸比对

```python
result = bc.face_compare("https://example.com/image.jpg"，"https://example.com/image1.jpg")
print(result)
```

当然，还有更多的使用方法，具体可以参考`baiducloud > main.py`，使用方法大同小异，文档就后续再更新。
