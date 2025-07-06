from django.utils.deprecation import MiddlewareMixin

class LogClientIPMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR', 'GUEST_IP')
        user_agent = request.META.get('HTTP_USER_AGENT', 'GUEST_AGENT')
        print(f"[客户端 {user_agent}] {ip} 请求了 {request.path}")
