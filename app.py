from flask_app import app #Importamos la app de la carpeta flask_app
from flask_app.controllers import cursos

if __name__ == "__main__":
    app.run(debug=True)