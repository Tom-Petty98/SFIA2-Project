# SFIA2-Project

## Story scenario generator with microservice arcitecture

### Table of contents

1. Introduction
1. Breif
1. Soloution
1. Trello board
1. Database
1. Risk Assessment
1. Issues
1. Testing
1. Deployment
1. Improvements for the future

### Introduction
The focus of this project was to make a core dev ops pipeline and design an application with a microservice arcitecture. 

### Brief 
Create a functional website following best practices. The website had to be comprised of four microservices that functioned and could be deployed inderpendently and must persist some data into a database. It must be fully intergrated with a vcs (git), have clear documentation and follow agile principles. This includes a project tracking board identifing user stories, tasks and progression. 

### Soloution 
I decided to create a website that would generate three random words. A setting word was randomly generated by service 2, a noun was generated by service 3 and service 4 returned the outputs of service 2 and 3, formated them and added a tempo. Service 1 was the frontend service and use a http request to get the words from service 4. Users could then create a story given the random scenario and share the story. The story database has full CRUD functionality. 

The app used Nginx for reverse proxy to allow access from only port 80. The develpoment features a jenkins pipeline which is activated by a webhook. Jenkins builds images and pushes them to docker hub. It uses ansible to setup the correct environment on additional VM's for a swarm deployment aswell as adds workers. Finally jenkins deploys the services as a stack using docker compose and each container is replicated allowing a rolling deployment.

### Trello board
![](documentation/Trello.jpg)

### Database
![](documentation/Model.jpg)

The database used allowed users to share the stories the created. It also stored the words that were given to create the story. GCP SQL was chosen as it is much easier to setup. 

### Risk Assessment
![](documentation/Risk_assessment.jpg)

### Issues
While there were no major issues many small issues did occur. An example of this was one of the fresh worker vms for some reason couldn't install docker. While a couple of fixes such as updating the apt cache on the vm were trialled none succeded. So this worker was removed and a new vm was booted up which seems to have worked.  

### Testing
![](documentation/coverage.jpg)

The missing coverage is due to my home view which has both a post story form and handles http requests. These requests throw an error due to it being an isolated service. This could be fixed using mocking but I didnt have the time to implement it. On top of this adding intergration testing would ensure the functionality of the website is working as expected. Finally the testing infrastructed should be incorpated into the jenkins pipeline.

### Deployment
![](documentation/CI-CD_pipeline.jpg)

Intital testing for the rolling deployment utilised a webhook between github and docker however, each image was queued for over 10 mins on average. Therfore it was decided it was too slow to showcase rolling deployment. Instead the images were built locally by jenkins and pushed to docker hub. Also if I had more time I would incorparate a testing stage and suite into the pipeline, creating a pipeline that more closely represents industry standards. Finally I would incorparate intergration testing with selenium.

### Improvements for the future
Due to this being an individual project and the app being very basic I didnt prioritise testing as much as I should of. So the biggest improvement I could make would be to add comprehensive testing with intergration testing. Which would be incorparated into the jenkins pipeline following a test driven development approach.

![](documentation/Future_ERD.jpg)

If I were to develop this app further I would like to:
1. Add mocking functionality to increase unit testing coverage.
1. Add intergration testing.
1. Add a testing stage to the jenkins pipeline.
1. Implement the users model with the ERD shown above. This would include login and restricted access.
1. Implement an upvoting system to reward some of the best stories.


### Authors
#### By Tom Petty
