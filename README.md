Hello, My name is Abdulellah. welcoome to my messy workplace ~ 

I can't count how many obstacles I had to overcome to reach this point, my bigest enemy was Vagrant..
But thanks to Allah and my kind Instracter Rwan and my classmates 
I beat it and every challenge that try to put me in.

one of the Problems is with this Smart Vagrant...
on of the worst problems IS: not copying my work from my OS to the VM so i had to copy every time i make a change.

### How to Run?

#### PreRequisites:
  * [Python3](https://www.python.org/)
  * [Vagrant](https://www.vagrantup.com/)
  * [VirtualBox](https://www.virtualbox.org/)
  * [gitBASH] (https://git-scm.com/downloads)
  
#### Setup Project:
  1. Downloud newsdata.sql
  2. Move the newsdata.sql file to Vagrant Folder 
  
#### Launching the Virtual Machine:
  1. Vagrant up (to lunch Vagrant)
  2. cd .vagrant (to Enter the vagrant folder in the VM)
  3. scp -P 2222 -r ../LogAnalysis vagrant@127.0.0.1:~/. (To copy my work From OS to VM; I had to do this every time so I alaway open to gitBash)
  4. vagrant ssh
  5. sudo pip3 install psycopg2-binary (to install psycopg2)
  6. cd LogAnalysis
  7. python3 logs.py (and all Magic will start ~)
  
  // or you can do the headic and mess with the data yourself:
  6. psql -d news -f newsdata.sql (to loud the data in local database)
  7. psql -d news (to Enter the server and mess with it)

#### Useful comands

- To show a table columns:
SELECT *
FROM information_schema.columns
WHERE table_schema = 'table_schema'
  AND table_name   = 'table_name';

- To see all tables with detles
\d


#### Views
Create view articlesTable  as
SELECT *
FROM information_schema.columns
WHERE table_schema = 'newsdata'
  AND table_name   = 'articles';
 
Create view authorsTable  as
SELECT *
FROM information_schema.columns
WHERE table_schema = 'newsdata'
  AND table_name   = 'authors';
  
Create view logTable  as
SELECT *
FROM information_schema.columns
WHERE table_schema = 'newsdata'
  AND table_name   = 'log';
 
