---
layout: home
title: "리눅스환경"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 리눅스환경

## 리눅스환경
리눅스 환경에서 volta를 설치합니다. Volta는 Bash 셀로 작성되어 있습니다. curl로 https://get.volta.sh 사이트에 스크립트 코드를 가지고 와서 파이프라인틀 통하여 bash를 실행합니다.  

다음과 같이 명령을 입력합니다.

```
# install Volta
curl https://get.volta.sh | bash
```

실행결과
```
hojin@hojin3:~$ curl https://get.volta.sh | bash
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 10930  100 10930    0     0  13078      0 --:--:-- --:--:-- --:--:-- 13089
  Installing latest version of Volta (1.1.1)
    Checking for existing Volta installation
    Fetching archive for Linux, version 1.1.1
######################################################################## 100.0%
    Creating directory layout
  Extracting Volta binaries and launchers
    Finished installation. Updating user profile settings.
Updating your Volta directory. This may take a few moments...
success: Setup complete. Open a new terminal to start using Volta!
```

설치가 완료되면 .profile에 volta 환경변수가 추가됩니다.
```
$ cat .profile
... 중간생략
export VOLTA_HOME="$HOME/.volta"
export PATH="$VOLTA_HOME/bin:$PATH"
```
> export는 시스템에게 변수를 알려주는 역할을 수행합니다.

콘솔창에서 volta 명령을 실행해 봅니다.
```
hojin@hojin3:~$ volta -v
1.1.1
```
> volta 명령이 실행되지 않는다면, 콘솔창을 재시작 해보시길 바랍니다.


---

[⬅️ 이전](../)
