---
layout: home
title: "cmp - 리눅스 파일 비교 명령어 - 개발자를 위한 리눅스"
description: "cmp 명령어의 사용법과 옵션을 알아보세요. 파일 비교, 바이너리 파일 비교, 스크립트에서 활용 방법을 포함한 포괄적인 가이드입니다."
keywords: "cmp, 파일비교, linux, 명령어, 바이너리, 비교, 리눅스"
author: "HojinLee"
og_title: "cmp - 리눅스 파일 비교 명령어 - 개발자를 위한 리눅스"
og_description: "cmp 명령어의 사용법과 옵션을 알아보세요. 파일 비교, 바이너리 파일 비교, 스크립트에서 활용 방법을 포함한 포괄적인 가이드입니다."
og_type: "article"
twitter_card: "summary"
---

# cmp 명령어

`cmp` 명령어는 리눅스 시스템에서 두 개의 파일을 바이트 단위로 비교하는 유틸리티입니다. 이 명령어는 파일이 동일한지 확인하거나, 차이점이 있는 경우 첫 번째 차이점의 위치를 알려줍니다.

## 기본 사용법

### 두 파일 비교

가장 기본적인 사용법으로, 두 파일을 비교합니다.

```console
hojin@DESKTOP-11LMH3B:~$ cmp file1.txt file2.txt
```

### 파일이 동일한 경우

두 파일이 완전히 동일한 경우, `cmp` 명령어는 아무것도 출력하지 않고 종료 코드 0을 반환합니다.

```console
hojin@DESKTOP-11LMH3B:~$ cmp file1.txt file1_copy.txt
hojin@DESKTOP-11LMH3B:~$ echo $?
0
```

### 파일이 다른 경우

두 파일이 다른 경우, 첫 번째 차이점의 위치와 바이트 정보를 출력합니다.

```console
hojin@DESKTOP-11LMH3B:~$ cmp file1.txt file2.txt
file1.txt file2.txt differ: byte 15, line 1
```

## 주요 옵션

### `-l` 옵션
모든 차이점을 자세히 출력합니다.

```console
hojin@DESKTOP-11LMH3B:~$ cmp -l file1.txt file2.txt
15 141 142
16 162 163
17 164 165
```

출력 형식: `바이트위치 파일1바이트 파일2바이트`

### `-s` 옵션
조용한 모드로, 출력 없이 종료 코드만 반환합니다.

```console
hojin@DESKTOP-11LMH3B:~$ cmp -s file1.txt file2.txt
hojin@DESKTOP-11LMH3B:~$ echo $?
1
```

### `-n` 옵션
지정된 바이트 수만큼만 비교합니다.

```console
hojin@DESKTOP-11LMH3B:~$ cmp -n 10 file1.txt file2.txt
```

### `-i` 옵션
지정된 바이트 위치부터 비교를 시작합니다.

```console
hojin@DESKTOP-11LMH3B:~$ cmp -i 10 file1.txt file2.txt
```

## 종료 코드

`cmp` 명령어는 다음과 같은 종료 코드를 반환합니다:

- **0**: 파일이 동일함
- **1**: 파일이 다름
- **2**: 오류 발생 (파일이 존재하지 않거나 읽을 수 없음)

## 실용적인 활용

### 스크립트에서 활용

`cmp` 명령어는 쉘 스크립트에서 파일 비교를 자동화할 때 매우 유용합니다.

```bash
#!/bin/bash
# 파일 비교 스크립트
file1="source.txt"
file2="backup.txt"

if cmp -s "$file1" "$file2"; then
    echo "파일이 동일합니다."
else
    echo "파일이 다릅니다."
    # 차이점 자세히 출력
    cmp -l "$file1" "$file2" | head -10
fi
```

### 백업 파일 검증

백업 파일이 원본과 동일한지 확인할 때 사용할 수 있습니다.

```bash
#!/bin/bash
# 백업 검증 스크립트
original_file="/path/to/original.txt"
backup_file="/backup/original.txt"

echo "백업 파일 검증 중..."

if cmp -s "$original_file" "$backup_file"; then
    echo "✓ 백업 파일이 원본과 동일합니다."
    exit 0
else
    echo "✗ 백업 파일이 원본과 다릅니다!"
    echo "첫 번째 차이점:"
    cmp "$original_file" "$backup_file"
    exit 1
fi
```

### 설정 파일 변경 감지

설정 파일이 변경되었는지 확인할 때 활용할 수 있습니다.

```bash
#!/bin/bash
# 설정 파일 변경 감지
config_file="/etc/myapp.conf"
config_backup="/var/backup/myapp.conf.backup"

if [ ! -f "$config_backup" ]; then
    echo "백업 파일이 없습니다. 현재 설정을 백업합니다."
    cp "$config_file" "$config_backup"
else
    if cmp -s "$config_file" "$config_backup"; then
        echo "설정 파일이 변경되지 않았습니다."
    else
        echo "설정 파일이 변경되었습니다!"
        echo "변경 사항:"
        diff "$config_backup" "$config_file"
    fi
fi
```

## 고급 사용법

### 바이너리 파일 비교

`cmp` 명령어는 특히 바이너리 파일 비교에 유용합니다.

```bash
#!/bin/bash
# 바이너리 파일 비교 스크립트
binary1="program1.bin"
binary2="program2.bin"

echo "바이너리 파일 비교 중..."

if cmp -s "$binary1" "$binary2"; then
    echo "바이너리 파일이 동일합니다."
else
    echo "바이너리 파일이 다릅니다."
    echo "차이점 분석:"
    cmp -l "$binary1" "$binary2" | while read -r byte_pos byte1 byte2; do
        printf "바이트 %d: 0x%02x -> 0x%02x\n" "$byte_pos" "0$byte1" "0$byte2"
    done
fi
```

