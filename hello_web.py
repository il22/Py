#Запуск скрипта python через mod_wsgi

#WSGI (англ. Web Server Gateway Interface) — стандарт взаимодействия между Python-программой, выполняющейся на стороне сервера, и самим веб-сервером, например, Apache.
#Стандарт интерфейса (на английском): http://www.python.org/dev/peps/pep-0333/

#По стандарту, WSGI-приложение должно удовлетворять следующим требованиям:
#
#    должно быть вызываемым (callable) объектом (обычно это функция или метод);
#    принимать два параметра:
#        словарь переменных окружения (environ);
#        обработчик запроса (start_response);
#    вызывать обработчик запроса с кодом HTTP-ответа и HTTP-заголовками;
#    возвращать итерируемый объект с телом ответа;
#
#Пример простого wsgi-приложения:

def application(environ, start_response):
    status = '200 OK'
    output = b'Hello World!'
    response_headers = [('Content-type', 'text/plain'),
                                   ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]
