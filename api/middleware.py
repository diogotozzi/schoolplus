import json

from django.http import HttpResponseBadRequest


class JSONParsingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'POST' and request.content_type == "application/json":
            try:
                request.POST = json.loads(request.body)
            except ValueError as ve:
                return HttpResponseBadRequest('unable to parse JSON data. Error : {0}'.format(ve))

        if request.method == 'PUT' and request.content_type == "application/json":
            try:
                request.PUT = json.loads(request.body)
            except ValueError as ve:
                return HttpResponseBadRequest('unable to parse JSON data. Error : {0}'.format(ve))

        if request.method == 'PATCH' and request.content_type == "application/json":
            try:
                request.PATCH = json.loads(request.body)
            except ValueError as ve:
                return HttpResponseBadRequest('unable to parse JSON data. Error : {0}'.format(ve))

        response = self.get_response(request)

        return response
