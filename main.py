from argparse import ArgumentParser
import sqlite3
import os.path
from openpyxl import load_workbook

def parse_args():
  parser = ArgumentParser(description="Messages")
  parser.add_argument('-w', '--write', action='store_true', default=False)
  parser.add_argument('-s', '--scan', action='store_true', default=False)
  parser.add_argument('files', metavar='FILE', nargs='+', \
                        help="files to process")
  return parser.parse_args();

def main():
  args = parse_args()

  messages = {}
  for filename in args.files:
    # if is directory, recursively traverss
    # if file, test if accepted format
    pass
  


def connect():
  imessage = sqlite3.connect('imessage/chat.db')
  imessage.row_factory = sqlite3.Row
  return imessage.cursor()

def pRows(rows):
  for row in rows:
    print()
    for k in row.keys():
      print(k, ' => ', row[k])

def pTable(rows, keys, padding=2, width=15):
  frmt = ("|" + "{:^" + str(width) + "}|") * len(keys)
  pads = ' ' * padding
  line = '-' * ((width + 2) * len(keys))

  print(pads + line)
  print(pads + frmt.format(*keys))
  print(pads + line)
  for row in rows:
    print(pads + frmt.format(*tuple(row)))
  print(pads + line)

def dumpToSpreadsheet(cur):
  pass

def dumpToCsv(rows, filename):
  f = open(filename, 'w')
  f.write(','.join([str(d[0]).replace(',', '\,') for d in cur.description]) + '\n')
  for row in rows:
    f.write(','.join([str(c).replace(',', '\,') for c in row]) + '\n')
  f.flush()
  f.close()

def createDB():
	db = sqlite3.connect('master.db')
	d = db.cursor()
	d.execute('''
		create table messages(
			date text,
			body text,
			service text,
			to text,
			from text)
		''');
	db.commit()

def titles(cur):
  return tuple(d[0] for d in cur.description)

cur = connect()
cols = [
'service',
'is_from_me',
'date',
'date_delivered',
'date_read'
'account_guid'
]
table = 'message'
constraints = [
  'where is_from_me = 0',
  'limit 100',
  'offset 10'
]
query = 'select ' \
  + (','.join(cols) if cols else '*') \
  + ' from ' + table + ' ' \
  + ' '.join(constraints)

print(query)
rows = cur.execute(query)
pTable(rows, titles(cur))
