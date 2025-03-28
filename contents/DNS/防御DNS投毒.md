![alt text](README_Images/防御DNS投毒/image-1.png)
![alt text](README_Images/防御DNS投毒/image-2.png)

# 实验

![alt text](README_Images/防御DNS投毒/image.png)

### R1

```sh
configure terminal
ip dns server
ip domain-lookup
ip name-server 8.8.8.8
ip domain name test.local
ip host pc1.test.local 192.168.1.2
ip host fsrv.test.local 192.168.1.3
ip host R1.test.local 192.168.1.1
end
```

![alt text](README_Images/防御DNS投毒/image-3.png)

### R2

```sh
configure terminal
interface FastEthernet0/0
ip address 192.168.1.2 255.255.255.0
no shutdown
ip domain lookup
ip name-server 192.168.1.1
ip domain name test.local
end
```

![alt text](README_Images/防御DNS投毒/image-4.png)
