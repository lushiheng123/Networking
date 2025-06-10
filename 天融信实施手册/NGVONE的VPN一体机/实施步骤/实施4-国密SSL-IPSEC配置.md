![alt text](README_Images/实施4-国密SSL-IPSEC配置/image-18.png)

# SSL 网关配置，DHCP 网段尽量写 16 位的

![alt text](README_Images/实施4-国密SSL-IPSEC配置/image.png)

# 常规设置-IPSEC 加密协议选择国密

![alt text](README_Images/实施4-国密SSL-IPSEC配置/image-1.png)

# 加资源组/区域

![alt text](README_Images/实施4-国密SSL-IPSEC配置/image-2.png)
![alt text](README_Images/实施4-国密SSL-IPSEC配置/image-3.png)
![alt text](README_Images/实施4-国密SSL-IPSEC配置/image-4.png)

# 本机服务（可信主机）开启 ssl-vpn 服务

![alt text](README_Images/实施4-国密SSL-IPSEC配置/image-5.png)

# 对象地址子网添加---NAT44

# 国密证书认证

## 用户管理-本地用户，选中 default 组，绑定地址池

![alt text](README_Images/实施4-国密SSL-IPSEC配置/image-6.png)

## 用户管理-全局设置里，选择“证书认账”或者“口令活证书认证”

![alt text](README_Images/实施4-国密SSL-IPSEC配置/image-7.png)

## 用户管理-角色管理，添加“证书”角色

![alt text](README_Images/实施4-国密SSL-IPSEC配置/image-8.png)

## 用户管理-认证设置，服务器"cert"，配置授权策略为整体，类型为“角色”

![alt text](README_Images/实施4-国密SSL-IPSEC配置/image-9.png)
![alt text](README_Images/实施4-国密SSL-IPSEC配置/image-10.png)
![alt text](README_Images/实施4-国密SSL-IPSEC配置/image-11.png)

## 用户管理-认证设置，服务器"cert"，认证属性取消授权策略

![alt text](README_Images/实施4-国密SSL-IPSEC配置/image-12.png)

## 用户管理-证书管理-第三方 CA 证书

![alt text](README_Images/实施4-国密SSL-IPSEC配置/image-13.png)

## key 驱动添加

![alt text](README_Images/实施4-国密SSL-IPSEC配置/image-14.png)

## 客户端 PC 配置，插入 ukey 就可读取证书

![alt text](README_Images/实施4-国密SSL-IPSEC配置/image-15.png)

## 用 NG 客户端，选择证书登录

![alt text](README_Images/实施4-国密SSL-IPSEC配置/image-16.png)
![alt text](README_Images/实施4-国密SSL-IPSEC配置/image-17.png)
