# 简介

## 操作系统：天融信自主知识产权的下一代安全操作系统—NGTOS

## 部署模式: 以在线方式部署于网络边界区域，用于检测和实时阻断从外网到内网的各种入侵行为。

## 部署位置：网络接口处，防火墙后端（前面？）清洗过滤网络流量

## 支持两路同时接入

# 部署模式

## 经典模式

![alt text](README_Images/README/image.png)

## 内网模式（独立式交换部署）

![alt text](README_Images/README/image-1.png)

# 缺省管理模式

## 缺省管理用户

## 系统管理员 （admin/talent）、 安全审计员（auditor/talent）、 安全保密员（grantor/talent）。

## 缺省接口配置

![alt text](README_Images/README/image-2.png)

## 缺省区域对象:area_feth0,绑定接口 feth0

## 默认服务

![alt text](README_Images/README/image-3.png)

# CLI 改变网卡/控制接口 IP

![alt text](README_Images/README/image-4.png)

# 接口分为物理接口和逻辑接口

## 物理接口的五种模式：路由模式、交换模式、监听模式、虚拟线模式和聚合模式

![alt text](README_Images/README/image-5.png)
