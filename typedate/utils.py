# coding: utf-8
from . import compat
from .type.delta import TypeDelta
from .type.zone import TypeZone


def parse_timezone(timezone):
    if not isinstance(timezone, compat.basestring):
        return timezone

    typezone = TypeZone()
    return typezone(timezone)


def parse_timedelta(timedelta):
    if not isinstance(timedelta, compat.basestring):
        return timedelta

    typedelta = TypeDelta(cls=compat.timedelta)
    return typedelta(timedelta)
