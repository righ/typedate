# coding: utf-8
from datetime import datetime, timedelta
from unittest import TestCase

from dateutil.relativedelta import relativedelta
import pytz


class TestTypeDate(TestCase):
    def _makeOne(self, *args, **kwargs):
        from typedate import TypeDate
        return TypeDate(*args, **kwargs)

    def test_fmt(self):
        typedate = self._makeOne('%Y')
        self.assertEqual(typedate('2016'), datetime(2016, 1, 1))

    def test_default_fmt(self):
        typedate = self._makeOne()
        self.assertEqual(typedate('2016/05/05'), datetime(2016, 5, 5))

    def test_timedelta_object(self):
        typedate = self._makeOne(timedelta=timedelta(days=-1, hours=2))
        self.assertEqual(typedate('2016-05-05'), datetime(2016, 5, 4, 2))

    def test_timedelta_string(self):
        typedate = self._makeOne(timedelta='-1days 2hours')
        self.assertEqual(typedate('2016-05-05'), datetime(2016, 5, 4, 2))

    def test_timezone_object(self):
        typedate = self._makeOne(timezone=pytz.timezone('Asia/Tokyo'))
        self.assertEqual(
            typedate('2016-05-05'),
            datetime(2016, 5, 5, tzinfo=pytz.timezone('Asia/Tokyo')))

    def test_timezone_string(self):
        typedate = self._makeOne(timezone='Asia/Tokyo')
        self.assertEqual(
            typedate('2016-05-05'),
            datetime(2016, 5, 5, tzinfo=pytz.timezone('Asia/Tokyo')))

    def test_callback(self):
        typedate = self._makeOne(callback=lambda dt: dt.strftime('%Y=%m=%d'))
        self.assertEqual(typedate('2016-05-05'), '2016=05=05')


class TestTypeZone(TestCase):
    def _makeOne(self, *args, **kwargs):
        from typedate import TypeZone
        return TypeZone(*args, **kwargs)

    def test_locale(self):
        typezone = self._makeOne()
        self.assertEqual(typezone('Asia/Tokyo'), pytz.timezone('Asia/Tokyo'))

    def test_timediff(self):
        typezone = self._makeOne()
        self.assertEqual(typezone('+09:00').utcoffset(), timedelta(hours=9))
    
    def test_callback(self):
        typezone = self._makeOne(callback=lambda tz: datetime(2018, 7, 14, tzinfo=tz))
        assert typezone('UTC') == datetime(2018, 7, 14, tzinfo=pytz.UTC)


class TestTypeDelta(TestCase):
    def _makeOne(self, *args, **kwargs):
        from typedate import TypeDelta
        return TypeDelta(*args, **kwargs)

    def test_relativedelta(self):
        typedelta = self._makeOne(cls=relativedelta)
        self.assertEqual(
            typedelta('1years 2months -3days'),
            relativedelta(years=1, months=2, days=-3))

    def test_timedelta(self):
        typedelta = self._makeOne(cls=timedelta)
        self.assertEqual(
            typedelta('1days 2hours -3minutes'),
            timedelta(days=1, hours=2, minutes=-3))

    def test_timedelta_raising(self):
        typedelta = self._makeOne(cls=timedelta)
        with self.assertRaises(TypeError):
            typedelta('1years 2months -3days')
        
    def test_callback(self):
        typedelta = self._makeOne(callback=lambda delta: datetime(2018, 1, 1) + delta)
        assert typedelta('3days 2hours') == datetime(2018, 1, 4, 2)