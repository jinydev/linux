---
layout: home
---

# Python Setup

## 설치
파이썬은 일부 몇몇 배포본에서 기본적으로 설치가 되는 경우가 많이 있습니다. 따라서, 기존에 파이썬이 설치가 되어 있는지 확인을 합니다.

```
hojin@hojin3:~$ phthon --version
phthon: command not found
```

### 패키지를 이용한 파이썬 설치
파이썬이 설치가 되어 있지 않는 것이 확인이 된다면, 파이썬을 설치해 보도록 하겠습니다.

데비안 계열:
```
$ sudo apt install python3 -y
```

레드햇 계열:
```
$ sudo yum install python3 -y
```

### 설치확인
파이썬이 잘 설치가 되었는지 확인을 해보도록 합니다.

```
hojin@hojin3:~$ python3 --version
Python 3.10.6
```