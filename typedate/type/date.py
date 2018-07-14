# coding: utf-8
from datetime import datetime, timedelta

from ..compat import default_parse
from ..utils import parse_timezone, parse_timedelta


class TypeDate(object):
    def __init__(self, fmt=None, timezone=None, timedelta=timedelta(), callback=None):
        self.fmt = fmt
        self.timezone = parse_timezone(timezone)
        self.timedelta = parse_timedelta(timedelta)
        self.callback = callback

    def __call__(self, datestr):
        if self.fmt:
            date = datetime.strptime(datestr, self.fmt)
        else:
            date = default_parse(datestr)
        date = date.replace(tzinfo=self.timezone) + self.timedelta
        return self.callback(date) if self.callback else date

