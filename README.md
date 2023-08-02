This repository aims to identify 28 (including neutral) emotions of a piece of text. 
Compared to the original paper that studied this, I have increased the metric score by almost 50%. (The f1 score went from 40 to 60.)
The list of emotions is: 
admiration, amusement, anger, annoyance, approval, caring, confusion, curiosity, desire, disappointment, disapproval, disgust, embarrassment,
excitement, fear, gratitude, grief, joy, love, nervousness, optimism, pride, realization, relief, remorse, sadness, surprise, neutral

# Inference
The model is deployed on AWS, but due to budget concerns, I only run it occasionally.
To do inference on your own machine, you can first acquire the docker image by

```docker pull lkkcpaul/goemotions```

Run the container

```docker run -p 8080:8080 lkkcpaul/goemotions .```

You should see an IP address. Say for example, mine was 127.0.0.1.
Then go to your browser and go to the address `127.0.0.1:8080`, you should see the welcome text.
Then to classify a piece of text, do a curl request 

```curl -X POST 127.0.0.1:8080/predict -d "Text I want to classify."```

You should see the emotion labels returned to you.
(If you are using Windows Powershell, to do the `curl` request, you might need to run `Remove-item alias:curl` first because Windows aliases Invoke-WebRequest as curl

# Structure of repo
To reproduce the results of this repo, run ```pip install -r requirements.txt``` and work through the exploration notebooks.
The subdirectory "GoEmotions" contains all the code for inference, except for the weights. "app.py" is the python script that does inferencing using REST API.
The "exploration" subdirectory includes all the experimentation and training of models 
- "data" contains the original data, which is public on https://www.kaggle.com/datasets/debarshichanda/goemotions. More about data in the Data section.
- "basic statistics" is an EDA on the data. 
- "reformat_data" is processing the original data to one-hot format, which will be later used for training.
- "testing_various_models" is what the name suggests. It tries out traditional regressions using TfIdf and also biLSTM. They perform significantly worse than LLM.
- "evaluate_pretrained_models" downloads LLM weights from Huggingface that was fine-tuned for this specific task (predicting the 28 emotion labels), and evaluate their metric scores.
- "finetune_LLM" is fine-tuning pretrained LLMs. It turns out that RoBERTa (a variation of BERT) performs the best. (The latest Llama model hasn't been tested yet.) The fine-tuned weights will be used for inference but are not included in this repo as they are too large.
- "finetune_LLM" also includes fine-tuning RoBERTa on a easier task, namely classifying texts into only 7 labels (the Ekman labels). This increases the performance.
- "data_scaling" is a proof of concept, showing that as the data size gets larger, the model can learn better and score higher in the metric.

# About the data
The data comprise of texts, each with its (possibly multiple)  emotion labels.
The data can be found on this Kaggle dataset https://www.kaggle.com/datasets/debarshichanda/goemotions, as well as in this Google research repo https://github.com/google-research/google-research/tree/master/goemotions.
The data was first released along with this paper "GoEmotions: A Dataset of Fine-Grained Emotions" https://arxiv.org/pdf/2005.00547.pdf.
Previous sentiment analysis classifies texts to only positive or negative labels, or for a slightly more sophisticated analysis, the Ekman labels. 
This data is the first to have such fine-grained emotion labels annotated by humans. 
The texts are curated from Reddit comments, each labeled by three different person. 
There is a huge imbalance in the labels. For example, "Grief" has less than 100 samples, while "admiration"" has order more than 4000. 
More details about the dataset can be found on the Kaggle page. 


