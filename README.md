# README #

### What is this repository for?

* Python lib used obtain a new token for OAuth access to the [TDAmeritrade API](https://developer.tdameritrade.com/apis)
* Version 1.0

### About 

#### TL;DR

This lib will pull your TDA Credentials and 2FA info from the `.env` file 
and inject them into the TDA web form using selenium.
 
#### The Quest...

Unfortunately the TDAmeritrade API does not offer a simple / automated approach 
for refreshing your OAuth token for the TDAmeritrade API. There is an OAuth endpoint to refresh your access token (and perhaps im just miss interpreting this),
but to use it you need a valid refresh token, which apparently expires every 90 days according to 
the TDA article ["Simple Auth for Local Apps"](https://developer.tdameritrade.com/content/simple-auth-local-apps).
This means going through the process described on this page manually every 90 days, 
which for me was not an option.

While doing some R&D to get a working fully automated TDA API Client I came across several Python TDA API clients.
To obtain an access token, most of these libs would just point you to the TDA API 
["Simple Auth for Local Apps"](https://developer.tdameritrade.com/content/simple-auth-local-apps) 
article which describes a rather lengthy process to obtain an OAuth token to be able to use the TDA API. 

I came across this lib, [addisonlynch/pyTD](https://github.com/addisonlynch/pyTD), 
and discovered it was using `webbrowser` to launch a browser to facilitate the auth process, which was one step in the right direction.

[See location in code](https://github.com/addisonlynch/pyTD/blob/28099664c8a3b6b7e60f62f5e5c120f01e3530af/pyTD/auth/manager.py#L73)

After more digging I found this lib, [timkpaine/tdameritrade](https://github.com/timkpaine/tdameritrade), 
which actually implemented a selenium web driver to automate the TDA Auth form. 

[See location in code](https://github.com/timkpaine/tdameritrade/blob/master/tdameritrade/auth/__init__.py)

Awesome, exactly what I was looking for! 

Well... Unfortunately the TDA Auth web form flow now requires 2FA so I couldn't use this to completely automate the process, but help me get started.

I only had to implement a few extra selenium calls for the remainder of the web flow by using the security questions 2FA option.

This all led to the development of this repo. 


This repo, like [timkpaine/tdameritrade](https://github.com/timkpaine/tdameritrade), uses Selenium under the hood 
to execute the entire TDAmeritrade Auth web flow in a chrome browser.

It will auto detect the OS and grab the proper selenium driver using the same implementation used 
[here in timkpaine/tdameritrade](https://github.com/timkpaine/tdameritrade/blob/master/tdameritrade/auth/__init__.py)


### How do I get set up?

* Install python3
* Install dependencies

```
$ pip install -r requirements.txt
```

* Copy `.env.default` to `.env` and fill in

### Usage

Ensure you have filled out the env var values in `.env`

```python
# For Silent mode ( Chrome in headless mode )
TDATokenRefresher.get_oauth_token()

# For Visual mode ( Shows Chrome window )
TDATokenRefresher.get_oauth_token(use_headless_web_driver=False)
```

`TDATokenRefresher.get_oauth_token()` will return a TDA OAuth token which should look like this:

```json
{
    "access_token": "<token_here>",
    "refresh_token": "<token_here>",
    "scope": [
        "PlaceTrades",
        "AccountAccess",
        "MoveMoney"
    ],
    "expires_in": 1800,
    "refresh_token_expires_in": 7776000,
    "token_type": "Bearer",
    "expires_at": 1587922086.2939131
}
```

NOTICE: The responsibility falls on the user to securely store these tokens.

### Resources

https://github.com/timkpaine/tdameritrade

https://github.com/addisonlynch/pyTD

Shout out to @timkpaine and @addisonlynch. Thank you!
