import config
import pymysql
import requests
import json
import urllib
import hashlib

userid = []
price = []

header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) Appl\
eWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}

def getSign(ret):
    # 将字典按键升序排列，返回一个元组tuple
    tuple = sorted(ret.items(), key=lambda e: e[0], reverse=False)
    md5_string = urllib.parse.urlencode(tuple).encode(encoding='utf_8', errors='strict')
    md5_string += b'&p=das41aq6'
    # md5计算 & 十六进制转化 & 根据规则从第6位开始取16位
    sign = hashlib.md5(md5_string).hexdigest()[5: 21]
    return sign

def getRankings():
	p
	page = 1
	while True:
		url = 'https://wds.modian.com/api/project/rankings'
		form = {
			'page': page,
			'pro_id': input('Please input pro_id:'),
			'type': 1
		}
		sign = getSign(form)
		form['sign'] = sign
		response = requests.post(url, form, headers=header).json()
		page +=1
		datas = response['data']
		if datas == []:
			break
		for data in datas:
			userid.append(data['nickname'])
			price.append(data['backer_money'])
	save_to_database()

def save_to_database():
	data = dict(zip(userid,price))

	mysql_conn = {
		'host': 'localhost',
		'port': 3306,
		'user': 'root',
		'password': config.dbPasswd(),
		'db': config.dbName(),
		'charset': 'utf8'}

	db = pymysql.connect(**mysql_conn)
	cursor = db.cursor()
	sql = """CREATE TABLE IF NOT EXISTS %s(
			ID varchar(255) NOT NULL,
			num double(10,2) NOT NULL)
			engine=innodb  default charset=utf8""" % (tableName())
	cursor.execute(sql)

	print('Database table create OK')
	for key in data:
		cursor.execute("INSERT INTO lxyjzdata VALUES (%s,%s)", (key,data[key]))
		db.commit()
	print('Data saved OK')
	db.close()
    


if __name__ == '__main__':
    getRankings() 
            
