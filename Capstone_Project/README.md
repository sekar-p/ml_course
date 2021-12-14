## Predict the price of your laptop

Dataset can be downloaded from https://www.kaggle.com/muhammetvarl/laptop-price

I was searching for the Capstone project idea and endup with this dataset which is something interesting to me to check my laptop price with my own ML model :-)

Attribute information as below,
- Company- String -Laptop Manufacturer
- Product -String -Brand and Model
- TypeName -String -Type (Notebook, Ultrabook, Gaming, etc.)
- Inches -Numeric- Screen Size
- ScreenResolution -String- Screen Resolution
- Cpu- String -Central Processing Unit (CPU)
- Ram -String- Laptop RAM
- Memory -String- Hard Disk / SSD Memory
- GPU -String- Graphics Processing Units (GPU)
- OpSys -String- Operating System
- Weight -String- Laptop Weight
- Price_euros -Numeric- Price (Euro)


# How to run the project:
  - Download all the files(Pipfile,Pipfile.lock,Dockerfile,data.csv and *.py files) to your local host and run follow below commands from the location where all the files resides

## 1. Install the virtualenv and activate it

  1.a - Installation
  ------------
  If you\'re using Debian:
      
      $ sudo apt install pipenv

  Or, if you\'re using Windows:

      # pip install --user pipenv

  1.b - Activate the virtual env
  ------------------------------
  To activate the virtual env use the below command, so that all the packages will be installed in isolated environment.
  
    pipenv shell

  1.c - Install the dependencies
  ------------------------------
  - Run the below command from where you have copied the pipfiles
    
      `$ pipenv install --dev`

Hurray!! Now we have activated virtualenv and installed all the dependencies required to this project

## 2. Run it Locally
  2.a - Run as script
  ------------------------------
  - Run the predict_without_flask.py script with modified data, output will be probability of the prediction
  
  `$ python predict_without_flask.py`
  
  2.b - Run as flask script
  ------------------------------
  - Run the predict_with_flask.py script in a terminal

  `$ python predict.py`
  
  - Make the request to the webservice using request_service.py script in another terminal
    Modify the data and run it again
  
  `$ python request_service.py`

  2.c - Run as webservice
  ------------------------------
  - Run the flask script as webservice using gunicorn

  `$ gunicorn --bind 0.0.0.0:1552 predict:app`
  
## 3. Run as Docker web service
  Make sure all the files in your directory where you are running the command, otherwise it wil thrown an error
  - Build the docker image using below command

  `$ docker build -t capstone_project .`
  
  - Run the docker image with port specified in the flask script. Port has to be specified in the command else request will not reach docker service.

  `$ docker run -it --rm -p 1552:1552 capstone_project`
  
  Now the service is up, you can make request with data and you will get the predicted value
