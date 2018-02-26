
from urllib import request

class Spider():
	url = 'https://www.panda.tv/cate/lol'

	# 私有方法,实例方法
	def __fetch_content(self):
		r = request.urlopen(Spider.url)
		# htmls为bytes,即字节码
		htmls = r.read()
		htmls = str(htmls,encoding='utf-8')
		a = 1
	
	# 分析方法
	def __analysis(self, htmls):
		pass
	
	# 入口方法
	def go(self):
		htmls = self.__fetch_content()
		self.__analysis(htmls)

spider = Spider()
spider.go()