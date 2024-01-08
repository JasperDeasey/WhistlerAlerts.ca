# Whistler_Blackcomb_Reservation_Tracker

### Background
I made this program for my friends, as days quickly became reserved on Whistler and we weren't able to go up when we wanted. 


### Usage
It is an online application that allows users to track days on Whistler Blackcomb and recieve an email when the day becomes available.
It was previously available on http://whistleralerts.ca/; however, it has been depreciated since Whistler no longer has a reservations system.

### How it's made
The application is created in Python using Flask to run the website, Selenium to scrape data from whistlerblackcomb.com, Bootstrap to style, a Linode server running Ubuntu, and Apache. The program running on Linode's linux server is slightly modified from the version on this repository.

### Challenges
Getting the linux server to work was very tricky - it was my first time using linux, and the debugging process took time to understand.
