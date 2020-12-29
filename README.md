# Whistler_Blackcomb_Reservation_Tracker

## Background


## Usage
I made this program for my friends, as days quickly became reserved on Whistler and we weren't able to go up when we wanted. 

It is an online application that allows users to track days on Whistler Blackcomb and recieve an email when the day becomes available.
Currently, it is available on http://172.105.11.44/; however, this will soon be taken down as Linode does not allow emails to send.put restrictions on free email managers to reduce spam, and without email functionality the program is useless. The version hosted on the linux server is slightly modified to avoid multi-threading.

## How it's made
The application is created in Python using Flask to run the website, Selenium to scrape data from whistlerblackcomb.com, a Linode server running Ubuntu, and Apache. The program running on Linode's linux server is slightly modified so that it avoids apache's restrictions.

## Challenges
Getting the linux server to work was very tricky - it was my first time using linux, and the debugging process took time to understand.

## Accomplishments
On a local host, the app works just as I hoped it would, and I am even more pround of putting up my first website (even if it doesn't work...) !

## Future
To finish the project, I would need to make the email work over the server. This would require:
  1) transition to a new server, such as AWL (using their email services), or
  2) pay for a 3rd party email manager
I also didn't make the app very future-proof, as the reservations are only available for this season (due to Covid-19).
