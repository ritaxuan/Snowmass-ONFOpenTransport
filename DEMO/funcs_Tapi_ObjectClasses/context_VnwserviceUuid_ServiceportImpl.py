import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_VnwserviceUuid_ServiceportImpl:

    @classmethod
    def get(cls, uuid):
        print 'handling get'
        if uuid in Context._vnwService:
            return Context._vnwService[uuid]._servicePort
        else:
            raise KeyError('uuid')
