#%%
import requests

tweet = {
    "username": "fede",
    "content": "Potato!"
}

requests.post("http://127.0.0.1:8080/tweets", json=tweet)
# %%
