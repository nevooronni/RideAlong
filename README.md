# RIDEALONG

## DESCRIPTION
This is a web application that allows users to book rides and let drivers share their ride space with the users at a charged fee.

## AUTHOR
Neville Oronni

## USER STORIES
A **user** should be albe to:
1. Sign in to the application to start using as a use or driver.

2. Set up a profile about me and a general location.
3. Find a list of drivers near me.
4. View a map with the location of all pickup points.
5. Review a driver and also be reviewed by the driver.
6. View the current space left in a driver's car and get to book It.

7. A user can sign up either as a passenger or as a driver.
8. A drivers profile must contain details about the car. Ie. capacity, Number plates color, and picture of the car.
A driver must set his current location and where he driving to.


## SPECIFICATIONS
| Behaviour | Input | Output |
| --------------- | :----------:| --------: |
|Sign into application |click sigin button | logged into the index page|
|set up a profile | click edit profile | see posted image display in profile page and details |
|find a list of drivers near me | Click ride | see list of drivers near me |
|view a map with picku points | click my booked rides | displayed map with pickup points |
| review a driver | Click review button and fill form | see listed review in my rides page |
|view current space left in car | click on book ride | should  see ride details and car space left |
|sign up or driver or rider| click sign in and choose | should be sigin in as either driver/rider |
|see details in driver profile about car | sign in to driver | see details about car,capacity,color,number plates e.t.c | 

## SETUP/INSTALLATION
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

* Clone the repo
  * git clone **repo_url** e.g git clone https://github.com/nevooronni/unsplash-new.git
* Create and start a virtual environment inside project directory
  * virtual venv virtual
  * source virtual/bin/activate

* Install all the dependencies in the file > requirements.txt
  * pip install -r requirements.txt
* Start the development server
  * python3.7 manage.py runserver

## PREREQUISITIES
* Python3.6
* Django

## TECHNOLOGIES USED
* Python3.6
* Django
* Postgresql
* Bootstrap3

## BUGS
No known bugs

## CONTACT
[nevooronni@gmail.com](nevooronni@gmail.com)

## LICENCE
Licenced under a MIT licence
