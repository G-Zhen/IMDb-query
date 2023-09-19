# IMDb-query
CRUD Flask app
#### App requirements:
* Search bar
* Search Filter (movies, shows, actors, ratings)
#### Goal: 
To create a basic Flask app to encompass what I've learned while working at UCI MIND as a student programmer.

## Terminal setup
### First time setup (only needs to be done once by me)
``` python
# Create a Python virtual environment:
python -m venv .venv

# Activate the virtual environment:
source /.venv/scripts/activate

# Download dependencies
pip -V
pip install flask

# Create a requirements.txt. After you download everything you need
pip3 freeze > requirements.txt
```

### Set up Dev Environment (for later or anyone who clones this repo)
#### 1. Virtual environment setup and download dependencies
``` python
#1 Go to this repo's folder

#2 Create a Python virtual environment:
python -m venv .venv

#3 Activate the virtual environment:
.\.venv\Scripts\Activate.ps1
    # On Windows: .ps1 for PowerShell 
source /.venv/scripts/activate
    # On Mac

#4 While in the virtual env, update pip and install packages (only need to do this once):
python -m pip install --upgrade pip
pip install -r requirements.txt

#5 Run the script: develop, debug, etc. or just click "Run" in VSCode
python app.py

#6 Press CTRL+C to close the development server

# Deactivate when done
deactivate
```
#### 2. Create a secrets.json file
1. Go to this repo's root directory
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
