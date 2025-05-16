### 2.2 配置 sudo 权限

在所有节点上配置 sudo 权限：

```sh
dnf install -y sudo
echo 'devops ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/devops
chmod 440 /etc/sudoers.d/devops
```

# 安装 vim

```sh
dnf install -y vim
```


