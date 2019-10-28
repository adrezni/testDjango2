import pandas as pd


class FormQDataFrame:
    @staticmethod
    def create_Q_dataframe(param_dict, original_dataframe):
        """
        Create the dataframe or arrays that will be used for the Q graphs
        :param param_dict: Python dict of user defined parameters
        :param original_dataframe: Original dataframe as read from csv
        :return: New dataframe for use in plotting Q graphs
        """
        for keys, values in param_dict.items():  #this code just shows how to retrieve the form data
            print (keys, values)
        # Create some dummy data for plots
        qx = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        q1y = [0.5, 0.4, 0.6, 0.4, 0.2, 0.1, 0.6, 0.7, 0.8, 0.8, 0.7, 0.5]
        q2y = [0.2, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.8, 0.9, 0.5, 0.4, 0.6]
        q3y = [0.3, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.5, 0.6, 0.5, 0.6]
        q4y = [0.4, 0.3, 0.5, 0.4, 0.7, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.1]

        q11y = (pd.Series(q1y) * 0.2).tolist()
        q21y = (pd.Series(q2y) * 0.2).tolist()
        q31y = (pd.Series(q3y) * 0.2).tolist()
        q41y = (pd.Series(q4y) * 0.2).tolist()

        return qx, q1y, q2y, q3y, q4y, q11y, q21y, q31y, q41y