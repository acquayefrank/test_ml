FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# set path to our python api file
ENV MODULE_NAME="api.server"

# copy contents of project into docker
COPY ./ /app

# install poetry
RUN pip install poetry

# disable virtualenv for peotry
RUN poetry config virtualenvs.create false

# install dependencies
RUN poetry install

# To fix strange issue between scikit-learn, poetry and pandas
RUN pip install -U scikit-learn
RUN pip install pandas