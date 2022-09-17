import mysql.connector
class Principal:
    def ListarPersona(self):
        try:
            mydb = mysql.connector.connect(host="localhost",
            user="root",
            password="",
            port="3306",
            database='ajax')
            mycursos = mydb.cursor()
            mycursos.execute("SELECT * FROM persona")
            myresult = mycursos.fetchall()
            for x in myresult:
                print(x)
        except:
            print("Error  !!!!")
objPrincipal = Principal()
objPrincipal.ListarPersona()
