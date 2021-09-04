from django.http import HttpResponse
from django.db import connection
from rest_framework.views import APIView
from rest_framework.response import Response

def index(request):
    return HttpResponse("hello world!")

class Activity(APIView):
    def post(self, request):

        print(request.data)

        from_date = request.data['from_date']
        to_date = request.data['to_date']
        status= request.data['status']
        activity= request.data['activity']

        with connection.cursor() as cursor:
            cursor.execute( '''  select user_id id,  al.activity_type activity, u.status status, u.display_name name, al.date_time date_time \
                                 from user u inner join activity_logs al on u.user_id=al.id  \
                                 where (al.date_time > %s and al.date_time < %s and u.status = %s and al.activity_type = %s) ''',(from_date, to_date, status, activity))
            #print(cursor.fetchall())
            rows = [x for x in cursor]
            cols = [x[0] for x in cursor.description]
            res= [ dict(zip(cols, row)) for row in cursor.fetchall() ]
            print(res)
            return Response({'result': res})
