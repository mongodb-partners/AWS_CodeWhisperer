## MongoDB + CodeWhisperer

```sh
python3 -m venv venv            # create python virtual env
source venv/bin/activate        # activate virtual env
pip install -r requirements.txt # install dependencies

uvicorn main:app --reload       # run web server

```

Access a list of documents
http://127.0.0.1:8000/posts/

Access a single document
http://127.0.0.1:8000/posts/50ab0f8bbcf1bfe2536dc3fa

Show structure of a single document, and tell that it would be ideal to be able to get a document by its `permalink`

Try to access a document by its permalink
http://127.0.0.1:8000/posts/jNsgObovWyKEoXNydtis

```sh
deactivate # once done, deactivate venv
```
