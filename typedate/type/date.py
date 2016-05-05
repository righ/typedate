# coding: utf-8
from datetime import datetime, timedelta

from ..compat import default_parse
from ..utils import parse_timezone, parse_timedelta


class TypeDate(object):
    def __init__(self, fmt=None, timezone=None, timedelta=timedelta()):
        self.fmt = fmt
        self.timezone = parse_timezone(timezone)
        self.timedelta = parse_timedelta(timedelta)

    def __call__(self, string):
        if self.fmt:
            date = datetime.strptime(string, self.fmt)
        else:
            date = default_parse(string)
        return date.replace(tzinfo=self.timezone) + self.timedelta
