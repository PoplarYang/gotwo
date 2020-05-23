# Interactive light-weight tool to connect server by ssh

It's only a lite tool.

## Principle
Read configration from `$HOME/.ssh/config`.

## Installation
> only supports python3.

```python
pip install gotwo
```
or  
```python
python3 -m pip install gotwo -i https://pypi.python.org/simple
```

## Usages
```bash
➜  ~ goto
           ____  ___ _____ ___  
          / ___|/ _ \_   _/ _ \ 
         | |  _| | | || || | | |
         | |_| | |_| || || |_| |
          \____|\___/ |_| \___/ 
                                

🌻 Up/Down - Move selection up/down
🌴 Enter   - Ssh to current selection
🌵 Ctrl+c  - Quit
🚀 Connecting to ...
HostName        Address         User      
bcc             6.2.7.3         root                                            
dahe            125.6.1.2       dahe           
ecs2            10.15.3.6       root  
```
