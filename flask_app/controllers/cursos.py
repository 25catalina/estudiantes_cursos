from flask_app import app #Importamos la app

from flask import render_template,redirect,request,session,flash


#importamos la clase que estamos controlando

from flask_app.models.curso import Curso

@app.route("/", methods=["GET", "POST"])
def registro():
    cursos = Curso.get_all()
    print(cursos)
    return render_template("menu.html", cursos=cursos)

@app.route('/guardar_curso', methods=["POST"])
def guardar():
    data = {
        "nombre": request.form['nombre'],
    }
    Curso.save(data)
    return redirect("/mostrar_cursos")


@app.route("/mostrar_cursos")
def mostrar_cursos():
    cursos = Curso.get_all()
    return render_template("mostrar_cursos.html", cursos=cursos)