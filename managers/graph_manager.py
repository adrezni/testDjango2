from models.linear_graph_generator import LinearGraphGenerator


class GraphManager():
    @staticmethod
    def render_graphs_HTML(form_dict, data_frame):
        """
        First calls LinearGraphGenerator.generate_Q_graphs() that returns the 4 graph images as base64 encoded
        strings, then creates and returns the HTML
        that eventually displays the images in the display <div> of the main page.
        :param form_dict: a dictionary of user parameters
        :param data_frame: a Python dataFrame that contains the data to plot
        :return:  A String of HTML that when placed in .innerHTML property of a <div> displays the graph imgages
        """

        buff1, buff2, buff3, buff4 = LinearGraphGenerator.generate_Q_graphs(form_dict, data_frame)

        html_str = ""
        html_str += "<div id='Q1' class='box'>" + "<img src = 'data:image/png;base64, " + buff1 + "' class='linearImgSize'/ >" + "</div>"
        html_str += "<div id='Q2' class='box'>" + "<img src = 'data:image/png;base64, " + buff2 + "' class='linearImgSize'/ >" + "</div>"
        html_str += "<div id='Q3' class='box'>" + "<img src = 'data:image/png;base64, " + buff3 + "' class='linearImgSize'/ >" + "</div>"
        html_str += "<div id='Q4' class='box'>" + "<img src = 'data:image/png;base64, " + buff4 + "' class='linearImgSize'/ >" + "</div>"
        return html_str

