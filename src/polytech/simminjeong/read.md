---
layout: home
---


# 키보드 입력 읽기

`대화식`모드 : 사용자와 프로그램 사이에 상호 작용하는 것

## read - 표준 입력에서 값 읽어오기
- 쉘의 내장 명령어로 표준 입력으로 들어온 내용을 한 줄씩 읽어올 때 사용
- `키보드 입력을 읽어올 때나 리다이렉션을 적용하여 파일의 데이터를 읽어올 때 사용`
  
    ```
    read [-options] [variable...]
    ```


    ### **read optinos**

    |옵션| 설명|
    |---|---|
    |-a array| 입력값을 array에 할당한다. 인덱스는 0으로 시작함.|
    |-d deLimiter| deLimiter 문자열에서 개행 문자가 아닌 가장 첫 번째 문자를 입력의 끝을 가리키는 데 사용한다. |
    |-e| Readline을 이용하여 입력을 관리한다. 이것은 커멘드라인과 같은 방식으로 입력 내용을 편집할 수 있게해준다 |
    |-n num |입력된 행 전체 대신 num 수의 문자만을 읽어온다 |
    |-p prompt |prompt 문자열을 이용하여 입력을 워한 프롬포트를 띄운다 |
    |-r |Raw 모드. 백슬래시 기호를 이스케이프로 해석하지 않는다 |
    |-s |묵음 모드. 문자를 입력할 때마다 해당 문자를 다시 표시하지 않는다. <br> 이것은 비밀번호를 입력할 때나 중요한 정보를 입력할 때 유용하다. |
    |-t seconds |타임아웃 일정 시간(초) 후에 입력을 종료한다. <br> read 명령은 입력 시간이 초과되면 이 아닌 종료 상태 값을반환한다 |
    |-u fd |표준 입력 대신 fd 파일 디스크립터를 입력으로 사용한다 |
    
    
    ### **read variable**
    - 입력 값을 할당할 변수명을 하나 이상 입력
    - 변수명을 입력하지 않으면 쉘 변수 REPLY가 데이터를 갖게 됨(기본값)

<br>

### 1. 기본적으로 read 명령은 표준 입력의 필드를 특정 변수에 할당할 수 있음.
```
#! / bin/bash 
# read-integer: evaluate the value of an integer. 
echo -n "Please enter an integer -> " 
read int

if [[ "$int" =~ " -?[0-9]+$ ]]; then 
        if [ $int -eq 0 ]; then 
                echo "$int is zero. " 
        else 
                if [ $int -lt 0 ] ; then 
                        echo "$int is negative ." 
                else 
                        echo "$int is positive. " 
                fi 

                if [ $((int % 2)) -eq 0 ]; then 
                        echo "$int is even." 
                else 
                        echo "$int is odd." 
                fi 
        fi 
else 
        echo "Input value is not an integer." >&2 
        exit 1 
fi
```
```
[mjsim@mjsim-virtual ~]$ read-integer 
Please enter an integer -> 5 
5 is positive. 
5 is odd.
``` 

<br>

### 2. read 명령은 여러번수에 값을 할당할 수 있음. 
- read 명령은 예상했던 수보다 적게 값을 입력 받으면, `나머지 변수들을 빈 값으로 채운다.` 
- 반면에 더 많은수의 값을 입력 받은 경우에는, `마지막 수가 나머지 모든값을 다 할당받는다.` 


```
# ! /bin/bash 
# read-multiple: read multiple values from keyboard 

echo -n "Enter one or more values > " 

read varl var2 var3 var4 vars 

echo "varl = '$varl'" 
echo "var2 = '$var2'" 
echo "var3 = '$var3'" 
echo "var4 = '$var4'" 
echo "vars = '$var5'" 
```
    
```
[mjsim@mjsim-virtual ~]$ read-multiple 
Enter one or more values > a b c d e 
varl = 'a' 
var2 = 'b' 
var3 = 'c' 
var4 = 'd' 
vars = 'e' 

[mjsim@mjsim-virtual ~]$ read-multiple 
Enter one or more values > a 
varl = 'a' 
var2 = ' ' 
var3 = ' ' 
var4 = ' ' 
vars = ' ' 

[mjsim@mjsim-virtual ~]$ read-multiple 
Enter one or more values > a b c d e f g 
varl = 'a' 
var2 = ' b' 
var3 = 'c' 
var4 = 'd ' 
vars = 'e f g'
```


