# coding: utf-8
import re
from datetime import timedelta, tzinfo

TIMEZONE_DEFINITION = re.compile(r'([+\-]?)(\d\d):?(\d\d)')


class TzInfo(tzinfo):
    def __init__(self, match):
        td = timedelta(
            hours=int(match.group(2)), minutes=int(match.group(3)))
        self.timedelta = -td if match.group(1) == '-' else td
        self.name = '{}{}:{}'.format(*match.groups())

    def utcoffset(self, *args, **kwargs):
        return self.timedelta

    def dst(self, *args, **kwargs):
        return timedelta(0)

    def tzname(self, *args, **kwargs):
        return self.name

    __repr__ = tzname


class TypeZone(object):
    def __call__(self, zonestr):
        match = TIMEZONE_DEFINITION.search(zonestr)
        if match:
            return TzInfo(match)
        else:
            import pytz
            return pytz.timezone(zonestr)
