import os
import pandas as pd

from flask import request, session


class DataManager:
    """
    This class manages the external data that is read from a CSV file.  It uploads the user's CSV file to the server
    ( upload_csv_file()), and creates a Pandas DataFrame (create_dataframe()) where the DataFrame is stored in a class
    attribute called static_data_frame.  This data member serves as a cache of the DataFrame so that loading of the CSV
    into a DataFrame is done only once.
    """
    # Declare a class attribute ( similar to Java 'static' variable), static_data_frame.  The value of
    # DataManager.static_data_frame is the same for all instances of DataManager.
    static_data_frame = None
    @staticmethod
    def upload_read_csv_file():
        """
        Get the csv file name from the request.  Upload the csv file to the server in directory
        'external_data'.  Put the filename into the session.  Then call upon create_dataframe()
        :return: Return success message.
        """
        csv_file = request.files['filechooser']
        csv_file.save(os.path.join('external_data', csv_file.filename))
        # Save the CSV file name in the session for display purposes.
        session['csvfilename'] = csv_file.filename
        DataManager.create_dataframe()
        return "File Successfully Uploaded and DataFrame Created"

    @staticmethod
    def get_max_min_dates():
        return DataManager.static_data_frame['Date'].min(), DataManager.static_data_frame['Date'].max()

    @staticmethod
    def create_dataframe():
        """
        Create Pandas DataFrame from the csv file stored in directory 'external_data'.  The file name
        is retrieved from the session with key: 'csvfilename'. The DateFrame is stored in the  static
        class variable, static_data_frame
        :return: No return value
        """
        csv_filename = session['csvfilename']
        file_url = os.path.join("external_data", csv_filename)
        DataManager.static_data_frame = pd.read_csv(file_url)
        return


