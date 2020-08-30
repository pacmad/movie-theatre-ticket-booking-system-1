# Movie-theatre-ticket-booking-system.(ZOMENTUM TEST)

# For Project's Full Working video and all functions Testing   https://drive.google.com/file/d/16QUUhD3Gl7Rbun28nrkIHwcA-yAgU4gh/view?usp=sharing<br>

<h4>Python Language and Flask is used to design this REST interface. The database used is MongoDB. It stores tickets and person's information which include Name, Mobile Number, Show timing etc</h4> 
The main.py file contains the code for all functions. To install modules pip install -r requirements.txt


<h4>Queries of assessment & their solution</h4>

● An endpoint to book a ticket using a user’s name, phone number, and timings.<br>

=> I created a form which accepts name, mobile, showtime from a user. This information is entered in the ticket database along with a generated unique ticket number. Entering this data in database simulates ticket booking.

● An endpoint to update a ticket timing.

=> Ticket Number and new timing is recieved as form data & the record is updated in database. Acknowlegement is shown as flash message 
 
● An endpoint to view all the tickets for a particular time.

=> User enters the Showtiming, And then database is searched for records with matching showtime. After it, ticket numbers & names of people in those records in database are displayed  

● An endpoint to delete a particular ticket.

=> This is done by searching through database with entered ticket no. and removing that record from database.

● An endpoint to view the user’s details based on the ticket id.

=> After User enters a ticket No. the database is searched using that ticket No . If found, then all other fields of that record are added to a list which is sent to HTML template and displayed . 


● Mark a ticket as expired if there is a diff of 8 hours between the ticket timing and current time.
●Plus point if you could delete all the tickets which are expired automatically.

=> The program visits each record & extracts ticket number & showtiming. Using datetime module, the difference between current time & showtime is calculated,if it exceeds 8hrs then that record is accessed from ticket number and is deleted . This function is automatically called before booking new ticket, so that it deletes all expired tickets.  

●  For a particular timing, a maximum of 20 tickets can be booked.

=> Before booking a new ticket in a particular showtiming, database is searched for all the records with the matching Showtiming . If the records are more than 20, User will not be able to book a ticket in that Showtime.   


 
