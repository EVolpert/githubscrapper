# githubscrapper
A small git hub scrapper

## Requirements
- Virtualenv==16.0.0
- Python==3.5.2
- requests==2.18.4
- beautifulsoup4==4.6.0

## Instalation
- Create a virtualenv with Python3 by using the command ```virtualenv -p python3 envname```
- Activate the enviroument with the command ```source path/to/env/bin/activate```
- Install all the requirements with ```pip install -r requirements.txt```

## Running the webscrapper
To run the webscrapper you will need a repositories.txt file in the project root folder. It's requirements are
- Only one project per line as many as you like
- Each line will have the path to the project you need to scrap like this ```EVolpert/githubscrapper/```.

With the repositories.txt file just type ```python3 webscrapperA.py``` or ```python3 webscrapperB.py``` and in the project folder a .txt file with tha name of the project you scrapped will be available for you.

To exit the virtual env just type ```deactivate```

## Example output
This is what you will get by using this project A version:
```A Output```

This is what you will get by using this project B version:
```B Output```
