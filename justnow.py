def convert_into_minutes(in_put):
    time=(in_put//60) 
    if time>1: 
        print("{} minutes ago".format(time))
    elif time==1:
        print("1 minute ago")
        
def convert_into_hours(in_put):
    time=(in_put//3600)
    if time>1:
        print("{} hours ago".format(time))
    elif time==1:
        print("1 hour ago")

def convert_into_days(in_put):
    time =(in_put//86400)
    if time>1:
        print("{} days ago".format(time))
    elif time==1:
        print("1 day ago")

def convert_into_weeks(in_put):
    time=(in_put//604800)
    if time>1:
        print("{} weeks ago".format(time))
    elif time==1:
        print("1 week ago")

def convert_into_months(in_put):
    time=(in_put//2678400)
    if time>1:
        print("{} months ago".format(time))
    elif time==1:
        print("1 month ago")
def convert_into_years(in_put):
    time=(in_put//31536000)
    if time>1:
        print("{} years ago".format(time))
    elif time==1:
        print("1 year ago")
    
import datetime
k=int(input())
for i in range(k):
    read_input1=input()
    read_input2=input()
    converted_time1=datetime.datetime.strptime(read_input1,"%a %d %b %Y %H:%M:%S %z")
    converted_time2=datetime.datetime.strptime(read_input2,"%a %d %b %Y %H:%M:%S %z")
    difference=abs(converted_time1-converted_time2)
    time_duration = int(difference.total_seconds())
    if time_duration<60:
        print("just now")
    elif  time_duration>=60 and time_duration<3600:
        convert_into_minutes(time_duration)
    elif time_duration>=3600 and time_duration<86400:
        convert_into_hours(time_duration)
    elif time_duration>=86400 and time_duration<604800:
        convert_into_days(time_duration)
    elif time_duration>=604800 and time_duration<2678400:
        convert_into_weeks(time_duration)
    elif time_duration>=2678400 and time_duration<31536000:
        convert_into_months(time_duration)
    elif time_duration>=31536000:
        convert_into_years(time_duration)
