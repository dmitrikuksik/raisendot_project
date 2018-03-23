# raisendot_project
Django project: User registration, login

I was using Django Rest Framefork for creating REST API.

For registration follow link : https://powerful-coast-39824.herokuapp.com/register/
After registration token will be returned.

To login follow link: https://powerful-coast-39824.herokuapp.com/login/
Enter email and password of user, which already exists (returns user's token).

To get information about user currently logged in: https://powerful-coast-39824.herokuapp.com/users/me/

To get all existing users go to link: https://powerful-coast-39824.herokuapp.com/users/

To logout current user use link: https://powerful-coast-39824.herokuapp.com/logout/

Simple example of request:

 curl https://powerful-coast-39824.herokuapp.com/login/ --data "email=maciek@mail.com&password=maciek"
 
 will return user token for this session.
 
 

