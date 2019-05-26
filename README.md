Bookstore sample project

# Setup
If you do not have anaconda setup on your machine. Please follow guide at
```bash
https://docs.anaconda.com/anaconda/install/
```

You will also need mongodb. Plesae follow the instruction at
```bash
https://docs.mongodb.com/manual/installation/
```
Once anaconda has been setup, you should be able to find version by running
```bash
conda -V
```

To setup conda environment for this project
```bash
conda env create environment.yml
```
Activate the new environment with
```bash
conda activate CMPE272
```
To run the unit tests
```bash
python -m pytest
```
To generate seed data for dev db
```bash
python db_seed <dev_db_name>
```
To start the app server in dev mode
```bash
export FLASK_APP=app
export FLASK_ENV=develop
flask run
```