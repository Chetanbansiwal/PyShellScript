#!/usr/bin/env python

import sys, os, subprocess
from xlrd import open_workbook, XL_CELL_NUMBER, XL_CELL_TEXT
from xlwt import Workbook
from xlutils.copy import copy


path = sys.argv[1]
path2 = sys.argv[2]
suffix=0
if len(sys.argv)==4:
	suffix = sys.argv[3]
	print suffix
print path, path2
book = open_workbook(path)
wbook = copy(book)
sheet = book.sheet_by_index(0)
wsheet = wbook.get_sheet(0)

for row_index in range(sheet.nrows):
	cell = sheet.cell(row_index, 0)
	if cell.ctype == XL_CELL_NUMBER: 
		print str(int(cell.value))
		variable = str(int(cell.value))
	else:
		variable = cell.value
	p = subprocess.Popen(['grep', '-w', variable if not suffix else suffix+variable , path2], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	out, err = p.communicate()
	print out
	if not out:
		wsheet.write(row_index, 1, "Not Live")
	else:
		checkstr = out.split(':',2); 
		p = subprocess.Popen(['grep', '-c', checkstr[0]+':'+checkstr[1], path2], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		out1, err = p.communicate()
		print out1
		if int(out1) == 1:
			wsheet.write(row_index, 1, "Live")
		else:
			wsheet.write(row_index, 1, "Over Clustered")

wbook.save(path)


