import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_TopologyUuid_NodeNode_Uuid_TransfercostCostcharacteristicCostalgorithmImpl:

    @classmethod
    def get(cls, uuid, node_uuid, costAlgorithm):
        print 'handling get'
        if uuid in Context._topology:
            if node_uuid in Context._topology[uuid]._node:
                if costAlgorithm in Context._topology[uuid]._node[node_uuid]._transferCost.costCharacteristic:
                    return Context._topology[uuid]._node[node_uuid]._transferCost.costCharacteristic[costAlgorithm]
                else:
                    raise KeyError('costAlgorithm')
            else:
                raise KeyError('node_uuid')
        else:
            raise KeyError('uuid')
