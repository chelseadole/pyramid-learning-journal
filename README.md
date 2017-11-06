# Pyramid Learning Journal 
### Code Fellows, Python 401
#### Author: Chelsea Dole
#### Deployed URL: https://frightening-blood-49491.herokuapp.com/
#### Version: 1.0


### Test Coverage Step 2 (tox, test_pyramid.py):
* *Python 2.7:* 92%
* *Python 3.6:* 92%

### Test Coverage Step 3 (tox, test_pyramid.py):
* *Problem with tox, unable to run, despite pytest working 100% well. (Hoping to resubmit.)*


### Project Description: 
* The "Pyramid Learning Journal" site is a resource used by the author for posting, editing, and viewing learning journals written while attending Code Fellows' 401 Python course in Seattle, WA. This project is created using the Pyramid web framework for Python.

### Technologies/Resources:
* Python
* Pyramid
* HTML/CSS
* Bootstrap (JS, jQuery, etc)

### Routes:

* / - the home page and a list of all LJ posts
* /journal/{id:\d+} - the view to see the detail of a single LJ post
* /journal/new-entry - for adding new LJ posts
* /journal/{id:\d+}/edit-entry - for editing previously created LJ posts

### Set Up and Installation:

* Clone this repository to your local machine.

* Once downloaded, cd into the chelsea_pyramid_learning_journal directory.

* Begin a new virtual environment with Python 3 and activate it.

* cd into the next chelsea_pyramid_learning_journal directory. It should be at the same level of setup.py

* pip install this package as well as the testing set of extras into your virtual environment.

* $ initialize_db development.ini to initialize the database

* $ pserve development.ini --reload to serve the application on http://localhost:6543

