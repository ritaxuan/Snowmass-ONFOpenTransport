import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_NotificationNotificationidImpl:

    @classmethod
    def get(cls, notificationId):
        print 'handling get'
        if notificationId in Context._notification:
            return Context._notification[notificationId]
        else:
            raise KeyError('notificationId')
