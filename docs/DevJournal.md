# Dev Log

## Intention: I'll log my progress here as I develop

## Initial
Started by creating a new flask application and adding poetry and creating a 'Walking Skeleton' for the application.

## 2023-04-05
Intention: The Coin Purse application acts as a 'running total' with additions and removals from a player's 'coin purse' it tracks the actions that a player takes... They buy arrows, sell an old sword all of that is tracked by date and session number.

tables: player, character, account, transaction

See the docs folder for ER diagram of the above tables.

## 2023-04-08
Trying to be really intentional with the addition of the DB tables, I've added my intended design to the docs folder with and Entity Diagram. Don't want to rush, Just want to add the tables and get migrations running. I expect I'll run this against postgres in production, but for testing it will run against an in-memory database. I'm anticipating some issues with: configuration, uwisgi setup and using the instance folder properly.

## 2023--4-30
Added an instance folder and I was able to also add a config.toml file, set up it's configuration values and add it to the application. I've also decided to make this an API vs. a web app. I'll do the front end in Vue... which I'm also learning.

## 2023-05-02
Adding Flask-Migrate to the application, found out that the following command initializes the migrations folder: `flask --app startup db init`
Note to self: see Obsidian Flask-Migrate Notes!

## 2023-05-22
After a painful run I have migrations working, looks like this version of flask-migrate or alembic doesn't recognise tables that have base classes and inherrit from them. When I removed the base class from the tables the migrations worked. I'll have to look into this more.

## 2023-07-20
Fixed up a bad test fixture, now running properly. 
