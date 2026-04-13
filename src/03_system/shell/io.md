---
layout: home
---

# 셀 입출력

## echo
---
`echo`명령은 화면에 텍스트를 출력하는 명령입니다. 

### 메시지 출력
기본적으로 텍스트 메시지를 출력합니다.

```bash
echo 옵션 메시지
```

* `-n` 메시지 출력후 newline 문자를 추가하지 않는다.
```bash
hojin@hojin3:~/bin$ echo "your name:"
your name:
hojin@hojin3:~/bin$ echo -n "your name:"
your name:hojin@hojin3:~/bin$   # 줄바꿈을 하지 않습니다.
```

* `-e` backslash escapes 문자를 해석하여 특별한 의미를 지정한다.
    * `\t` tab키
    * `\n` 줄 바꿈
    * `\a` alert bell

```bash
hojin@hojin3:~/bin$ echo -e "hello \nLinux World" # \n 줄바꿈을 인식합니다.
hello
Linux World
```

### 변수출력
echo 명령은 셀의 변수의 내용을 출력합니다.

```bash
echo $변수
```

## Read
---
셀에서 사용자 입력을 받을 수 있습니다. 

### 변수에 입력받기
입력을 받기 위해서는 변수를 같이 사용해야 합니다.

```bash
read 옵션 변수명
```

### 실습
```bash
read score
```
입력한 값이 `scroe`변수에 저장합니다. 만일, 이전에 `scroe`변수가 존재한다면, 덥어쓰게 됩니다.

2개의 입력 값도 받을 수 있습니다.
```bash
read fname lname
```
2개의 값을 입력받습니다. 2개의 값의 구분은 공백으로 구분합니다.
만일 입력 변수보다 더 많은 데이터를 입력할 경우, 나머지 모두를 마지막 변수에 담기게 됩니다.

### 옵션
옵션을 추가하여 입력동작을 더 세밀하게 제어할 수 있습니다.

* `-n` 지정한 문자수 많큼 입력 받는다
```bash
read -n8 password
```
패스워드로 8자리만 입력 받습니다.

* `-t` 지정된 시간안에 입력 받는다
```bash
read -t10 -n8 password
```
입력시간을 10초 이내로 한다.

* `-s` silent mode로 입력하는 글자가 보이지 않는다.
```bash
read -t10 -n8 -s password
```
입력할때는 화면에 보이지 않는다.

> read 명령에서 변수를 생략하게 되면 `REPLY` 변수에 채워진다.



