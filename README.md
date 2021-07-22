# Data Engineering Python Test

## Case - Marvel Superheroes

The main goal for Z-Tech is to help small and medium businesses to grow.

With that being said, Z-Tech is starting a new project to improve the security for these businesses by hiring a Marvel Superhero that will beat any bad guys' ass who try to rob or steal any customer from Z-Tech. 

To choose the correct hero, the Data Engineering Team has to provide for the Data Science Team a database with the list of all Marvel's heroes, with a description of the hero, and the number of times that each hero appeared in comics, series, stories and events.


## Technical Goal:

Create a dataframe in Python with all the information mentioned above, using Marvel's Characters API. The dataframe should be similar to this:

![alt text](https://github.com/ztech-company/ztech-data-code-challenge/blob/main/Data%20Engineer/Screen%20Shot%202021-07-12%20at%2011.12.45.png?raw=true)


## Requirements

To run this project you'll have to use Python 3.9.1 and run the following command to install all the required libraries:
````
pip install -r requirements.txt
````
Also, you'll have to insert both your private and public keys to run the API requests in the marvel_keys.config.json file.
You can genarate them by accessing Marvel's Developers website ([https://developer.marvel.com/](https://developer.marvel.com/)) and creating an account.

## Tools

I developed this project using PyCharm to code and test the python scripts and Insomnia to test my API requests.

## Classes

**MarvelService:** This class fetches data from Marvel's API.

**MarvelTransform:** This class transforms the data fetched by MarvelService's class into a dataframe.

## How to run it

You can run it by simply running the main.py file in your Jupyter Notebook or terminal after you met the specified requirements.
There is already an Jupyter Notebook file in the project to see an example on how to run it.
