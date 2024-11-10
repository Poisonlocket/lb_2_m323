from flask import Flask, Response, request

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
app.run()

#B2F
