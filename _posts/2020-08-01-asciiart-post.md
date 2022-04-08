---
title: "[TMI]ASII ART TEXT 생성"
date: 2020-08-01 00:15:28 -0400
categories: TMI
---

### ASCII ART TEXT 작성

### INSTALL
- ``pip install art`` : **Not Work**
- ``sudo easy_install "art==4.7"`` : **Work**

### How to Use

```python
from art import *
Rummicube = text2art("Rummicube Solver")
print(Rummicube)
# output
#  ____                                _               _             ____          _                    
# |  _ \  _   _  _ __ ___   _ __ ___  (_)  ___  _   _ | |__    ___  / ___|   ___  | |__   __  ___  _ __ 
# | |_) || | | || '_ ` _ \ | '_ ` _ \ | | / __|| | | || '_ \  / _ \ \___ \  / _ \ | |\ \ / / / _ \| '__|
# |  _ < | |_| || | | | | || | | | | || || (__ | |_| || |_) ||  __/  ___) || (_) || | \ V / |  __/| |   
# |_| \_\ \__,_||_| |_| |_||_| |_| |_||_| \___| \__,_||_.__/  \___| |____/  \___/ |_|  \_/   \___||_|   
                                                                                                      
```

### **더 많은게 궁금하다면?**
***
[참고 링크](https://github.com/sepandhaghighi/art)