import time
import re
import sys

class Tools(object):
    def get_current_time(format_= "[%Y-%m-%d %H:%M:%S]"):
        return time.strftime(format_,time.localtime(time.time()))

    def log(msg=None):
        print(Tools.get_current_time(),msg)

    def wash_off_html_tag(str=None):
        if str is None:
            return str
        return re.sub(re.compile(r'<\w+>|</\w+>|<\w+/>|&quot'),'',str)

    def set_up_long_mode(use_file =False, file_name = 'record.log'):
        if use_file :
            sys.stdout = open(file_name,"w")


