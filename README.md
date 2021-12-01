# Whose Your Human

## __App overview__
---
This app was created to solve the problem I have every single day while walking my dog. More often than not I am walking down the road with my dog and we spot a dog we have met and of course I remember the dog's name without forgetting a dog name like taco or cheddar!
It is the Humans name I can't remember for the life of me! Was it Chris or another name? This app aims to solve that problem.
Designed primarily using Django and Python to query and store information on a Postgres database. Whose your Human aims to eliminate the uncertainty of dog walks. You can upload a photo and Have it stored in an AWS S3 bucket so you always have references. If not you can store a detailed or short description of the dog. and Nowadays almost every pet has an Instagram so if you record that correctly you can access the Instagram feed in a click of a button! 
 



## __Once you get to the app__
---
Upon visiting the app you will be greeted with a login page where you may enter credentials or sign up. You have no real ability to do anything else until you become a user in the database.
 
From there you can use the nav bar to view all pets, but if you are a new user you will not see anything. From there the user should add a pet. The only fields that are required are the pet name and parent 1's name. Everything else you can fill in as you learn more!
 
Once a pet is created the user can click on the card and see the details page this is where you can do a lot of steps. From here you can edit the information to anything new you've learned or even misheard. You can delete the pet from your stored list because sometimes friends move away! The user can select a file then upload that file which will be stored and displayed on AWS an S3 bucket.


ERD: <img width="500" alt="ERD" src="https://user-images.githubusercontent.com/51840257/144247696-07e07058-37c8-4927-a736-703f29e212f9.png">

**[Trello Board](https://trello.com/b/dR6YJCxS/whos-your-human)** 

You can access the site **[here](https://whoseyourhuman.herokuapp.com/)**!

## Technologies Used:
 * HTML
 * CSS
 * JavaScript
 * Postgres DB
 * Python
 * Django library 


# screenshots

<img width="258" alt="Not logged in" src="https://user-images.githubusercontent.com/51840257/144248575-c790b44f-8628-4972-a426-0b7c76c65a5e.png">
<img width="258" alt="Index page" src="https://user-images.githubusercontent.com/51840257/144248743-ce191847-2d38-4c91-9b5d-c9f450c5ee68.png">
<img width="500" alt="Create page" src="https://user-images.githubusercontent.com/51840257/144248980-fef2455a-6c1a-46fa-be7a-1c9df11bc6d6.png">
<img width="500" alt="More details" src="https://user-images.githubusercontent.com/51840257/144249044-72b40397-0ea7-48df-981e-06f6639f8729.png">
<img width="500" alt="Mobile Home Page" src="https://user-images.githubusercontent.com/51840257/144250171-98db3343-8206-4c7a-a127-f41f75cd1665.png">
<img width="500" alt="mobile create Page" src="https://user-images.githubusercontent.com/51840257/144250336-dbe69865-a3d7-46e2-bea8-afc849a27b87.png">


## Future Enhancements/ Next Steps
---
 * Store instgram tokens and display a table of instagram the pets current instagram feed
 * Quality of images
 * Implement a playdate resource and maybe schedule playdates.
 * send an email the day before a scheduled playdate. 
 * Delete photos option/ when a user changes the picture the previos one is deleted in s3
 * If deleting in s3 is to laborsome. Add a section of photos where the user can see all the photos they have taken!
