# ShortURL Example App

### by Hasan Rayan

ShortURL is a URL shortener backend app. It reduces the number of characters in a URL, making it easier to share.
It has been developed with Python, Django and Django REST Framework.

## APIs

The app has the following APIs:

### Root

`GET /`
It shows welcome message

### Create URL

`POST /url`
It creates a short URL for a provided URL

### Forward to target URL

`GET /{url_key}`
It forwards a short URL to a target URL

### Get admin info of a short URL

`GET /manage/{secret_key}`
It returns the details of a short URL, only if you have the secret key of that short URL.
Also, it shows how many times the short URL has been visited so far.

### Delete a short URL

`DELETE /manage/{secret_key}`
If you have a secret key of a short URL, you can delete it with this URL.
