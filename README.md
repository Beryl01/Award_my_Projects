# Awards
#### By:
Beryl Negesa Otieno

<img src="./pic.png">

### Description  
This is application allows a user to post a project he/she has created and get it reviewed by his/her peers.When you post a project you will be able to rate the project into three parts Usability Design `Content. The application is build with Django Framework in Pthyon.

## User story
As a user of the web application you will be able to:
1. View posted projects and their details
2. Post a project to be rated/reviewed
3. Rate/ review other users' projects
4. Search for projects 
5. View projects overall score
6. View my profile page

### Deployed link
https://awardmyprojects.herokuapp.com/

### BDD
|        User Requirements                 |           Input                           |           Output                         |
|------------------------------------------|-------------------------------------------|------------------------------------------|
| Sign Up/Login                            | To create a new account, click on the sign| If login is successful, the user is      |
|                                          | up link and fill in the form details. To  | redirected to the home page              |
|                                          | login, fill in the details                |                                          |
| Add a new project                        | Click on the submit new project tab on the| You will be navigated to a page which    |
|                                          | navbar and submit the project details     | has a form to submit the project         |
| Review a project                         | Click on the Review button                | You will be navigated to a page where you|
|                                          |                                           | can post your review                     |
| Create a profile                         | Click on the profile tab then Edit Profile| A new profile for the user will be       |
|                                          | button                                    | created                                  |
| Search for a project                     | Enter the project's name into the search  | You will be redirected to a page with all||                                          | bar in the navbar                         | results matching your search. You can    |
|                                          |                                           | then click on the project you want       |
| Log out                                  | Click on the Account button and select    | You will be logged out                   ||                                          | log out                                   |                                          |

### Setup and Installation  
To get the project .......    
##### Cloning the repository:  
 ```bash 
git clone https://github.com/Beryl01/Awards.git
```
##### Navigate into the folder 
 ```bash 
cd Awards
```
##### Install and activate Virtual  
 ```bash 
python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
pip install -r requirements.txt 
```  
##### Setup Database  
SetUp your database User,Password, Host then make migrations
 ```bash 
python manage.py makemigrations
 ``` 
 Now Migrate  
 ```bash 
python3.6 manage.py migrate 
```
##### Run the application  
 ```bash 
python3.6 manage.py runserver 
```  
##### Testing the application  
 ```bash 
python3.6 manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
## Technologies Used
* Python3.6
* Django 3.0
* HTML5
* CSS3
* Bootstrap4
  
## Known Bugs
None known for now.

## Support and contact details
* Email-berylnegesa@gmail.com

## License
[MIT License](License.md)
Copyright (c) [2020] [Beryl Negesa Otieno]
</a>
