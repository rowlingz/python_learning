import pymysql


class AccountMessage:
    def __init__(self, id, money):
        self.id = id
        self.money = money


class AccountRun():
    def __init__(self):
        """获取连接 返回conn"""
        conn = pymysql.connect(host="localhost", user="root", password="root", database="njust", port=3306)
        self.conn = conn

    def insert(self, account_message):
        cur = self.conn.cursor()
        sql_select = "select * from account where account_id = %s"
        sql_insert = "insert into account (account_id, money) values (%s, %s)"
        cur.execute(sql_select, account_message.id)
        if cur.rowcount != 0:
            print(str(account_message.id) + "该账户已经存在, 无需创建")
        else:
            cur.execute(sql_insert, (account_message.id, account_message.money))
            self.conn.commit()
        cur.close()

    def transfer(self, from_id, to_id, money):
        if not self.check_account(from_id):
            print(str(from_id) + "汇款账户不存在")
            return
        if not self.check_account(to_id):
            print(str(to_id) + "到款账户不存在")
            return
        if not self.check_money(from_id, money):
            print(str(from_id) + "账户余额不足")
            return

        cur = self.conn.cursor()
        try:
            sql_add = "update account set money = money + %s where account_id = %s"
            sql_deduct = "update account set money = money - %s where account_id = %s"
            cur.execute(sql_deduct, (money, from_id))
            if cur.rowcount != 1:
                raise Exception("扣款失败")
            cur.execute(sql_add, (to_id, money))
            if cur.rowcount != 1:
                raise Exception("到款失败")
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print("转账失败--" + str(e))
        finally:
            cur.close()

    def check_account(self, id):
        cur = self.conn.cursor()
        try:
            sql_select = "select * from account where account_id = %s"
            cur.execute(sql_select, id)
            numrows = cur.rowcount
            if numrows != 1:
                return False
            else:
                return True
        except Exception as e:
            print(str(id) + "查询报错" + e)
        finally:
            cur.close()

    def check_money(self, id, money):
        cur = self.conn.cursor()
        sql_select = "select * from account where account_id = %s and money >= %s"
        cur.execute(sql_select, (id, money))
        numrows = cur.rowcount
        cur.close()
        if numrows != 1:
            return False
        else:
            return True


account1 = AccountMessage(12, 500.50)
account2 = AccountMessage(34, 510.98)
account3 = AccountMessage(35, 110.98)
run = AccountRun()
# run.insert(account1)
run.transfer(1, 2, 400)