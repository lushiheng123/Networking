<h1 align="center">Cisco Meraki学习</h1>

```sh
git init

git checkout -b Meraki

git add .和 git status 常规进行

git commit -m "first commit"设置任务

git remote add origin git@github.com:lushiheng123/Networking.git

git push -u origin Meraki

```

# API: a55f85b1b95936dfeca51bc1ed96a5ba3f495438

# 验证简单的 API 能否使用

```py
import meraki
API_KEY = "a55f85b1b95936dfeca51bc1ed96a5ba3f495438"
dashboard = meraki.DashboardAPI(API_KEY)
response = dashboard.organizations.getOrganizations()
print(response)
```

## 会有输出和日志

![alt text](README_Images/README/image.png)
![alt text](README_Images/README/image-1.png)

# 将 org_id 导入后查看 network_id,先添加 home，

![alt text](README_Images/README/image-4.png)

```py
import meraki
API_KEY = "a55f85b1b95936dfeca51bc1ed96a5ba3f495438"
org_id = 1684610
dashboard = meraki.DashboardAPI(API_KEY)
response = dashboard.organizations.getOrganizationNetworks(org_id)
print(response)
```

![alt text](README_Images/README/image-2.png)
![alt text](README_Images/README/image-5.png)

## network_id = L_813462682693806092
