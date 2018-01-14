# 模拟银行转账
import pymysql


class Account_message:
    def __init__(self, account_id, money):
        self.account_id = account_id
        self.money = money


class Account_run:
    def __init__(self):
        """获取连接 返回conn"""
        conn = pymysql.connect(host="localhost", user="root", password="root", database="njust", port=3306)
        self.conn = conn
        # self.cur = conn.cursor()

    def insert(self, account):
        try:
            sql_insert = "insert into account (account_id, money) values (%s, %s)"
            message = (account.account_id, account.money)
            cur = self.conn.cursor()
            cur.execute(sql_insert, message)
            self.conn.commit()
        except Exception as e:
            print("insert error" + str(e))
        finally:
            cur.close()
            self.conn.close()

    def transfer(self, from_account, to_account, money):
        try:
            self.check_account(from_account)
            self.check_account(to_account)
            self.check_money(from_account, money)
            self.deduct_money(from_account, money)
            self.add_money(to_account, money)
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            self.conn.rollback()
            raise e

    def check_money(self, account, money):
        cur = self.conn.cursor()
        try:
            sql = "select * from account where account_id = %s and money >= %s"
            cur.execute(sql, (account.account_id, money))
            if len(cur.fetchall()) != 1:
                raise Exception("汇钱账户余额不足")
        finally:
            cur.close()

    def check_account(self, account):
        cur = self.conn.cursor()
        try:
            sql = "select * from account where account_id = %s"
            cur.execute(sql, account.account_id)
            if len(cur.fetchall()) != 1:
                raise Exception(str(account.account_id) + "该账户不存在")
        finally:
            cur.close()

    def add_money(self, account, money):
        cur = self.conn.cursor()
        try:
            sql = "update account set money = money + %s where account_id = %s "
            cur.execute(sql, (money, account.account_id))
            if cur.rowcount != 1:
                raise Exception("收款失败")
        finally:
            cur.close()

    def deduct_money(self, account, money):
        cur = self.conn.cursor()
        try:
            sql = "update account set money = money - %s where account_id = %s "
            cur.execute(sql, (money, account.account_id))
            if cur.rowcount != 1:
                raise Exception("收款失败")
        finally:
            cur.close()


account1 = Account_message(12, 500.50)
account2 = Account_message(34, 510.98)
account3 = Account_message(35, 110.98)
run = Account_run()
# run.insert(account3)
run.transfer(account1, account3, 100)
print("end...")

