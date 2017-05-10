# Koha scrape

Our public library uses [Koha](http://www.koha.org/).
This script logs into my account and my wife's account and downloads our list of books.
It then creates a very basic report of those books and when they are due.

## Getting started

Clone this repo.

```bash
git clone https://github.com/ldfritz/koha-scrape.git
```

Setup your Python environment with the following dependencies.

```
lxml
cssselect
requests
```

These can be installed using `pip` and the requirements file.

```bash
pip install -r requirements.txt
```

Create a `config.json` file with the following pieces of information.
Only the first user record requires a URL.
The filename is optional and is only needed if you want to save the downloaded page.

```json
[
  {
    "url": "http://some.koha-login.url.com/cgi-bin/koha/opac-user.pl",
    "username": "your_username",
    "password": "your_password"
  },
  {
    "filename": "some-filename.html",
    "username": "another_username",
    "password": "another_password"
  },
]
```

Run the script.

```bash
python books.py
```

## License

MIT License

Copyright (c) 2017 Luke Fritz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
