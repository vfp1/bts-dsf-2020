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
1. Create account in Heroku
2. sudo snap install --classic heroku
heroku login
heroku create houses-bts or whatever is free
(Make sure your git repo is ready)
Make sure that you have setup.sh (ask me for it)
heroku git:remote -a yourapp
heroku buildpacks:set heroku/python
git subtree push --prefix Session_12 heroku main

git push heroku master
heroku logs (to check outputs)
heroku run bash -a APPNAME (to debug app within apps folder in local)