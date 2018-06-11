# githubscrapper
A small git hub scrapper

## Requirements
- Virtualenv==16.0.0
- Python==3.5.2
- requests==2.18.4
- beautifulsoup4==4.6.0
- pytest==3.6.1

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

# Difference between webscrapperdirectorytree and webscrapperfiledetails
The main difference between the two versions is how they deal with file location information.

The webscrapperdirectorytree writes on the file a traditional directory tree, but violates SOLID by doing this while creates the file list on the iterate_over_director_tree function. This is not a perfect solution but gives a nice visual way to tell the file location in the project.

The webscrapperfiledetails creates a list of dictionaries that is ordered by their file path. This focus on the where a specific file is on the project, since they are dictionaries this is also good if you need to use the information for another code, and since they are sorted by their file path it organically groups files in the same folder closer together.


## Example output
This is what you will get by using this project A version:
```A Output```

This is what you will get by using this project B version:
```B Output```
