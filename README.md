# IMDb-query
CRUD Flask app
#### App requirements:
* Search bar
* Search Filter (movies, shows, actors, ratings)
#### Goal: 
To create a basic Flask app to reinforce what I've learned while working at UCI MIND as a student programmer.
* full stack web app using Flask
* Deploy with Docker

# Terminal setup (note: I'm using Mac)
## First time setup
More info on virtual environment setup and Windows commands [here](https://flask.palletsprojects.com/en/2.3.x/installation/).

``` python
# Create a Python virtual environment:
python3 -m venv .venv

# Activate the virtual environment:
source .venv/bin/activate

# Download dependencies 
pip -V
pip install --upgrade pip
pip install flask 
pip install requests

# Create/update a requirements.txt. After I download everything I need (only needs to be done once by me)
pip3 freeze > website/requirements.txt
```

### Set up Dev Environment (for anyone who clones this repo)
#### 1. Virtual environment setup and download dependencies
``` python
#1 Go to this repo's folder

#2 Create a Python virtual environment (same steps as above)
#3 Activate the virtual environment (same steps as above)

#4 While in the virtual env, update pip and install packages (only need to do this once):
pip install --upgrade pip
pip install -r website/requirements.txt

#5 Run the script: develop, debug, etc. or just click "Run" in VSCode
python3 app.py

#6 Press CTRL+C to close the development server

# Deactivate when done
deactivate
```
### Potential pip downloading errors
An error you might encounter is when you're installing MySQL. Here's what worked for me:
``` python
# outside of .venv (Mac)
brew install pkg-config

# in .venv
find / -name 'mysqlclient.pc' 2>/dev/null #find path to mysqlclient
export PKG_CONFIG_PATH=/path/to/mysqlclient.pc #use found path
export MYSQLCLIENT_LDFLAGS=$(pkg-config --libs mysqlclient)
export MYSQLCLIENT_CFLAGS=$(pkg-config --cflags mysqlclient)
```
After those steps, try downloading from requirements.txt again. 

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
## Run the web app
* In VSCode: 
    *   Click "Run without debugging"
* Through Terminal:
    *   ``` python3 app.py ``` 

# Docker setup
For local development I'm using [Docker Desktop](https://www.docker.com/products/docker-desktop/).



