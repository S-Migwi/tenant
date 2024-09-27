import sqlite3


class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS tenants(id INTEGER PRIMARY KEY, Tenant_Name text, House_Rent text, House_Number text, Outstanding_Balance text, Last_payment text, Phone_Number INTEGER)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM tenants")
        rows = self.cur.fetchall()
        return rows

    def insert(self,Tenant, Number, Rent, balance, lastpayment, phonenumber):
        self.cur.execute("INSERT INTO tenants VALUES (NULL, ?, ?, ?, ?, ?, ?)",(Tenant, Number, Rent, balance, lastpayment, phonenumber))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM tenants WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, Tenant, Number, Rent, balance, lastpayment, phonenumber):
        self.cur.execute("UPDATE tenants SET Tenant= ?, Number= ?, Rent= ?, balance= ?, lastpayment= ?, phonenumber=? WHERE id=?", (Tenant, Number, Rent, balance, lastpayment, phonenumber, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

