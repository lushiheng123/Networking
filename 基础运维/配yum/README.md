# 删除下面所有源：

```sh
rm -f /etc/yum.repos.d/*.repo
```

#

```sh
cat > /etc/yum.repos.d/aliyun.repo <<EOF
[base]
name=Aliyun BaseOS
baseurl=https://mirrors.aliyun.com/centos-stream/9-stream/BaseOS/x86_64/os/
enabled=1
gpgcheck=0

[appstream]
name=Aliyun AppStream
baseurl=https://mirrors.aliyun.com/centos-stream/9-stream/AppStream/x86_64/os/
enabled=1
gpgcheck=0
EOF
```
# 其他镜像

```sh
cat > /etc/yum.repos.d/aliyun.repo <<EOF
[base]
name=Aliyun BaseOS
baseurl=https://mirrors.aliyun.com/centos-stream/9-stream/BaseOS/x86_64/os/
enabled=1
gpgcheck=0

[appstream]
name=Aliyun AppStream
baseurl=https://mirrors.aliyun.com/centos-stream/9-stream/AppStream/x86_64/os/
enabled=1
gpgcheck=0
EOF
```

# 记得 dnf clean all,dnf makecache
