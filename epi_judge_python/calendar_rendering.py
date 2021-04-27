import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))

Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))


def find_max_simultaneous_events(A: List[Event]) -> int:
    endpoints = (
        [Endpoint(a.start, 1) for a in A] +
        [Endpoint(a.finish, 0) for a in A]
    )

    endpoints.sort(key=lambda e: (e.time, not e.is_start))

    sol, cur = 0, 0

    for e in endpoints:
        if e.is_start:
            cur += 1
            sol = max(sol, cur)
        else:
            cur -= 1

    return sol


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
