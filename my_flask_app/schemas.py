from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True, validate=validate.Length(min=6))
    created_at = fields.DateTime(dump_only=True)

class TaskSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    title = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    description = fields.Str()
    status = fields.Str(validate=validate.OneOf(["pending", "in progress", "completed"]))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)
task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