### 3. read 명령어 다음에 변수가 없다면 쉘 변수인 REPLY에 모든 입력 값이 할당될 것.
```
#! / bin/ bash 
# read-single: read multiple values into default variable 

echo - n "Enter one or more values > " 
read 

echo "REPLY = '$REPLY"' 
```
```
[mjsim@mjsim-virtual ~]$ read-single 
Enter one or more values > a b c d 
REPLY = ' a b c d ' 
```

## 옵션

### 1. -p 옵션으로 프롬프트 문자열을 생성할 수 있다.
```
# ! /bin/bash 
# read-single: read multiple values into default variable

read -p "Enter one or more values > " 
echo "REPLY = '$REPLY"' 
```

### 2. -t 옵션과 -s 옵션으로 "비밀" 입력 기능과 입력 간이 초과되면 종료되는 기능을 추가할수 있다. 
- 사용자에게 비밀번호를 입력하라는 프롬프트를 띄우고 10 초 동안 입력을 기다린다. 
- 그 시간 동안 입력이 없으면 오류 메시지를 띄우고 종료된다.
- -s 옵션을 사용하였기 때문에 비밀번호는 입력될 때마다 다시 표시되지 않는다. 

```
#!/bin/bash 
# read-secret: input a secret passphrase 

if read -t 10 -sp "Enter secret passphrase > " secret_pass; then 
        echo -e "\ nSecret passphrase = '$secret_pass'" 
else 
        echo -e "\ninput timed out " >&2 
        exit 1 
fi 
```

## IFS로 입력 필드 구분하기
- 입력행에서 스페이스로 분리된 단어들이 read에 의해 별도의 변수에 할당
- 이러한 방식은 IFS (입력 필드 구분자)라고 하는 쉘 변수에 의해 설정
- IFS 의 기본 값은 스페이스, 탭, 개행 문자를 포함하고 었고 각각 별도의 항목으로 구분

### 입력 필드 구분자를 제어하기 IFS 의 값을 조절할 수 였다.
- / erc/passwd 파일은 필드 구분자로 콜론 기호를 사용하여 데이터를 포함
- IFS 을 세미콜론으로 함으로써 read를 사용하여 /etc/passwd 파일 내용을 입력 받을 수 있고 각기 다른 변수에 각 항목들을 구분 할 수 있음.
  
```
#!/bin/ bash 
# read-ifs: read fields from a file 

FILE=/etc/passwd 
read -p "Enter a username > " user_name 
file_info=$(grep "A$user_name : " $FILE) (1) 

if [ -n "$file_info" ]; then 
        IFS=" : " read user pw uid gid name home shell <<< "$file_info" (2) 
        echo "User = '$user'" 
        echo "UID = ' $uid ' " 
        echo "GID = '$gid'" 
        echo "Full Name = '$name'" 
        echo "Home Dir. = '$home'" 
        echo "Shell = ' $shell' " 
else 
        echo "No such user '$user_name'" >&2 
        exit 1 
fi
```
사용자에게 시스템의 사용자 계정명을 입력하라는 메시시를 띄우고 /erc/passwd 파일에서 해당 사용자 정보를 찾아 각 필드들을 표시 <br>

### (1) 
  1. grep 명령어의 결과 값을 file_info 라는 변수에 할당. 
  2. grep에 사용한 정규 표현식을 통해 입력된 사용자명과 일치하는 내용을 /etc/passwd 파일에서 찾음.
### (2) 

 1. 변수할당문
   
    ```
    OLD_IFS="$IFS " 
    IFS=":" 
    read user pw uid gid name home shell «< "$file_info" 
    IF5= "$0LD_IFS " 
    ```
    - IFS 을 콜론 문자로 변경
    - IFS 값을 저장하고 새로운 값을 할당하여 read 명령을 실행한 뒤 IFS의 값을 원래 값으로 복구
  
 2. read 명령과 그 인자로 입력된 변수명
    - read 명령 통해 $file_info 받아옴
 3. 리다이렉션 연산자(<<<) : <<< 연산자는 here 문자열
    - READ 명령어는 파이프라인(|)과 함께 사용할 수 없다 
    - 파이프라인 : 하나의 명령어가 실행되는 도중 다른 명령어 실행을 시작하여 동시에 여러개의 명령어를 실행하는 기법

## 입력 값 검증
- 정규표현식을 사용하여 입력값을 검증할 수 있음

## 메뉴
- 사용자에게 선택지를 주어 case문 처럼 사용 가능하다.