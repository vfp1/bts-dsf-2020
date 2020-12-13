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
Create account in Heroku
sudo snap install --classic heroku
heroku login
heroku create bikes-bts or whatever is free
(Make sure your git repo is ready)
Make sure that you have setup.sh (ask me for it)
heroku git:remote -a yourapp
git push heroku master (from the root path of git repo)
heroku buildpacks:add --index 1 heroku-community/apt (you need this for sudo apt shit)
git push heroku master
heroku logs (to check outputs)