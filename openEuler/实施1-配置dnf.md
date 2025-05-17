# dnf 的配置文件保存位置： /etc/dnf/dnf.conf

![alt text](README_Images/实施1-配置dnf/image.png)

# 需要配置 yum 源的话，在/etc/yum.repos.d/openEuler.repo

![alt text](README_Images/实施1-配置dnf/image-2.png)
![alt text](README_Images/实施1-配置dnf/image-1.png)

# （dnf install dnf-plugins-core）安装好了工具后 dnf config-manager --dump 显示当前配置信息

![alt text](README_Images/实施1-配置dnf/image-3.png)

# dnf repolist 显示相应软件源的配置

![alt text](README_Images/实施1-配置dnf/image-4.png)

# nmcli 网络控制工具

```sh
 dnf install -y NetworkManager
 dnf install -y iproute
```

![alt text](README_Images/dnf安装工具/image.png)

![alt text](README_Images/dnf安装工具/image-1.png)

# （可选）安装 ifconfig 命令（来自 net-tools 包）

![alt text](README_Images/dnf安装工具/image-2.png)
