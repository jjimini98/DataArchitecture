from urllib.request import urlopen
from bs4 import BeautifulSoup

def wiki_python_crawler(url): 
   site = urlopen(url)
   bs = BeautifulSoup(site, 'html.parser',from_encoding='utf-8')
   title = bs.select("#content > div:nth-child(2) > div > div")
   print(title)
   # for t in title: 
   #    with open("./crawling/wiki_python_crawling.txt","a", encoding='utf-8') as f:
   #       f.write(t.text)
   #       f.write("\n")


   context = bs.select("#tabs_1 > div > p:nth-child(3)")
   for c in context:
      with open("./crawling/wiki_python_crawling.txt","a", encoding='utf-8') as f:
            f.write(c.text)
            f.write("\n")
            f.write("\n")


#url 모음에서 한 줄씩 읽어서 크롤러 함수에 인자로 넣음. 
with open("./crawling/wiki_python_url.txt","r") as f :
   while True:
      line = f.readline()
      if not line: break
      hanbit_python_crawler(line)

#크롤링할 때 생기는 빈칸들(제대로 크롤링되지 않은 것들)은 손수 삭제함.


