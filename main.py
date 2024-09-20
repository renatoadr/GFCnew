#!python3

from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/home', methods=['POST'])
def abrir_home(): 
#    print(request.values)
#    print(request.CombinedMultiDict()
#    email =  request.args.get('email')
#    email =  request.form.getlist('email')
#    for x in email:
#        print(x)  
#    print(request.form.values().lenght)
    for key, value in request.form.items():
        print("key: {0}, value: {1}".format(key, value))
#    for i in request.form.items():
#        print(i)
    return render_template("home.html")

@app.route('/cad_empreend')
def abrir_cad_empreend():
    return render_template("cad_empreend.html")

@app.route('/efetuar_cad_empreend', methods=['POST'])
def efetuar_cad_empreend():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="BIM@db2024"
    )

    mySql_insert_query = """INSERT INTO db_fgc.tb_empreendimentos (Id_empreendimento, nm_empreendimento) 
                VALUES (1, 'GFC') """
    cursor = connection.cursor()     
    cursor.execute(mySql_insert_query)     
    connection.commit()     
    print(cursor.rowcount,"Record inserted successfully into Laptop table")     
    cursor.close()
    connection.close()

    return render_template("home.html")

'''    print(mydb)
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM mysql.tb_empreendimento")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
'''
app.run()