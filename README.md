Flask Frontend Template. 
======
Work in progress using Dataforth Maq20 and variables from SHED.

## Application Overview:

![alt text](/docs/SystemOverview.jpg "System Overview")

This is intended to be a modular template that can be used to quickly start future projects. Ideally there will be Javascript, css, html and python modules that can be chosen based on the projects needs. 

Current modules:
===
### Python
1. app.py - This is the Flask application. It includes basic route functions for serving the front end, responding to AJAX requests, and starts a background thread and queue for adding additional control operations.

2. daq.py - This is an in between layer for the Maq20 API. It allows the app to interact with the daq using established variable names that are consistent throughout the python, javascript and html. Multiple instances can be used if multiple Maq20's are used for a project.
### Javascript
1. base.js - This module is used to update the front end with current values from the variable list in python. It also monitors inputs for changes and send the requested change to app.py to be updated. This functions using HTML tag id's. If the tag id = variable name in app.variables, the value will be requested. Add input_ as a prefix to the tag id for inputs and these will be monitored for changes and sent to app.py on changes.

2. index.js - working file with lots of functionality. Needs to be cleaned up and split into further modules. Has socket functionality.

3. Chart.js/Chart.bundle.js - Chart.js library for adding charts to front ends. Index.js has example of a chart with live updates.
### CSS

base.js - provides front end refresh functions. It gets the id's from the html and uses these as variable names to pass to the server. This also monitors inputs and sends values to the server when they are changed.
        - To use, set all values that should be updated in html to have the id="variable used in Python" (currently working for maq20 daq only, needs added function for variables directly.)
        - for inputs to be monitored, add the prefix input_ to variable name in the id="input_variable used in Python".

checkbox1.css - basic color changing button for on off inputs. Works with div class="inputgroup".. See permeation.html for example.

Install Instructions
===

1. Fork the repository and change name for new project

2. Create a local virtual environment for the project using "python -m venv folder_name"

3. Clone the fork into the new folder using "git clone location_of_new_repo"

4. Activate the virtual environment. 
 * Within VSCode - Set /Scripts/python.exe as the interpreter and open new terminal
 * From terminal (Windows) -  "/Scripts/activate.bat"
 * From terminal (linux) - "source /bin/activate"

5. Install dependencies from requirements.txt using pip install -r requirements.txt

6. if using Maq20:
 * Install pymodbus (note: pymodbus3 is no longer supported. Install pymodbus and confirm updated maq20com.py from /dependencies is used)
 * Get the modified MAQ20 api from https://github.com/tmacinc/MAQ20_API_Python.git and install within venv using "python setup.py install"
 * Or install using "python /dependencies/MAQ20_APR_Python-master/setup.py" and copy the files from dependencies/Updates_to_maq20_api into the following folders after installation.
  1. "maq20com.py" -> /Lib/site-packages/maq20/
  2. "diol.py" -> /Lib/site-packages/maq20/modules/

Running Application
===
### Windows

1. Uncomment waitress lines in app.py
2. Install waitress using "pip install waitress"
3. Run project using python app.py

### Linux (need to confirm options. Can use eventlet with python app.py. Gunicorn uses different method)

1. Using Eventlet
 * Uncomment eventlet lines in app.py
 * Install eventlet using "pip install eventlet"
 * Run project using python app.py

2. Using gunicorn with Eventlet worker
 * Uncomment eventlet and gunicorn lines in app.py
 * install eventlet and gunicorn using "pip install eventlet gunicorn"
 * run using "gunicorn -b 127.0.0.1:5000 --worker-class eventlet -w 1 app:app" <- or something very close. Need to test.