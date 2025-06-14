from django.utils.deprecation import MiddlewareMixin

class LogClientIPMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        print(f"[客户端 IP] {ip} 请求了 {request.path}")
