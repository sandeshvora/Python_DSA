from collections import deque
q=deque()

class EventRequest():
    def __init__(self,EventType=None,RetryCount=None):
        self.EventType = EventType
        self.RetryCount = RetryCount

class EventStatus():
    def __init__(self,EventType=None, StatusType=None, RetryCount=None):
        self.EventType = EventType
        self.StatusType = StatusType
        self.RetryCount = RetryCount

q.append(EventStatus('S','P',0))
q.append(EventRequest('R',0))
q.append(EventStatus('S','M',0))
q.append(EventStatus('S','P',0))
q.append(EventStatus('S','T',0))
q.append(EventStatus('S','P',0))
q.append(EventStatus('S','C',0))
q.append(EventStatus('S','M',0))

status=[]

while q:
    item = q.popleft()
    if item.EventType == 'S':
        status.append(item.StatusType)
        if (item.StatusType == 'C' or item.StatusType == 'T') and item.RetryCount < 2:
            item.RetryCount+=1
            q.append(item)
        else:
            print("Event Status",item.EventType, item.StatusType, item.RetryCount)

    if item.EventType == 'R':
        if status[-1]=='C' or status[-1]=='T':
            print("Event Request",item.EventType, item.RetryCount)
        else:
            item.RetryCount+=1
            q.append(item)
