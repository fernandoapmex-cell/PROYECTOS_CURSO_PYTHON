from flask import Flask, render_template, url_for
from werkzeug.utils import redirect

import cliente_dao
import cliente_form
from cliente import Cliente
from cliente_dao import ClienteDAO
from cliente_form import  ClienteForma

app = Flask(__name__)

app.config['SECRET_KEY'] = 'llave_secreta'

titulo_app = 'Zona Fit (GYM)'

@app.route('/')  # url: http://localhost:5000/
@app.route('/index.html')  # url http://localhost:5000/index.html
def inicio():
    app.logger.debug('Entramos al path de inicio /')
    # Recuperamos los clientes de la bd
    clientes_db = ClienteDAO.seleccionar()
    #creamos un objeto de formulario cliente vacio
    cliente=Cliente()
    #usamos el cliente vacio para crear el formulario vacio
    cliente_forma=ClienteForma(obj=cliente)
    return render_template('index.html', titulo=titulo_app, clientes=clientes_db,forma=cliente_forma)
@app.route('/guardar',methods=['POST'])
def guardar():
    #creamos un cliente vacio
    cliente = Cliente()
    #creamos la forma de cliente
    cliente_form = ClienteForma(obj=cliente)
    if cliente_form.validate_on_submit():
        #llenamos el objeto cliente con los valores del formulario
        cliente_form.populate_obj(cliente)
        if not cliente.id:
            #guardamos el nuevo client en la base de datos
            ClienteDAO.insertar(cliente)
        elif cliente.id:
            #editamos el cliente
            ClienteDAO.actualizar(cliente)
    #redireccionamos a la pagina deinicio con el metodo inicio para cargar tabla
    return redirect(url_for('inicio'))
@app.route('/limpiar')
def limpiar():
    return redirect(url_for('inicio'))
@app.route('/editar/<int:id>')
def editar(id):
    cliente=ClienteDAO.seleccionar_id(id)
    cliente_forma=ClienteForma(obj=cliente)
    #recuperar el listado de clientes para volver a mostrarlo en la plantilla
    clientes_db=ClienteDAO.seleccionar()
    return render_template('index.html',titulo=titulo_app,clientes=clientes_db,forma=cliente_forma)
@app.route('/eliminar/<int:id>')
def eliminar(id):
    cliente=Cliente(id=id)
    ClienteDAO.eliminar(cliente)
    return redirect(url_for('inicio'))
if __name__ == '__main__':
    app.run(debug=True)
