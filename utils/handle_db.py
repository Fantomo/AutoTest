# -*- encoding:utf-8 -*-

import pymysql

from utils.config import Config



class HandleDB:

	def __init__(self):
		db_config = Config().get('db')
		self.conn = pymysql.connect(
			host=db_config['host'],
			port=db_config['port'],
			user=db_config['user'],
			passwd=db_config['passwd'],
			charset=db_config['charset'],
			# cursorclass=pymysql.cursors.DictCursor
		)
		self.cur = self.conn.cursor()

	def search_one(self, sql, *args):
		self.cur.execute(sql, *args)
		result = self.cur.fetchone()
		return result

	def search_all(self, sql, *args):
		self.cur.execute(sql, *args)
		result = self.cur.fetchall()
		return result

	def __del__(self):
		self.cur.close()
