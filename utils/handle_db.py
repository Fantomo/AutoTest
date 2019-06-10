# -*- encoding:utf-8 -*-

import pymysql


class HandleDB:

	def __init__(self):
		self.conn = pymysql.connect(
			host='localhost',
			port=3306,
			user='root',
			passwd='2018',
			charset='utf8'
		)
		self.cur = self.conn.cursor()

	def search_one(self, sql):
		self.cur.execute(sql)
		result = self.cur.fetchone()
		return result

	def search_all(self, sql):
		self.cur.execute(sql)
		result = self.cur.fetchall()
		return result


if __name__ == "__main__":
	mysql = HandleDB()
	res = mysql.search_all("SELECT name from db_user_prod.bmuser a where a.`status`=1 and a.store_id = 4")
	res1 = mysql.search_all("SELECT count(a.id) from db_user_prod.bmuser a where a.`status`=1 and a.store_id = 4")
	print(res)
	print(res1)
