# supreme-bot

Automates purchases for newyorksupreme.com product drops.

# Usage:

#### STEP ONE
```
$ git clone https://github.com/jg-fisher/supreme-bot
$ cd supreme-bot
$ virtualenv venv --python=python3.7
$ pip install -r requirements.txt
```

#### STEP TWO
Create a config.py file in the local directory that looks similar to this for each order you are placing.

```
keys = {
        "email": "youremail@email.com",
        "password": "yourpassword",
        "search_key": "dunk",
        "target": ["premium"],
        "sizes": ["400", "410"],
        "payment_method": "credit_card",
        "test": False,
        "credit_card_number": "5185363648774253",
        "credit_card_name": "JOHN C OLIVER",
        "credit_card_month": "11",
        "credit_card_year": "2021",
        "credit_card_cvv": "537",
        "parcelamento": "6"
}
```

#### STEP THREE
You may have to download the correct chromedriver for you operating system (Linux/OSX/Windows), put the chromedriver the supreme-bot directory with the script.

chromdriver: http://chromedriver.chromium.org/downloads

#### STEP FOUR
```
$ python bot.py
```
