Classifying texts into 27 (+neutral) emotions.

Directions:
1. pip install -r requirements.txt
2. go to subfolder GoEmotions
3. run python app.py
4. In another terminal, run curl -X POST 127.0.0.1:80/predict -d "Text I want to classify"
   (Change to whatever IP address was shown after running app.py. Example here is 127.0.0.1:80)
   (On Windows Powershell, you might need to run the command "Remove-item alias:curl" because Windows aliases Invoke-WebRequest as curl)