import config
from qqbot import qqbotsched
import pymysql


groupid = config.groupid()

def onQQMessage(bot, contact, member, content):
        global chatdetail
        if contact.ctype == 'group':
                if '集资查询' in content :
                        querryId(bot, contact, member, content)

def querryId(bot, contact, member, content):
        gl = bot.List('group', groupid)
        if gl is not None:
                for group in gl:
                        querryId = content[5:]
                        mysql_conn = {'host': localhost,
                        'port': 3306,
                        'user': 'root',
                        'password': config.dbPasswd(),
                        'db': config.dbName(),
                        'charset': 'utf8'}

                        db = pymysql.connect(**mysql_conn)
                        cursor = db.cursor()

                        try:
                                sql = "SELECT SUM(num) FROM lxyjzdata WHERE ID like '%s'" % (querryId)
                                cursor.execute(sql)
                                msg = '%s聚聚已累计为%s投入了：' % (querryId,config.idolName())
                                results = cursor.fetchall()
                                for row in results:
                                        price = row[0]
                                msg = msg+str(price)+'元'
                                db.close()
                                bot.SendTo(contact,msg)
                        except:
                                msg = '查询失败'
                                db.close()
                                bot.SendTo(contact,msg)

