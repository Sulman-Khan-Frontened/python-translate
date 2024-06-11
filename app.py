from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/translate', methods=['POST'])
def translate():
    try:
        data = request.get_json()
        text = data['text']
        dest = data['dest']
        translated = translator.translate(text, dest=dest)
        return jsonify({
            'translated_text': translated.text,
            'src': translated.src,
            'dest': translated.dest
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
