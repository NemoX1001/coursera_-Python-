import requests
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
r = requests.get('https://api.douban.com/v2/movie/subject/1292720') 
# 1292720, 1292052, 1295644, 1291546
data = r.json()
print(data['title'],data['rating']['average'])