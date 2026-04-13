---
layout: home
title: "문제 해결"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 문제 해결

## 문제 해결

### 로케일 오류

한글 로케일이 설치되지 않은 경우 다음 명령어로 설치할 수 있습니다.

```console
# Ubuntu/Debian
sudo apt-get install locales
sudo locale-gen ko_KR.UTF-8

# CentOS/RHEL
sudo yum install glibc-locale-source
sudo localedef -c -f UTF-8 -i ko_KR ko_KR.UTF-8
```

### 달력이 제대로 표시되지 않는 경우

터미널의 폰트 설정이나 인코딩 문제일 수 있습니다. 다음을 확인해보세요.

```console
# 터미널 인코딩 확인
hojin@DESKTOP-11LMH3B:~$ echo $LANG
ko_KR.UTF-8

# UTF-8 지원 확인
hojin@DESKTOP-11LMH3B:~$ locale -a | grep ko
ko_KR.utf8
```


---

[⬅️ 이전](../)
