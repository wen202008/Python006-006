import requests
from lxml import etree
from pathlib import Path

def getContent(url,wfile):
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    header = {'user-agent':ua}
    response = requests.get(url,headers=header)
    selector = etree.HTML(response.text)

    title = selector.xpath('//div[@class="bg_htit"]/h2/text()')

    comment = selector.xpath('//p[@class="eat_s"]/a/text()')

    #print(f'title:{title}')
    #print(f'comment:{comment}')
    if not Path(Path(wfile).parent).is_dir():
        Path(Path(wfile).parent).mkdir()
    with open(wfile,'a') as f:
        f.write('title： '+ title[0] + '\n')
        f.write('comment:\n')
        for c in comment:
            f.write(c + '\n')



if __name__ == '__main__':
    getContent('https://www.solidot.org/story?sid=66532','c:\\tmp\\tmp.txt')

