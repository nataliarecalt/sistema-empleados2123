from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL

app=Flask(__name__) #instanciamos flask

mysql= MySQL()  #instancia de conexion a la base de datos
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'    #es el nombre de usuario de xammp
app.config['MYSQL_DATABASE_PASSWORD']=''    #password no tiene xammp
app.config['MYSQL_DATABASE_DB']='sistema2123'   #el nombre de la base de datos que creamos en mysql
mysql.init_app(app)


@app.route('/') #rooteo cuando se entra al servidor, se ejecuta la funcion index

#cada vez que se ejecuta crea un nuevo registro en la base de datos
def index():
    sql="INSERT INTO `empleados` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, 'Natalia', 'natyrec93@gmail.com', 'fotodenat.jpg');"  #inserta en la base de datos un registro al ingresar
    conn=mysql.connect()    #abrimos la conexion a la base de datos
    cursor=conn.cursor()    #crea un cursor
    cursor.execute(sql)    #ejecuta
    conn.commit()   #hace un commit

    return render_template('empleados/index.html')  #la funcion retorna el index dentro de la carpeta empleados usando render_templates

if __name__ =='__main__':
    app.run(debug=True) 

