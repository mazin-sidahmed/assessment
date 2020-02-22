# Koncept Co. Ltd Coding Assessment

This assessment is not a coding challenge. The goal is to cover some of the different programming
aspects and assess the candidate's knowledge. We do not expect the candidate to be familiar with
everything in the code base. However, we expect you to be able to understand the design and programming
concept covered. Our team will discuss them with you to evaluate the level of your knowledge. Moreover,
we would like to see your effort to apply your knowledge to evolve the code.

## About The Application
The application is a simple **API** that offers three simple functionalities of a very premitive inventory.
The available features are create item, search for items by name, delete items by name. The application
writes the records to a flat csv file with the company's name stored in the db directory.

The application is built using **Python Flask** framework. The unit tests can be found in the test directory. The
**RESTful API** was tested manually using a REST client.


## What To Do

The duration of the assessment is one week. During the week we would like to see you to acheive the
following points: 

1. Highlight design problems and implement a better designed solutions
2. Expand the project by implementing a second inventory with your company's name. The company requires
a solution similar to the existing one, however, they would like to use different params to create inventory
items. For example, the items in their inventory have an id, name, price, brand. The search and delete
functionalities are expected to remain the same. Implement the new inventory and try to add unit tests.
3. The search and delete functionalities are not optimal. Make some changes to the code design to enhnace
their performance and ensure the existing unit tests are still green.
4. Any additions will earn you extra points.

## How To Do It
1. Fork the repository into your personal github account.
2. Clone the repository locally
3. Create a virtual python environment and install the required dependencies. If you are using Linux Ubuntu, the
*development.sh* script will create the environment and install the required dependencies.
4. From the root directory run the unit tests using *python -m unittest test.modules.item_test*.
5. To start the server from the root directory run *python src/main.py*.

After finishing the assessment, please share the link with the team and ensure that the right access level is granted.