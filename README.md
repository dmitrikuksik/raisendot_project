# raisendot_project
Django project: User registration, login
Project used Django Rest Framefork

For registration go to link : https://powerful-coast-39824.herokuapp.com/register/
Enter email, username and two passwords.
After registration token will be returned.

To login go to link: https://powerful-coast-39824.herokuapp.com/login/
Enter email and password of user, which already exists (returns user's token).

To get information about user currently logged in: https://powerful-coast-39824.herokuapp.com/users/me/

To get all existing users go to link: https://powerful-coast-39824.herokuapp.com/users/

To logout current user use link: https://powerful-coast-39824.herokuapp.com/logout/

Simple example of request:

 curl https://powerful-coast-39824.herokuapp.com/login/ --data "email=maciek@mail.com&password=maciek"
 
 will return user token for this session.
 
 

