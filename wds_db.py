import config
import pymysql
import requests
from lxml import etree

userid = []
price = []

def main():
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
	data = dict(zip(userid,price))	

	mysql_conn = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': config.dbPasswd(),
            'db': config.dbName(),
            'charset': 'utf8'
        }
    
	db = pymysql.connect(**mysql_conn)
	cursor = db.cursor()
	sql = """CREATE TABLE IF NOT EXISTS %s(
                ID varchar(255) NOT NULL,
                num double(10,2) NOT NULL)
                engine=innodb  default charset=utf8"""  % (tableName())
	cursor.execute(sql)
	
	print('Database table create OK')
	for key in data:
		cursor.execute("INSERT INTO lxyjzdata VALUES (%s,%s)", (key,data[key]))
		db.commit()
	print('Data saved OK')
	db.close()

if __name__ == '__main__':
	main()
	save_to_database()
































