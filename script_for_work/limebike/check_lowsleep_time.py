import csv

class Check_report_time(object):
	def __init__(self):
		self.allData = [('AT+CMD_sendtime','codec_playtime','RESP_sendtime','result')]
		self.report = [('AT+QRY_sendtime','RESP_sendtime','result')]

	# 读取ap.log文件
	def readfile(self):
		# ap.log中有编码问题，需忽略
		mfile = open('ap.log',encoding='gb18030',errors='ignore')
		content = mfile.readlines()
		mfile.close()
		return content

	def analy_data(self):
		content = self.readfile()

		for line in content:
			if "+RESP:" in line:

				# 将空格替换为'#'
				Mline = '#'.join(line.split())

				# 分隔每行字符串获取LOG打印时间和Report产生时间
				LOG_time = Mline.split('#')[2]
				Report_time = Mline.split('#')[8].split(',')[3]

				# 在数组中保存两个时间值
				self.allData.append((LOG_time,Report_time))

				#将logtime和reporttime转换为整数
				log_list_time = LOG_time.split(':')
				logtime = int(log_list_time[0]+log_list_time[1]+log_list_time[2])
				reporttime = int(Report_time[8:])

				#对比logtime和reporttime并输出结果
				time_diff = (logtime-reporttime)
				
				if time_diff >= 0 and time_diff <5:
					result = 'pass'
				else:
					result = 'fail'

				self.report.append((line,result))


	def SaveDataToCSV(self):
		csvfile = open('Check_report_time.csv','w')
		writer = csv.writer(csvfile)
		writer.writerows(self.allData)
		csvfile.close()

	def SaveReportToCSV(self):
		csvfile = open('report_result.csv','w')
		writer = csv.writer(csvfile)
		writer.writerows(self.report)
		csvfile.close()


if __name__ == '__main__':
	Check_Time = Check_report_time()
	Check_Time.analy_data()
	Check_Time.SaveDataToCSV()
	Check_Time.SaveReportToCSV()
