---
layout: home
---

# Bash 스크립트: 흐름 제어 (while, until 루프)

터미널에서 수십 번 반복해야 하는 단순 작업을 자동화할 때 쉘 스크립트의 **반복문(Loop)** 기능이 핵심적인 역할을 수행합니다. Bash 스크립트에서 가장 널리 쓰이는 `while`과 `until` 루프의 문법과 원리를 정리합니다.

## 1. `while` 루프
프로그래밍에서 가장 전통적인 방식입니다. **"주어진 조건식이 참(True)인 동안 계속해서"** 블록 내부의 명령어를 반복 실행합니다. 조건식이 거짓(False)이 되는 순간 루프를 종료합니다.

### 📝 While 문법 예시
전통적인 Bash 방식의 카운트다운 스크립트입니다.
```bash
count=1

# count가 5보다 작거나 같은(-le) '동안' 계속 반복합니다.
while [ $count -le 5 ]
do
    echo "현재 카운트: $count"
    count=$((count + 1))  # count 값을 1씩 증가시킵니다.
done

echo "Finished!"
```

## 2. `until` 루프
`while` 루프와 정반대로 동작합니다. **"주어진 조건식이 참(True)이 될 때까지 (=조건식이 거짓인 동안)"** 명령을 계속 실행합니다. 조건문이 0(참)의 상태 코드를 반환하는 순간 루프가 그 즉시 종료됩니다.

특정 프로세스가 죽을 때까지 기다리거나, 네트워크 핑(Ping)이 응답할 때까지 계속 재시도하는 스크립트를 짤 때 매우 유용합니다.

### 📝 Until 문법 예시
```bash
count=1

# count가 5보다 커지는(-gt) '순간까지' (즉, 5를 초과하기 전까지) 반복합니다.
until [ $count -gt 5 ]
do
    echo "현재 카운트: $count"
    count=$((count + 1))
done

echo "Finished!"
```

## 3. 무한 루프와 탈출 제어문 (break / continue)
때로는 의도적으로 영원히 반복되는 무한 루프를 만들어두고, 내부에서 특정 사용자의 입력값을 받아 루프를 빠져나오게 설계해야 할 때가 있습니다.

* **`break`:** 무한 반복의 고리를 완전히 끊어버리고 루프 블록을 **완전히 탈출**합니다.
* **`continue`:** 루프를 탈출하지는 않지만, 자신 아래에 있는 코드들의 실행을 전부 건너뛰고(Skip) **다음 번 반복 사이클의 맨 처음으로 다시 올라갑니다.**

### 📝 탈출 제어문 예제
```bash
while true
do
    echo "1: 시스템 가동 시간 (uptime)"
    echo "2: 디스크 용량 (df -h)"
    echo "0: 종료"
    read -p "확인할 메뉴를 입력하세요: " menu

    if [ "$menu" = "0" ]; then
        echo "프로그램을 종료합니다."
        break  # 0이 입력되면 무한 루프를 탈출합니다.
    elif [ "$menu" = "1" ]; then
        uptime
        continue # 아래 코드를 건너뛰고 다시 메뉴 처음으로 돌아갑니다.
    elif [ "$menu" = "2" ]; then
        df -h
        continue
    else
        echo "잘못된 입력입니다."
    fi
done
```