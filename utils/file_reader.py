# coding:utf-8

import os
import yaml

from xlrd import open_workbook


# 读取配置文件yaml文件
class YamlReader:

	def __init__(self, yamlfilepath):
		if os.path.exists(yamlfilepath):
			self.yamlfilepath = yamlfilepath
		else:
			raise FileNotFoundError('文件未找到!')
		self._data = None

	@property
	def data(self):
		if not self._data:
			with open(self.yamlfilepath, 'rb') as f:
				self._data = list(yaml.safe_load_all(f))
			return self._data


class SheetTypeError(Exception):
	pass


# 读取excel文件中的内容
class ExcelReader:

	def __init__(self, excelpath, sheet=0, title_line=True):
		if os.path.exists(excelpath):
			self.excelpath = excelpath
		else:
			raise FileNotFoundError('文件未找到!')
		self.sheet = sheet
		self.title_line = title_line
		self._data = list()

	@property
	def data(self):
		if not self._data:
			workbook = open_workbook(self.excelpath)
			if type(self.sheet) not in [int, str]:
				raise SheetTypeError('Please pass in <type int> or <type str>, not {0}').format(type(self.sheet))
			elif type(self.sheet) == int:
				s = workbook.sheet_by_index(self.sheet)
			else:
				s = workbook.sheet_by_name(self.sheet)

			if self.title_line:
				title = s.row_values(0)
				for col in range(1, s.nrows):
					self._data.append(dict(zip(title, s.row_values(col))))
			else:
				for col in range(0, s.nrows):
					self._data.append(s.row_values(col))
			return self._data


if __name__ == "__main__":
	# y = 'G:\WebAutoTest\config\config.yml'
	# reader = YamlReader(y)
	# print(reader.data)

	excelfile = 'G:/WebAutoTest/data/order.xlsx'
	reader = ExcelReader(excelfile, title_line=False)
	print(reader.data)
