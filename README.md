# test_ml
A microservice for ML model training and prediction


## Folder Structure
`notebooks` --- contains all notebooks used for model development \
`api` --- contains api


## Assumptions

* All training and model selection will be done in notebooks environemnt.

* For now, development and production environment for API will be run from api environment.

* Docker Compose assumed for running notebooks, but for API raw Docker will be used

* API will be serving a pretrained model at /predict

* API will be saving labelled train data at /train for retraining/updating model in the future

* Cleaned data will be sent to API hence validation will be added later

* It should be assumed that the most recent model should always be used

## Known Issues:
* Notebooks run on port 8888, but if you are already running some code on said port you will be greated with the image below:
![Jupyterlab Login Page](images/token_wahala.png "Jupyterlab login"). To solve this change port in notebooks.yml or kill the server running at said port. \
**If you change port in notebooks.yml don't forget to change it back before you push to a git repository**

* ssh into API server and manually install scikit-learn due to a strange issue with poetry and scikit-learn


## Getting started

### Running Notebooks
 * `docker-compose -f notebooks.yml up`
 * Follow the link shown in your terminal to view the code. \
 **Follow the link starting with `http://127.0.0.1:8888/` orther links may make you cry, trying to figure out what went wrong.**
 * ssh into notebooks container with the command `docker exec -it test_ml_lab_1 /bin/bash` and install requirements as needed. This was not added to the docker process because different devs may want different environments/libraries ... my assumptions. But base requirements are added in `environment.yml`

 ### Running API
 * Run this command `docker build -t test_ml .` from root folder
 * Run this command after `docker run -d --name test_ml0 -p 80:80 test_ml`

 ## Stopping API
 * `docker kill test_ml0`
 * `docker rm test_ml0`

 ## ALT Running API
 * `docker-compose up`

 ## To test API:

 **Ensure all `X` values follow the headings listed in the image below. In the exact order**
 ![Expected X-Values](images/headers.png "Expected X-Values")

* `/train` --- 
```json
{
    "X": ["2Story", "RL", 2, "Pave", "Y", "AllPub", "CollgCr",	"1Fam",	7,	5],
    "Y": [208500]
}

```

* `/predict` --- 
```json
{
    
    "X": ["2Story", "RL", 2, "Pave", "Y", "AllPub", "CollgCr",	"1Fam",	7,	5]
}

```



 ## TODO
 * CrossValidation on chosen model
 * Some Hyperparameter tuning as well
 * Add docker-compose for api
 * Exempt notebook from api folder :thinking:
 * Add Extra Validation for data types
 * Store train data in DB in another iteration
 * Add extra validation for unforseen errors
 * Add Unit Tests
 * Swicth from poetry to miniconda to resolve scikit-learn and pandas issue