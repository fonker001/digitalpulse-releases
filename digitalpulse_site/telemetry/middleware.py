from .models import Visit

class VisitTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        ip = self.get_ip(request)

        Visit.objects.create(
            ip_address=ip,
            user_agent=request.META.get('HTTP_USER_AGENT', ''),
            path=request.path
        )

        return response

    def get_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0]
        return request.META.get('REMOTE_ADDR')