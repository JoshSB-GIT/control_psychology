from models.Roles import RolesModel

class RolesController():

    def get_roles(self):
        response = 'Rol no encontrado', 404
        rol = RolesModel.query.all()

        if rol is None:
            return response

        response = {
            'rol_id': rol.rol_id,
            'name': rol.name,
            'description': rol.description,
            'status': rol.status,
            'created_at': rol.created_at,
            'updated_at': rol.updated_at
        }

        return response, 200