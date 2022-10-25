Project Description:

This app is inspired by the project #664 from https://app.datacamp.com/learn/projects/664
The aim of this repo to demonstrate my skills in python, docker, data analysis and visualization

Intro: 

Climate is changing around the world. This change is impacting species of wild animals. In this project, we will use four decades of bird sightings and climate data to predict the distribution of a bird species in the Scottish Highlands and see how its distribution changed over the years.

The technical description of desired app
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
