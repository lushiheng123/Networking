# 什么是 NSEL(NetFlow Secure Event Logging)?

## 📘 NSEL 概述

NetFlow Secure Event Logging（NSEL）是基于 NetFlow 版本 9 的安全日志记录机制，主要用于 ASA 和 ASASM 设备  它提供了一种有状态的 IP 流量跟踪方法，仅导出表示流中重大事件的记录  在有状态流量跟踪中，跟踪的流会经历一系列状态更改，NSEL 事件用于导出有关流状态的数据，并由导致状态更改的事件触发

---

## ⚙️ 配置 NSEL

### 1. 启用 NSEL

 在 ASA CLI 中使用以下命令启用 NSEL


````bash
asa(config)# flow-export destination <collector_ip> <port>
asa(config)# flow-export template timeout-rate <rate>
asa(config)# flow-export template data-timeout <timeout>
asa(config)# flow-export template delete-timeout <timeout>
```

-`<collector_ip>`：指定 NetFlow 收集器的 IP 地址
-`<port>`：指定 NetFlow 收集器的端口
-`<rate>`：指定模板超时率
-`<timeout>`：指定数据超时和删除超时

### 2. 配置流导出行为
使用 Modular Policy Framework（MPF）配置流导出行为

```bash
asa(config)# policy-map global_policy
asa(config-pmap)# class inspection_default
asa(config-pmap-c)# flow-export
```

-`flow-export`：启用流导出

### 3. 配置模板超时
设置模板的超时值

```bash
asa(config)# flow-export template timeout-rate <rate>
asa(config)# flow-export template data-timeout <timeout>
asa(config)# flow-export template delete-timeout <timeout>
```

-`<rate>`：指定模板超时率
-`<timeout>`：指定数据超时和删除超时

---

## 📊 监控 NSEL
使用以下命令监控 NSEL 状：

```bash
asa# show flow-export status
asa# show flow-export template
asa# show flow-export statistics
``


 `show flow-export status`：显示流导出状。
 `show flow-export template`：显示流模板信。
 `show flow-export statistics`：显示流导出统计信。

---

## 🧠 小贴士
- 确保 ASA 与 NetFlow 收集器之间的网络连接定。- 定期检查流导出统计信息，确保流量数据的正常出。- 根据网络流量的特点，合理配置模板超时值，以优化能。

---

如果你需要更详细的配置示例或遇到具体问题，欢迎继续提问！
````
