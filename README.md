# FundamentalProject
This is the first repo regarding my QA fundamental project

Website: http://35.246.21.143:5000/

Trello: https://trello.com/b/qkV41XqE/devops-fundamental-project

Risk Assessment: https://docs.google.com/spreadsheets/d/1KDOYPHiO6hBObNmLxmTj6owbHyyz476xQ-NGfvWHOrs/edit?usp=sharing

# Objective
The objective of the project was: "To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training." 

This means I am to create an application that uses (C)reate, (R)ead, (U)pdate and (D)elete functaionality.

# My Approach
I decided to make an application that lets you jot down a wall and add/see what activities that wall is suitible for. The app should:

-Create a wall name with relevent location infomation

-From that wall be able to add an activity 

-Update either wall or activity post

-A view for all of the walls and from each wall, view the acivities that wall is suitable for.

-Delete any posts

# Summary
I first made VM and MYSQL on GCP and a Github repository. I then cloned the repository down into VSC (Visual Studio Code) and my VM and pushed and pulled to get work between the computers. I did pip3 install -r requirements.txt to install all the extras (including Flask and Selenium) and then created the python and html files needed for the application, i knew what files i would need by checking my trello board to see what work there was to be done. I allowed the application to access the MYSQL database, and installed Jenkins on the VM. I then linked my repository to Jenkins and input the build tools and build the app using the VM's IP. I then did unit testing and integrated testing (using Selenium) using pytest --cov ./application/ --cov-report term-missing.

# CI Pipeline
Here is the CI Pipeline i used:
![CIpipe](https://github.com/Almathex/FundamentalProject/blob/main/Documentation/CIpipe.png?raw=True)

# Initial ERD 
![Initial ERD](https://github.com/Almathex/FundamentalProject/blob/main/Documentation/WallFinder-ERD.png?raw=True)

# 2nd ERD
![2nd ERD](https://github.com/Almathex/FundamentalProject/blob/main/Documentation/WallFinder-ERD-2.png?raw=True)

# Final ERD  
![Final ERD](https://github.com/Almathex/FundamentalProject/blob/main/Documentation/Updated%20ERD.png?raw=True)

Due to time constraints and to make life easier I chose to revert back to a two table design with one relationship.

# Trello Board
![Trello Board](https://github.com/Almathex/FundamentalProject/blob/main/Documentation/trelloboard.png?raw=true)

# Risk Assessment
![Risk Assessment](https://github.com/Almathex/FundamentalProject/blob/main/Documentation/Risk.png?raw=True)

# Jenkins Build Tools
These are the instructions i gave jenkins when building the app.
![jenkinsBuild](https://github.com/Almathex/FundamentalProject/blob/main/Documentation/Inkedjenkinsbuildtool_LI.jpg?raw=True)

# Testing 
Here I have run 'pytest --cov ./application/ --cov-report term-missing' once the application was live, which performed 7 unit tests and 3 integrated tests 
![testing1](https://github.com/Almathex/FundamentalProject/blob/main/Documentation/test.PNG?raw=True)
And here are the results: 82% Coverage
![Testing](https://github.com/Almathex/FundamentalProject/blob/main/Documentation/pytest.PNG?raw=True)

# Demo
Here is the home page for the app
![Demo1](https://github.com/Almathex/FundamentalProject/blob/main/Documentation/demo1.PNG?raw=True)

This is a the add a wall page
![Demo2](https://github.com/Almathex/FundamentalProject/blob/main/Documentation/demo3.PNG?raw=True)

This is the home page with a view of all added walls
![Demo3](https://github.com/Almathex/FundamentalProject/blob/main/Documentation/demo4.PNG?raw=True)

This a view of the add activity page, which can be accessed from the wall post
![Demo4](https://github.com/Almathex/FundamentalProject/blob/main/Documentation/demo6.PNG?raw=True)

This is a view of the activities available for this wall post
![Demo5](https://github.com/Almathex/FundamentalProject/blob/main/Documentation/demo7.PNG?raw=True)

This is the SQL tables showing the working relationship between walls (location) and activities.
![Relaionship](https://github.com/Almathex/FundamentalProject/blob/main/Documentation/relationship.png?raw=True)

This is editing the activity post
![Demo6](https://github.com/Almathex/FundamentalProject/blob/main/Documentation/demo8.PNG?raw=True)

This is the updated activity
![Demo7](https://github.com/Almathex/FundamentalProject/blob/main/Documentation/demo9.PNG?raw=True)

Here is the change in effect in SQL
![sqlchange](https://github.com/Almathex/FundamentalProject/blob/main/Documentation/activiy.PNG?raw=True)

This is the home page after removing the wall post, which in turn removes the activities assosiated with that post.
![Demo8](https://github.com/Almathex/FundamentalProject/blob/main/Documentation/demo10.PNG?raw=True)

# Room for improvements
There are numerous thing I could have impliemented to make the app more functional, the main thing for me would be making sure there couldnt be any duplicate posts in either of the wall or activity forms, which at the moment the application allows.


