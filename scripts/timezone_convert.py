#!/usr/bin/python
#Author : Vignesh Ragupathy - me@vikki.in
from datetime import datetime
from pytz import timezone
import sys

def default():
    Madrid_Zone = timezone('Europe/Madrid')
    Madrid_time = datetime.now(Madrid_Zone)
    India_time = datetime.now()
    print "Current time in India is", India_time.strftime('%Y-%m-%d_%H:%M:%S')
    print "Current time in Madrid is", Madrid_time.strftime('%Y-%m-%d_%H:%M:%S')
    sys.exit(0)

def validate(date_text):
    import datetime
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        print "Incorrect date time format, should be YYYY-MM-DD HH:MM:SS"
        sys.exit(0)
            
def convert_timezone(time_to_convert,country):
    from dateutil import tz
    
    if country in ['Madrid']:
        from_zone = tz.gettz('GMT+5:30')
        to_zone = tz.gettz('Europe/Madrid')
    else:
        from_zone = tz.gettz('GMT+1')
        to_zone = tz.gettz('GMT+5:30')        
    validate(time_to_convert)
    utc = datetime.strptime(time_to_convert, '%Y-%m-%d %H:%M:%S')
    utc = utc.replace(tzinfo=from_zone)
    central = utc.astimezone(to_zone)
    print "Time in %s is %s" %(country,central)
    sys.exit(0)

def indian():
    time_to_convert = raw_input("Enter the Indian time to convert(%Y-%m-%d %H:%M:%S):")
    country = "Madrid"
    convert_timezone(time_to_convert,country)
    sys.exit(0)
def madrid():
    time_to_convert = raw_input("Enter the Madrid time to convert(%Y-%m-%d %H:%M:%S):")
    country = "India"
    convert_timezone(time_to_convert,country)
    sys.exit(0)

def extended():
    User_input = raw_input("Do you want to check any specfic time in Madrid/India zone instead of current time(y/n) ?")
    if User_input in ['y', 'Y']:
        User_input1 = raw_input("To Convert Indian to Madrid time enter I /To convert Madrid to Indian enter M (I/M)?")
        if User_input1 in ['-i', '-I', 'i', 'I']:
            indian()
        elif User_input1 in ['-m', '-M', 'm', 'M']:
            madrid()
        else:
	    print "Invalid county"	
            sys.exit(0)
    else:
        sys.exit(0) 

arg_len = len(sys.argv)
if arg_len == 2:
    Argument_1 = sys.argv[1]
    if Argument_1 in ['-e', '-E', 'e', 'E']:
        extended()
    elif Argument_1 in ['-i', '-I', 'i', 'I']:
        indian()
    elif Argument_1 in ['-m', '-M', 'm', 'M']:
        madrid()
    else:
        import optparse
        parser = optparse.OptionParser()
        parser.add_option('-i', help='Convert Indian time to Madrid time')
        parser.add_option('-m', help='Convert Madrid time to Indian time')
        (opts, args) = parser.parse_args()
        sys.exit(0)
else:
    default()
    sys.exit(0)
