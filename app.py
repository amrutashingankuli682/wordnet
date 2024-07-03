from flask import Flask, render_template, request, jsonify
import nltk
from nltk.corpus import wordnet

app = Flask(__name__)

# Download WordNet data
nltk.download('wordnet')

# Function to get synonyms and antonyms
def get_synonyms_antonyms(word):
    synonyms = []
    antonyms = []

    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
            if lemma.antonyms():
                antonyms.append(lemma.antonyms()[0].name())

    return list(set(synonyms)), list(set(antonyms))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/synonyms_antonyms')
def synonyms_antonyms():
    word = request.args.get('word')
    synonyms, antonyms = get_synonyms_antonyms(word)
    return jsonify({'synonyms': synonyms, 'antonyms': antonyms})

if __name__ == '__main__':
    app.run(debug=True)
