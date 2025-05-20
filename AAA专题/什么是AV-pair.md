这里讲的 **AV pair**（Attribute-Value pair，属性-值对）是 **RADIUS 协议中的一种标准格式**，表示一条授权或认证信息的具体内容，比如：

> 用户应该拥有怎样的权限？使用哪个 IP 池？登录后的权限等级是多少？……

---

### ✅ 什么是 AV pair？

**AV pair 就是 "属性 = 值" 的格式，比如：**

```
Service-Type = Framed
cisco-avpair = "shell:priv-lvl=15"
```

在 RADIUS 中，每条信息都是一个 AV pair。比如用户的用户名是 `bob`，就会写成：

```
User-Name = bob
```

---

### ✅ 什么是 Vendor-Specific Attribute（VSA）？

有时候，标准 RADIUS 协议的属性不够用，各厂商就定义了**自己专用的扩展属性**，这就叫 **Vendor-Specific Attributes (VSA)**。

IETF 把这个设计放在了属性 **26** 中，也就是说：

> 属性 26 专门用于“厂商自定义”的内容。

---

### ✅ Cisco 的 Vendor-Specific AV Pair 怎么写？

Cisco 使用的格式是：

```
cisco-avpair = "protocol:attribute=value"
```

其中：

- `protocol`：表示这个属性是用于哪个协议的（如 `ip`, `shell`, `voip` 等）
- `attribute`：是 TACACS+ 中定义的属性，比如 `priv-lvl`（权限等级）
- `value`：属性的值，如 `15`
- `=`：代表这是必须的属性
- `*`：代表是可选属性

---

### ✅ 举例说明

| AV Pair 示例                                      | 含义                                         |
| ------------------------------------------------- | -------------------------------------------- |
| `cisco-avpair = "shell:priv-lvl=15"`              | 登录后默认进入特权模式（enable）             |
| `cisco-avpair = "ip:addr-pool=first"`             | 分配 IP 时使用名为 "first" 的 IP 地址池      |
| `cisco-avpair = "ipv6:start-ra-on-ipv6-enable=1"` | 在 IPv4 用户上线时，启动 IPv6 路由通告（RA） |

---

### ✅ Attribute 26 的结构（总结）

RADIUS 的属性 26 包含以下字段：

- **Type**：固定是 26（代表这是一个 Vendor-Specific 的属性）
- **Length**：总长度
- **String (Data)**：包含下面几项：

  - **Vendor-ID**：厂商编号，Cisco 的 Vendor-ID 是 `9`
  - **Vendor-Type**：厂商定义的子类型，比如 `1` 就代表 `cisco-avpair`
  - **Vendor-Length**：这个子结构的长度
  - **Vendor-Data**：真正的 `AV pair` 数据，比如 `shell:priv-lvl=15`

---

### ✅ 总结一句话：

**AV pair 就是“属性=值”的一条指令，用来告诉 RADIUS 服务端：“这个用户应该拥有什么权限或设置”。**
Cisco 用属性 26 扩展了 AV pair 的使用范围，可以实现很多 TACACS+ 的功能。

是否需要我画一个图解释 Attribute 26 的结构？
