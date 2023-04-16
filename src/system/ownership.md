---
layout: home
---

# 소유권

## 소유권(ownership)
파일이나 디렉토리는 `소유자`가 해당 사용 권한을 가지고 있읍니다. 권환의 변경은 사용자 및 관리자(root)가 할 수 있습니다.

* 파일을 및 디랙터리를 만들 때에는 생성 사용자가 소유권을 가집니다.
* 소유자는 나중에 `chown`으로 변경이 가능
* `chgrp`로 소유 그룹을 변경할 수 있음


## 파일 소유권 개념

* 파일 소유권은 특정 사용자와 그룹이 파일에 대한 소유 권한을 가지는 것을 의미

* Mydata.txt 파일의 경우, 소유자가 root 사용자이고 소유 그룹도 root


## 소유권 관련 명령어

### chown
* 파일 소유권을 변경하는 명령어

* chown 새사용자명(.새그룹명) 파일명’과 같은 형식으로 사용

* chown ubuntu mydata.txt 명령은 mydata.txt 파일의 소유자를 ubuntu 사용자로 바꾸라는 의미

* chown ubuntu:ubuntu mydata.txt 명령은 파일 그룹도 ubuntu 그룹으로 바꾸라는 의미

* chgrp ubuntu mydata.txt 명령은 그룹만 ubuntu 그룹으로 바꾸라는 의미

