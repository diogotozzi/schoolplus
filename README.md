# School Plus - API
## _General API system for schools_

[![N|Solid](https://static.wixstatic.com/media/27e25a_240a8c48d21944f0ae16a0f3c730c19c%7Emv2.png/v1/fill/w_32%2Ch_32%2Clg_1%2Cusm_0.66_1.00_0.01/27e25a_240a8c48d21944f0ae16a0f3c730c19c%7Emv2.png)]()

## Features

- Alpine Linux (very light!)
- Python +3.9
- Docker
- MySQL +8.0
- Tests

## Tech

In order to work properly, make sure you have the following installed on your system:

- Linux
- Docker
- Docker Compose
- postman.com - Postman for APIs requests(optional)


## Installation

First, run the following command to add a new entry in you _/etc/hosts_

Let's use [RFC 2606](https://datatracker.ietf.org/doc/html/rfc2606) for local domain names 😉

```sh
echo '127.0.0.1 schoolplus.localhost' | sudo tee -a /etc/hosts
```

Now, inside the project's directory, let's run the following to create all Docker images

```sh
make install
```

With all images up and running, let's create our database

```sh
make migration
```

That's it! Our API is up and running 🙌

## Tests

There are a few functional tests to test the API behavior and responses. Fell free to run the
command below as many times as you want. Tests here are idempotent 🤩

```sh
make test
```

## Endpoints
Our API talks only JSON format.

The file **schoolplus.postman_collection.json** is a Postman file. Import it to test manually the API endpoints:

| URL                  |  Verb  |                               Behavior |
| -------------------- | :----: | -------------------------------------: |
| /api/v1/student      |  GET   |                   Returns all students |
| /api/v1/student/<ID> |  GET   | Returns the student whose ID was given |
| /api/v1/student/<ID> | PATCH  |             Changes a specific student |
| /api/v1/student/<ID> | DELETE |             Deletes a specific student |

PS: I **DO RECOMMEND** use Postman with the *schoolplus.postman_collection.json* file for more API details

## Database
We use MySQL +8.0 database, and all the schema information is at **/api/migrations/0001_initial.py**

## License

BSD [Zero Clause License](https://opensource.org/licenses/0BSD)

**Free Software, Hell Yeah!**
