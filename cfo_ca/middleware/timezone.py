# import pytz    
# from django.utils import timezone

# class TimezoneMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         timezone.activate(pytz.timezone('Asia/Kolkata'))
#         print("Timezone activated")
#         return self.get_response(request)