from flask import Flask, render_template, session, request

from managers.data_manager import DataManager
from managers.graph_manager import GraphManager
from managers.property_manager import PropertiesManager

app = Flask(__name__)


@app.route('/')
def main():
    json_data = PropertiesManager.read_properties()
    return render_template('main.html', init_dict = json_data)


@app.route('/uploadCSV', methods=['POST'])
def upload_and_read_csv():
    return_string = DataManager.upload_read_csv_file()
    min_date, max_date = DataManager.get_max_min_dates()
    session['min_date'] = min_date
    session['max_date'] = max_date
    return return_string


@app.route('/calculate_linear_graphs', methods=['POST'])
def make_graphs():
    # This is callback function from an asynchronous request.
    form_dict = request.form.to_dict() # contains all form data in dictionary form to make graphs

    # Note:  DataFrame is cached in DataManager.static_data_frame, which is a class attribute.
    data_frame = DataManager.static_data_frame
    # Get html with imbedded graph images
    returnedHTML = GraphManager.render_graphs_HTML(form_dict, data_frame)
    return returnedHTML


if __name__ == '__main__':
    app.secret_key = 'prunknurp'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(port=5004, debug=True)