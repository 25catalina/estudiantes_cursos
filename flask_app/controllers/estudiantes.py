from flask_app import app #Importamos la app

from flask import render_template,redirect,request,session,flash


#importamos la clase que estamos controlando
from flask_app.models.estudiante import Estudiante
from flask_app.models.curso import Curso


@app.route("/estudiante", methods=["GET"])
def registro_estudiante():
    cursos = Curso.get_all()
    return render_template("crear_estudiante.html", cursos=cursos)

@app.route('/guardar_estudiante', methods=["POST"])
def guardar_estudiante():
    data = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "edad": request.form['edad'],
        "curso_id": request.form['curso_id']
    }
    Estudiante.save(data)
    return redirect("/cursos")


