#!/usr/bin/python3

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import info, setLogLevel

B1=10
B2=1
DELAY="10ms"

class Topology(Topo):
    def __init__(self):
        Topo.__init__(self)

        setLogLevel("info")

        info("*** Add Switches\n")
        sconfig1 = {"dpid": "%016x" % 1}
        sconfig2 = {"dpid": "%016x" % 2}
        sconfig3 = {"dpid": "%016x" % 3}
        sconfig4 = {"dpid": "%016x" % 4}
        self.addSwitch("s1",**sconfig1)
        self.addSwitch("s2",**sconfig2)
        self.addSwitch("s3",**sconfig3)
        self.addSwitch("s4",**sconfig4)

        info("*** Add Hosts\n")
        host_config = dict(inNamespace=True)
        self.addHost("h1", **host_config, ip="192.0.0.1")
        self.addHost("h2", **host_config, ip="192.0.0.2")
        self.addHost("h3", **host_config, ip="192.128.0.3")
        self.addHost("h4", **host_config, ip="192.0.0.4")
        self.addHost("h5", **host_config, ip="192.0.0.5")
        self.addHost("h6", **host_config, ip="192.0.0.6")
        self.addHost("h7", **host_config, ip="192.0.0.7")

        info("*** Add Links\n")
        self.addLink("h1","s1", bw=B1)
        self.addLink("h2","s1", bw=B1)
        self.addLink("h3","s1", bw=B1)
        self.addLink("h4","s1", bw=B1)
        self.addLink("s1","s2", bw=B1)
        self.addLink("s2","s3", bw=B1, delay=DELAY)
        self.addLink("s3","s4", bw=B1, delay=DELAY)
        self.addLink("s2","s4", bw=B2)
        self.addLink("s1","s4", bw=B1)
        self.addLink("s4","h5", bw=B1)
        self.addLink("s4","h6", bw=B1)
        self.addLink("s4","h7", bw=B1)

topos = {"networkslicingtopo": (lambda: Topology())}

if __name__ == "__main__":
    topo = Topology()
    net = Mininet(
        topo=topo,
        switch=OVSKernelSwitch,
        build=False,
        autoSetMacs=True,
        autoStaticArp=True,
        link=TCLink,
    )
    
    info("*** Add controller\n")
    controller = RemoteController("c1", ip="127.0.0.1", port=6633)
    net.addController(controller)
    net.build()
    net.start()
    CLI(net)
    net.stop()


        