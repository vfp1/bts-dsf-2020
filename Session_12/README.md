# Deployment of HOUSING ML CORPORTATION

(albeit a very modest deployment)

## Train the model

### Environment!
`conda env create -f environment.yml
`

## Streamlit

Testing that Streamlit works

`$ streamlit hello`

### Developing with streamlint
`$ streamlit run run.py
`    

### Steps to deploy
Step | Code | Description
--- | --- | ---
1 | Create account in Heroku | Create account there
2 | `sudo snap install --classic heroku` | Install Heroku CLI
3 | `heroku login` | Logins into Heroku CLI
4 | `heroku create <my app name>` | Create the app with the name that you want
5 | `heroku git:remote -a <my app name>` | Push branch to heroku remote (from root folder not Session_12)
6 | `heroku buildpacks:set heroku/python` | Build packs to support Python in Heroku
7 | `git subtree push --prefix Session_12 heroku main` | Push subtree of Session_12 to heroku (from root folder)
8 | `heroku logs` | To check heroku app
9 | `heroku run bash -a <my app name>` | Run from pushed folder (Session_12) to check whats inside the bash within the app

You can also check releases in your Heroku account.

The app deployed here is available here: https://houses-bts.herokuapp.com/

### Where is the model being pushed?
The app runs `python train.py` at build time, so that the scalers and model are available. 
Usually, we should store those in blob storage, also with DVC (Data Versioning Control) for better control of versions. 