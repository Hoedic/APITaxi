# -*- coding: utf8 -*-
from flask.ext.restplus import fields as basefields

class Date(basefields.BaseField):
    __schema_type__ = 'date'
    __schema_format__ = None

    def schema(self):
        return {
            'type': self.__schema_type__,
            'format': self.__schema_format__,
            'title': self.title,
            'description': self.description,
            'readOnly': self.readonly,
        }

    def format(self):
        return self.isoformat()

    def output(self, key, value):
        if isinstance(value, dict):
            return value[key]
        value = value[key]
        if isinstance(value, str):
            return value
        date = getattr(value, key)
        return date.isoformat() if date else None
