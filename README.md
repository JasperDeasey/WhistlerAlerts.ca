# Whistler_Blackcomb_Reservation_Tracker

### Background
I made this program for my friends, as days quickly became reserved on Whistler and we weren't able to go up when we wanted. 


### Usage
It is an online application that allows users to track days on Whistler Blackcomb and recieve an email when the day becomes available.
It is available on http://whistleralerts.ca/ and alerts users (after a LOT of trial and error).

### How it's made
The application is created in Python using Flask to run the website, Selenium to scrape data from whistlerblackcomb.com, Bootstrap to style, a Linode server running Ubuntu, and Apache. The program running on Linode's linux server is slightly modified from the version on this repository.

### Challenges
Getting the linux server to work was very tricky - it was my first time using linux, and the debugging process took time to understand.

### Accomplishments
On a local host, the app works just as I hoped it would, and I am even more pround of putting up my first website!

### Future
Currently, the data is held in JSON files; however, adding an SQL database would be a nice addition if I have time. Also, I didn't make it very future-proof. It requires manual changes to update it every month, and automating these will be necessary if the user base becomes big enough.
