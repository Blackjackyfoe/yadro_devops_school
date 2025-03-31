# java17

Role for installing Java 17 on Ubuntu

## Variables

- **`java17_default_package_name`**: str (default: `openjdk-17-jdk`)

## Example Playbook

```yaml
---
- name: Install Java 17 on Ubuntu hosts
  hosts: all
  roles:
    - name: java17
      become: true
```
