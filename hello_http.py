import hug

@hug.get(examples = 'a=10&b=20')
@hug.local()
def addition(a: hug.types.number, b: hug.types.number):
    return {"result":(a + b)}


@hug.get(examples = 'name=Daniel&age=30')
@hug.local()
def welcome(name: hug.types.text, age: hug.types.number):
    return {"message" : f"You are {age} number of years old {name}"}
