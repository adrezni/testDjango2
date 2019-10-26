import json
from flask import request


class PropertiesManager():
    data_url = 'properties/default_properties.json'
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

    @staticmethod
    def write_properties():
        json_dict = PropertiesManager.read_properties()
        min_dump_dist = request.form['minDumpDistP']
        max_dump_dist = request.form['maxDumpDistP']
        min_trav = request.form['minFullTravelDurationP']
        max_trav = request.form['maxFullTravelDurationP']
        num_trips = request.form['minTripsP']
        date_col_name = request.form['dateColNameP']

        json_dict['min_dump_dist'] = min_dump_dist
        json_dict['max_dump_dist'] = max_dump_dist
        json_dict['min_travel_duration'] = min_trav
        json_dict['max_travel_duration'] = max_trav
        json_dict['num_trips'] = num_trips
        json_dict['date_col_name'] = date_col_name

        temp = json.dumps(json_dict)
        f = open(PropertiesManager.data_url, "w")
        #f = open('properties/test.json', "w")
        f.write(temp)
        f.close()
