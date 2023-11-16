## How To Build APIs
Install packages in requirements.txt.
```
pip install -r requirements.txt
```
Create the first terminal, then run:
```
python app.py
```
Create the second terminal, then run:
```
ngrok http 5000
```

Take the Forward link created by ngrok in second terminal and paste it into the host_name variable in file ./UI/demo/js/fetch.js