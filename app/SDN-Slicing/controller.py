from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib.packet import ether_types
from ryu.lib.packet import udp
from ryu.lib.packet import tcp
from ryu.lib.packet import icmp


#settare porte con link

class TrafficSlicing(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(TrafficSlicing, self).__init__(*args, **kwargs)

        # outport = self.mac_to_port[dpid][mac_address]
        self.mac_to_port = {
            1: {"00:00:00:00:00:01": 1, "00:00:00:00:00:02": 2, "00:00:00:00:00:03": 3, "00:00:00:00:00:04": 4},
            4: {"00:00:00:00:00:05": 4, "00:00:00:00:00:06": 5, "00:00:00:00:00:06": 6},
        }
        self.slice_TCport = 9999

        # outport = self.slice_ports[dpid][slicenumber]
        self.slice_ports = {1: {1: 5, 2: 5, 3: 6}, 2: {1: 2, 2: 3},4: {1: 2, 2: 2, 3: 3}}
        self.end_swtiches = [1, 4]

#nuovo flusso da mandare a controller

#settare risposta a packet-in
#definire flussi in base alla porta