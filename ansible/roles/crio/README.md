# crio

Role for installing CRI-O runtime on Ubuntu.

## Variables

- **`crio_version`**: `v1.32`

## Example Playbook

```yaml
---
- name: Install crio utils
  vars_files:
    - secret.yml
  hosts: all
  roles:
    - name: crio
      become: true

