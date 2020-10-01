# mongodb-flask-python with docker
This project is the part of Software Defined System(SDS) at Chulalongkorn University.

App:
  - Python
  - Flask
  
Database:
  - MongoDB
  
Features:
  - counting the refresh time of user and timestamp to show in list.
  - persistant data
  
To run this:
  - clone this repository
  - go inside the repository
  - run `docker-compose up -d`
  - to check the result, go to localhost:5000 and trying to refresh the webpage
  - to check the persistant, run `docker-compose down` then run `docker-compose up -d`
  
