# Koha scrape

Our public library uses [Koha](http://www.koha.org/).
This scripts logs into my account and my wife's account and downloads our list of books.
It then creates a very basic report of those books and when they are due.

## Getting started

Clone this repo.

Setup your Python environment with the following dependencies.

```
lxml
cssselect
requests
```

Create a `config.json` file with the following pieces of information.

```json
[
  {
    "url": "http://some.koha-login.url.com/cgi-bin/koha/opac-user.pl",
    "filename": "some-filename.html",
    "username": "your_username",
    "password": "your_password"
  }
]
```

Run the download and then the parser.

```bash
python download.py
python parse.py
```
