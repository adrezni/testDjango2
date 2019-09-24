import json

class PropertiesManager():
    @staticmethod
    def read_properties():
        """
        Read properties file found in /properties/default_properties.json
        :return: Python dictionary of properties
        """
        data_url = 'properties/default_properties.json'
        with open(data_url) as json_file:
            json_str = json_file.read()
        json_dict = json.loads(json_str)
        return json_dict
