import matplotlib.pyplot as plt
from models.linear_graph_generator import LinearGraphGenerator


class GraphManager():
    @staticmethod
    def render_graphs_HTML(form_dict, data_frame):
        """
        First calls create_linear_Q_graphs() that saves the 4 graph images, then creates and returns the HTML
        that eventually displays the images in the display <div> of the main page.
        :param form_dict:
        :param data_frame:
        :return:  A String of HTML that when placed in .innerHTML property of a <div> displays the imgages
        """
        GraphManager.create_linear_Q_graphs(form_dict, data_frame)
        html_str = ""
        html_str += "<div id='Q1' class='box'>" + "<img src='/static/graphimages/linearQ1.png' " \
                                                  "class='linearImgSize'/>" + "</div>"
        html_str += "<div id='Q2' class='box'>" + "<img src='/static/graphimages/linearQ2.png' " \
                                                  "class='linearImgSize'/>" + "</div>"
        html_str += "<div id='Q3' class='box'>" + "<img src='/static/graphimages/linearQ3.png' " \
                                                  "class='linearImgSize'/>" + "</div>"
        html_str += "<div id='Q4' class='box'>" + "<img src='/static/graphimages/linearQ4.png' " \
                                                  "class='linearImgSize'/>" + "</div>"
        return html_str

    @staticmethod
    def create_linear_Q_graphs(form_dict, data_frame):
        """
        Use the form_dict to extract the input values and use the data_frame to plot the linear graphs.  There
        must be 4 graphs, one for each quarter.  Their names MUST be linearQ1.png, linearQ2.png, linearQ3.png,
        and linearQ4.png.  The images MUST be stored in the project directory: /static/graphimages
        NOTE:  Plots are saved with matplotlib.plt.savefig("linearQ1.png", bbox_inches='tight').  The second
        parameter, bbox_inches removes a default white border around the image.
        :param form_dict: A Python Dictionary of form parameters.  The keys are the input names in the form.
        :param data_frame: The data frame read from the csv file.
        :return: Nothing to return since this method stores the graph images in the specified directory.
        """
        plot = LinearGraphGenerator.generate_Q_graphs(form_dict, data_frame)

        for counter in range(1,5):
            plot.figure(counter)
            plot.savefig("static/graphimages/linearQ" + str(counter) + ".png")

        return