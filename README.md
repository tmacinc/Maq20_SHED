Flask frontend template. Work in progress using Dataforth Maq20 for testing and variables from SHED.

To use,

create venv folder for project using python -m venv <folder>

Install dependencies from requirements.txt using pip install -r requirements.txt

For Maq20:
Install pymodbus3
Get the modified MAQ20 api from https://github.com/tmacinc/MAQ20_API_Python.git and install within venv using python setup.py install
    Or copy the files from dependecies/Updates to maq20 api after installation to update the code.


Run project using python app.py