from flask import Flask, render_template, url_for, jsonify, request
from translate import get_translation

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate-text', methods=['POST'])
def translate_text():
    data = request.get_json()
    text_input = data['text']
    translation_output = data['to']
    response = get_translation(text_input, translation_output)
    return jsonify(response)