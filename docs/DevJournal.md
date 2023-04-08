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