### 부분 파일 비교

특정 부분만 비교할 때 사용할 수 있습니다.

```bash
#!/bin/bash
# 파일의 특정 부분만 비교
file1="data1.bin"
file2="data2.bin"
offset=1000
length=500

echo "파일의 $offset 바이트부터 $length 바이트만 비교합니다."

if cmp -s -i $offset -n $length "$file1" "$file2"; then
    echo "지정된 부분이 동일합니다."
else
    echo "지정된 부분이 다릅니다."
    cmp -i $offset -n $length "$file1" "$file2"
fi
```

### 대량 파일 비교

여러 파일을 일괄적으로 비교할 때 활용할 수 있습니다.

```bash
#!/bin/bash
# 대량 파일 비교 스크립트
source_dir="/source"
backup_dir="/backup"

echo "대량 파일 비교 시작..."

for file in "$source_dir"/*; do
    if [ -f "$file" ]; then
        filename=$(basename "$file")
        backup_file="$backup_dir/$filename"
        
        if [ -f "$backup_file" ]; then
            if cmp -s "$file" "$backup_file"; then
                echo "✓ $filename: 동일"
            else
                echo "✗ $filename: 다름"
            fi
        else
            echo "! $filename: 백업 파일 없음"
        fi
    fi
done
```

## 문제 해결

### 권한 문제

파일에 읽기 권한이 없는 경우 오류가 발생할 수 있습니다.

```bash
#!/bin/bash
# 권한 확인 후 비교
file1="protected1.txt"
file2="protected2.txt"

# 파일 권한 확인
if [ ! -r "$file1" ] || [ ! -r "$file2" ]; then
    echo "파일에 읽기 권한이 없습니다."
    ls -l "$file1" "$file2"
    exit 1
fi

# 파일 비교 실행
cmp "$file1" "$file2"
```

### 파일 크기 문제

파일 크기가 매우 큰 경우 비교 시간이 오래 걸릴 수 있습니다.

```bash
#!/bin/bash
# 큰 파일 비교 스크립트
file1="large1.bin"
file2="large2.bin"

# 파일 크기 확인
size1=$(stat -c%s "$file1")
size2=$(stat -c%s "$file2")

if [ "$size1" != "$size2" ]; then
    echo "파일 크기가 다릅니다: $size1 vs $size2"
    exit 1
fi

echo "파일 크기가 동일합니다. 비교를 시작합니다..."
cmp "$file1" "$file2"
```

### 메모리 부족 문제

매우 큰 파일을 비교할 때 메모리 부족이 발생할 수 있습니다.

```bash
#!/bin/bash
# 메모리 효율적인 비교
file1="very_large1.bin"
file2="very_large2.bin"

# 청크 단위로 비교
chunk_size=1048576  # 1MB
offset=0

while true; do
    if cmp -s -i $offset -n $chunk_size "$file1" "$file2"; then
        echo "청크 $offset: 동일"
        offset=$((offset + chunk_size))
    else
        echo "청크 $offset: 다름"
        cmp -l -i $offset -n $chunk_size "$file1" "$file2" | head -5
        break
    fi
done
```

## 활용 예제

### 자동화된 테스트

자동화된 테스트에서 예상 결과와 실제 결과를 비교할 때 사용할 수 있습니다.

```bash
#!/bin/bash
# 자동화된 테스트 스크립트
test_input="test_input.txt"
expected_output="expected_output.txt"
actual_output="actual_output.txt"

echo "테스트 실행 중..."
./myprogram < "$test_input" > "$actual_output"

echo "결과 비교 중..."
if cmp -s "$expected_output" "$actual_output"; then
    echo "✓ 테스트 통과"
    exit 0
else
    echo "✗ 테스트 실패"
    echo "차이점:"
    cmp "$expected_output" "$actual_output"
    exit 1
fi
```

### 파일 동기화 확인

파일 동기화가 제대로 되었는지 확인할 때 활용할 수 있습니다.

```bash
#!/bin/bash
# 파일 동기화 확인 스크립트
source_dir="/source"
destination_dir="/destination"

echo "파일 동기화 확인 중..."

find "$source_dir" -type f | while read -r file; do
    relative_path="${file#$source_dir/}"
    dest_file="$destination_dir/$relative_path"
    
    if [ -f "$dest_file" ]; then
        if cmp -s "$file" "$dest_file"; then
            echo "✓ $relative_path: 동기화됨"
        else
            echo "✗ $relative_path: 동기화 안됨"
        fi
    else
        echo "! $relative_path: 대상 파일 없음"
    fi
done
```

### 무결성 검사

파일의 무결성을 검사할 때 사용할 수 있습니다.

```bash
#!/bin/bash
# 파일 무결성 검사 스크립트
original_file="important.dat"
checksum_file="important.dat.md5"

echo "파일 무결성 검사 중..."

# MD5 체크섬 생성
current_checksum=$(md5sum "$original_file" | cut -d' ' -f1)
stored_checksum=$(cat "$checksum_file")

if [ "$current_checksum" = "$stored_checksum" ]; then
    echo "✓ 파일 무결성 확인됨"
else
    echo "✗ 파일 무결성 검사 실패"
    echo "예상 체크섬: $stored_checksum"
    echo "실제 체크섬: $current_checksum"
fi
```

`cmp` 명령어는 파일 비교에 매우 유용한 리눅스 명령어입니다. 특히 스크립트에서 자동화된 파일 비교와 검증 작업을 수행할 때 필수적인 도구로 활용됩니다.
