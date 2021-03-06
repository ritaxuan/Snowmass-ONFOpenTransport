import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_PathcompserviceUuid_RoutingconstraintRiskcharacteristicRiskcharacteristicnameImpl:

    @classmethod
    def get(cls, uuid, riskCharacteristicName):
        print 'handling get'
        if uuid in Context._pathCompService:
            if riskCharacteristicName in Context._pathCompService[uuid]._routingConstraint.riskCharacteristic:
                return Context._pathCompService[uuid]._routingConstraint.riskCharacteristic[riskCharacteristicName]
            else:
                raise KeyError('riskCharacteristicName')
        else:
            raise KeyError('uuid')
