---
layout: home
---

# 쉘 스크립트 작동 원리

### 쉘 스크립트란?
- 쉘 스크립트는 간단한 설명으로 쉘이 읽고 해석하여 실행할 수 있는 명령어들로 이루어진 파일
```
#!/bin/bash
// 실행할 쉘 지정

if [$1 = "yes"]
then
    echo "argument is apple"
else
    echo "argument is not apple"
fi
```
- 쉘 스크립트는 리눅스 서버의 편집기를 사용하여 작성할 수 있는데, 특별히 쉘 스크립트 첫 번째 라인은 스크립트를 실행할 shell을 지정해야 한다.
- 쉘 스크립트(shell script) 실행 방식은 `현재 쉘에서 실행되는 방식`과 `서브 쉘에서 실행되는 방식`이 있다.

### 쉘 스크립트 실행 방법
- 서브 쉘에서 스크립트 실행 <br>
💡 작성된 스크립트 파일을 `chmod 명령어로 실행 권한을 부여한 후 실행`
```
$ chmod 755 runfile.sh
$ ./runfile.sh
Hello
```
- 현재 쉘에서 스크립트 실행 <br>
💡 `작성된 스크립트 파일을 source 명령어`로 실행
```
$ source runfile.sh
Hello
```

### 쉘 스크립트 실행 방식
- 서브 쉘 스크립트 실행 방식 <br>
runfile.sh 스크립트 파일을 실행 가능 파일로 하여 직접 실행하는 경우 현재 쉘에서 runfile.sh를 실행하고 `서브 쉘에서 명령어를 실행`한다.
- 현재 쉘 스크립트 실행 방식 <br>
runfile.sh 스크립트 파일을 source 명령어로 실행하는 경우 현재 쉘에서 runfile.sh를 실행하고 `현재 쉘에서 그대로 명령어를 실행`한다.