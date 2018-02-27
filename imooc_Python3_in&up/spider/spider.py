'''
	This is module
	爬取熊猫TV-英雄联盟首页主播名字和人气，人气高往低排序
'''
import re

from urllib import request

class Spider():
	'''
		This is a class
	'''
	url = 'https://www.panda.tv/cate/lol'
	
	# \s\S 匹配所有字符, []表示字符集, *表示匹配多次, ?表示非贪婪, ()表示组
	root_pattern = '<div class="video-info">([\s\S]*?)</div>'
	name_pattern = '</i>([\s\S]*?)</span>'
	number_pattern = '<span class="video-number">([\s\S]*?)</span>'

	# 私有方法,实例方法
	# 获取网页的html信息
	def __fetch_content(self):
		r = request.urlopen(Spider.url)
		# htmls为bytes,即字节码
		htmls = r.read()
		htmls = str(htmls,encoding='utf-8')
		return htmls
	
	# 分析方法
	# 正则匹配，获取关键信息
	def __analysis(self, htmls):
		# 获取匹配到的初始字符串
		root_html = re.findall(Spider.root_pattern, htmls)

		anchors = []
		# 从初始字符串中匹配到名称和次数，并组成字典元素的列表
		for html in root_html:
			name = re.findall(Spider.name_pattern, html)
			number = re.findall(Spider.number_pattern, html)
			anchor = {"name":name, "number":number}
			anchors.append(anchor)
		
		return anchors
	
	# 数据精炼，规范格式
	def __refine(self, anchors):
		l = lambda anchor:{
			'name':anchor['name'][0].strip(),
			'number':anchor['number'][0]
		}
		return map(l, anchors)
	
	# 排序
	def __sort(self, anchors):
		# key的作用是指定元素作为比较大小的元素
		anchors = sorted(anchors, key=self.__sort_seed,reverse=True)
		return anchors
	
	# 获取列表中作为比较大小的元素
	def __sort_seed(self, anchor):
		r = re.findall('\d*', anchor['number'])
		number = float(r[0])
		if '万' in anchor['number']:
			number *= 10000
		return number
	
	# 将结果以一种好看的形式打印出来
	def __show(self, anchors):
		for rank in range(0, len(anchors)):
			print('rank' + str(rank + 1) + ' : ' + anchors[rank]['name']
				+ '  ' + anchors[rank]['number'])
	
	# 入口方法
	def go(self):
		htmls = self.__fetch_content()
		anchors = self.__analysis(htmls)
		anchors = list(self.__refine(anchors))
		anchors = self.__sort(anchors)
		self.__show(anchors)

spider = Spider()
spider.go()