![alt text](README_Images/实施3-搭建FTP服务器/image.png)

# vsftpd

![alt text](README_Images/实施3-搭建FTP服务器/image-1.png)

# dnf install vsftpd

## vsftpd 直接运行

## ps aux | grep vsftpd 检查进程是否运行

![alt text](README_Images/实施3-搭建FTP服务器/image-2.png)

## ss -tnlp | grep :21 或者 netstat -tnlp | grep :21(需先安装 net-tools)检查是否监听了 FTP 端口（默认 21）

![alt text](README_Images/实施3-搭建FTP服务器/image-3.png)
