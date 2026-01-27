from rest_framework_simplejwt.authentication import JWTAuthentication

class CookiesJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        # Try cookie first (works in Chrome)
        access_token = request.COOKIES.get('access_token')

        # Fallback to Authorization header (for Safari ITP)
        if not access_token:
            auth_header = request.headers.get('Authorization', '')
            if auth_header.startswith('Bearer '):
                access_token = auth_header[7:]

        if not access_token:
            return None

        validated_token = self.get_validated_token(access_token)

        try:
            user = self.get_user(validated_token)
        except:
            return None
        return (user, validated_token)