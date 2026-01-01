# 引入通信库发送请求
import http.client
# 解析url库
from urllib.parse import urlsplit

# 解析url
def parse_url(url:str) -> dict:
    _urlsplit = urlsplit(url) # 拆分url
    scheme = _urlsplit.scheme # 获得协议
    netloc = _urlsplit.netloc # 获得网络位置
    # 解析网络位置，获得其ip地址和端口
    if ":" not in netloc:
        # 无明确端口
        # 根据协议使用默认端口
        if scheme == "http":
            port = 80
        if scheme == "https":
            port = 443
        host = netloc # 获得ip
    else:
        # 明确端口
        netlocsplit = netloc.split(":") # 拆分ip地址和端口
        # 检查合法性
        if len(netlocsplit) != 2:
            print("无法正常解析:因为非常格式")
        host = netlocsplit[0] # 获得ip
        port = netlocsplit[-1] # 获得未格式化端口
        port = int(port) # 格式化为int类型
    path = _urlsplit.path # 获得目录
    query = _urlsplit.query # 获得未格式化参数
    # 解析结束，返回值
    return {
        "scheme": scheme, 
        "host": host, 
        "port": port, 
        "path": path, 
        "query": query, 
    }

# 发送请求
def request(url:str, method:str="GET", **other) -> http.client.HTTPResponse:
    urlinfo = parse_url(url) # 解析url
    # 根据协议选择不同方式
    if urlinfo["scheme"] == "http":
        conn = http.client.HTTPConnection(urlinfo["host"], urlinfo["port"])
    elif urlinfo["scheme"] == "https":
        conn = http.client.HTTPSConnection(urlinfo["host"], urlinfo["port"])
    # 发送请求
    response = conn.request(method,urlinfo["path"]+"?"+urlinfo["query"], **other)
    # 返回请求
    return response