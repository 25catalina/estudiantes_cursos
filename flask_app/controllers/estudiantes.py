from flask_app import app #Importamos la app

from flask import render_template,redirect,request,session,flash


#importamos la clase que estamos controlando
from flask_app.models.estudiante import Estudiante

@app.route("/crear_estudiante", methods=["GET"])
def registro():
    estudiantes = Estudiante.get_all()
    print(estudiantes)
    return render_template("crear_estudiante.html")

@app.route('/guardar_estudiante', methods=["POST"])
def guardar():
    data = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "edad": request.form['edad']
    }
    Estudiante.save(data)
    return redirect("/mostrar_cursos")


