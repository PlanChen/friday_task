# -*- coding: utf-8 -*- 
from openpyxl import Workbook
from openpyxl import load_workbook
import python_query as query
import python_email as email
import time
import datetime	
import python_constant as constant


date_time = datetime.datetime.now()
dayOfWeek = date_time.weekday()
#假如是星期五则执行查询
if dayOfWeek == 4:
	start_date = date_time + datetime.timedelta(-6)
	end_time = date_time.strftime("%Y%m%d")
	start_time = start_date.strftime("%Y%m%d")
	print "开始时间：{0}, 结束时间：{1}".format(start_time, end_time)
	#获取当前月份
	month = date_time.month
	#获取统计周
	query_day = start_date.strftime("%m.%d") + '-' + date_time.strftime("%m.%d")
	wb = load_workbook('/Users/chenlili/Desktop/BI立项/汇报数据模版/第3周活跃会员数.xlsx')
	sheet = wb.get_sheet_by_name(u'Sheet1')
	sheet['B2'] = str(month) + '月'
	sheet['B4'] = query_day
	
	#填充b2c数据
	b2c_result = query.query_b2c(start_time, end_time)
	if b2c_result:
		for data in b2c_result:
			first_level_region = data['FirstLevelRegion'].encode('utf-8')
			row = constant.data_b2c[first_level_region]
			print first_level_region + ', ' + str(data['ActiveMem'])
			if row:
				sheet[row] = data['ActiveMem']
	#填充o2o数据
	o2o_result = query.query_o2o(start_time, end_time)
	if o2o_result:
		for data in o2o_result:
			first_level_region = data['FirstLevelRegion'].encode('utf-8')
			row = constant.data_o2o[first_level_region]
			print first_level_region + ', ' + str(data['ActiveMem'])
			if row:
				sheet[row] = data['ActiveMem']

	#填充b2b数据
	b2b_result = query.query_b2b(start_time, end_time)
	if b2b_result:
		for data in b2b_result:
			first_level_region = data['FirstLevelRegion'].encode('utf-8')
			row = constant.data_b2b[first_level_region]
			print first_level_region + ', ' + str(data['ActiveMem'])
			if row:
				sheet[row] = data['ActiveMem']

	path = '/Users/chenlili/Desktop/BI立项/汇报数据模版/第3周活跃会员数副本.xlsx'
	wb.save(path)

	#发送邮件
	email.send(path)
else:
	print "未到星期五！"