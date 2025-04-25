**NMAP probe** 和 **DHCP probe** 属于 **Cisco ISE（Identity Services Engine）中的探针技术（Probes）范畴**，用于设备识别与用户上下文感知（**Context Visibility**）的关键组成部分。

---

## 🎯 一句话理解：

> NMAP probe 和 DHCP probe 是 **Cisco ISE 的探针技术**，用于主动或被动地发现和识别网络中的终端设备类型、操作系统、用户身份等信息。

---

## 🔍 所属范畴：

它们属于：

> **Cisco ISE 的终端探针（Endpoint Probing）机制**  
> 是实现 **身份感知、安全策略控制（TrustSec）和上下文可视化** 的重要数据来源。

---

## 🔧 各探针作用解析：

| 探针类型       | 功能                       | 特点                                   |
| -------------- | -------------------------- | -------------------------------------- |
| **DHCP Probe** | 被动监听网络上的 DHCP 请求 | 可提取 MAC 地址、主机名、IP 等信息     |
| **NMAP Probe** | 主动扫描网络设备           | 可识别操作系统、开放端口、服务、类型等 |

---

## 🧠 用途和工作原理：

### 1. **DHCP Probe（被动）**

- ISE 监听 DHCP 数据包（特别是 Discover、Request）
- 识别设备的：
  - MAC 地址
  - IP 地址
  - 主机名
  - Vendor 信息（Option 55/60）
- **无需中断流量**，对网络透明

### 2. **NMAP Probe（主动）**

- Cisco ISE 主动使用 NMAP 工具扫描网络 IP 范围
- 识别终端设备的：
  - 操作系统
  - 开放端口
  - 服务类型
  - 设备类型（Printer, Camera, IoT, etc.）

---

## ✅ 应用场景：

- **BYOD 设备识别**
- **策略映射（不同设备/用户获取不同策略）**
- **设备分类（Profiling）**
- **安全事件调查（可视化端点行为）**

---

## 🚀 常见配套探针还包括：

| 探针                   | 描述                         |
| ---------------------- | ---------------------------- |
| SNMP Trap Probe        | 从交换机收集 MAC-IP 映射信息 |
| RADIUS Probe           | 从认证请求中提取身份信息     |
| HTTP Probe             | 解析 Web 请求头获取终端类型  |
| NetFlow Probe          | 提取流量行为特征             |
| DNS Probe              | 提取设备发起的 DNS 请求域名  |
| Active Directory Probe | 从 AD 提取用户登录信息       |

---

## ✅ 总结一句话：

> NMAP probe 和 DHCP probe 是 Cisco ISE 探针机制中的重要组成，前者主动探测设备属性，后者被动监听 DHCP 流量，用于设备识别、上下文建立和策略应用。

---

如果你要看一个完整的 ISE Profiling 流程图、实验配置方式，或想区分 probe 和 sensor 的关系，我也可以详细整理一份。要不要？
