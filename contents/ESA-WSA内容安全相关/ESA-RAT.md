在 Cisco ESA（Email Security Appliance）中，**RAT** 指的是：

> **Recipient Access Table** —— 收件人访问表

---

## ✅ 一句话解释：

> **RAT（Recipient Access Table）** 是 Cisco ESA 用来**控制入站邮件中目标收件人地址是否被接受、拒绝或转发**的一个机制，是邮件流控制的第一道关卡。

---

## 📦 RAT 的主要功能：

| 功能                  | 描述                                       |
| --------------------- | ------------------------------------------ |
| ✅ **接收验证**       | 判断收件人地址是否存在，防止发给无效地址   |
| ✅ **防垃圾邮件攻击** | 阻止“收件人枚举攻击”（收件人地址爆破）     |
| ✅ **内部邮件路由**   | 将不同收件人地址的邮件转发到不同内部服务器 |
| ✅ **拒绝某些收件人** | 某些特定地址可以设置拒收或重定向           |

---

## 🔧 工作流程简述：

1. 邮件到达 ESA
2. ESA 查询 RAT 表
3. 根据规则判断收件人地址是否：
   - ✅ 接收（ACCEPT）
   - ❌ 拒收（REJECT）
   - ↪️ 重定向（RELAYS TO）
   - ⛔ 黑洞（DROP）

---

## 💡 示例：

| 收件人地址          | 动作                           |
| ------------------- | ------------------------------ |
| `user1@example.com` | ACCEPT                         |
| `sales@example.com` | RELAYS TO mail1.internal.local |
| `test@fake.com`     | REJECT                         |

---

## ⚙️ 配置入口：

在 Cisco ESA 的 GUI 管理界面：

> **Mail Policies** ➝ **Recipient Access Table (RAT)**

也可以通过 CLI 配置。

---

## 🚧 与 LDAP 配合使用：

RAT 也可配合 **LDAP 接收验证（LDAP Recipient Validation）**，自动将组织的合法邮箱地址同步进来，动态生成规则，避免人工维护。

---

## 🛡️ 安全意义：

启用 RAT 可以显著提升 ESA 防御能力：

- 避免攻击者通过 SMTP 枚举收件人地址
- 减少垃圾邮件处理负担
- 提高资源使用效率

---

## 🎯 总结一句话：

> Cisco ESA 的 **RAT（Recipient Access Table）** 是入站邮件的“第一道门卫”，它决定是否接受某个收件人地址的邮件，是垃圾邮件防御和流量管控的重要工具。

---

如果你在准备考试、写文档或汇报，我可以帮你画出“RAT 判定流程图”或“常见配置表格”，需要吗？
