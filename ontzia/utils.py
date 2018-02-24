from datetime import datetime

from icalendar import Calendar
from icalendar.prop import vDate, vDatetime, vDDDTypes, vText, vUri
from pytz import timezone, utc
from pytz.exceptions import UnknownTimeZoneError


def get_events_from_ics(filepath):
    """
    Extract text, URL, date and datetime properties of all events from an ics file

    Date and datetime properties are converted to timezone-aware datetime objects.
    If missing, timezone defaults to UTC.

    :param filepath: filepath of the ics
    :return: dictionary
    """
    with open(filepath, 'rb') as f:
        cal = Calendar.from_ical(f.read())

    events = []

    for raw_event in cal.walk('VEVENT'):
        event = {}

        for prop, value in raw_event.items():
            if type(value) in (vText, vUri):
                event[prop] = str(value)
            elif type(value) in (vDate, vDatetime, vDDDTypes):
                dt = datetime(*(value.dt.timetuple()[:6]))  # assure naive datetime object
                tzid = value.params.get('TZID', 'UTC')

                try:
                    tz = timezone(tzid)
                except UnknownTimeZoneError:
                    if tzid == 'UTC+1':
                        tz = timezone('CET')
                    else:
                        tz = utc

                event[prop] = tz.localize(dt, is_dst=None)

        if event:
            events.append(event)

    return events
