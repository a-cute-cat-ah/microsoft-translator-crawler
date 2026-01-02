from _requests import request,urlencode
from re import findall
from json import loads

#----
text = request("https://cn.bing.com/translator")

t = text.read().decode()

IG = findall('IG:"(.*?)"',t)[0]

_ = loads(findall(r'params_AbusePreventionHelper[\s]=[\s](.*?);',t)[0])
key = _[0]
token = _[1]
tt = {}

from time import time
with open(round(time()).__str__()+".txt","w") as f:
    for v,k in text.headers.items():
        if v != "Set-Cookie":
            continue
        f.write(k+"\n")
        exec("tt[\"{}\"] = \"{}\"".format(
            k.split(";")[0].split("=")[0], 
            "=".join(k.split(";")[0].split("=")[1:])
            ))

print(tt)

#----


z = "你好"

aa = []
for v,k in tt.items():
    aa.append("{}={}".format(v,k))
aa = ";".join(aa)

print(aa)

h = request(
    "https://cn.bing.com/ttranslatev3?"+urlencode({
        "isVertical":"1", 
        "IG":IG, 
        "IID":"translator.5025"
    }),
    "POST",
    body={
        "fromLang": "zh-Hans", 
        "to": "en", 
        "text": z, 
        "tryFetchingGenderDebiasedTranslations": "true", 
        "token":token, 
        "key":key
    }, 
    headers={"Cookie":aa,"Content-Type":"application/x-www-form-urlencoded"}
)

print(h.read().decode())