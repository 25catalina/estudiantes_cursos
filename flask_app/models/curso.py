from flask_app.config.mysqlconnection import connectToMySQL

class Curso:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cursos;"
        results = connectToMySQL('esquema_estudiantes_cursos').query_db(query)
        cursos = []
        for curso in results:
            cursos.append(cls(curso))
        return cursos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO cursos (nombre, created_at, updated_at) VALUES (%(nombre)s, NOW(), NOW());"
        resultado = connectToMySQL("esquema_estudiantes_cursos").query_db(query, data)
        return resultado