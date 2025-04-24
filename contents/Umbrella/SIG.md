Cisco Umbrella 的 **SIG Essentials（Secure Internet Gateway Essentials）** 是 Umbrella 的一个核心子功能套件，主要为企业提供一个**基础级别的云安全网关（Cloud-delivered Secure Web Gateway）**，用来保护用户访问互联网时不受威胁，同时也增强对流量的可视性和控制力。

---

## ✅ SIG Essentials 包括哪些核心功能？

| 功能模块                                      | 描述                                                                                         |
| --------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **DNS-layer Security**                        | Umbrella 最基本的防线：当用户尝试解析恶意域名时，直接在 DNS 层阻止访问。                     |
| **Secure Web Gateway（SWG）**                 | 云端的 Web 安全网关功能：可以检测 HTTP/HTTPS 流量，实施 URL 过滤、内容检查、恶意软件检测等。 |
| **Cloud Delivered Firewall（CDFW）**          | 基于云的 L3/L4 防火墙：对非 Web 流量（如 TCP、UDP、ICMP）进行分析与控制。                    |
| **CASB Lite（Cloud Access Security Broker）** | 提供对 SaaS 应用（如 Dropbox、Google Drive）的可见性，检测滥用云服务。                       |
| **Threat Intelligence（威胁情报）**           | 集成 Cisco Talos 提供的实时威胁情报，对 IP、域名、URL 进行高精度识别。                       |
| **集中日志和报告**                            | 所有活动都能统一记录和可视化分析，便于取证和策略优化。                                       |

---

## 💡 通俗理解：

> **SIG Essentials 就像一个轻量版的云安全平台**，它把 DNS 安全、Web 安全、网络层防护、应用可见性这些“基础但必要”的能力，集成到了 Umbrella 云端，无需部署硬件。

---

## 📦 SIG Essentials 和 Umbrella 基础版的区别？

| 功能对比            | Umbrella DNS Essentials | Umbrella SIG Essentials |
| ------------------- | ----------------------- | ----------------------- |
| DNS 安全            | ✅ 有                   | ✅ 有                   |
| URL 屏蔽 / SWG      | ❌ 没有                 | ✅ 有                   |
| 云防火墙（L3/L4）   | ❌ 没有                 | ✅ 有                   |
| SaaS 可视性（CASB） | ❌ 没有                 | ✅ 有                   |
| 全流量日志记录      | ❌ 限制                 | ✅ 全部                 |
| 适合对象            | 仅做 DNS 安全的客户     | 需要全面上网控制的客户  |

---

## ✍️ 场景举例：

- 你公司员工在家远程办公，上网访问各种网站或 SaaS 服务；
- 通过 Umbrella SIG Essentials，可以：
  - 拦截访问恶意网址；
  - 阻止访问特定类型网站（如博彩、社交媒体）；
  - 限制某些 SaaS 应用的使用；
  - 对所有上网行为进行记录和取证。

---

如果你正在评估安全方案、准备汇报或项目建议书，我可以帮你做一份 **Umbrella 产品线对比表 + 选型建议** 或者 **常见竞品对比（如 Zscaler）**。要不要我帮你整理一下？
