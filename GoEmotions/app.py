from transformers import pipeline
import torch
from flask import Flask, request
device = 0 if torch.cuda.is_available() else -1
model_checkpoint = 'DiracGiraf/roberta-base-goemotions'
classifier = None
app = Flask(__name__)
def load_model():
    global classifier
    # Make global so we only load once
    classifier = pipeline("sentiment-analysis", model=model_checkpoint, device=device, return_all_scores=True)

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

if __name__ == '__main__':
    load_model()
    app.run(host = '0.0.0.0', port = 80)

