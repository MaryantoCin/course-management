# Course Management

This project is created for learning the basics of DRF(Django Rest Framework), especially creating and reading using nested serializers.

## Tech

This project uses:

- Django 2.2
- DjangoRestFramework 3.9.2
- Vagrant

## Installation

This project requires:

- Vagrant
- VirtualBox

Run Vagrant

```sh
vagrant up
vagrant ssh
cd /vagrant
```

Create and activate Python virtual environment

```sh
python -m venv ~/env
source ~/env/bin/activate
```

Install the dependencies from requirements.txt

```
pip install -r requirements.txt
```

## Development

Run server

```sh
python manage.py runserver 0.0.0.0:8000
```

Migrate:

```sh
python manage.py makemigrations
python manage.py migrate
```

In this project, Vagrant will map port 8000 in the VM to port 8001 in local machine. You may change this within the VagrantFile if necessary.

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:8001
```

## License

MIT
