# from flask import Flask, render_template, request
# from mtranslate import translate as m_translate

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/translate', methods=['POST'])
# def translate():
#     data = request.json
#     input_text = data.get('input_text')
#     dest_language = data.get('dest_language')
#     if not input_text or not dest_language:
#         return 'Missing input_text or dest_language', 400
#     translated_text = m_translate(input_text, dest_language)
#     return translated_text


# from flask import Flask, request, jsonify
# from mtranslate import translate as m_translate

# app = Flask(__name__)

# @app.before_request
# def before_request():
#     # Check if the request content type is not JSON
#     if request.method in ['POST', 'PUT', 'PATCH'] and request.content_type != 'application/json':
#         # Change the request content type to JSON
#         request.environ['CONTENT_TYPE'] = 'application/json'

# @app.route('/translate', methods=['POST'])
# def translate():
#     # Handle the translation logic here
#     data = request.json  # Access JSON data from the request body
#     # Perform translation and return the result
#     translated_text = translate_function(data['input_text'], data['dest_language'])
#     return jsonify({'translated_text': translated_text})

# # Run the Flask app
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, jsonify
from mtranslate import translate as m_translate

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    if request.is_json:
        data = request.json
    else:
        data = request.form

    input_text = data.get('input_text')
    dest_language = data.get('dest_language')

    if not input_text or not dest_language:
        return jsonify({'error': 'Missing input_text or dest_language'}), 400

    translated_text = m_translate(input_text, dest_language)
    return jsonify({'translated_text': translated_text})

if __name__ == "__main__":
    app.run(debug=True)
