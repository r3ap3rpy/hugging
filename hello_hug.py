import hug

@hug.local()
def hello_world(name: hug.types.text):
    return {"message" : f"Welcome {name} to the hug framework!"}
