import MySQLdb.cursors          # 在工程目录下安装才成功
import json
class OperationMySQL:
        def __init__(self):
                self.conn = MySQLdb.connect(
                        host='192.168.0.233',
                        port=3306,
                        user='root',
                        password='123456',
                        db='daodangui',
                        charset='utf8',
                        cursorclass=MySQLdb.cursors.DictCursor
                )
                self.cur = self.conn.cursor()

        # 查询一条数据
        def search_one(self,sql):
                self.cur.execute(sql)
                result = json.dumps(self.cur.fetchone())
                return result

if __name__ == '__main__':
    mysql = OperationMySQL()
    result = mysql.search_one("select user_account_id,phone from user_account where account = '18328207604'")
    print(result)
    print(type(result))