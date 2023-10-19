from flask import Flask, render_template, request, jsonify
import json
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = {
            'name': request.form['name'],
            'email': request.form['email'],
            'address': request.form['address'],
            'land_type': request.form['land_type'],
            'season': request.form['season'],
            'water_resources': request.form['water_resources'],
            'details': request.form['details']
        }
        with open('data.json', 'a') as json_file:
            json.dump(data, json_file)
            json_file.write('\n')
        return jsonify({'message': 'Data saved successfully!'})
    return render_template('page.html')


if __name__ == '__main__':
    app.run(debug=True)




# from flask import Flask, render_template, request, jsonify
# import json
# app = Flask(__name__)
#
#
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         data = {
#             'name': request.form['name'],
#             'email': request.form['email'],
#             'address': request.form['address'],
#             'land': request.form['land'],
#             'season': request.form['season'],
#             'water': request.form['water'],
#             'message': request.form['message'],
#         }
#         save_to_json(data)
#         return "Data saved successfully."
#     return render_template('test.html')
#
#
# def save_to_json(data):
#     with open('data.json', 'a') as json_file:
#         json.dump(data, json_file)
#         json_file.write('\n')
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
