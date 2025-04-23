# 什么是 ZFW(Zone-Based Policy Firewall)?(和 ASA 的区别？)

## 🔐 什么是 Zone-Based Policy Firewall（ZFW）？

ZFW 是 Cisco IOS 引入的一种基于区域的防火墙配置模型，替代了传统的基于接口的防火墙配置方式（如 CBAC）在 ZFW 模型中，接口被分配到不同的“区域”，并通过策略定义区域之间的流量控制规则 这种方式提供了更高的灵活性和精细度，适用于多接口的复杂网络环境

---

## 🧱 ZFW 的核心组件

1. \*_区域（Zone）_： 将具有相似安全级别的接口分。
2. \*_类映射（Class Map）_： 定义匹配特定流量的条件，如协议类型、访问控制列表（ACL）。
3. \*_策略映射（Policy Map）_： 指定对匹配到的流量执行的操作，如检查（inspect）、允许（pass）或丢弃（drop。
4. \*_区域对（Zone Pair）_： 定义源区域和目标区域之间的流量策。

---

## ⚙️ 配置 ZFW 的基本步骤

1. **定义区域**：

   ```bash
   zone security INSIDE
   zone security OUTSIDE
   ``
   

   ```

2. **将接口分配到区域**：

   ```bash
   interface GigabitEthernet0/0
     zone-member security INSIDE
   interface GigabitEthernet0/1
     zone-member security OUTSIDE
   ``
   

   ```

3. **创建类映射**：

   ```bash
   class-map type inspect match-any CLASS-INTERNET
     match protocol http
     match protocol https
   ``
   

   ```

4. **创建策略映射**：

   ```bash
   policy-map type inspect POLICY-INTERNET
     class type inspect CLASS-INTERNET
       inspect
   ``
   

   ```

5. **创建区域对并应用策略**：
   ```bash
   zone-pair security ZP-IN-OUT source INSIDE destination OUTSIDE
     service-policy type inspect POLICY-INTERNET
   ``
   
   ```

---

## 🚦 ZFW 的默认行为

- \*_区域间流量_： 默认被拒绝，除非明确配置许。
- \*_同一区域内流量_： 默认被许。
- \*_未分配到任何区域的接口_： 不能与其他区域通信，除非将其分配到某个域。
- \*_设备自身流量（Self Zone）_： 默认允许与设备自身的通信，如管理量。

---

## 🧠 设计建议

- **区域划**： 根据安全级别和功能将接口划分到不同的区域，如 INSIDE、OUTSIDE、DM 等。
- **策略配**： 根据实际需求配置类映射和策略映射，精确控流量。
- **逐步实**： 在部署 ZFW 时，建议逐步实施和测试，确保不会中断正通信。

---
