heroku create birds-and-climate-app
git push heroku master
heroku ps:scale web=1
heroku open