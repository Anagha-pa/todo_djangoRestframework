from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import get_tokens_for_user
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from .emails import *

# Create your views here.

class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        try:
            data = request.data
            serializer = RegisterSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                send_otp_via_email(data['email'])
                return Response(
                    {  
                        'status':200,
                        'message': f'An OTP is send to {request.data["email"]} Successfully',
                        'data':serializer.data,
                    }           
                )
            return Response(
                {
                    'status':400,
                    'message':'User with this email is already exists',
                    'error':serializer.errors
                }
            )
        
        except Exception as e:
            return Response(
                {
                    'status':500,
                    'message':'Something wnt wrong',
                    'error':str(e)
                }
            )



class VerifyOTPView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        try:
            data = request.data
            serializer = VerifyOTPSerializer(data=data)
            serializer.is_valid(raise_exception=True)  
            email = serializer.validated_data['email']
            otp = serializer.validated_data['otp']

            user = UserData.objects.filter(email=email,otp=otp).first()
            if user:
                if user.otp == otp:
                    user.is_staff = True
                    user.save()
                    return Response(
                        {
                            'status':400,
                            'message':'OTP verified , Registration Successfull'
                        }
                    )
                
                return Response(
                    {
                        'status':400,
                        'message':'Wrong OTP'
                    }
                )
            
            return Response(
                {
                    'status':500,
                    'message':'User not found'
                }
            )
        
        except Exception as e:
            return Response(
                {
                    'status':500,
                    'message':'Something went wrong',
                    'error':str(e)
                }
            )


class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):       
        data = request.data
        serializer = LoginSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token = get_tokens_for_user(user)
        return Response(
            {
                'status':200,
                'msg' : 'Login Success',
                'token' : token
            }
        )
            

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        try:
           
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                {
                    'status':200,
                    'message':'Logout successful'
                }
            )
        except Exception as e:
            return Response(
                {
                    'status':500,
                    'error':str(e)
                }
            )





                






