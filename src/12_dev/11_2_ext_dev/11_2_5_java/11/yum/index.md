---
layout: home
typora-copy-images-to: ./img
---

# Java11 (Yum)
yum 패키지 관리자를 사용하여 Linux 시스템에 최신의 Java를 설치합니다.

## 저장소 목록 갱신
Java 설치를 위한 Yum 저장소를 추가합니다.

```bash
sudo wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat-stable/jenkins.repo
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
```
> wget이 설치되어 있지 않는 경우 `sudo yum install -y wget`를 설치합니다.

Yum 패키지 목록을 업데이트합니다.
```bash
sudo yum update
```

## 자바설치
Java를 설치합니다.

```bash
sudo yum install java-11-openjdk-devel
```

위 명령어는 OpenJDK 11을 설치합니다. 다른 버전을 설치하려면 패키지 이름을 바꿔서 설치하면 됩니다. 설치 후에는 java -version 명령어를 사용하여 설치된 Java 버전을 확인할 수 있습니다.

```bash
[poly@localhost ~]$ java -version
openjdk version "11.0.19" 2023-04-18 LTS
OpenJDK Runtime Environment (Red_Hat-11.0.19.0.7-1.el9_1) (build 11.0.19+7-LTS)
OpenJDK 64-Bit Server VM (Red_Hat-11.0.19.0.7-1.el9_1) (build 11.0.19+7-LTS, mixed mode, sharing)
```




