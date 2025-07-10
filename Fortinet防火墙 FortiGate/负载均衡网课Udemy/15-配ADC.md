# 192.168.114.21

# admin/123

# 记住用 http 而不是 https

```sh
config system global
set hostname FortiADC
end
```

```sh
config system interface
edit port1
set allowaccess https http ping ssh
set mode dhcp
end
```
