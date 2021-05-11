# Get started
Run the following: <br>
`docker-compose up` <br> <br>
Sample data will be created, you can view / create / edit it by accessing `localhost/admin/` <br>
Default user: `ben`
Default pass: `123`

### If you are debugging this yourself
##### Do the following: <br>
Install Requirements: 
`pip install -r requirements.txt` <br>
Run PostgreSQL docker:
`docker-compose up db` <br>
Run the server: 
`python manage.py runserver <port>` <br> <br>
You can use this admin command from root dir to generate sample data: <br>
`python manage.py init_sample_data` <br>
And this one to reset and generate new data: <br>
`python manage.py reset_sample_data`
<br><br>
Note the `DEBUG=True` was left for convenience

# Use the Candidate Finder
Perform a GET request to `/api/job/<job_id>/find/candidates/` <br>
You can find ids from the django admin or just try ids `1-8`