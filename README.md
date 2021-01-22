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

### 1.1. Conda environment
In order to control our development resources we are going to use Conda environment.
```
conda create -n data_eng_project1 python=3.7
conda activate data_eng_project1
```
After this step we can work inside a compartmentalized environment with Python 3.7 and specify the requirements need to develop the project.

### 1.2. Installing PostgreSQL
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
Next, we create an user an a database to use in our project.
```
sudo -u postgres createuser -D -A -P student
sudo -u postgres createdb -O student sparkifydb
```
### 1.3. Installing requirements
Finally we install the Python libraries to connect to Postgres Database and perform data manipulation.
```
pip install -r requirements.txt
```
### 1.4. Install Jupyter Kernel
In order to help us develop and test our code we need to install Jupyter Kernel, so that we can run the code on the created Conda environment.
```
ipython kernel install --user --name=data_eng_project1
```

## 2. Create the Relational Database Schema
After setting the working environment is time to start creating the Database arquitecture to store our data.

