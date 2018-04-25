##################################################################################################

After cloning from git, go to the root folder and follow the following steps

1. virtualenv env
2. source env/Scripts/activate (Windows) OR source env/bin/activate (Linux/Mac)
3. pip install -r requirements.txt
4. gunicorn --reload dev:api (Linux) OR 

4. pip install waitress 
   waitress-serve --port=8000 dev:api (Windows)
