Flask frontend template. Work in progress using Dataforth Maq20 and variables from SHED.

Application Overview:

![alt text](/docs/System_Overview.pdf "System Overview")

This is meant to have Javascript and css modules that can be used as needed for future projects. Can also create template front end layouts that require id's to be set for future projects.
Current modules:

base.js - provides front end refresh functions. It gets the id's from the html and uses these as variable names to pass to the server. This also monitors inputs and sends values to the server when they are changed.
        - To use, set all values that should be updated in html to have the id="variable used in Python" (currently working for maq20 daq only, needs added function for variables directly.)
        - for inputs to be monitored, add the prefix input_ to variable name in the id="input_variable used in Python".

    checkbox1.css - basic color changing button for on off inputs. Works with div class="inputgroup".. See permeation.html for example.


To use,

create venv folder for project using python -m venv <folder>

Clone repository into folder.

Install dependencies from requirements.txt using pip install -r requirements.txt

For Maq20:
Install pymodbus (note: pymodbus3 is no longer supported. Install pymodbus and confirm updated maq20com.py forom dependencies is used)
Get the modified MAQ20 api from https://github.com/tmacinc/MAQ20_API_Python.git and install within venv using python setup.py install
    Or copy the files from dependecies/Updates to maq20 api after installation to update the code.


Run project using python app.py