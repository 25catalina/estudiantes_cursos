from flask_app.config.mysqlconnection import connectToMySQL

class Estudiante:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.edad = data['edad']
        self.curso_id = data['curso_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM estudiantes;"
        results = connectToMySQL('esquema_estudiantes_cursos').query_db(query)
        estudiantes = []
        for estudiante in results:
            estudiantes.append(cls(estudiante))
        return estudiantes

    @classmethod
    def save(cls, data):
        query = "INSERT INTO estudiantes (nombre, apellido, edad, curso_id, created_at, updated_at) VALUES (%(nombre)s, %(apellido)s, %(edad)s, %(curso_id)s, NOW(), NOW());"
        return connectToMySQL('esquema_estudiantes_cursos').query_db(query, data)

    @classmethod
    def get_estudiantes_de_curso(cls, data):
        query = "SELECT * FROM estudiantes WHERE curso_id = %(id)s;"
        results = connectToMySQL('esquema_estudiantes_cursos').query_db(query, data)
        resultado = []
        for estudiante in results:
            resultado.append(cls(estudiante))
        return resultado