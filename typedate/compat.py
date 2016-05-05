# coding: utf-8
try:
    from dateutil.relativedelta import relativedelta as timedelta
except ImportError:
    from datetime import timedelta

try:
    from dateutil.parser import parse as default_parse
except ImportError:
    from datetime import datetime

    def default_parse(timestr):
        return datetime.strptime(timestr, '%Y-%m-%d')

try:
    basestring = basestring
except NameError:
    basestring = str
