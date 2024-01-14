
# This project is deployed also you can use below api(domain) instead of localhost.
https://django-crud-apis.vercel.app/api/v1/auth/register
https://django-crud-apis.vercel.app/api/v1/auth/login
https://django-crud-apis.vercel.app/api/v1/auth/logout
etc..


# SIMPLE CRUD API WITH DJANGO REST FRAMEWORK
[Django REST framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.

## Requirements
- Python 3.12
- Django 3.1
- Django REST Framework
- Postgres

## Installation
After you cloned the repository, you want to create a virtual environment, so you have a clean python installation.
You can do this by running the command
```
python -m venv env
```

After this, it is necessary to activate the virtual environment, you can get more information about this [here](https://docs.python.org/3/tutorial/venv.html)

You can install all the required dependencies by running
```
pip install -r requirements.txt
```

## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around _collections_ and _elements_, both of which are resources.


In our case, we have one single resource, `animals`, so we will use the following URLS - `/animals/` and `/animals/<id>` for collections and elements, respectively:

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`animals` | GET | READ | Get all animals
`animals/:id` | GET | READ | Get a single animals
`animals`| POST | CREATE | Create a new animals
`animals/:id` | PUT | UPDATE | Update a animals
`animals/:id` | DELETE | DELETE | Delete a animals


## Use
We can test the API using [Postman](https://www.postman.com/).


First, we have to start up Django's development server.
```
python manage.py runserver
```
Only authenticated users can use the API services, for that reason if we try this:
```
http  http://127.0.0.1:8000/api/v1/animals/
```
we get:
```
{
    "detail": "Authentication credentials were not provided."
}
```
Instead, if we try to access with credentials:
```
http http://127.0.0.1:8000/api/v1/animals/3 "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE2MjA4Mjk1LCJqdGkiOiI4NGNhZmMzMmFiZDA0MDQ2YjZhMzFhZjJjMmRiNjUyYyIsInVzZXJfaWQiOjJ9.NJrs-sXnghAwcMsIWyCvE2RuGcQ3Hiu5p3vBmLkHSvM"
```
we get the animal with id = 3
```
{  "name":  "cow",  "type":  "Herbivore",  "sound":  mou-mou,  "owner":  "admin"  }
```

## Create users and Tokens

First we need to create a user, so we can log in
```
http POST http://127.0.0.1:8000/api/v1/auth/register email="email@email.com" username="USERNAME" password1="PASSWORD" password2="PASSWORD" 
```

After we create an account we can use those credentials to get a token

To get a token first we need to request
```
http http://127.0.0.1:8000/api/v1/auth/login username="username" password="password"
```
after that, we get the token
```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxNjI5MjMyMSwianRpIjoiNGNkODA3YTlkMmMxNDA2NWFhMzNhYzMxOTgyMzhkZTgiLCJ1c2VyX2lkIjozfQ.hP1wPOPvaPo2DYTC9M1AuOSogdRL_mGP30CHsbpf4zA",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE2MjA2MjIxLCJqdGkiOiJjNTNlNThmYjE4N2Q0YWY2YTE5MGNiMzhlNjU5ZmI0NSIsInVzZXJfaWQiOjN9.Csz-SgXoItUbT3RgB3zXhjA2DAv77hpYjqlgEMNAHps"
}
```
We got two tokens, the access token will be used to authenticated all the requests we need to make, this access token will expire after some time.
We can use the refresh token to request a need access token.

requesting new access token
```
http http://127.0.0.1:8000/api/v1/auth/token/refresh/ refresh_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxNjI5MjMyMSwianRpIjoiNGNkODA3YTlkMmMxNDA2NWFhMzNhYzMxOTgyMzhkZTgiLCJ1c2VyX2lkIjozfQ.hP1wPOPvaPo2DYTC9M1AuOSogdRL_mGP30CHsbpf4zA"
```
and we will get a new access token
```
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE2MjA4Mjk1LCJqdGkiOiI4NGNhZmMzMmFiZDA0MDQ2YjZhMzFhZjJjMmRiNjUyYyIsInVzZXJfaWQiOjJ9.NJrs-sXnghAwcMsIWyCvE2RuGcQ3Hiu5p3vBmLkHSvM"
}
```


requesting logout
```
http http://127.0.0.1:8000/api/v1/auth/logout  refresh_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxNjI5MjMyMSwianRpIjoiNGNkODA3YTlkMmMxNDA2NWFhMzNhYzMxOTgyMzhkZTgiLCJ1c2VyX2lkIjozfQ.hP1wPOPvaPo2DYTC9M1AuOSogdRL_mGP30CHsbpf4zA
```
token will not generated & refresh_token will be blacklisted. Remember access token will valid till its expiry.




The API has some restrictions:
-   The animals are always associated with a owner (user who created it).
-   Only authenticated users may create and see animals.
-   Only the owner of animal delete it.
-   The API doesn't allow unauthenticated requests.


### Manangement Commands

-  python manage.py create_animal Lion Carnivore Roar test --extra_information '{\"color\": \"golden\", \"weight\": \"200\"}'

```
Above command will create one animal 
```

-  python manage.py create_animals_from_file D:\New folder\crud_api\animal\animal_file.json 
```
Above command will create list  of animal which is stored in your location(file)

```




### Animal API
```
Get all animals
http http://127.0.0.1:8000/api/v1/animals/ "Authorization: Bearer {YOUR_TOKEN}" 

Get a single animal
http GET http://127.0.0.1:8000/api/v1/animals/{animal_id}/ "Authorization: Bearer {YOUR_TOKEN}" 

Create a new animals
http POST http://127.0.0.1:8000/api/v1/animals/ "Authorization: Bearer {YOUR_TOKEN}" name="Deer" type="Herbivore" owner="admin" 

Full update a animal
http PUT http://127.0.0.1:8000/api/v1/animals/{animal_id}/ "Authorization: Bearer {YOUR_TOKEN}" name="Deer" type="Carnivore" owner="admin"

 
Delete a animal
http DELETE http://127.0.0.1:8000/api/v1/animals/{animal_id}/ "Authorization: Bearer {YOUR_TOKEN}"
```

### Pagination
The API supports pagination, by default responses have a page_size=10 but if you want change that you can pass through params page_size={your_page_size_number}
```
http http://127.0.0.1:8000/api/v1/animals/?page=1 "Authorization: Bearer {YOUR_TOKEN}"
http http://127.0.0.1:8000/api/v1/animals/?page=3 "Authorization: Bearer {YOUR_TOKEN}"
http http://127.0.0.1:8000/api/v1/animals/?page=3&page_size=15 "Authorization: Bearer {YOUR_TOKEN}"
```

### Filters
The API supports filtering, you can filter by the attributes of a animals like this
```
http http://127.0.0.1:8000/api/v1/animals/?name="Deer" "Authorization: Bearer {YOUR_TOKEN}"
http http://127.0.0.1:8000/api/v1/animals/?type="Carnivore" "Authorization: Bearer {YOUR_TOKEN}"
http http://127.0.0.1:8000/api/v1/animals/?sound="mou-mou" "Authorization: Bearer {YOUR_TOKEN}"
http http://127.0.0.1:8000/api/v1/animals/?owner__username=" myUsername" "Authorization: Bearer {YOUR_TOKEN}"
```

You can also combine multiples filters like so
```
http http://127.0.0.1:8000/api/v1/animals/?title="AntMan"&year=2020 "Authorization: Bearer {YOUR_TOKEN}"
http http://127.0.0.1:8000/api/v1/animals/?type=Carnivore&name="Deer" "Authorization: Bearer {YOUR_TOKEN}"
```

