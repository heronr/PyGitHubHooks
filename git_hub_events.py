from enum import Enum

class EventTypes(Enum):
    push = 1
    ping = 2

def GetEventType(event_str):
    for event in EventTypes:
        if event.name == event_str:
            return event
    return None

def HandlePushEvent(push_event):
    print(push_event)
    return True

def HandlePingEvent(ping_event):
    print(ping_event)
    return True