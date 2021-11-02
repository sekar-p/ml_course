# Classify the Mushroom whether its edible or not

Dataset downloaded from https://archive.ics.uci.edu/ml/datasets/Mushroom

Not all the mushrooms are good for human to consume. Using this dataset we gonna make model to identify the edible mushrooms and the model will be used to classify the mushrooms. 

This data set includes descriptions of hypothetical samples corresponding to 23 species of gilled mushrooms in the Agaricus and Lepiota Family (pp. 500-525). Each species is identified as definitely edible or definitely poisonous.

Attribute Information:

1. cap-shape: bell=b,conical=c,convex=x,flat=f, knobbed=k,sunken=s
2. cap-surface: fibrous=f,grooves=g,scaly=y,smooth=s
3. cap-color: brown=n,buff=b,cinnamon=c,gray=g,green=r, pink=p,purple=u,red=e,white=w,yellow=y
4. bruises?: bruises=t,no=f
5. odor: almond=a,anise=l,creosote=c,fishy=y,foul=f, musty=m,none=n,pungent=p,spicy=s
6. gill-attachment: attached=a,descending=d,free=f,notched=n
7. gill-spacing: close=c,crowded=w,distant=d
8. gill-size: broad=b,narrow=n
9. gill-color: black=k,brown=n,buff=b,chocolate=h,gray=g, green=r,orange=o,pink=p,purple=u,red=e, white=w,yellow=y
10. stalk-shape: enlarging=e,tapering=t
11. stalk-root: bulbous=b,club=c,cup=u,equal=e, rhizomorphs=z,rooted=r,missing=?
12. stalk-surface-above-ring: fibrous=f,scaly=y,silky=k,smooth=s
13. stalk-surface-below-ring: fibrous=f,scaly=y,silky=k,smooth=s
14. stalk-color-above-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o, pink=p,red=e,white=w,yellow=y
15. stalk-color-below-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o, pink=p,red=e,white=w,yellow=y
16. veil-type: partial=p,universal=u
17. veil-color: brown=n,orange=o,white=w,yellow=y
18. ring-number: none=n,one=o,two=t
19. ring-type: cobwebby=c,evanescent=e,flaring=f,large=l, none=n,pendant=p,sheathing=s,zone=z
20. spore-print-color: black=k,brown=n,buff=b,chocolate=h,green=r, orange=o,purple=u,white=w,yellow=y
21. population: abundant=a,clustered=c,numerous=n, scattered=s,several=v,solitary=y
22. habitat: grasses=g,leaves=l,meadows=m,paths=p, urban=u,waste=w,woods=d

# How to run the project:
  - Download all the files(Pipfile,Pipfile.lock,Dockerfile,mushrooms.csv and *.py files) to your local host and run follow below commands from the location where all the files resides

## 1. Install the virtualenv and activate it

  1.a - Installation
  ------------
  If you\'re using Debian Buster+:
      $ sudo apt install pipenv

  Or, if you\'re using Fedora:

      $ sudo dnf install pipenv

  Or, if you\'re using FreeBSD:

      # pkg install py36-pipenv

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
  - Run the predict.py script with modified data, output will be probability of the prediction
  
  `$ python predict.py`
  
  2.b - Run as flask script
  ------------------------------
  - Run the predict_with_flask.py script in a terminal

  `$ python predict_with_flask.py`
  
  - Make the request to the webservice using request_service.py script in another terminal
    Modify the data and run it again
  
  `$ python request_service.py`

  2.c - Run as webservice
  ------------------------------
  - Run the flask script as webservice using gunicorn

  `$ gunicorn --bind 0.0.0.0:1552 predict_with_flask:predict`
  
## 3. Run as Docker web service
  Make sure all the files in your directory where you are running the command, otherwise it wil thrown an error
  - Build the docker image using below command

  `$ docker build -t midterm_project .`
  
  - Run the docker image with port specified in the flask script. Port has to be specified in the command else request will not reach docker service.

  `$ docker run -it --rm -p 1552:1552 midterm_project`
  
  Now the service is up, you can make request with data and you will get the predicted value
  
