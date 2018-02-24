from datetime import date, datetime
from random import randint
from tempfile import NamedTemporaryFile

from icalendar import Calendar, Event
from pytz import timezone, utc

from ontzia.utils import get_events_from_ics


def test_get_events_from_ics():
    cal = Calendar()
    event1, event2 = Event(), Event()
    props1 = {
        'SUMMARY': 'summary1',
        'URL': 'https://example1.com',
        'DTSTART': date(randint(1900, 2000), randint(1, 12), randint(1, 28)),
        'DTEND': datetime(randint(1900, 2000), randint(1, 12), randint(1, 28), randint(0, 23), randint(0, 59)),
        'CREATED': datetime(randint(1900, 2000), randint(1, 12), randint(1, 28), randint(0, 23), randint(0, 59), tzinfo=timezone('CET')),
    }
    props2 = {
        'SUMMARY': 'summary2',
        'URL': 'https://example2.com',
        'DTSTART': date(randint(1900, 2000), randint(1, 12), randint(1, 28)),
        'DTEND': datetime(randint(1900, 2000), randint(1, 12), randint(1, 28), randint(0, 23), randint(0, 59)),
        'CREATED': datetime(randint(1900, 2000), randint(1, 12), randint(1, 28), randint(0, 23), randint(0, 59), tzinfo=timezone('CET')),
    }

    for props, event in zip((props1, props2), (event1, event2)):
        for prop, value in props.items():
            event.add(prop, value)

        cal.add_component(event)

    tf = NamedTemporaryFile(delete=False)

    with open(tf.name, 'wb') as f:
        f.write(cal.to_ical())

    for props in (props1, props2):
        for prop in props:
            if type(props[prop]) is date:
                props[prop] = datetime(props[prop].year, props[prop].month, props[prop].day, tzinfo=utc)
            elif type(props[prop]) is datetime and not props[prop].tzinfo:
                props[prop] = props[prop].replace(tzinfo=utc)

    events = get_events_from_ics(tf.name)
    assert props1 == events[0]
    assert props2 == events[1]
