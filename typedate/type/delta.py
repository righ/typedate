# coding: utf-8
import re
from functools import reduce

from .. import compat

NUMBER_DEFINITION = re.compile(r'[0-9+\-]+')


class TypeDelta(object):
    def __init__(self, cls=compat.timedelta, callback=None):
        self.cls = cls
        self.callback = callback

    def __call__(self, deltastr):
        value = reduce(self.cls.__add__, (self.parse(token) for token in deltastr.split()))
        return self.callback(value) if self.callback else value

    def parse(self, token):
        match = NUMBER_DEFINITION.search(token)
        return self.cls(**{
            token[match.end():] or 'days': int(match.group())
        })
