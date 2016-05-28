#coding = utf-8
import urllib.request
import re

def getHtml(url):
	page = urllib.request.urlopen(url)
	html = page.read()
	return html
	
def getImg(html):
	reg = r'<img .* src="(.*imgsrc.+\.jpg)"'
	imgre = re.compile(reg)
	imglist = re.findall(imgre,html)
	x = 0
	for imgurl in imglist:
		print("downloading... %d %s" % (x,imgurl))
		urllib.request.urlretrieve(imgurl,'./img/%s.jpg'% x)
		x+=1
	print("图片下载完毕！")

url = input("输入要下载图片的网址:")
html = getHtml(url).decode("utf-8")
getImg(html)



