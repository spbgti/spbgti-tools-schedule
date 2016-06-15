from django.http import HttpResponse


class HttpResponseNoContent(HttpResponse):
    status_code = 204


class HttpResponseMethodNotAllowed(HttpResponse):
    status_code = 405


class HttpResponseMethodNotImplemented(HttpResponse):
    status_code = 501
