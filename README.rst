.. image:: https://circleci.com/gh/righ/typedate.svg?style=svg
    :target: https://circleci.com/gh/righ/typedate

Requirements
============

- Python 2.7
- Python 3.3 or later

- Tested with 2.7, 3.7

Installation
============

.. code-block:: sh

  $ pip install typedate

Types
=====
This library provides 3 classes parsing string, and outputting object related to time.

:TypeDate: Date (and time) parser parses string. Time format, timezone and timedelta are specified when it is made.
:TypeDelta: Delta parser parses numbers with time units separeted a space. It will be interpreted as delta function arguments.
:TypeZone: Timezone parser parses timezone string. 

Usage
=====
For example, use the classes with `argparse` as follows:

.. code-block:: python

  #!/usr/bin/env python
  from typedate import TypeDate, TypeDelta, TypeZone
  
  if __name__ == '__main__':
      import argparse
      parser = argparse.ArgumentParser()

      # datetime parsing
      parser.add_argument("--datetime1", type=TypeDate('%Y%m%d'))
      parser.add_argument("--datetime2", type=TypeDate(timezone='Asia/Tokyo'))
      parser.add_argument("--datetime3", type=TypeDate(timezone='+09:00'))
      parser.add_argument("--datetime4", type=TypeDate(timedelta='1years -2months 3days 4hours 5minute 6seconds'))

      # timezone parsing
      parser.add_argument("--timezone1", type=TypeZone())
      parser.add_argument("--timezone2", type=TypeZone())

      # timedelta parsing
      ## if python-dateutil installed, used automatically dateutil.relativedelta.relativedelta else datetime.timedelta.
      parser.add_argument("--defaultdelta", type=TypeDelta())

      ## it can be specified by cls argument.
      from datetime import timedelta
      from dateutil.relativedelta import relativedelta
      parser.add_argument("--timedelta", type=TypeDelta(cls=timedelta))
      parser.add_argument("--relativedelta", type=TypeDelta(cls=relativedelta))

      args = parser.parse_args()
      print('datetime1:\t', args.datetime1, type(args.datetime1))
      print('datetime2:\t', args.datetime2, type(args.datetime2))
      print('datetime3:\t', args.datetime3, type(args.datetime3))
      print('datetime4:\t', args.datetime4, type(args.datetime4))

      print('timezone1:\t', args.timezone1, type(args.timezone1))
      print('timezone2:\t', args.timezone2, type(args.timezone2))

      print('defaultdelta:\t', args.defaultdelta, type(args.defaultdelta))
      print('timedelta:\t', args.timedelta, type(args.timedelta))
      print('relativedelta:\t', args.relativedelta, type(args.relativedelta))

Saving a file like above as `command.py`, and execute it as follows.

.. code-block:: sh

  $ python command.py \
    --datetime1='19880522' \
    --datetime2='2016-01-01' \
    --datetime3='2016/01/01' \
    --datetime4='01/01 00:00 2016' \
    --timezone1='-0500' \
    --timezone2='Asia/Tokyo'  \
    --defaultdelta='1years -2months 3days 4hours 5minutes 6seconds' \
    --timedelta='3days 4hours 5minutes 6seconds' \
    --relativedelta='1years -2months 3days 4hours 5minutes 6seconds'

  datetime1:       1988-05-22 00:00:00 <class 'datetime.datetime'>
  datetime2:       2016-01-01 00:00:00+09:00 <class 'datetime.datetime'>
  datetime3:       2016-01-01 00:00:00+09:00 <class 'datetime.datetime'>
  datetime4:       2016-11-04 04:05:06 <class 'datetime.datetime'>
  timezone1:       -05:00 <class 'typedate.type.zone.TzInfo'>
  timezone2:       Asia/Tokyo <class 'pytz.tzfile.Asia/Tokyo'>
  defaultdelta:    relativedelta(years=+1, months=-2, days=+3, hours=+4, minutes=+5, seconds=+6) <class 'dateutil.relativedelta.relativedelta'>
  timedelta:       3 days, 4:05:06 <class 'datetime.timedelta'>
  relativedelta:   relativedelta(years=+1, months=-2, days=+3, hours=+4, minutes=+5, seconds=+6) <class 'dateutil.relativedelta.relativedelta'>

History
==========
1.0.X
-----
* first release

