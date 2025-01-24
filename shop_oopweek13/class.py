import mysql.connector
class Managerdb:
    def __init__(self, host, user, password, database):
        self.mydb = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database,
        )
        self.mycursor = self.mydb.cursor()
    
    def selectdb(self, table):
        sql = f"SELECT * FROM {table}"
        self.mycursor.execute(sql)
        show = self.mycursor.fetchall()
        return show
    
    def deletedb(self, table, id_name, id):
        sql = f"DELETE FROM {table} WHERE {id_name} = {id}"
        self.mycursor.execute(sql)
        self.database.mydb.commit()
        if self.mycursor.rowcount > 0:
            return True
        else:
            return False
    
    def editdb(self, table, colum, id_name, id, val):
        sql = f"UPDATE {table} SET {colum} = %s WHERE {id_name} = %s"
        val_sql = (val, id)
        self.mycursor.execute(sql, val_sql)
        self.database.mydb.commit()
        if self.mycursor.rowcount > 0:
            return True
        else:
            return False
    
    def insert_users(self, username, password, email, user_role):
        sql = "INSERT INTO users VALUES (%s, %s, %s, %s, %s)"
        val_sql = (None, username, password, email, user_role)
        self.mycursor.execute(sql, val_sql)
        self.mydb.commit()
        if self.mycursor.rowcount > 0:
            return True
        else:
            return False
        
    def insert_products(self, product_name, description, price, stock, category_id):
        sql = "INSERT INTO products VALUES (%s, %s, %s, %s, %s, %s)"
        val_sql = (None, product_name, description, price, stock, category_id)
        self.mycursor.execute(sql, val_sql)
        self.mydb.commit()
        if self.mycursor.rowcount > 0:
            return True
        else:
            return False
    
    def insert_categories(self, name):
        sql = "INSERT INTO categories VALUES (%s, %s)"
        val_sql = (None, name)
        self.mycursor.execute(sql, val_sql)
        self.mydb.commit()
        if self.mycursor.rowcount > 0:
            return True
        else:
            return False
        
    def insert_orders(self, user_id, order_date, total_amount, status, product_id):
        sql = "INSERT INTO orders VALUES (%s, %s, %s, %s, %s, %s)"
        val_sql = (None, user_id, order_date, total_amount, status, product_id)
        self.mycursor.execute(sql, val_sql)
        self.mydb.commit()
        if self.mycursor.rowcount > 0:
            return True
        else:
            return False
ใ
table = Managerdb("localhost", "root", "1234", "shop")

print(table)