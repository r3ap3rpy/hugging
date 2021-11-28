import hug

def fibonacci(number):
    if number in {0,1}:
        return number
    else:
        return fibonacci(number - 1) + fibonacci(number -2)
    
print(fibonacci(10))

@hug.cli()
@hug.get()
@hug.local()
def fibo(n: hug.types.number, hug_timer=3):
    return {f"The {n}th fibonacci number is":fibonacci(n),'time_elapsed':float(hug_timer)}

if __name__ == '__main__':
    fibo.interface.cli()