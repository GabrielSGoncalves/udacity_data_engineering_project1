# Udacity Data Engineering Nanodegree Project 1
# Data Modeling with PostgreSQL

## 1. Creating the Conda environment
In order to control our development resources we are going to use Conda environment.<br>
```
conda create -n data_eng_project1 python=3.7
conda activate data_eng_project1
```

## 2. Installing PostgreSQL
Next, we need to install PostgreSQL to run locally the database.
```
sudo apt-get install postgresql postgresql-contrib
```

### 2.1. Checking the database status
sudo /etc/init.d/postgresql status

### 2.2. Starting Postgres if needed
``` 
sudo service postgresql start
```

### 2.1. Create user and database to store project data
```
sudo -u postgres createuser -D -A -P student
sudo -u postgres createdb -O student sparkifydb
```

## 3. Installing requirements
Finally we install the Python libraries to connect to Postgres Database and perform data manipulation
```
pip install -r requirements.txt
```

## 3.1. Install Jupyter Kernel
```
ipython kernel install --user --name=data_eng_project1
```

