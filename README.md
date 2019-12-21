# A small ssh list tool
## Background
I need a light-weight tool to list the servers that can be connected via ssh. However, I find no one. Therefore, I create it.

It's only a small tool.

## Principle
Read configration from `$HOME/.ssh/config`.

## Installation

```python
pip install tobe
```

## Usages
```bash
# list
➜ tobe
           Servers can be connected
  ID   Hostname            Host
   1   dev            39.10.14.9
   2   prod           192.68.5.31
version: 0.1.1
date: 2019-12-21

# connect
➜ ssh dev
```
