# 怎么查看定制？

```sh
system liscense show  #如果有 custom_name字段很可能是定制
```

# 怎么看是 nat 先还是 fw 先？

```sh
network debug se show # 看哪个模块在前面
```

# 怎么看放通的可信主机的服务？

```sh
pf service show
```
# 