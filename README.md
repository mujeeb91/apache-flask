# apache-flask
How to integrate Flask with apache (Python 3)

**Instructions**
1) Create a folder in /var/www/ name this folder flask_app
2) Copy server.py and app.wsgi (from this repository) to that folder
3) Go to your desktop (any directory not requiring root permissions may work), create a virtual environment using this command
`python3 -m venv venv`
4) Activate the virtual environment
`source venv/bin/activate`
5) Install Flask
`pip install Flask`
6) Move this folder to the apache folder
`sudo cp -r venv /var/www/flask_app`
7) Now lets set up the apache configuration
8) Move flask.conf to sites-available
`sudo cp flask.conf /etc/apache2/sites-available/`
9) Enable configuration
`sudo a2ensite flask.conf`
10) Restart Apache
`sudo service apache2 restart`
