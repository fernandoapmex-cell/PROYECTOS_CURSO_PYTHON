from flask import Flask, request, render_template, url_for, jsonify, session
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

app = Flask(__name__)
app.secret_key='Mi_llave_secreta'

@app.route('/')
def inicio():
    if 'username' in session:
        return f'El usuario ya ah echo login{session["username"]}'
    #app.logger.debug('Mensaje nivel debug')
    #app.logger.info(f'Entramos al path {request.path}')
    # app.logger.warning('Mensaje nivel warning')
    # app.logger.error('Mensaje nivel error')
    return 'No ah echo login'
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #Omitimos validacion de usuario y password
        usuario = request.form['username']
        #agregar el usuario a la sesion
        session['username'] = usuario
        #regresamos a la pagina de inicio
        return redirect(url_for('inicio'))
    return render_template('login.html')
@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f'Saludos {nombre.upper()}..'

@app.route('/edad/<int:edad>')
def edad(edad):
    return f'Edad: {edad}'

@app.route('/mostrar/<nombre>',methods=['GET','POST'])
def mostrar_nombre(nombre):
    return render_template('mostrar.html',nombre=nombre)

@app.route('/redireccionar')
def redireccionar():
    return redirect(url_for('mostrar_nombre',nombre='Juan'))
@app.route('/salir')
def salir():
    return abort(404)
@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('error404.html',error=error), 404
#REST Representational state transfer
@app.route('/api/mostrar/<nombre>',methods=['GET','POST'])
def  mostrar_json(nombre):
    valores = {'nombre': nombre,'metodo HTTP':request.method}
    return jsonify(valores)
@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('inicio'))

