
# user_profile
### Create virtual environment

```
$ virtualenv venv -p python3
```

### Activate virtual environment

```
$ source env/bin/activate
```


### Migration command

```
$ python manage.py makemigrations
$ python manage.py migrate
    
```

### Create super admin user

```
$  python manage.py createsuperuser
	>>>  email_address : admin@123.com
	>>>  username : admin
	>>>  password : admin
```

### Run django server

```
$ python3 manage.py runserver
```


### Create docker build using below command 

```
$ sudo docker build -t django-app .
$ sudo docker-compose up --build
```

### Check doker image using below command

```
$ sudo docker ps -a

OR

$ sudo docker images
```

### Download docker image using below command

```
$ sudo docker pull django
```


"# test_prac" 
