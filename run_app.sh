heroku create birds-and-climate-app
dt=$(date '+%d/%m/%Y %H:%M:%S')
git add .
git commit -m "app update {$dt}"
git push heroku master
heroku ps:scale web=1
