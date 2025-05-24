Welcome to Little Lemon Capstone Project, the last django framework application in the Meta Backend Developer professional certificate.

I'm proud to say that this application passed all the requirements and allowed to me to obtain said professional certificate on the May 22, 2025.

To test this application you'll be required to:
1. Clone the git repo
2. Create a virtual environment 
3. install django, djangorestframework, djoser and mysqlclient
4. modify the settings.py file at the project level dir to correctly establish a connection with your sql server or modify to a different database.
5. make migration and migrate to database.
6. change directory to main repo folder, where module manage.py is located, and run the server on local host. 

Here are the credential to access admin page, allowing data population for registred models or user/token creation:

endpoint: http://127.0.0.1:8000/admin
superuser: mirko / mirko
superuser token: a7a730514b3dee2f4c5b6c58618401cbaf239ff2

The scope of this project was to design a REST APIs application, capable of accepting HTTP requests on menu items and reservation and return serialized models in Json format.
Also, with Djoser, providing APIs to create user/token authentication.

Here are the endpoint designed to be tested:

MenuItems API endpoint:
    http://127.0.0.1:8000/menu/
Booking API endpoint:
    http://127.0.0.1:8000/booking/

DJOSER User view and creation:
http://127.0.0.1:8000/auth/users/ 

DJOSER User token assignment:
http://127.0.0.1:8000/auth/token/login/

The REST APIs can be tested directly visiting the endpoint on your browser, thanks to Browsable API built in the django rest framework, or via specific tools such as Insomnia (suggested by the META team throughout the course).
