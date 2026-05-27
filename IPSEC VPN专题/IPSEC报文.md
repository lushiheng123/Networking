# IPSEC通信中有哪些报文？
**IPsec 的“建路”和“走路”** 两个阶段。

下面我为你画一个 **IKE 协商报文 vs 数据报文** 的对比图，并逐层解释。

---

## 一、宏观对比图（文字版）

```
┌─────────────────────────────────────────────────────────────────────┐
│                    IPsec 通信的两类报文                              │
├──────────────────────────┬──────────────────────────────────────────┤
│   IKE 协商报文            │   数据报文                               │
│   (UDP 500 / 4500)       │   (ESP 协议号 50 / AH 协议号 51)         │
├──────────────────────────┼──────────────────────────────────────────┤
│  功能：建立 SA            │  功能：传输数据                           │
│  频率：偶尔（建立时/重协商）│  频率：频繁（每个数据包）                   │
│  内容：明文（但可加密）     │  内容：加密（ESP）或明文（AH）              │
│  能看到：算法、模式、密钥材料│  能看到：SPI、序列号                      │
│  看不到：实际数据           │  看不到：算法、模式（需要关联到 SA）         │
└──────────────────────────┴──────────────────────────────────────────┘
```

---

## 二、报文结构对比图

### 场景：Site-to-Site VPN，隧道模式，ESP

```
┌─────────────────────────────────────────────────────────────────────┐
│  IKE 协商报文（UDP 500）                                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  [IP 头]                                                            │
│    Source: 172.16.1.1 (网关A)                                       │
│    Destination: 172.16.2.1 (网关B)                                  │
│    Protocol: 17 (UDP)                                               │
│                                                                     │
│  [UDP 头]                                                           │
│    Source Port: 500                                                 │
│    Destination Port: 500                                            │
│                                                                     │
│  [IKE 头]                                                           │
│    Initiator SPI: 0xA1B2C3D4E5F6                                    │
│    Responder SPI: 0x000000000000 (初始为0)                           │
│    Message Type: 1 (SA Init)                                        │
│                                                                     │
│  [IKE 载荷 - 安全提议]  ← 这里能看到算法和模式                          │
│    Proposal #1:                                                     │
│      Protocol: ESP                                                  │
│      Encryption: AES-CBC (128 bits)                                 │
│      Authentication: HMAC-SHA1                                      │
│      Encapsulation Mode: Tunnel                                     │
│      Lifetime: 28800 seconds                                        │
│      DH Group: 14 (2048-bit MODP)                                   │
│                                                                     │
│  [IKE 载荷 - 密钥交换]                                               │
│    DH Public Key: [2048-bit value]                                  │
│                                                                     │
│  [IKE 载荷 - 身份]                                                   │
│    ID Type: IPv4 Address                                            │
│    ID Value: 172.16.1.1                                             │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘

                              ↓
                   IKE 协商完成，SA 建立
                              ↓

┌─────────────────────────────────────────────────────────────────────┐
│  数据报文（ESP 协议号 50）                                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  [外层 IP 头]  ← 隧道模式特征：两个IP头                                 │
│    Source: 172.16.1.1 (网关A)                                       │
│    Destination: 172.16.2.1 (网关B)                                  │
│    Protocol: 50 (ESP)                                               │
│                                                                     │
│  [ESP 头]                                                           │
│    Security Parameters Index (SPI): 0x12345678  ← 关联到 SA          │
│    Sequence Number: 42                                              │
│                                                                     │
│  [加密数据]  ← 看不到算法、模式，看不到内层IP头                             │
│    ┌─────────────────────────────────────┐                          │
│    │ [内层 IP 头]                         │                          │
│    │   Source: 10.1.1.1 (主机A)          │                          │
│    │   Destination: 10.2.2.2 (主机B)     │                          │
│    │ [内层数据]                           │                          │
│    │   TCP/UDP + 应用数据                 │                          │
│    └─────────────────────────────────────┘                          │
│                                                                     │
│  [ESP 尾]                                                           │
│    Padding (0-255 bytes)                                            │
│    Pad Length                                                       │
│    Next Header: 4 (IPv4)                                            │
│                                                                     │
│  [ESP 认证数据 (ICV)]                                               │
│    HMAC-SHA1: [160-bit value]                                       │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 三、Wireshark 过滤与观察

### 1. 过滤 IKE 协商报文

```bash
# 过滤 IKE 主模式/野蛮模式
udp.port == 500

# 过滤 NAT-T 场景的 IKE
udp.port == 4500
```

**Wireshark 展开后看到：**

```
Internet Security Association and Key Management Protocol (ISAKMP)
  Initiator SPI: a1b2c3d4e5f6
  Responder SPI: 000000000000
  Next Payload: Security Association (1)
  Message Type: 1 (SA Init)
  Security Association
    Proposal #1
      Protocol: ESP
      Transform #1
        Encryption Algorithm: AES-CBC (12)
        Authentication Algorithm: HMAC-SHA1 (2)
        Encapsulation Mode: Tunnel (1)
        Lifetime: 28800 seconds
```

### 2. 过滤数据报文

```bash
# 过滤 ESP 数据包
ip.proto == 50

# 过滤特定 SPI 的 ESP 包
esp.spi == 0x12345678
```

**Wireshark 展开后看到：**

```
Internet Protocol
  Source: 172.16.1.1
  Destination: 172.16.2.1
  Protocol: ESP (50)

Encapsulating Security Payload
  SPI: 0x12345678
  Sequence: 42
  Payload: [encrypted]  ← 看不到算法、模式、内层IP
```

---

## 四、关键对比总结表

| 对比项 | IKE 协商报文 | 数据报文 |
|--------|-------------|----------|
| **端口/协议号** | UDP 500 / 4500 | IP 50 (ESP) / 51 (AH) |
| **SPI 出现位置** | IKE 头中（64位） | ESP/AH 头中（32位） |
| **能看到算法** | ✅ 明文列出 | ❌ 不可见 |
| **能看到模式** | ✅ 明文列出 | ❌ 需通过报文结构推断 |
| **能看到密钥** | ❌ 只有 DH 公钥 | ❌ 密钥不在报文中 |
| **能看到数据** | ❌ 只有协商信息 | ✅ 加密后的数据 |
| **频率** | 偶尔（建立/重协商） | 频繁（每个数据包） |
| **Wireshark 过滤** | `udp.port == 500` | `ip.proto == 50` |

---

## 五、一句话总结

> **IKE 协商报文是“建路图纸”（明文，能看到算法、模式、SPI），数据报文是“路上跑的车”（加密，只能看到 SPI 来关联图纸）。没有 IKE 协商，数据报文就只是一堆无法解读的乱码。**

这个对比图应该能帮你把两个阶段彻底分清楚了。如果你需要，我可以再画一个 **IKE 完整交互流程（主模式 6 个包）** 的报文序列图。