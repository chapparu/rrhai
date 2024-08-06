from flask import Flask
from flask_restful import Api
from config import Config
from models import db
from resources import UserListResource, UserResource, TaskListResource, TaskResource

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
api = Api(app)

api.add_resource(UserListResource, '/users')
api.add_resource(UserResource, '/users/<int:id>')
api.add_resource(TaskListResource, '/tasks')
api.add_resource(TaskResource, '/tasks/<int:id>')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
