---
layout : home
---

리눅스 커맨드라인 완벽입문 - 33.for
======================

# 흐름 제어 : for 루프

- for 루프는 반복 중에 작업 순서를 제공한다는 점에서 while과 until루프와 차이가 있다.
- for 루프는 for 명령어로 구현된다.
- 최신 bash 버전은 두 가지 형식의 for 문을 제공한다.

## for : 전통적인 쉘 형식

for 명령어의 원 문법은 다음과 같다.

```bash
for variable [in words]; do
				commands
done
```

`**vriable**`은 루프 수행 중에 증가되는 변수명이고, **`words`**는 선택적인 **`variable`**에 순차적으로 할당되는 항목 목록이다. 그리고 **`commands`**는 반복마다 실행되는 명령들이다.

위 코드는 커맨드 라인에서 아래와 같은 방식으로 동작한다.

```bash
$ for i in A B C D; do echo $i; done
A
B
C
D
```

이 예제에서 for 명령어에 네 개의 단어 목록(A, B, C, D)이 주어진다.
네 단어 목록으로 루프는 네 번 실행된다.
각 루프가 실행될 때 마다 단어가 변수 i에 할당된다.
루프 내에서 echo 명령어로 할당 내용을 보기 위해 i 값을 표시한다.
while과 until 루프처럼 done 키워드로 루프를 닫는다.

## for : C 언어 형식

bash의 최신 버전에는 C 언어에서 사용하는 형식과 닮은 for 명령 문법의 두 번째 형식이 추가되었다.

```bash
for (( expression1; expression2; expression3 )); do
							commands
done
```

expression1, expression2, expression3는 모두 산술식이고, commands는 루프의 각 반복마다 실행되는 명령들이다.

이 형식은 동작 측면에서 다음 구조와 동일하다.

```bash
(( expressin1 ))
while (( expression2 )); do
				 commands
					(( expression3 ))
done
```

expression1는 루프를 위한 초기 상태이고, expression2는 루프가 끝나는 시점을 결정하는 데 사용된다.
그리고 expression3는 루프의 각 반복 끝 부분에서 실행된다.

아래는 그 전형적인 예제이다.

```bash
#!/bin/bash

# simple_counter : demo of C style for command

for (( 1=0; i<5; i=i+1 )); do
				echo $i
done
```

실행 결과는 아래와 같다.

```bash
[me@linuxbox ~]$ simple_counter
0
1
2
3
4
```