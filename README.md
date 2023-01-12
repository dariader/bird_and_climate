## Pitch
Cyprus is a dazzling place. This island is literally a museum, but if you don't know where to look, you won't see the exibition. 
How great would it be to go somewhere, knowing what was the story of this place? To know who lives there?
The aim of this project is to make Cyprus natural and geological sights more visible.  

## Project Description

This app is inspired by the project #664 from https://app.datacamp.com/learn/projects/664
The aim of this repo to demonstrate my skills in python, docker, data analysis and visualization

### Intro: 
_The technical description of desired app_

Tech Stack:
1) Python Dash/Flask app
2) Runs from docker container
3) Deploys on local server on heroku (while this is free)
4) Code checks: flake8 (https://melevir.medium.com/pycharm-loves-flake-671c7fac4f52)
5) jenkins autotest on github (https://www.jenkins.io/solutions/python/)

App UI:
1) map depicting climate in UK
2) selector to choose bird species
3) Filter the climate data to compare 1970 and 2010.

Data processing:
1) no data is stored, it is retrieved and processed on the fly each time
1) get climate and bird data
2) merge by dates as precise as possible
3) make pivot tables, where climate condition is rows and bird species are columns
4) create pseudo-absence model
5) use glmnet, which fits a generalized logistic regression (glm) with elastic net regularization (net). All we need to do is define a "tuning grid" with sets of possible values for each training parameter. Then use cross-validation to evaluate how well the different combinations of hyperparameters did building the predictive model. glmnet models have two hyperparameters, alpha and lambda. If you would like to learn what they do, have a look at the vignette.http://ww.web.stanford.edu/~hastie/Papers/Glmnet_Vignette.pdf
6) We will make a prediction for each decade and each cell of the grid. Since we fit a logistic regression model, we can choose to predict the probability. In our case, this becomes the "probability of occurrence" for our species.


Data: 
1) The Global Biodiversity Information Facility (GBIF), an international network and research infrastructure aimed at providing anyone, anywhere, open access to data about life on Earth. We will use their data in this project.
    "issues" - We will only use records where no doubts about the observation were listed.
    "license" - We will only use records under a creative commons license.
    "date" - We will only use records between 1965 and 2015 because that matches our climate dataset.
2) We can find the CRS string for any specific projection at spatialreference.org.
5) We will use data from the Global Biodiversity Information Facility and a subset of the UKCP09 climate data from the UK Met Office.

### How to run locally

**How to store credentials**

for local usage of app: 

1. In `~/.bashrc` file: 

`export BIRD_DB_PASSW = '<passw>'`

`export EBIRD_API_KEY = '<api_key>'`

2. Then run in terminal
`source ~/.bashrc`
and optionally reload IDE


how to pass credentials to docker: 


**How to run in heroku**

chmod +x run_app.sh
This will create project and push changes to the remote heroku repository

**How to dockerize**

sudo docker build -t docker_bird_and_climate ./src

8051 - outer
8050 - inner

sudo docker run --detach -p 8051:8050 docker_bird_and_climate 


**How to create a db in docker**

1. create an instance of mysql database
docker run -d -p 3306:3306 -v /home/daria/PycharmProjects/bird_and_climate/db_src/conf:/etc/mysql/conf.d -v /home/daria/PycharmProjects/bird_and_climate/db_src/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=<passw> --name docker_mysql c2c2eba5ae85
3. create an image 
docker build -t docker_mysql
