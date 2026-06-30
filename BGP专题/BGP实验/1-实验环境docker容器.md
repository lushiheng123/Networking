```sh
name: bgp-demo

topology:
  nodes:
    spine1:
      kind: linux
      image: frrouting/frr:latest
    leaf1:
      kind: linux
      image: frrouting/frr:latest
    leaf2:
      kind: linux
      image: frrouting/frr:latest

  links:
    - endpoints: ["spine1:eth1", "leaf1:eth1"]
    - endpoints: ["spine1:eth2", "leaf2:eth1"]

mgmt:
  network: bgp-mgmt
  ipv4-subnet: 172.30.20.0/24
  ipv6-subnet: 3fff:172:30:20::/64

```
# 运行指令
```sh
clab deploy -t bgp-demo.yaml
```

# 如何停止实验
```sh
clab destroy -t bgp-demo.yaml
```