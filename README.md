# extreme-tech
### Problem statement
Create a django server integrang database for email automaon, where the user can
enter an email address, the name of the receiver and his/her city. The email subject
should contain "Hi (Name_of_the_reciever), interested in our services' . The email body
should contain the temperature of the city at the time of sending mail, and an emoji of
your choice depicng the temperature correctly.

### Third party API used in this project
*http://api.openweathermap.org* To get the weather data of a given city <br>
*https://www.mailjet.com/email-api/* To send the email to the user

### Project details 
Challenge was to send the email to the users after there contact and email is saved to the model so I had to figure out to how to send email to user from django admin side itself withouht building any UI. So Django signals enables us to do certain action post/pre changes in django models. So I have used Django model `post_save` signal to send the email to user just after saving their data to the model. 
