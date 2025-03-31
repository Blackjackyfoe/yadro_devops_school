# kubernetes

Role for installing Kubernetes components on Ubuntu.

## Variables

- **`k8s_version`**: `v1.32`

## Example Playbook

```yaml
---
- name: Install k8s utils
  vars_files:
    - secret.yml
  hosts: all
  roles:
    - name: k8s
      become: true
