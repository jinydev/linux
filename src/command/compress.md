---
layout: home
title: "compress - 리눅스 파일 압축 명령어 - 개발자를 위한 리눅스"
description: "compress 명령어의 사용법과 옵션을 알아보세요. 파일 압축, 압축 해제, 압축률 조정, Lempel-Ziv 압축 방법을 포함한 포괄적인 가이드입니다."
keywords: "compress, 압축, linux, 명령어, 파일압축, Lempel-Ziv, 리눅스"
author: "HojinLee"
og_title: "compress - 리눅스 파일 압축 명령어 - 개발자를 위한 리눅스"
og_description: "compress 명령어의 사용법과 옵션을 알아보세요. 파일 압축, 압축 해제, 압축률 조정, Lempel-Ziv 압축 방법을 포함한 포괄적인 가이드입니다."
og_type: "article"
twitter_card: "summary"
---

# compress 명령어

`compress` 명령어는 리눅스 시스템에서 파일을 압축하는 유틸리티입니다. 이 명령어는 Lempel-Ziv 압축 알고리즘을 사용하여 파일을 압축하며, 압축된 파일은 `.Z` 확장자를 가집니다.

## 기본 사용법

### 파일 압축

가장 기본적인 사용법으로, 파일을 압축합니다.

```console
hojin@DESKTOP-11LMH3B:~$ compress example.txt
hojin@DESKTOP-11LMH3B:~$ ls -la example.txt*
-rw-r--r-- 1 hojin hojin 2048 May 21 15:30 example.txt.Z
```

압축이 완료되면 원본 파일은 삭제되고 `.Z` 확장자가 붙은 압축 파일이 생성됩니다.

### 여러 파일 압축

여러 파일을 동시에 압축할 수 있습니다.

```console
hojin@DESKTOP-11LMH3B:~$ compress file1.txt file2.txt file3.txt
hojin@DESKTOP-11LMH3B:~$ ls -la *.Z
-rw-r--r-- 1 hojin hojin 1024 May 21 15:30 file1.txt.Z
-rw-r--r-- 1 hojin hojin 1536 May 21 15:30 file2.txt.Z
-rw-r--r-- 1 hojin hojin 2048 May 21 15:30 file3.txt.Z
```

## 주요 옵션

### `-v` 옵션
압축 진행 상황을 상세히 출력합니다.

```console
hojin@DESKTOP-11LMH3B:~$ compress -v example.txt
example.txt: -- replaced with example.txt.Z Compression: 45.2%
```

### `-f` 옵션
기존 압축 파일이 있어도 강제로 덮어씁니다.

```console
hojin@DESKTOP-11LMH3B:~$ compress -f example.txt
```

### `-c` 옵션
원본 파일을 유지하고 압축 결과를 표준 출력으로 출력합니다.

```console
hojin@DESKTOP-11LMH3B:~$ compress -c example.txt > example.txt.Z
hojin@DESKTOP-11LMH3B:~$ ls -la example.txt*
-rw-r--r-- 1 hojin hojin 4096 May 21 15:30 example.txt
-rw-r--r-- 1 hojin hojin 2048 May 21 15:30 example.txt.Z
```

### `-b`션
압축 비트 수를 지정합니다 (9-16, 기본값: 16).

```console
hojin@DESKTOP-11LMH3B:~$ compress -b 12 example.txt
```

### `-d` 옵션
압축 파일을 해제합니다 (uncompress와 동일).

```console
hojin@DESKTOP-11LMH3B:~$ compress -d example.txt.Z
hojin@DESKTOP-11LMH3B:~$ ls -la example.txt*
-rw-r--r-- 1 hojin hojin 4096 May 21 15:30 example.txt
```

## 압축 해제

### uncompress 명령어 사용

압축된 파일을 해제할 때는 `uncompress` 명령어를 사용합니다.

```console
hojin@DESKTOP-11LMH3B:~$ uncompress example.txt.Z
hojin@DESKTOP-11LMH3B:~$ ls -la example.txt*
-rw-r--r-- 1 hojin hojin 4096 May 21 15:30 example.txt
```

### compress -d 사용

`compress` 명령어에 `-d` 옵션을 사용하여 해제할 수도 있습니다.

```console
hojin@DESKTOP-11LMH3B:~$ compress -d example.txt.Z
```

## 실용적인 활용

### 스크립트에서 활용

`compress` 명령어는 스크립트에서 파일 압축을 자동화할 때 유용합니다.

