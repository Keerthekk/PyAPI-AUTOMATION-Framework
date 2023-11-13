1project-
Integration Test cases
URL: 

1. verify Get, POST, PATCH, PUT, Delete
2. Response Body, Headers, Status Code.
3. Auth - Basic Auth, Cookie Based Auth.
4. Json Schema validation

### Tech Stack--
1. Request Module
2. Pytest, pytest-html
3. Allure Report
4. faker, CSV, JSON, YAML
5. Run Via commandline -jenkins

P.S - DB Connecction(in)

### install pip packages
### command line for installation
pip install requests pytest pytest-html faker allure-pytest jsonschema

pip install requirments.txt

pip freeze>requirments.txt


### run command line
'pytest "path" -s -v --alluredir=./reports --html=reports.html'

