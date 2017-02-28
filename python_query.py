# -*- coding: utf-8 -*- 
import pymssql
import python_constant as constant

#读取b2c的会员数据
def query_b2c(start_time, end_time):
	print('开始查询b2c数据')
	conn = pymssql.connect(**constant.config_b2c)
	cursor = conn.cursor(as_dict=True)

	sql = "select ds.FirstLevelRegion, COUNT(distinct consignee_mobile) ActiveMem from ( \
		 select * from openquery(B2C,'SELECT ord.* FROM tbl_order ord, tbl_seller ts \
		WHERE ord.seller_no = ts.id AND ord.basic_state <> 404 AND DATE_FORMAT(ord.create_time, ''%Y%m%d'')  between ''{0}'' and ''{1}'' ') ) ord \
		inner join Dim_Store ds on ord.seller_no = ds.StoreId group by ds.FirstLevelRegion".format(start_time, end_time)
	cursor.execute(sql)
	result = [row for row in cursor]
	conn.close()
	print('结束查询b2c数据')
	return result

#读取o2o的会员数据
def query_o2o(start_time, end_time):
	print('开始查询o2o数据')
	conn = pymssql.connect(**constant.config_o2o)
	cursor = conn.cursor(as_dict=True)

	sql = "select ds.FirstLevelRegion, COUNT(distinct buyer_phone) ActiveMem from ( \
		 select * from openquery(O2O, 'SELECT tod.* FROM tbl_order tod,tbl_outlet_basic_info tobi WHERE 1 = 1 AND tod.outlet_id = tobi.outlet_id \
		AND DATE_FORMAT(tod.create_time, ''%Y%m%d'')  between ''{0}'' and ''{1}'' ') ) ord  \
		inner join Dim_Store ds on ord.outlet_id = ds.StoreId group by ds.FirstLevelRegion".format(start_time, end_time)
	cursor.execute(sql)
	result = [row for row in cursor]
	conn.close()
	print('结束查询o2o数据')
	return result

#读取b2b的会员数据
def query_b2b(start_time, end_time):
	print('开始查询b2b数据')

	conn = pymssql.connect(**constant.config_b2b)
	cursor = conn.cursor(as_dict=True)

	sql = "select ds.FirstLevelRegion, COUNT(distinct contact_mobile) ActiveMem from ( \
		 select * from openquery(B2B, 'SELECT * FROM order_info tod\
		 where DATE_FORMAT(tod.create_time, ''%Y%m%d'')  between ''{0}'' and ''{1}'' ') ) ord  \
		inner join Dim_Store ds on ord.supply_user_code = ds.StoreId \
		group by ds.FirstLevelRegion".format(start_time, end_time)
	print sql
	cursor.execute(sql)
	result = [row for row in cursor]
	conn.close()
	print('结束查询b2b数据')
	return result
