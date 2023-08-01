from transformers import pipeline
from flask import Flask, request
import os

model_checkpoint = 'DiracGiraf/roberta-base-goemotions'
classifier = None
app = Flask(__name__)
def load_model():
    global classifier
    # Make global so we only load once
    classifier = pipeline("sentiment-analysis", model=model_checkpoint, return_all_scores=True)

@app.route('/')
def home_endpoint():
    return 'Hello, I can identify emotions of texts.'

@app.route('/predict', methods=['POST'])
def get_prediction():
    if request.method == 'POST':
        #Raise error if not useful?
        data = request.get_data().decode('utf-8')
        scores = classifier(data)[0]
        labels_list = [d['label'] for d in scores if d['score']>=0.5]
        if not labels_list:
            labels_list = ['neutral']
        return ', '.join(labels_list)

PORT = int(os.environ.get("PORT", 8080))
if __name__ == '__main__':
    load_model()
    app.run(host = '0.0.0.0', port = PORT)

