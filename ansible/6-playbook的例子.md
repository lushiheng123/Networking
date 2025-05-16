# ansible.builtin

![alt text](README_Images/6-playbook的例子/image.png)

## 写 ping_playbook.yaml

```sh
- name: My first play
  hosts: all_nodes
  tasks:
   - name: Ping my hosts
     ansible.builtin.ping:

   - name: Print message
     ansible.builtin.debug:
       msg: Hello world
```

![alt text](README_Images/6-playbook的例子/image-1.png)

# ping 的结果

![alt text](README_Images/6-playbook的例子/image-2.png)
