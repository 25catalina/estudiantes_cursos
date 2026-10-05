from flask_app import app #Importamos la app

from flask import render_template,redirect,request,session,flash


#importamos la clase que estamos controlando

from flask_app.models.curso import Curso
from flask_app.models.estudiante import Estudiante

@app.route("/")
def inicio():
    return redirect("/cursos")

@app.route("/cursos")
def cursos_page():
    cursos = Curso.get_all()
    return render_template("menu.html", cursos=cursos)

@app.route("/crear_curso", methods=["POST"])
def crear_curso():
    data = {
        "nombre": request.form["nombre"]
    }
    Curso.save(data)
    return redirect("/cursos")

@app.route("/cursos/<int:id>")
def mostrar_curso(id):
    datos = {"id": id}
    curso = Curso.get_one(datos)
    estudiantes = Estudiante.get_estudiantes_de_curso(datos)
    return render_template("mostrar_cursos.html", curso=curso, estudiantes=estudiantes)