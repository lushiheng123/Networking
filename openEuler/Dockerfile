# Dockerfile
FROM openeuler/openeuler:22.03

# 安装你日常需要的组件
RUN dnf update -y && \
    dnf install -y vim iproute net-tools curl && \
    dnf clean all

# 设置默认命令
CMD ["/bin/bash"]
