from flask import Flask, Response, request
from math import pow

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


@app.post("/calc/func")
def calc_func() -> Response:
    data = request.get_json()
    num_to_square = data["number"]
    result = num_to_square ** 2
    return Response(result, 200)

@app.post("/calc/oop")
def calc_oop() -> Response:
    data = request.get_json()
    num_to_square = data["number"]
    num_to_square.pow(2)
    return Response(num_to_square, 200)




app.run()

