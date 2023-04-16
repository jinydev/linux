---
layout: home
---

# Volta

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

## volta로 노드 설치하기
volta를 이용하면 시스템에 쉽게 nodejs를 설치할 수 있습니다. 다음과 같이 명령을 입력합니다.

```
# install Node
volta install node
```

> volta는 최신의 안정화된 LTS 버젼의 nodejs를 설치합니다. 만일, 다른 버젼을 설치하고자 할때에는 `@버젼`을 붙여서 명령을 실행하면 됩니다.
> ```
> # current 버젼설치
> volta install node@19
> ```

nodejs가 잘 설치가 되었는지 실행을 해봅니다.

```
# start using Node
node -v
```

> volta는 윈도우에서도 사용이 가능합니다.

volta를 이용하면 node pakage manager인 npm도 같이 설치가 됩니다.

```
hojin@hojin3:~$ npm -v
9.5.0
```