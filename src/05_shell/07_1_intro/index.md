---
layout: home
title: 7.1 쉘 및 변수 기초
---
# 쉘 스크립트의 기초

리눅스 쉘(Shell)은 사용자의 명령을 커널에 전달하는 해석기입니다. 스크립트 상단에 `#!/bin/bash` 를 선언하여 실행합니다.

```bash
NAME="Linux"
echo "Hello, $NAME"
```