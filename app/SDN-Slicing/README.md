# SDN-Slicing-in-ComNetsEmu

```text
h1 ----  
h2 ----             |  |          |  |         ---- h5
      |  |--10Mbps-- s2 --10Mbps-- s3 ------|  |
      |  |          |  |          |  |      |  |
      |  |            |                     |  |
       s1             |--------10Mbps------  s4
      |  |                                  |  |
      |  |				    |  |
      |  |----------1Mbps-------------------|  |
h3 ----  		  	               ---- h6
h4 ----                                        ---- h7
```
./build_docker_images.sh

ryu manager controller.py &

sudo docker Slice_Topo.py



Jacopo Barcellesi, Nicola Fiorello, Gianlorenzo Moser