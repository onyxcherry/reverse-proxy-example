# Reverse proxy example

Example configuration of reverse proxy using NGINX to Python backend server and static frontend site

## Installation

1. [Install NGINX](https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-open-source/#installing-a-prebuilt-debian-package-from-an-os-repository)
2. Have Python and pip installed  
   Verify with

    ```shell
    $ python -V
    Python 3.12.4
    $ python -m pip -V
    pip 24.0 from ...
    ```

3. Create venv

   ```shell
   python -m venv venv
   source venv/bin/activate
   ```

4. Install pip requirements

   ```shell
   python -m pip install -r requirements.txt
   ```

## Run Gunicorn

Run gunicorn

```shell
gunicorn -w 1 -b 127.0.0.1:5000 'app:app'
```

You should see server logs

```plain
... [INFO] Starting gunicorn 23.0.0
... [INFO] Listening at: http://127.0.0.1:5000 (...)
... [INFO] Using worker: sync
... [INFO] Booting worker with pid: ...
```

Then verify server's response with curl

```shell
$ curl 'http://127.0.0.1:5000/api/aa'
Called api endpoint of path /api/aa
```

## Run NGINX

1. Run nginx

    ```shell
    sudo nginx
    ```

2. Copy static index.html file

    ```shell
    sudo mkdir -p /var/www/html/mysite/
    ```

    ```shell
    sudo cp index.html /var/www/html/mysite/
    ```

3. Use our site config

    ```shell
    sudo cp nginx-site.conf /etc/nginx/sites-available/
    ```

    Linking enables the site

    ```shell
    sudo ln -s /etc/nginx/sites-available/nginx-site.conf /etc/nginx/sites-enabled/
    ```

4. Reload nginx

   ```shell
   sudo nginx -s reload
   ```

   There should not be any (error) output from the command

    You are ready to go!

## Usage

```html
$ curl localhost:8080/
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Frontend</title>
</head>

<body>
    Frontend site
</body>

</html>
```

**Gunicorn server has to be running!**

```shell
$ curl localhost:8080/api/sth
Called api endpoint of path /api/sth
```

```shell
$ curl localhost:8080/whole/prefix/will/be/stripped/
Called endpoint '/'
```

```shell
$ curl localhost:8080/whole/prefix/will/be/stripped/api/abc
Called api endpoint of path /api/abc
```
