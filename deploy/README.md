## How To Build APIs

You need to set up the environment for this repository first ([Read here](./README.md))

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

Take the *Forwarding* link created by ngrok in second terminal and paste it into the *host_name* variable in 3 files:
- `./UI/demo/js/fetch.js`
- `./UI/additional_demo/js/fetch.js`
- `./UI/admin/js/script.js`

**Note that if you want to use the *admin* page, you must create the `password.txt` file and set your own password into it.**

## How To Build User Interface

The `./UI` folder contains all the source code for building the user interface (UI).

You can create a new GitHub repository and copy everything inside the UI folder to it. 
Then, use **GitHub Pages** feature to quickly create a demo website.