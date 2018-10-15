from xlrd import open_workbook
from os.path import join, dirname, abspath


def get_data_from_excel(ticker):

	# Data from loss gain table

	fname = join(dirname(dirname(abspath(__file__))), 'algo_task/files', 'lossgaingraph.xls')
	book = open_workbook(fname)
	sheet = book.sheet_by_index(0)

	# read header values into the list    
	keys = [sheet.cell(0, col_index).value for col_index in xrange(sheet.ncols)]

	final_data = {}
	for row_index in xrange(1, sheet.nrows):
		required_dict = {}
		for col_index in xrange(sheet.ncols):
			required_dict[keys[col_index]] = sheet.cell(row_index, col_index).value
		if required_dict.get("Ticker") == ticker:
			final_data["lossgain_data"] = required_dict
			break

	# Data from generalnumber table
	fname = join(dirname(dirname(abspath(__file__))), 'algo_task/files', 'generalnumber.xls')
	book = open_workbook(fname)
	sheet = book.sheet_by_index(0)

	# read header values into the list    
	keys = [sheet.cell(0, col_index).value for col_index in xrange(sheet.ncols)]

	for row_index in xrange(1, sheet.nrows):
		required_dict = {}
		for col_index in xrange(sheet.ncols):
			required_dict[keys[col_index]] = sheet.cell(row_index, col_index).value
		if required_dict.get("Ticker") == ticker:
			final_data["generalnumber_data"] = required_dict
			break

	return final_data

def get_ticker_list_from_excel():
	fname = join(dirname(dirname(abspath(__file__))), 'algo_task/files', 'generalnumber.xls')
	book = open_workbook(fname)
	sheet = book.sheet_by_index(0)

	# read header values into the list    
	keys = [sheet.cell(0, col_index).value for col_index in xrange(sheet.ncols)]

	ticker_list = []
	for row_index in xrange(1, sheet.nrows):
		for col_index in xrange(sheet.ncols):
			if keys[col_index] == "Ticker":
				ticker_list.append(sheet.cell(row_index, col_index).value)
		
	return ticker_list