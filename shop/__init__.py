import database
mycursor = database.mydb.cursor()
#----------------------------------------------------
def selectdb(table):
    sql = f"SELECT * FROM {table}"
    mycursor.execute(sql)
    show = mycursor.fetchall()
    return show
#----------------------------------------------------
def deletedb(table,id_name,id):
    sql = f"DELETE FROM {table} WHERE {id_name} = {id}"
    mycursor.execute(sql)
    database.mydb.commit()
    if mycursor.rowcount > 0:
        return True
    else:
        return False
#----------------------------------------------------
def editdb(table,colum,id_name):
    sql = f"UPDATE {table} SET {colum} = %s WHERE {id_name} = %s"
    val_sql = (None,id)
    mycursor.execute(sql,val_sql)
    database.mydb.commit()
    if mycursor.rowcount > 0:
        return True
    else:
        return False
# print(editdb("product","product_name","product_id",8,"ไอโฟน10"))
#----------------------------------------------------
def insert_product(name,description,price,stock):
    sql = "INSERT INTO product VALUES (%s,%s,%s,%s)"
    val_sql =(None,name,description,price,stock)
    mycursor.execute(sql,val_sql)
    database.mydb.commit()
    if mycursor.rowcount > 0:
        return True
    else:
        return False
# print(insert_product())
#----------------------------------------------------
def insert_categories(name):
    sql = "INSERT INTO categories VALUES (%s,%s)"
    val_sql =(None,name)
    mycursor.execute(sql,val_sql)
    database.mydb.commit()
    if mycursor.rowcount > 0:
        return True
    else:
        return False
print(insert_categories("เสื้อผ้า"))      