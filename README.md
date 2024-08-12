# url_shortify

##
URL Shortening Project
This project is a simple Flask application that allows users to shorten long URLs and redirect to shortened URLs.

	
## Running project
Clone project to your computer

	git clone https://github.com/busraocal/url_shortify.git
 
Navigate to the project directory

	cd url_sortify

Install require packages

	pip install -r requirements.txt

Configure the .flaskenv file

	FLASK_RUN_HOST=127.0.0.1
  	FLASK_RUN_PORT=8080
  	FLASK_DEBUG=1
  	DATABASE_URL=postgresql://username:password@localhost/db_name

		
Start the Flask application

	flask run
