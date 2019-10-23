from io import BytesIO
import matplotlib.pyplot as plt



class LinearGraphGenerator:
    """
    This class generates the quarterly plots.  Strategy is to
    create a pyplot with multiple figures  for each quarter and to return that pyplot
    """
    @staticmethod
    def generate_Q_graphs(form_dict, data_frame):
        """
        Generate 4 graph images from input parameters form_dict and
        data frame data_frame.  Return a list of images
        """
        for keys, values in form_dict.items():
            print (keys, values)

        # Create some dummy data for plots
        qx = [1,2,3,4,5,6,7,8,9,10,11,12]
        q1y = [0.5,0.4,0.6,0.4,0.2,0.1,0.6,0.7,0.8,0.8,0.7,0.5]
        q2y = [0.2,0.4,0.5,0.6,0.7,0.8,0.9,0.8,0.9,0.5,0.4,0.6]
        q3y = [0.3,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.5,0.6,0.5,0.6]
        q4y = [0.4,0.3,0.5,0.4,0.7,0.8,0.7,0.6,0.5,0.4,0.3,0.1]
        LinearGraphGenerator.generate_Q_graph(qx, q1y, 1)
        LinearGraphGenerator.generate_Q_graph(qx, q2y, 2)
        LinearGraphGenerator.generate_Q_graph(qx, q3y, 3)
        LinearGraphGenerator.generate_Q_graph(qx, q4y, 4)

        return plt

    @staticmethod
    def generate_Q_graph(qx, qy, quarter_no):
        plt.figure(quarter_no)
        plt.scatter(qx, qy)
        plt.title('Quarter' + str(quarter_no))
        # img = BytesIO()
        # plt.savefig(img)
        # img.seek(0)
        return
