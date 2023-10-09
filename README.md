# IMDb-query
CRUD Flask app
#### App requirements:
* Search bar
* Search Filter (movies, shows, actors, ratings)
#### Goal: 
To create a basic Flask app to encompass what I've learned while working at UCI MIND as a student programmer.


# Terminal setup (note: I'm using Mac)
## First time setup (only needs to be done once by me)
More info on virtual environment setup [here](https://flask.palletsprojects.com/en/2.3.x/installation/).

``` python
# Create a Python virtual environment:
python3 -m venv .venv

# Activate the virtual environment:
source .venv/bin/activate

# Download dependencies
pip -V
pip install --upgrade pip
pip install flask
pip install mysql-connector-python

# Create a requirements.txt. After you download everything you need
pip3 freeze > website/requirements.txt
```

### Set up Dev Environment (for later or anyone who clones this repo)
#### 1. Virtual environment setup and download dependencies
``` python
#1 Go to this repo's folder

#2 Create a Python virtual environment:
python3 -m venv .venv

#3 Activate the virtual environment:
source .venv/bin/activate

#4 While in the virtual env, update pip and install packages (only need to do this once):
pip install --upgrade pip
pip install -r website/requirements.txt

#5 Run the script: develop, debug, etc. or just click "Run" in VSCode
python3 app.py

#6 Press CTRL+C to close the development server

# Deactivate when done
deactivate
```
### 2. Create a secrets.json file
1. Go to website directory
2. Create a new file called secrets.json
3. Add the api keys and urls in this format: 
``` json
{
    "api": {
        "api_key": "your_api_key_here",
        "api_base_url": "https://api.example.com/"
    },
    "database": {
        "database_url": "your_database_url_here",
        "db_username": "your_db_username_here",
        "db_password": "your_db_password_here"
    },
    "app": {
        "secret_key": "your_secret_key_here"
    }
}
```
