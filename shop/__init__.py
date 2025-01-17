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
    val_sql = (val,id)
    mycursor.execute(sql,val_sql)
    database.mydb.commit()
    if mycursor.rowcount > 0:
        return True
    else:
        return False
# print(editdb("product","product_name","product_id",8,"ไอโฟน10"))
#----------------------------------------------------
def insert_product(name, description, price, stock):
    try:
        # คำสั่ง SQL สำหรับการแทรกข้อมูลลงในตาราง product
        sql = "INSERT INTO product (name, description, price, stock) VALUES (%s, %s, %s, %s)"
        
        # เตรียมค่าที่จะส่งไปในคำสั่ง SQL
        val_sql = (name, description, price, stock)
        
        # รันคำสั่ง SQL
        mycursor.execute(sql, val_sql)
        
        # ทำการ commit การเปลี่ยนแปลงลงฐานข้อมูล
        database.mydb.commit()
        
        # เช็คว่ามีการแทรกข้อมูลสำเร็จหรือไม่
        if mycursor.rowcount > 0:  # แถวถูกแทรก
            return True
        else:
            return False
    except mysql.connector.Error as err:
        # ถ้ามีข้อผิดพลาดในการเชื่อมต่อหรือคำสั่ง SQL
        print(f"Error: {err}")
        return False

# ตัวอย่างการเรียกใช้งาน
print(insert_product("เสื้อผ้า", "เสื้อผ้าผู้ชายขนาด M", 499.99, 100))  
# print(insert_product())
#----------------------------------------------------
def insert_categories(name):
    try:
        # คำสั่ง SQL สำหรับการแทรกข้อมูลลงในตาราง categories
        sql = "INSERT INTO categories (category_name) VALUES (%s)"
        
        # เตรียมค่าที่จะส่งไปในคำสั่ง SQL
        val_sql = (name,)
        
        # รันคำสั่ง SQL
        mycursor.execute(sql, val_sql)
        
        # ทำการ commit การเปลี่ยนแปลงลงฐานข้อมูล
        database.mydb.commit()
        
        # เช็คว่ามีการแทรกข้อมูลสำเร็จหรือไม่
        if mycursor.rowcount > 0:  # แถวถูกแทรก
            return True
        else:
            return False
    except mysql.connector.Error as err:
        # ถ้ามีข้อผิดพลาดในการเชื่อมต่อหรือคำสั่ง SQL
        print(f"Error: {err}")
        return False

# ตัวอย่างการเรียกใช้งาน
print(insert_categories("เสื้อผ้า"))      