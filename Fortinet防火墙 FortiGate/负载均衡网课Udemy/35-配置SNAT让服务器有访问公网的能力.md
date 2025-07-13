# 现在先回顾下防火墙策略，是不能通公网 8.8.8.8

![alt text](README_Images/35-配置SNAT让服务器有访问公网的能力/image-1.png)

# 能访问公网的是 192.168.2.0/24 网段

![alt text](README_Images/35-配置SNAT让服务器有访问公网的能力/image-2.png)

# 真实的服务器是无法访问的

![alt text](README_Images/35-配置SNAT让服务器有访问公网的能力/image.png)

# 在 egress port 也就是出口流量，配置 SNAT 转换

![alt text](README_Images/35-配置SNAT让服务器有访问公网的能力/image-4.png)

# 发现通了

![alt text](README_Images/35-配置SNAT让服务器有访问公网的能力/image-5.png)
