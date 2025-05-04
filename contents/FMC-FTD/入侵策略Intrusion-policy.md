你提到的是 Cisco Firepower 中的 **Intrusion Policy（入侵策略）**，这是 Cisco FTD 系统中用来提供 **入侵检测和防御功能（IDS/IPS）** 的核心部分。下面是对这部分内容的系统介绍：

---

## 🔐 什么是 Intrusion Policy？

**Intrusion Policy 是一组 Snort 规则的集合，用来检测和拦截已知的攻击行为。**

- 通过对网络流量进行 **签名匹配（signature-based）**，判断是否存在已知威胁。
- 属于 **深度包检测（Deep Packet Inspection）**，需要更多计算资源。
- 只能在流量经过 Access Control Policy（ACP）并被允许时才进行检测。

---

## 🧠 Intrusion Policy 的核心机制

| 元素               | 说明                                                         |
| ------------------ | ------------------------------------------------------------ |
| **Snort 引擎**     | Intrusion Policy 运行在 Snort 引擎上，是基于签名的检测系统。 |
| **规则（Rules）**  | 每个规则定义一个攻击特征（例如：SQL 注入、端口扫描）。       |
| **策略（Policy）** | 一组规则的集合，按优先级和启用状态进行编排。                 |
| **部署位置**       | 必须附加在 ACP 策略中的某一条 Rule 上才能生效。              |

---

## 🔄 Intrusion Policy 的工作流程

1. 流量进入 FTD。
2. 匹配 **Pre-Filter Policy**（如有配置）。
3. 进入 **Access Control Policy（ACP）**。
4. 如果 ACP Rule 上附加了 Intrusion Policy，且流量被允许 → 进入 Snort 检查。
5. 若匹配规则（威胁），可执行阻断、警报等动作。

---

## 📦 Cisco 提供的默认 Intrusion Policies（预定义策略）

| 名称                                   | 描述                                                               |
| -------------------------------------- | ------------------------------------------------------------------ |
| **Balanced Security and Connectivity** | 默认推荐策略，在安全和性能之间取得平衡，适合大多数环境。           |
| **Connectivity over Security**         | 侧重连通性，启用最关键的规则，误报少，适合对安全要求不高的场景。   |
| **Security over Connectivity**         | 侧重安全性，启用更多规则，但可能引起更多误报。适合高安全需求场景。 |
| **Maximum Detection**                  | 启用所有规则，用于测试或实验室，误报率非常高，不建议用于生产环境。 |
| **No Rules Active**                    | 所有规则都禁用，适合作为模板使用或排查问题时使用。                 |

---

## 🧱 自定义策略结构

- 你可以从某个默认策略 **复制一份作为 Base Layer**，然后在其上创建额外的自定义策略层（Policy Layers）。
- **策略层是叠加的（类似防火墙规则栈）**，你可以根据实际业务，选择启用哪些规则，定义优先级。
- Cisco 会定期更新默认策略中的规则数据库（如果你开启了自动更新）。

---

## 📌 配置路径（在 FMC 中）

```
Policies → Intrusion → Intrusion Policies
```

- 可以在这里新建或编辑策略。
- 在 **Access Control Policy（ACP）→ 某条规则 → Advanced → Intrusion Policy** 中附加此策略。

---

## 🧪 举个例子：

如果你希望：

- 对业务系统的 Web 流量做 SQL 注入检测
- 又不希望因轻微误报影响正常连接

你可以选择：

- 使用 **Balanced Security and Connectivity** 作为基础
- 然后禁用一些对你环境干扰较大的规则（通过 Rule Tuning）

---

需要我帮你展示 Snort 规则长什么样，或讲一下怎么自定义启用/禁用规则吗？
