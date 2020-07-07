# SDN-Slicing-in-ComNetsEmu

```text
h1 ----  
h2 ----             |  |          |  |         ---- h6
      |  |---5Mbps-- s2 ---5Mbps-- s3 ------|  |
      |  |          |  |          |  |      |  |
      |  |            |                     |  |
       s1             |--------5Mbps-------  s4
      |  |                                  |  |
      |  |				    |  |
      |  |----------1Mbps-------------------|  |
  h3 --  		  	               ---- h7
 |  |                                          ---- h8
 |  |
 h4 h5
```

First at all run:
```text
./build_docker_images.sh
```

Then to start the RYU:
```text
ryu manager controller.py &
```

Finally to start the topology:
```text
sudo docker Slice_Topo.py
```

## The topology is as follows:
the three clients (h6, h7, h8) request their respective services from the servers (h1, h2, h3).
### First Slice
The h1 server simulates an autonomus driving service for which low latency and high throughput is required. For this the service is provided through a special slice server-h1-s1-s4-end user which guarantees 5Mbps and the lowest hop number. The service is identified based on the server IP.
### Second Slice
The second slice instead allows the transmission of services by the h2 server (video streeming). In this case the requirement is a high throughput. The service is therefore transmitted on the slice server-h2-s1-s2-s3-s4-end user which guarantees 5Mbps even if with a (simulated) delay of 20ms. In this specific case the request follows a different path (end-user-s4-s2-s1-server) from the previous one to leave the link more free and to use a connection without delay. The service is identified based on the type of UDP protocol.
### Third Slice
The third slide provides on the server side a brocker (h3) which has exclusive access to two Iot devices (h4, h5) from which it receives data. since IoT data generally do not require excessive bandwidth use, the server-s1-s2-s4-enduser path was chosen in order to have immediate data transmission at the expense of the band: in fact, the s2-s4 connection is limited to 1Mbps. The service is identified based on the type of TCP protocol.

Finally, the second slice is used for the ICMP protocol as it uses all the hops.

## How to test the topology:

Inside mininet
```text
pingall
```
The results will be a reachability of all servers and end users except for the IoT (h4, h5).
subsequently by deactivating one or more switches 

Inside mininet (where X is the number of the switch)
```text
switch sX stop
```
it is possible to verify that some services will remain reachable and others not.

### To test IoT service

Inside mininet (where X is the number of the host)
```text
xterm hX
```

on client side (h7):
```text
iperf -c 192.0.0.3
```
on server side (h3):
```text
iperf -s
```

### To test Streeming service

Inside mininet (where X is the number of the host)
```text
xterm hX
```

on client side (h6):
```text
iperf -c 192.0.0.2 -u -b 10M
```
on server side (h2):
```text
iperf -s -u -i 1
```

### To test Autonomous Driving service

Inside mininet (where X is the number of the host)
```text
xterm hX
```

on client side (h8):
```text
telnet 192.0.0.1 65000
```



Jacopo Barcellesi, Nicola Fiorello, Gianlorenzo Moser