from enum import Enum
import subprocess

class EventTypes(Enum):
    push = 1
    ping = 2

def GetEventType(event_str):
    for event in EventTypes:
        if event.name == event_str:
            return event
    return None

def HandlePushEvent(push_event):
    print('Push event is: {}'.format(push_event))
    # set up some important variables for the operations to come


    output = subprocess.check_output(['git', 'rev-parse', '--is-inside-working-tree'])
    if output in ['true', 'false']:
        if (output == 'false'):
            #need to get to the working tree somehow
            print('was false')
        #if output is true then we don't need to do anything
    else:
        #do some cloning or something
        print('clone?')



    return True

def HandlePingEvent(ping_event):
    print('Ping event is: {}'.format(ping_event))
    return True