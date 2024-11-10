from typing import List, Set
from venv import create
from typing import List, Union

from flask import Flask, Response, request

from closure import create_multiplier
from funcs import square, eliminate_odd, all_of_them
from higher_order import apply_operation, add, multiply
from number import Number


from palindrome import palindrome_check

app = Flask("app")

@app.get("/418")
def teapot() -> Response:
    tea=r"""
                 ;,'
     _o_    ;:;'
 ,-.'---`.__ ;
((j`=====',-'
 `-\     /
    `-=-' 
    """
    return Response(tea, mimetype="text/plain")

# A
@app.post("/calc/func")
def calc_func() -> Response:
    data = request.get_json()
    num_to_square = data["number"]
    result = num_to_square ** 2
    number = str(result)
    return Response(number, 200)

@app.post("/calc/oop")
def calc_oop() -> Response:
    data = request.get_json()
    num_to_square = data["number"]
    num_to_square = Number(value=num_to_square)
    num_to_square=num_to_square.square()
    num_to_square = str(num_to_square)
    return Response(num_to_square, 200)

# B1
@app.post("/palindrome")
def palindrome() -> Response:
    data = request.get_json()
    word=data["word"]
    if palindrome_check(word):
        return Response(f"{word} is a palindrome", 200)
    else:
        return Response(f"{word} is not a palindrome", 200)

# B2G
@app.get("/greet/<name>")
def greeting(name:str) -> Response:
    greet = lambda name: f"Hello, {name}!"
    return Response(greet(name))

@app.post("/advanced_calc")
def advanced_calc() -> Response:
    data = request.get_json()
    operation = data["operation"]
    num1 = data["num1"]
    num2 = data["num2"]
    match operation:
        case "add":
            action = add
        case "mult":
            action = multiply

    result = apply_operation(num1, num2, action)
    number = str(result)
    return Response(number, 200)

#B3E
@app.get("/multiply_by_3/<int:number>")
def multiply_by_3(number:int) -> Response:
    multiply_3=create_multiplier(3)
    result=str(multiply_3(number))
    return Response(result, 200)


@app.post("/text/upper")
def upper() -> Response:
    data = request.get_json()
    text=data["text"]
    convert_to_upper = lambda text: text.upper()
    upper = convert_to_upper(text)
    return Response(upper, 200)

@app.post("/shapes/volume")
def shapes_volume() -> Response:
    data = request.get_json()
    height=data["height"]
    length=data["length"]
    width=data["width"]
    volume = lambda a, b, c: a * b * c
    result = volume(height, length, width)
    return Response(str(result), 200)


@app.get("/public/users/<criteria>")
def get_users(criteria: str) -> Union[List[dict], Response]:
    # List of users as tuples (name, age)
    users = [{"name": "Anna", "age": 28}, {"name": "Ben", "age": 35}, {"name": "Charlie", "age": 22},
             {"name": "Diana", "age": 30}]

    if criteria == "n":  # Sort by name
        sorted_users = sorted(users, key=lambda user: user["name"])
        return {"users": sorted_users}
    elif criteria == "a":  # Sort by age
        sorted_users = sorted(users, key=lambda user: user["age"])
        return {"users": sorted_users}
    else:
        return Response("Invalid criteria. Use 'n' for name or 'a' for age.", status=400)

@app.post("/helper/square")
def square_nums() -> Response:
    data = request.get_json()
    return square(data["numbers"])

@app.post("/helper/eliminate_odd")
def eliminate_odd_nums() -> Response:
    data = request.get_json()
    return eliminate_odd(data["numbers"])

@app.post("/helper/sum")
def sum_nums() -> str:
    data = request.get_json()
    return str(sum(data["numbers"]))

@app.post("/helper/all")
def all_nums() -> str:
    data = request.get_json()
    return all_of_them(data["numbers"])

app.run()


#B2F
