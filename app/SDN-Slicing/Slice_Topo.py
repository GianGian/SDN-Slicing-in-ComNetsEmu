#!/usr/bin/python3



from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink

B1=10
B2=1
DELAY="10ms"

class Topology(Topo):
    def __init__(self):
        Topo.init(self)

        #Create switches
        info("*** Add Switches\n)
        switch1=self.addSwitch("s1")
        switch2=self.addSwitch("s2")
        switch3=self.addSwitch("s3")
        switch4=self.addSwitch("s4")

        #Create Hosts
        info("*** Add Hosts\n)
        host1=self.addDockerhost("h1", dimage="dev_test", ip="192.0.0.1", docker_args={"hostname"="h1"},)
        host2=self.addDockerhost("h2", dimage="dev_test", ip="192.0.0.2", docker_args={"hostname"="h2"},)
        host3=self.addDockerhost("h3", dimage="dev_test", ip="192.0.0.3", docker_args={"hostname"="h3"},)
        host4=self.addDockerhost("h4", dimage="dev_test", ip="192.0.0.4", docker_args={"hostname"="h4"},)
        host5=self.addDockerhost("h5", dimage="dev_test", ip="192.0.0.5", docker_args={"hostname"="h5"},)
        host6=self.addDockerhost("h6", dimage="dev_test", ip="192.0.0.6", docker_args={"hostname"="h6"},)
        host7=self.addDockerhost("h7", dimage="dev_test", ip="192.0.0.7", docker_args={"hostname"="h7"},)

        #Creating Links
        info("*** Add Links\n)
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

        #Create Controller
        info("*** Add controller\n")
        net.addController("c0")

        