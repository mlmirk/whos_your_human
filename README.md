# Whose Your Human

## __App overview__
---
This app was created to solve the problem I have every single day while walking my dog. More often than not I am walking down the road with my dog and we spot a dog we have met and of course I remember the dog's name without forgetting a dog name like taco or cheddar!
It is the Humans name I can't remember for the life of me! Was it Chris or another name? This app aims to solve that problem.
Designed primarily using Django and Python to query and store information on a Postgres database. Whose your Human aims to eliminate the uncertainty of dog walks. You can upload a photo and Have it stored in an AWS S3 bucket so you always have references. If not you can store a detailed or short description of the dog. and Nowadays almost every pet has an Instagram so if you record that correctly you can access the Instagram feed in a click of a button! 
 



## __Once you get to the app__
---
Upon visiting the app you will be greated with a login page where you may enter credetails or sign up. You have no real ability to do antything else until you become a user in the database.

From there you can use the nav bar to view all pets, but if you are a new user you will not see anything. From there the user should add a pet. The only fields that are required are the pet name and parent 1's name. Everything else you can fill in as you learn more!

Once a pet is created the user can click on the card and see the details page this is where you can do a lot of steps. From here you can edit the infomation to anything new you've learn or even misheard. You can delete the pet from you stored list because sometimes friend move away! The user can select a file then upload that file which will be stored and displayed on AWS an S3 bucket

ERD: <img width="500" alt="ERD" src="">


You can access the site **[here]()**!

## Technologies Used:
 * HTML
 * CSS
 * JavaScript
 * Postgres DB
 * Python
 * Django library 


# screenshots

<img width="258" alt="Not logged in" src="">
<img width="258" alt="Landing page" src="">
<img width="500" alt="Index page" src="">
<img width="500" alt="More details" src="">
<img width="500" alt="Home Page" src="">
<img width="500" alt="Home Page" src="">
<img width="500" alt="Home Page" src="">


## Future Enhancements/ Next Steps
---
 * Store instgram tokens and display a table of instagram the pets current instagram feed
 * Quality of images
 * Implement a playdate resource and maybe schedule playdates.
 * send an email the day before a scheduled playdate. 
 * Delete photos option/ when a user changes the picture the previos one is deleted in s3
 * If deleting in s3 is to laborsome. Add a section of photos where the user can see all the photos they have taken!
  