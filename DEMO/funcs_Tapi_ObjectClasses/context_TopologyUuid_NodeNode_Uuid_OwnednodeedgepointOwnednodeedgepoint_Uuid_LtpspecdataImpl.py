import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LtpspecdataImpl:

    @classmethod
    def get(cls, uuid, node_uuid, ownedNodeEdgePoint_uuid):
        print 'handling get'
        if uuid in Context._topology:
            if node_uuid in Context._topology[uuid]._node:
                if ownedNodeEdgePoint_uuid in Context._topology[uuid]._node[node_uuid]._ownedNodeEdgePoint:
                    return Context._topology[uuid]._node[node_uuid]._ownedNodeEdgePoint[ownedNodeEdgePoint_uuid]._ltpSpecData
                else:
                    raise KeyError('ownedNodeEdgePoint_uuid')
            else:
                raise KeyError('node_uuid')
        else:
            raise KeyError('uuid')
