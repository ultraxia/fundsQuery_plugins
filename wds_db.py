import config
import pymysql
import requests
from lxml import etree

userid = []
price = []

def connect_database():
	mysql_conn = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': 'config.dbPasswd(),
            'db': config.dbName(),
            'charset': 'utf8'
        }
    
	db = pymysql.connect(**mysql_conn)
	cursor = db.cursor()
	sql = """CREATE TABLE IF NOT EXISTS %s(
                ID varchar(255) NOT NULL,
                num double(10,2) NOT NULL)
                engine=innodb  default charset=utf8""" % (config.tableName())
	cursor.execute(sql)
	return db


def getData():
	ajax_url = 'https://wds.modian.com/ajax/backer_ranking_list'
	header = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
	form = {
		'pro_id': input('Please input pro_id:'),
		'type': '1',
		'page': 1,
		'page_size': '20'}
	try:
		while True:
			response = requests.post(ajax_url, form, headers=header).json()
			if response['status'] == '-1':
				break
			html = response['data']['html']
			seletor = etree.HTML(html)
			nicknames = seletor.xpath('//*[@class="nickname"]/text()')
			moneys = seletor.xpath('//*[@class="money"]/text()')
			for nickname in nicknames:
				userid.append(nickname)
			for money in moneys:
				price.append(float(money[2:].replace(',','')))
			form['page'] += 1
	except KeyError:
		print('Data access success')
	
def save_to_database():
	db = connect_database()
	cursor = db.cursor()
	data = dict(zip(userid,price))	
	for key in data:
		cursor.execute("INSERT INTO test VALUES (%s,%s)", (key,data[key]))
		db.commit()
	print('Data saved OK')
	db.close()

def start():
	connect_database()
	getData()
	save_to_database()

if __name__ == '__main__':
	start()















































































































































































