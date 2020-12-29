# Whistler_Blackcomb_Reservation_Tracker
This is an online application that allows users to track days on Whistler Blackcomb and recieve an email when the day becomes available. 
It is created in Python using Flask to display the website and Selenium to scrape data from whistlerblackcomb.com.


Currently, it is available on http://172.105.11.44/, hosted on a Linode linux server and using Apache to reach the web; however, this will soon be taken down as Linode put restrictions on free email managers to reduce spam, and without email functionality the program is useless. The version hosted on the linux server is slightly modified to avoid multi-threading.
