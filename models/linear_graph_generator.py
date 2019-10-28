from io import BytesIO
import base64
import matplotlib.pyplot as plt
from modeldata.form_q_dataframe import FormQDataFrame


class LinearGraphGenerator:
    """
    This class generates the quarterly plots.  Strategy is to
    create a pyplot with multiple figures and save each figure as an encoded base64 string.
    """
    @staticmethod
    def generate_Q_graphs(form_dict, data_frame):
        """
        Generate 4 graph images from input parameters form_dict and
        data frame data_frame.  Return as 4 base64 encoded strings
        """
        qx, q1y, q2y, q3y, q4y, q11y, q21y, q31y, q41y = \
            FormQDataFrame.create_Q_dataframe(form_dict, data_frame)

        encoded1 = LinearGraphGenerator.generate_Q_graphNew(qx, q1y, qx, q11y, 1)
        encoded2 = LinearGraphGenerator.generate_Q_graphNew(qx, q2y, qx, q21y,2)
        encoded3 = LinearGraphGenerator.generate_Q_graphNew(qx, q3y, qx, q31y,3)
        encoded4 = LinearGraphGenerator.generate_Q_graphNew(qx, q4y, qx, q41y, 4)

        return encoded1, encoded2, encoded3, encoded4

    @staticmethod
    def generate_Q_graph(qx, qy, quarter_no):
        plt.figure(quarter_no)
        plt.scatter(qx, qy)
        plt.title('Quarter' + str(quarter_no))
        buffer = BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)
        encoded = base64.b64encode(buffer.getvalue()).decode("ascii")
        return encoded

    @staticmethod
    def generate_Q_graphNew(qx1,qy1,qx2,qy2,quarter_no):
        fig = plt.figure(quarter_no)
        ax1 = fig.add_subplot(111)
        ax1.scatter(qx1, qy1, c='b')
        ax1.scatter(qx2, qy2, c='g')
        plt.title('Quarter' + str(quarter_no))
        buffer = BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)
        encoded = base64.b64encode(buffer.getvalue()).decode("ascii")
        return encoded
