---
layout: home
typora-copy-images-to: ./img
---

## Java11 설치

### openjdk 설치
Ubuntu 리포지토리에서 JRE(Java Runtime Environment를 설치합니다. 
apt 목록에 등록된 기본 jdk를 설치합니다.

```bash
sudo apt install default-jdk -y
```

만일 버젼을 지정하여 설치하고자 하는 경우 다음과 같이 할 수 있습니다.

```bash
sudo apt install openjdk-11-jdk
```

JER를 설치한 후에는 다음과 같이 버젼을 확인할 수 있습니다.

```bash
hojin@hojin3:~$ java --version
openjdk 11.0.18 2023-01-17
OpenJDK Runtime Environment (build 11.0.18+10-post-Ubuntu-0ubuntu122.04)
OpenJDK 64-Bit Server VM (build 11.0.18+10-post-Ubuntu-0ubuntu122.04, mixed mode, sharing)
```
