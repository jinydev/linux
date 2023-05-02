# 위치 매개변수

### 커맨드라인 항목 접근
- 쉘은 `위치 매개변수`라는 변수의 집합을 제공한다. 그것은 커맨드라인 명령의 개별 요소들을 가지고 있으며 변수들은 0부터 9까지 이름 붙인다.

### 인자 수 확인
- 쉘은 커맨드라인의 인자 수를 넘겨주는 변수 `$#`을 제공한다.
```
$ posit-param a b c d

Number of arguments: 4
$0 = /home/me/bin/posit-param
$1 = a
$2 = b
$3 = c
$4 = d
$5 =
...
$9 = 
```

### shift - 다수의 인자에 접근
- 수많은 인자가 주어진다면?
```
$ posit-param *

Number of arguments: 82
$0 = /home/me/bin/posit-param
$1 = addresses.ldif
$2 = bin
$3 = bookmarks.html
$4 = debian-500-i386-netinst.iso
$5 = debian-500-i386-netinst.jigdo
$6 = debian-500-i386-netinst.template
$7 = debian-cd_info.tar.gz
$8 = Desktop
$9 = dirlist-bin.txt
```
-> 이 예제에서 와일드카드 *은 82개의 인자들로 확장된다. 이를 처리하기 위해 shift 명령어는 실행될 때마다 각 매개변수가 `하나씩 다음으로 이동`하게끔 한다. shift를 이용하면 단 하나의 매개변수를 가져오는 것도 가능하다.
```
# !/bin/bash

# posit-param2: script to display all arguments

count=1
while [[ $# -gt 0 ]]; do
    echo "Argument $count = $1"
    count=$((count + 1))
    shift
done
```
-> shift가 실행될 때 마다 $#의 값은 1씩 감소한다. <br>
-> posit-params2는 남은 인자 수를 확인하고 인자가 남는 한 계속되는 루프를 만들고, 현재 인자를 표시한 뒤 처리된 인자 수를 세기 위해 루프가 반복할 때 마다 변수 count를 증가시킨다. 마지막으로 shift는 다음 인자를 $1로 불러온다.
```
posit-param2 a b c d 
Argument 1 = a
Argument 2 = b
Argument 3 = c
Argument 4 = d
```

### 쉘 함수에서 위치 매개변수 사용
- 인자를 전달하기 위해 쉘 스크립트에 위치 매개변수를 사용했던 것처럼 쉘 함수에 인자를 전달할 수 있다. 
```
file_info() {
    #file_info: function to display file information

    if [[ -e $1 ]]; then
        echo -e "\nFile Type:"
        file $1
        echo -e "\nFile Status:"
        stat $1
    else
        echo "$FUNCNAME: usage: $FUNCNAME file" >&2
        return 1
    fi
}
```
-> 쉘 함수 file_info를 포함한 스크립트가 파일명 인자와 함께 함수를 호출하면, 그 인자는 함수에 전달된다.
-> 이 기능으로 우리는 스크립트뿐만 아니라 .bashrc 파일에서도 사용할 수 있는 유용한 쉘 함수를 작성할 수 있다.

### 특수 매개변수
|매개변수|설명|
|---|---|
|$*|항목 1부터 시작하여 위치 매개변수 목록으로 확장된다. 이것을 쌍 따옴표로 둘러싸면 쌍 따옴표 내의 문자열 모두가 위치 매개변수로 확장되고 각각 IFS 쉘 변수의 첫 번째 문자에 의해 구분된다.(default : space)|
|$@|항목 1부터 시작하여 위치 매개변수 목록으로 확장된다. 이것을 쌍 따옴표로 둘러싸면, 각 위치 매개변수는 쌍 따옴표로 구분된 단어로 확장된다.|


### 응용 프로그램
- 출력 파일: 프로그램 출력을 저장할 파일명을 지정하기 위한 옵션 추가 (-f file or --file file)
- 대화식 모드: 출력 파일명을 사용자에게 표시하고 그 파일의 존재 여부를 확인한다. 만약 존재한다면 사용자에세 해당 파일을 덮어쓰기 전에 물어본다. (-i or --interactive)
```
// 커맨드라인 처리를 구현하기 위해 필요한 코드
usage() {
    echo "$PROGNAME: usage: $PROGNAME [-f file | -i]"
    return
}

# process command line options
interactibe=
filename=

while [[ -n $1 ]]; do
    case $1 in
        -f | --file)        shift
                            filename=$1
                            ;;
        -i | --interactive) interactive=1
                            ;;
        -h | --help         usage
                            exit
                            ;;
        *)                  usage >$2
                            exit 1
                            ;;
        esac
        shift
done
```
```
// 대화식 모드 구현하는 코드
# interactive mode

if [[ -n $interactive ]]; then
    while true; do
            read -p "Enter name of output file: " filename
            if [[ -e $filename ]]; then
                read -p "'$filename' exists. Overwrite? [y/n/q] >"
                case $REPLY in
                    Y/y)    break
                            ;;
                    Q/q)    echo "Program terminate."
                            exit
                            ;;
                    *)      continue
                            ;;
                esac
            elif [[ -z $filename ]]; then
                continue
            else
                break
            fi
    done
fi
```