---
layout: home
title: "실용적인 예제"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 실용적인 예제

## 실용적인 예제

### 사용자별 디렉터리 접근

사용자별로 다른 디렉터리에 접근하는 스크립트 예제입니다.

```bash
#!/bin/bash
current_user=$(whoami)

case $current_user in
    "root")
        work_dir="/root/workspace"
        ;;
    "hojin")
        work_dir="/home/hojin/workspace"
        ;;
    "admin")
        work_dir="/home/admin/workspace"
        ;;
    *)
        work_dir="/home/$current_user/workspace"
        ;;
esac

echo "작업 디렉터리: $work_dir"
cd $work_dir
```

### 권한 확인 스크립트

파일이나 디렉터리의 권한을 확인하는 스크립트입니다.

```bash
#!/bin/bash
target_file="$1"
current_user=$(whoami)

if [ -z "$target_file" ]; then
    echo "사용법: $0 <파일명>"
    exit 1
fi

if [ -r "$target_file" ]; then
    echo "사용자 $current_user는 파일 $target_file을 읽을 수 있습니다."
else
    echo "사용자 $current_user는 파일 $target_file을 읽을 수 없습니다."
fi

if [ -w "$target_file" ]; then
    echo "사용자 $current_user는 파일 $target_file을 쓸 수 있습니다."
else
    echo "사용자 $current_user는 파일 $target_file을 쓸 수 없습니다."
fi
```


---

[⬅️ 이전](../)
