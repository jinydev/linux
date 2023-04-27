---
layout : home
---
# Choi Kyeong Min Report 
# 쉘 프로그래밍을 하는 이유

 리눅스에서는 다양한 개발 도구와 IDE(Integrated Development Environment)가 제공되어 있어서, VS Code와 같은 편리한 에디터를 사용하여 프로그래밍할 수 있습니다. 그러나 셸 스크립트는 다른 프로그래밍 언어와 달리 운영 체제와의 상호작용을 목적으로 하기 때문에, 셸 스크립트를 사용하는 것이 좋은 경우가 있습니다.

 예를 들어, 셸 스크립트를 사용하면 파일과 디렉토리를 생성하고 관리하거나, 프로세스를 실행하고 종료하는 등 운영 체제 수준에서의 작업을 쉽게 수행할 수 있습니다. 또한, 셸 스크립트는 다른 프로그램의 출력을 파싱하거나, 다양한 필터링 작업을 수행하는 등 다양한 운영 체제 관련 작업을 자동화하는 데 유용합니다.

 또한, 셸 스크립트는 배치(batch) 작업을 수행하는 데 유용합니다. 예를 들어, 일괄적으로 파일을 이동하거나 복사하는 작업, 일정한 시간마다 실행해야 하는 프로그램을 자동으로 실행하는 작업 등을 수행할 수 있습니다.

1. 파일 이동하기

```
#!/bin/bash

# 원본 파일 경로
SOURCE_DIR="/home/user/documents"

# 이동할 파일 경로
DEST_DIR="/home/user/backups"

# 이동할 파일 확장자
FILE_EXT=".txt"

# SOURCE_DIR 디렉토리에서 FILE_EXT 확장자를 가진 파일을 DEST_DIR로 이동
mv "$SOURCE_DIR"/*"$FILE_EXT" "$DEST_DIR"
```

2. 파일 복사하기

```
#!/bin/bash

# 원본 파일 경로
SOURCE_DIR="/home/user/documents"

# 복사할 파일 경로
DEST_DIR="/home/user/backups"

# 복사할 파일 확장자
FILE_EXT=".txt"

# SOURCE_DIR 디렉토리에서 FILE_EXT 확장자를 가진 파일을 DEST_DIR로 복사
cp "$SOURCE_DIR"/*"$FILE_EXT" "$DEST_DIR"
```

3. 프로그램 자동 실행하기

```
#!/bin/bash

# 프로그램 경로
PROGRAM="/usr/bin/myprogram"

# 실행 간격 (초)
SLEEP_TIME=60

while true
do
  # 프로그램 실행
  $PROGRAM
  
  # SLEEP_TIME 초 동안 대기
  sleep "$SLEEP_TIME"
done
```

마지막으로, 셸 스크립트는 간단하고 빠르게 작성할 수 있기 때문에, 작은 작업을 수행하는 프로그램을 빠르게 작성하고 실행할 수 있습니다.

따라서, 셸 스크립트는 운영 체제와의 상호작용이 필요한 작업을 수행할 때 특히 유용하며, 빠르고 간단한 작업을 수행하는 데 적합합니다.

쉘은 인터프리트(Interprete) 되는 언어를 사용하여 한 줄씩 실행할 수 있고 재 컴파일 시간이

없기 때문에 일반적으로 디버깅(Debugging) 이 쉽다.