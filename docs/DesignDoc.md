
# PROJECT Design Documentation

> _The following template provides the headings for your Design
> Documentation.  As you edit each section make sure you remove these
> commentary 'blockquotes'; the lines that start with a > character
> and appear in the generated PDF in italics._

## Team Information
* Team name: TEAMNAME
* Team members
  * MEMBER1
  * MEMBER2
  * MEMBER3
  * MEMBER4

## Executive Summary

This is a summary of the project.


## Requirements

This section describes the features of the application.

### Definition of MVP
> _Provide a simple description of the Minimum Viable Product._

### MVP Features
>  _Provide a list of top-level Epics and/or Stories of the MVP._


## Architecture and Design

### Software Architecture
![architectural-pattern](..%2Fassets%2Farchitectural-pattern.png)

For the software architecture design diagram of “TigerBets”, we adopt a layered approach. From top to bottom, it contains four layers:

**Presentation Layer**:

- Contains the User Interface (UI) and Simple Visual Charts.

**Application Layer**:

- Consists of Business Logic, Application Controllers for Authentication (Auth), Events, Accounts, Betting, and Analytics.

**Domain Layer**:

- Involves Business Rules and Data Analytics, along with Entities such as Event, User, and Bet.

**Persistence Layer:**

- Includes the Database for Authentication (Auth), User information, Events, Bets, and the Leaderboard.

Each layer communicates information down to the next, indicating that the upper layers rely on the data and services provided by the lower ones. This architectural design emphasizes separation of concerns, with each layer focusing on specific functionalities to enhance the maintainability and scalability of the software.


### Use Cases
 
![use-case-diagram](..%2Fassets%2Fuse-case-diagram.png)
 
***

**Use Case Detailed Descriptions**

This use case diagram describes two actors in the TigerBets system: regular end users and system administrators. Each has their own functions and use cases. The diagram also illustrates the relationship between these two different actors. 

------

**Actor: End User**

- **Register or Login User**:  Users must log in with their own account to access the main page. If they do not have an account, they need to register a new account that has not been used by other users on the login interface. Once the registration is complete, users can log into the system with their new account.

- **Manage Profile**: After logging into the page, users can fill in or update their personal information on the user information page.

- **View Events**: Users can view the sporting events they are interested in on the event page. 

- **Place Bets and update points**: Users can choose the events they are interested in and place bets on an outcome with points. If the user does not have any points to spend, they will receive an alert message and the event will not accept bets from said user.

- **Update Points**: Once an event has ended, Users who bet on the event will receive additional points depending on the outcome of the event.

- **View Leaderboard**: Users can view the standing of points among all other users through the system's leaderboard

------

**Actor: Admin**

- **Login User**: Different from regular users, administrators have a different login interface. Accounts of regular users cannot log into the administrator's account. Only accounts with administrator privileges can log into the administrator page.

- **View Leaderboard**: Admins can view the standing of points among all end users through the system's leaderboard

- **Manage Users**: Administrators can manage the accounts of end users, such as updating their information and deleting their accounts from the system.

- **Manage Events**: Administrators can update and upload new events, as well as delete events.

 


### Class Diagram
> _Place a class diagram here._
> _Describe your class diagram._
