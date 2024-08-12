from marshmallow import Schema, fields, validate

class UrlSchema(Schema):
    id = fields.Int(dump_only=True)
    original_url = fields.Url(required=True, validate=validate.Length(min=1))
    short_url = fields.Str(required=True, validate=validate.Length(min=1))
