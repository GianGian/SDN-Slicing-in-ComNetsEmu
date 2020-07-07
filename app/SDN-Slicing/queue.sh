sudo ovs-vsctl set port s1-eth4 qos=@newqos -- --id=@newqos create QoS type=linux-htb other-config:max-rate=100000 queues:123=@1q queues:234=@2q -- --id=@1q create queue other-config:min-rate=100000 other-config:max-rate=700000 -- --id=@2q create queue other-config:min-rate=100000 other-config:max-rate=700000
#sudo ovs-vsctl set port s2-eth1 qos=@newqos -- --id=@newqos create QoS type=linux-htb other-config:max-rate=100000 queues:123=@1q queues:234=@2q -- --id=@1q create queue other-config:min-rate=100000 other-config:max-rate=700000 -- --id=@2q create queue other-config:min-rate=100000 other-config:max-rate=700000
#sudo ovs-vsctl set port s2-eth3 qos=@newqos -- --id=@newqos create QoS type=linux-htb other-config:max-rate=100000 queues:123=@1q queues:234=@2q -- --id=@1q create queue other-config:min-rate=100000 other-config:max-rate=700000 -- --id=@2q create queue other-config:min-rate=100000 other-config:max-rate=700000
#sudo ovs-vsctl set port s4-eth2 qos=@newqos -- --id=@newqos create QoS type=linux-htb other-config:max-rate=100000 queues:123=@1q queues:234=@2q -- --id=@1q create queue other-config:min-rate=100000 other-config:max-rate=700000 -- --id=@2q create queue other-config:min-rate=100000 other-config:max-rate=700000
sudo ovs-ofctl add-flow s1 ip,priority=65500,nw_src=192.0.0.2,nw_dst=192.0.0.7,idle_timeout=0,action=set_queue:123,normal
sudo ovs-ofctl add-flow s1 ip,priority=65500,nw_src=192.0.0.3,nw_dst=192.0.0.8,idle_timeout=0,action=set_queue:234,normal
#sudo ovs-ofctl add-flow s2 ip,priority=65500,nw_src=192.0.0.7,nw_dst=192.0.0.2,idle_timeout=0,action=set_queue:123,normal
#sudo ovs-ofctl add-flow s2 ip,priority=65500,nw_src=192.0.0.8,nw_dst=192.0.0.3,idle_timeout=0,action=set_queue:234,normal
#sudo ovs-ofctl add-flow s2 ip,priority=65500,nw_src=192.0.0.2,nw_dst=192.0.0.7,idle_timeout=0,action=set_queue:123,normal
#sudo ovs-ofctl add-flow s2 ip,priority=65500,nw_src=192.0.0.3,nw_dst=192.0.0.8,idle_timeout=0,action=set_queue:234,normal
#sudo ovs-ofctl add-flow s4 ip,priority=65500,nw_src=192.0.0.7,nw_dst=192.0.0.2,idle_timeout=0,action=set_queue:123,normal
#sudo ovs-ofctl add-flow s4 ip,priority=65500,nw_src=192.0.0.8,nw_dst=192.0.0.3,idle_timeout=0,action=set_queue:234,normal