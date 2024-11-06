from database.DB_connect import DBConnect
from model.product import Product


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getYear():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor()
            query = """select distinct YEAR(gds.`Date`) from go_daily_sales gds"""
            cursor.execute(query)
            for row in cursor:
                result.append(row[0])
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def getColors():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor()
            query = """select distinct Product_color from go_products gp """
            cursor.execute(query)
            for row in cursor:
                result.append(row[0])
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def getProducts(color):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select * from go_products gp where Product_color = %s"""
            cursor.execute(query, (color,))
            for row in cursor:
                result.append(Product(**row))
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def getArchi(anno):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor()
            query = """select gds1.Product_number, gds2.Product_number, count(distinct(gds1.Date)) as peso
                from go_daily_sales gds1, go_daily_sales gds2 
                where gds1.Product_number < gds2.Product_number and gds1.Retailer_code = gds2.Retailer_code 
                and year(gds1.`Date`) = %s and gds1.`Date` = gds2.`Date`
                group by gds1.Product_number, gds2.Product_number"""
            cursor.execute(query, (anno,))
            for row in cursor:
                result.append(row)
            cursor.close()
            cnx.close()
            return result
