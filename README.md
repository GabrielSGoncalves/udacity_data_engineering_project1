# Udacity Data Engineering Nanodegree Project 1 - Data Modeling with PostgreSQL

## Project Overview
The goal of this project is to create a relational database for a Music Streaming Startup called Sparkify, to help the analytics team understand its customers behaviour. 
Currently, the data is stored in JSON files, and needs to be transferred to a relational schema, so the analytics team can easily answer business questions. 

This project is divided in three parts:

1) Create the working environment and install the database and libraries needed for the project;
2) Create the Relational Database Schema;
3) Define the ETL code for transforming data and loading it into tables;
4) Validate the data arquitecture by performing analytics queries.

---

## 1. Creating the working environment
The first part of the project consists on setting the working environment by creating a new one using Conda and installing PostgreSQL. 

There are two ways to create your working environment, using a conda environment Yaml file or manually creating an environment and installing each library.

### 1.1. Using Conda Env Yaml file
After cloning the project repository, simply create a new environment using the Yaml file.
```
git clone https://github.com/$GitHubName/DataScience_DevEnv.git
conda env create --file=data_eng_project1.yaml
conda activate data_eng_project1
ipython kernel install --user --name=data_eng_project1
```
PostgreSQL and all Python libraries will be installed after running the command above.

### 1.2. Specifying instalation steps

#### 1.2.1. Creating Conda environment
In order to control our development resources we are going to use Conda environment.
```
conda create -n data_eng_project1 python=3.7
conda activate data_eng_project1
```
After this step we can work inside a compartmentalized environment with Python 3.7 and specify the requirements need to develop the project.

#### 1.2.2. Installing PostgreSQL
Next, we need to install PostgreSQL to run locally the database.
```
sudo apt-get install postgresql postgresql-contrib
```
With PostgreSQL installed, we can check its status.
```
sudo /etc/init.d/postgresql status
```
And start it if needed:
``` 
sudo service postgresql start
```

#### 1.2.3. Installing requirements
Finally we install the Python libraries to connect to PostgreSQL Database and perform data manipulation.
```
pip install -r requirements.txt
```

#### 1.2.4. Install Jupyter Kernel
In order to help us develop and test our code we need to install Jupyter Kernel, so that we can run the code on the created Conda environment.
```
ipython kernel install --user --name=data_eng_project1
```
---
## 2. Create the Relational Database Schema
After setting the working environment is time to start creating the Database architecture to store our data.

### 2.1. Creating the default database

In order to run the `create_tables.py` script we need to have a default database already available, so we need to create it first.

Next, we create an user an a database to use in our project.
```
sudo -u postgres createuser -D -A -P student
sudo -u postgres createdb -O student studentdb
```



In order to check if the default database was successfully created we can use the following commands:

```
sudo -i -u postgres
```

And access `psql` command line tool to check the settings:

```
psql
postgres=# \l
```

 You should get the following information in return:

```
                                  List of databases
   Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
-----------+----------+----------+-------------+-------------+-----------------------
 postgres  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 studentdb | student  | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 template0 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
(4 rows)

```

### 2.2. Setting permissions for student user

In order to allow user student to create databases we need add the following permission:

```
postgres=# ALTER USER student WITH CREATEDB;
```

Next, we can check the  user permission.

```
postgres=# \du
```

And student should appear with the Create DB attribute.

```
            List of roles
 Role name |                         Attributes                         | Member of 
-----------+------------------------------------------------------------+-----------
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}
 student   | Create DB                                                  | {}

```

After creating working environment and the default database we are ready to start implementing the scripts to organize data for Sparkify in a relational schema. 

### 2.3. Creating the database and tables

The file `create_tables.py` has the instructions for creating the database and tables. To execute it:

```
python create_tables.py
```

## 3. Creating the ETL code for loading data into tables

With the tables available, the next step consist in extracting, transforming and loading data into it. This process is also known as ETL (acronym for Extract, Transform and Load) and is coded in the `etl.py` file.

```
create etl.py
```

To check if the creation was successful you can run `test.ipynb` Jupyter Notebook.



## 4. Validating the data with SQL queries

Finally, in order to check if the process of creation and loading of data into the database we can use a few queries to aggregate data. You can perform the following queries using the `test.ipynb` Notebook using the `%sql` magic command.

- Get rows with  artist_id and song_id not null:

```sql
%sql SELECT * FROM songplays where song_id is NOT NULL and artist_id is NOT NULL
```

- Number of unique artists in artists table:

```sql
SELECT COUNT(DISTINCT name) FROM artists
```



## 5. Final thoughts

Throughout this project we have reviewed a few key concepts in Relational Database modeling by creating a new schema and parsing and adding data to it. We followed good practices in terms of database normalization and code formatting.

