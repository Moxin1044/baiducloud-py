from setuptools import setup
import io

with io.open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='baiducloud',
    version='1.0.8',
    packages=['baiducloud'],
    url='https://github.com/Moxin1044/baiducloud-py',
    long_description=long_description,
    long_description_content_type='text/markdown',  # This is important!
    license='MIT License',
    author='Moxin',
    author_email='1044631097@qq.com',
    description='Python的百度智能云api调用'
)
