from config.settings import dev


class ResponseTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.warning = 'WARNING, DEBUG MODE ON'

    def __call__(self, request):
        response = self.get_response(request)

        return response

    def process_template_response(self, request, response):
        if dev.DEBUG:
            response.context_data['warning'] = self.warning

        return response
