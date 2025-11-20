from flask import Flask, render_template, request, url_for
from flask_migrate import Migrate
from werkzeug.utils import redirect

from database import db
from models import Persona
from forms import PersonaForm

app = Flask(__name__)

#configuracion de la db

USER_DB = 'postgres'
PASS_DB = 'admin'
URL_DB = 'localhost'
NAME_DB = 'sap_flask_db'
PORT_DB = '5432'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}:{PORT_DB}/{NAME_DB}'
app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#inicializamos la bae de datos
db.init_app(app)

#configuramos flask-migrate para hacer migraciones a la base de datos
migrate=Migrate()
migrate.init_app(app, db)
#configuracion de flask wtf
app.config['SECRET_KEY'] = 'llave_secreta'

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def inicio():
    #listado de personas
    #personas= Persona.query.all()
    personas=Persona.query.order_by('id')
    total_personas=Persona.query.count()
    app.logger.debug(f'Listado de personas: {personas}')
    app.logger.debug(f'Listado de total: {total_personas}')
    return render_template('index.html', personas=personas, total_personas=total_personas)
@app.route('/ver/<int:id>')
def ver_detalle(id):
    #recuperamos la persona segun el id proporcionado
    persona=Persona.query.get_or_404(id)
    app.logger.debug(f'Ver persona: {persona}')
    return render_template('detalle.html', persona=persona)
@app.route('/agregar',methods=['GET', 'POST'])
def agregar():
    persona =Persona()
    personaForm=PersonaForm(obj=persona)
    if request.method == 'POST':
        if personaForm.validate_on_submit():
            #aca llenamos el objeto con los datos del formulario
            personaForm.populate_obj(persona)
            #app.logger.debug(f'Persona a insertar: {persona}')}
            #insertamos le nuevo registro
            db.session.add(persona)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('agregar_persona.html', forma=personaForm)

@app.route('/editar/<int:id>',methods=['GET', 'POST'])
def editar(id):
    #recuperamos el objeto persona a editar
    persona=Persona.query.get_or_404(id)
    personaForma=PersonaForm(obj=persona)
    if request.method == 'POST':
        if personaForma.validate_on_submit():
            personaForma.populate_obj(persona)
            #editamos el registro
            app.logger.debug(f'Editar a persona: {persona}')
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('editar_persona.html', forma=personaForma)
@app.route('/eliminar/<int:id>')
def eliminar(id):
    persona=Persona.query.get_or_404(id)
    app.logger.debug(f'Eliminar a persona: {persona}')
    db.session.delete(persona)
    db.session.commit()
    return redirect(url_for('inicio'))






