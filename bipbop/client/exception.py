# BIPBOPB
# -*- coding: utf-8 -*-

class Exception(Exception):

    INVALID_ARGUMENT = 1 

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message.encode('utf-8')
    
    def get_bipbop_code(self):
        return self.bipbop_code

    def get_bipbop_source(self):
        return self.bipbop_source

    def get_bipbop_id(self):
        return self.bipbop_id
    
    def get_bipbop_message(self):
        return self.bipbop_message

    def get_bipbop_pushable(self):
        return self.bipbop_pushable

    def set_attributes(self, code, source, id, message, pushable):
        self.bipbop_code = code
        self.bipbop_source = source
        self.bipbop_id = id
        self.bibpbop_message = message
        self.bipbop_pushable = pushable