```bash
#!/bin/bash
# 파일 압축 스크립트
source_dir="/source"
backup_dir="/backup"

echo "파일 압축 시작..."

# 소스 디렉터리의 모든 텍스트 파일 압축
for file in "$source_dir"/*.txt; do
    if [ -f "$file" ]; then
        echo "압축 중: $(basename "$file")"
        compress -v "$file"
        
        # 압축된 파일을 백업 디렉터리로 이동
        compressed_file="${file}.Z"
        if [ -f "$compressed_file" ]; then
            mv "$compressed_file" "$backup_dir/"
            echo "백업 완료: $(basename "$compressed_file")"
        fi
    fi
done

echo "압축 작업이 완료되었습니다."
```

### 백업 시스템

정기적인 백업 시스템에서 파일을 압축하여 저장 공간을 절약할 수 있습니다.

```bash
#!/bin/bash
# 자동 백업 스크립트
backup_dir="/backup/$(date +%Y%m%d)"
source_dir="/data"

mkdir -p "$backup_dir"

echo "백업 시작: $(date)"

# 소스 디렉터리의 모든 파일을 압축하여 백업
find "$source_dir" -type f -name "*.txt" -o -name "*.log" | while read -r file; do
    relative_path="${file#$source_dir/}"
    backup_path="$backup_dir/$(dirname "$relative_path")"
    
    # 백업 디렉터리 생성
    mkdir -p "$backup_path"
    
    # 파일 압축
    compress -c "$file" > "$backup_path/$(basename "$file").Z"
    echo "백업 완료: $relative_path"
done

echo "백업 완료: $(date)"
```

### 로그 파일 관리

로그 파일을 압축하여 저장 공간을 절약할 수 있습니다.

```bash
#!/bin/bash
# 로그 파일 압축 스크립트
log_dir="/var/log"
compress_after_days=30

echo "로그 파일 압축 시작..."

# 30일 이상 된 로그 파일 찾아서 압축
find "$log_dir" -name "*.log" -type f -mtime +$compress_after_days | while read -r log_file; do
    if [ ! -f "${log_file}.Z" ]; then
        echo "압축 중: $(basename "$log_file")"
        compress -v "$log_file"
    fi
done

echo "로그 파일 압축 완료."
```

## 고급 사용법

### 압축률 최적화

압축률을 조정하여 압축 시간과 파일 크기의 균형을 맞출 수 있습니다.

```bash
#!/bin/bash
# 압축률 최적화 스크립트
for file in *.txt; do
    if [ -f "$file" ]; then
        echo "파일: $file"
        
        # 기본 압축 (16비트)
        compress -v "$file"
        size_16=$(stat -c%s "${file}.Z")
        
        # 12비트 압축
        compress -b 12 -v "$file"
        size_12=$(stat -c%s "${file}.Z")
        
        echo "16비트 압축: ${size_16} 바이트"
        echo "12비트 압축: ${size_12} 바이트"
        echo "---"
    fi
done
```

### 조건부 압축

파일 크기가 특정 크기 이상일 때만 압축하는 스크립트입니다.

```bash
#!/bin/bash
# 조건부 압축 스크립트
min_size=1048576  # 1MB

for file in *; do
    if [ -f "$file" ] && [ ! -f "${file}.Z" ]; then
        file_size=$(stat -c%s "$file")
        
        if [ "$file_size" -gt "$min_size" ]; then
            echo "대용량 파일 압축: $file ($(numfmt --to=iec $file_size))"
            compress -v "$file"
        else
            echo "작은 파일 스킵: $file ($(numfmt --to=iec $file_size))"
        fi
    fi
done
```

### 압축 파일 검증

압축 파일의 무결성을 검증하는 스크립트입니다.

```bash
#!/bin/bash
# 압축 파일 검증 스크립트
for compressed_file in *.Z; do
    if [ -f "$compressed_file" ]; then
        echo "검증 중: $compressed_file"
        
        # 압축 파일 테스트
        if compress -t "$compressed_file" 2>/dev/null; then
            echo "✓ $compressed_file: 정상"
        else
            echo "✗ $compressed_file: 손상됨"
        fi
    fi
done
```

## 문제 해결

### 압축 파일 손상

압축 파일이 손상된 경우 복구를 시도할 수 있습니다.

