import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request

url = 'https://www.withone.co.jp'

opener = urllib.request.build_opener()
opener.addheaders = [
    (
        'User-agent',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.2 Safari/605.1.15'
    )
]

htmldata = urllib.request.urlopen(url)
print(htmldata.read().decode('UTF-8'))

htmldata.close()
