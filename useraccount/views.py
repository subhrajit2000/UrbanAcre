from django.contrib.auth import get_user_model
User = get_user_model()
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

class SignupView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = request.data

        name = data['name']
        email = data['email']
        phone_number = data['phone_number']
        password = data['password']
        password2 = data['password2']

        # Validate password complexity 
        if not any(char.isupper() for char in password):
            return Response({'error': 'Password must contain at least one uppercase letter'})
        if not any(char.islower() for char in password):
            return Response({'error': 'Password must contain at least one lowercase letter'})
        if not any(char.isdigit() for char in password):
            return Response({'error': 'Password must contain at least one digit'})
        if len(password) < 8:
            return Response({'error': 'Password must be at least 8 characters long'})

        if password != password2:
            return Response({'error': 'Passwords do not match'})

        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email already exists'})
        elif User.objects.filter(phone_number=phone_number).exists():
            return Response({'error': 'Phone number already exists'})

        try:
            user = User.objects.create_user(email=email, password=password, name=name, phone_number=phone_number)
            user.save()
            return Response({'success': 'User created successfully'})
        except ValidationError as e:
            return Response({'error': str(e)})  # Improve error handling by providing specific messages
