Central Web Authentication（CWA）是一种基于 Web 的身份验证机制，常用于访客网络接入控制。在 Cisco Meraki 无线网络中，CWA 通过与 Cisco Identity Services Engine（ISE）的集成，实现集中式的访客身份验证和授权管理。

### CWA 工作流程概述

1. **客户端连接**：终端设备连接到配置了开放式 SSID（无需预先身份验证）的无线网络。

2. **MAC 地址认证请求**：Meraki 接入点（AP）将客户端的 MAC 地址作为用户名和密码，向 ISE 发送 RADIUS Access-Request 请求。

3. **重定向响应**：ISE 返回 RADIUS Access-Accept 响应，并包含一个 URL 重定向属性，指向 ISE 托管的 Web 认证门户。

4. **客户端获取网络配置**：客户端通过 DHCP 获取 IP 地址和 DNS 配置。

5. **HTTP 请求拦截与重定向**：当客户端尝试访问网页时，Meraki AP 拦截 HTTP GET 请求，并将其重定向到 ISE 的 Web 认证页面。

6. **用户身份验证**：用户在 ISE 的 Web 门户上完成身份验证。

7. **授权变更通知（CoA）**：ISE 通过 Change of Authorization（CoA）请求通知 Meraki AP，客户端已成功认证，并应更新其网络访问权限。

8. **重新认证与访问授权**：Meraki AP 向 ISE 发送新的 Access-Request 请求，ISE 返回 Access-Accept 响应，客户端获得完整的网络访问权限。

### 配置要点

- **Walled Garden 设置**：在 Meraki Dashboard 的高级 Splash 设置中，将 ISE 服务器的 IP 地址添加到 Walled Garden，以确保客户端在认证前能够访问 ISE 的 Web 门户。

- **禁止使用 Hybrid Authentication**：如果启用了 Hybrid Authentication 并选择了“增加访问速度”选项，CWA 将无法正常工作。

- **启用 CoA 支持**：确保 Meraki AP 的 SSID 配置支持 CoA 功能，以便 ISE 能够在用户认证后通知 AP 更新客户端的访问权限。

### 注意事项

- **DNS 流量默认允许**：Walled Garden 默认允许 DNS 流量通过，无需额外配置。

- **客户端浏览器行为**：某些设备（如 iOS 和 Android）可能会自动弹出浏览器进行认证，确保认证页面在这些设备上能够正常显示。

- **CoA 端口要求**：CoA 请求使用 UDP 端口 1700，确保网络防火墙允许该端口的通信。

通过上述配置，Cisco Meraki 与 Cisco ISE 的集成能够实现集中式的 Web 认证管理，提升访客网络的安全性和用户体验。
