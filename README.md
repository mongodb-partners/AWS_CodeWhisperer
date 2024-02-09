## MongoDB + CodeWhisperer

#### Step 0

Make sure **python3** is installed. **Step 1** (see below) will ensure you have all dependencies installed on a virtual environment.

Make sure you have a **MongoDB Atlas cluster** with the **[sample dataset loaded](https://www.mongodb.com/docs/atlas/sample-data/#load-sample-data)**. This demo uses the `sample_training` dataset.

Copy the `.env.example` file to `.env` and replace `ATLAS_URI` with the proper connection string of your Atlas cluster.

#### Step 1

```sh
python3 -m venv venv            # create python virtual env
source venv/bin/activate        # activate virtual env
pip install -r requirements.txt # install dependencies

uvicorn main:app --reload       # run web server

```

#### Step 2

Access a list of documents
http://127.0.0.1:8000/posts/

Access a single document
http://127.0.0.1:8000/posts/50ab0f8bbcf1bfe2536dc3fa

Show structure of a single document, and tell that it would be ideal to be able to get a document by its `permalink`

Try to access a document by its permalink
http://127.0.0.1:8000/posts/jNsgObovWyKEoXNydtis

#### Step 3

On `routes.py` delete everything below `def find_post(id: id,` and alter the route declaration to the following:

```py
@router.get("/{permalink}", response_description="Get a single post by permalink", response_model=Post)
def find_post(permalink: str, request: Request):
  	█
```

Place your cursor on the position of the block character above (`	█`) and CodeWhisperer should autocomplete with the proper suggestion. Ideally the suggestion will look like the following:

```py
@router.get("/{permalink}", response_description="Get a single post by permalink", response_model=Post)
def find_post(permalink: str, request: Request):
    if (post := request.app.db["posts"].find_one({"permalink": permalink})) is not None:
        return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with permalink {permalink} not found")
```

Save the file.

#### Step 4

Since `uvicorn` is running, it should auto-reload the changes automatically.

Try to access a document by its permalink. This time it should work. ✅
http://127.0.0.1:8000/posts/jNsgObovWyKEoXNydtis

#### Step 5

Now tell how it's required to have an API endpoint that gives the total amount of posts of each tag

**before** `@router.get("/{permalink}"` add the following code snippet:
> (⚠️ it's important this is added before the permalink route!)

```py
@router.get("/tags", response_description="Get the total of posts of each tag")
def post_totals_per_tag(request: Request):
    """
    Get the total of posts of each tag using MongoDB facets
    """
    █
```

Place your cursor on the position of the block character above (`	█`) and CodeWhisperer should autocomplete with the proper suggestion. Ideally the suggestion will look like the following:

```py
@router.get("/tags", response_description="Get the total of posts of each tag")
def post_totals_per_tag(request: Request):
    """
    Get a list of total of posts of each tag using MongoDB facets
    """
    return list(request.app.db["posts"].aggregate([
        {"$unwind": "$tags"},
        {"$group": {"_id": "$tags", "total": {"$sum": 1}}}
        # {"$project": {"_id": 0, "tag": "$_id", "total": 1}} # valid (CodeWhisperer might suggests this)
    ]))
```

> (⚠️ it's important the result is converted into a **list**. AKA: `list(`)

CodeWhisperer might suggest additional lines (often comments showing what the output looks like). You can discard those lines or use _`Cmd/CTRL`+`->`_ to accept just the code portion of its suggestion.

#### Step 6

Select the aggregation the body of the function that was generated in the previous step.
In the example above, this is the portion that should be selected:

```txt
    return list(request.app.db["posts"].aggregate([
        {"$unwind": "$tags"},
        {"$group": {"_id": "$tags", "total": {"$sum": 1}}}
        # {"$project": {"_id": 0, "tag": "$_id", "total": 1}} # valid (CodeWhisperer might suggests this)
    ]))
```

In the Activity Bar, select Amazon Q and ask the following to it:

```txt
**"Explain selected code"**
```

> (ℹ️ feel free to click in the "explain selected code" suggestion if it shows up)

Quickly read the response and highlight how useful it is for developers to quickly understand portions of the code that they are not familiar with.

#### Step 7

Debrief on what has been shown

```sh
deactivate # once done, deactivate venv
```
