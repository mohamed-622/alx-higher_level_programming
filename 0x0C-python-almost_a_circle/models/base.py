#!/usr/bin/python3

""" base class for the entir project """

class Base:
    
    __nb_objects = 0
    
    def __init__(self, id=None):
        
        if id is not None:
            self.id = id
        
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
    
     @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
    
    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        json_list = []
        if list_objs is not None:
            json_list = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(json_list))
    
    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return dummy
    
    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_data = file.read()
                dictionaries = cls.from_json_string(json_data)
                instances = [cls.create(**dictionary) for dictionary in dictionaries]
                return instances
        except FileNotFoundError:
            return []