![拓扑](README_Images/README/image.png)

# cisco ASA: show mode 显示默认是单模式

![alt text](README_Images/README/image-1.png)

# cisco ASA: mode multiple 切换模式，确认后会重启

![alt text](README_Images/README/image-2.png)
![alt text](README_Images/README/image-3.png)

# ASA: show context 看，当下有一个默认的 context

![alt text](README_Images/README/image-4.png)

# ASA: context context1,config-url disk0:/context1.cfg

![alt text](README_Images/README/image-5.png)

# 加上 allocate interface eth0 后，看加上的端口情况

![alt text](README_Images/README/image-7.png)

# 创建 context2

![alt text](README_Images/README/image-8.png)
![alt text](README_Images/README/image-9.png)

# 创建好后，changeto context context1

![alt text](README_Images/README/image-10.png)

## 配下 inside

![alt text](README_Images/README/image-11.png)

# changeto context context2 切换到 context2

![alt text](README_Images/README/image-13.png)

# 检查一下 mac 地址，发现 mac 地址一样

![alt text](README_Images/README/image-14.png)
![alt text](README_Images/README/image-15.png)

# changeto system

![alt text](README_Images/README/image-16.png)

# 改了 mac 地址前缀后，发现 mac 地址自动不一样了

![alt text](README_Images/README/image-17.png)

# 改 eth1 在不同 context 的地址

![alt text](README_Images/README/image-19.png)

# 最后在 system 视图看下配置

![alt text](README_Images/README/image-20.png)
![alt text](README_Images/README/image-21.png)
![alt text](README_Images/README/image-22.png)

# 给两台 pc 配 ip

![alt text](README_Images/README/image-23.png)

# 给路由器配 ip

![alt text](README_Images/README/image-24.png)
![alt text](README_Images/README/image-25.png)

# asa 的 context2 中看 route

![alt text](README_Images/README/image-26.png)

# 在 R1 上写 route

![alt text](README_Images/README/image-27.png)