```bash
#!/bin/bash
# 손상된 압축 파일 처리
for compressed_file in *.Z; do
    if [ -f "$compressed_file" ]; then
        if ! compress -t "$compressed_file" 2>/dev/null; then
            echo "손상된 파일 발견: $compressed_file"
            
            # 백업 파일이 있는지 확인
            backup_file="${compressed_file}.backup"
            if [ -f "$backup_file" ]; then
                echo "백업 파일에서 복구 시도..."
                cp "$backup_file" "$compressed_file"
            else
                echo "백업 파일이 없습니다. 복구 불가능."
            fi
        fi
    fi
done
```

### 디스크 공간 부족

압축 중 디스크 공간이 부족한 경우를 처리합니다.

```bash
#!/bin/bash
# 디스크 공간 확인 후 압축
min_space=104857600  # 100MB

for file in *.txt; do
    if [ -f "$file" ]; then
        # 사용 가능한 디스크 공간 확인
        available_space=$(df -B1 . | awk 'NR==2 {print $4}')
        
        if [ "$available_space" -gt "$min_space" ]; then
            echo "압축 중: $file"
            compress -v "$file"
        else
            echo "디스크 공간 부족. 압축을 중단합니다."
            exit 1
        fi
    fi
done
```

### 권한 문제

파일에 대한 압축 권한이 없는 경우를 처리합니다.

```bash
#!/bin/bash
# 권한 확인 후 압축
for file in *; do
    if [ -f "$file" ] && [ ! -f "${file}.Z" ]; then
        if [ -r "$file" ] && [ -w "$(dirname "$file")" ]; then
            echo "압축 중: $file"
            compress -v "$file"
        else
            echo "권한 없음: $file"
        fi
    fi
done
```

## 활용 예제

### 자동 정리 스크립트

오래된 파일을 자동으로 압축하여 정리하는 스크립트입니다.

```bash
#!/bin/bash
# 자동 정리 스크립트
source_dir="/home/user/documents"
days_old=90

echo "오래된 파일 정리 시작..."

find "$source_dir" -type f -mtime +$days_old ! -name "*.Z" | while read -r old_file; do
    echo "압축 중: $old_file"
    compress -v "$old_file"
    
    # 압축 성공 시 원본 파일 삭제 확인
    if [ -f "${old_file}.Z" ]; then
        echo "압축 완료. 원본 파일을 삭제합니다."
        rm "$old_file"
    fi
done

echo "정리 작업이 완료되었습니다."
```

### 압축 파일 모니터링

압축 파일의 상태를 모니터링하는 스크립트입니다.

```bash
#!/bin/bash
# 압축 파일 모니터링 스크립트
backup_dir="/backup"

echo "=== 압축 파일 상태 모니터링 ==="
echo "시간: $(date)"
echo ""

# 압축 파일 통계
total_files=$(find "$backup_dir" -name "*.Z" | wc -l)
total_size=$(find "$backup_dir" -name "*.Z" -exec stat -c%s {} + | awk '{sum+=$1} END {print sum}')
compressed_size=$(du -sb "$backup_dir" 2>/dev/null | cut -f1)

echo "총 압축 파일 수: $total_files"
echo "압축된 파일 총 크기: $(numfmt --to=iec $total_size)"
echo "실제 디스크 사용량: $(numfmt --to=iec $compressed_size)"

# 압축률 계산
if [ "$total_size" -gt 0 ]; then
    compression_ratio=$(echo "scale=2; $compressed_size * 100 / $total_size" | bc)
    echo "평균 압축률: ${compression_ratio}%"
fi
```

### 대화형 압축 도구

사용자와 상호작용하며 파일을 압축하는 스크립트입니다.

```bash
#!/bin/bash
# 대화형 압축 도구
echo "파일 압축 도구"
echo "=============="

read -p "압축할 파일 또는 디렉터리를 입력하세요: " target

if [ -e "$target" ]; then
    if [ -f "$target" ]; then
        echo "파일 압축 중: $target"
        compress -v "$target"
    elif [ -d "$target" ]; then
        echo "디렉터리 내 파일들을 압축합니다."
        find "$target" -type f ! -name "*.Z" | while read -r file; do
            echo "압축 중: $file"
            compress -v "$file"
        done
    fi
else
    echo "오류: '$target' 파일 또는 디렉터리를 찾을 수 없습니다."
fi
```

`compress` 명령어는 리눅스에서 파일 압축을 위한 전통적인 도구입니다. 특히 스크립트에서 자동화된 파일 압축과 백업 작업을 수행할 때 매우 유용합니다.
