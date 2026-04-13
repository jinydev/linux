---
layout: home
---

# 숫자 계산
`+`, `-`, `*`, `/` 등으로 연산하려면 `let`, `expr` 키워드 사용

## let
---
### 명령타입
expr은 산술연산을 위한 셀의 내부명령 입니다.
```bash
hojin@hojin3:~/bin$ type let
let is a shell builtin
```
> let은 bash셀의 내부 명령문으로 셀의 타입에 종속됩니다.
> let은 외부의 실행파일인 expr보다, 내부의 명령으로 실행 속도가 더 빠르다는 장점이 있습니다.

### 연산유형
정수형 산술연산, bit 연산(`<<`,`>>`,`&`,`|`), 논리연산(`&&`,`||`), 단항연산(`++`,`+=`,`-=`)

```bash
hojin@hojin3:~$ let sum=5+5
hojin@hojin3:~$ echo $sum
10
```

### 연산실습
```bash
let sum=x+5
let x++
let x+=1
$((sum=x+5))
$((x++))
$((x-=1))
```


## expr
---

### 명령타입
expr 명령은 산술연산을 위한 외부의 실행파일 입니다.
```bash
hojin@hojin3:~/bin$ type expr
expr is hashed (/usr/bin/expr)
```

### 연산유형
정수형 산술연산(+,-,*,/,%), 논리연산(|,&),관계연산(=,!=,>,>=,<,<=)

### 연산실습
숫자를 취급하여 계산하며 각 단어를 띄어쓰기해야 함  

```bash
expr 10 + 5
expr 10 - 5
expr 5 '*' 2
expr 25 `/` 5
expr 25 % 4

x=5
expr $x > 4
expr $x = 8
```


### nesting 연산
수식을 백틱(```)으로 묶어서 작성합니다.

```bash
sum=`expr $x + 10`
```

### 괄호 삽입

수식에 괄호를 사용하려면 그 앞에 반드시 \(\)를 넣어야 함.
+, -, /와 달리 *도 예외적으로 앞에 \(\)를 넣어야 함.
```bash
num1=100
num4=`expr \( $num1 + 200 \) / 10 \* 2`
echo num4
```







