#!/bin/bash


## Find the interface used by ONOS
iflink=`docker exec -it onos bash -c 'cat /sys/class/net/eth0/iflink'`
iflink=`echo $iflink|tr -d '\r'`
veth=`grep -l $iflink /sys/class/net/veth*/ifindex`
veth=`echo $veth|sed -e 's;^.*net/\(.*\)/ifindex$;\1;'`


export interfaceONOS=$veth


tshark -i ${interfaceONOS} -w trafic.pcap