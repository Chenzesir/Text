from werkzeug.wrappers import Request,Response
from werkzeug.serving import run_simple
@Request.application
def hello(request):
    return Response("Hello World1")

if __name__ == '__main__':
    #请求一旦到来，执行第3个参数，hello(上下文)
    run_simple('localhost', 4000, hello)