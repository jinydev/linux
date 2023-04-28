---
layout: home
---

## 파일과 디렉토리 조작<br/>
<hr/>

- 파일이나 디렉토리를 다룰 때 가장 빈번하게 사용되는 명령어

    `cp` - 파일 및 디렉토리 복사

    `mv` - 파일 및 디렉토리 이동 그리고 이름 바꾸기

    `mkdir` - 디렉토리 새로 만들기

    `rm` - 파일 및 디렉토리 삭제

    `ln` - 하드 링크 또는 심볼릭 링크 만들기

    복잡한 파일 관리작업들은 커맨드라인 프로그램으로 하는 것이 더 쉬움

    ex) 어떤 디렉토리에 저장된 모든 html파일을 다른 디렉토리로 복사

    ```bash
    cp -u *.html destination
    ```

- 와일드카드
    
    파일명의 그룹을 지정할 수 있도록 특수한 문자들을 지원 글로빙이라고도 함 
    
    - `*` : 모든문자
        
        ex) `b*.txt` - b로 시작하되 .txt형식 파일
        
    - `?` :
        
        ex) `Data???` - Data로 시작하면서 뒤에 정확히 세개의 문자만 있는 파일
        
    - `[characters]` : characters 문자셋에 포함된 문자
        
        ex) `[abc]*` - a,b,c로 시작하는 모든 파일
        
    - `[!characters]` : characters 문자셋에 포함되지 않은 문자
        
        ex) `[![:digit:]]*` - 숫자가 포함되지 않은 모든 파일
        
    - `[[:class:]]` : 지정된 문자 클래스에 포함된 문자<br/><br/>
    *가장 많이 사용되는 문자 클래스*
    - `[:alnum:]` : 모든 알파벳과 숫자 문자
    - `[:alpha:]` : 모든 알파벳 문자
    - `[:digit:]` : 모든 숫자
    - `[:lower:]` : 모든 소문자
        
        ex) `[[:lower:123]` : 파일명이 소문자로 끝나거나 1, 2, 3 으로 끝나는 파일
        
    - `[:upper:]` : 모든 대문자
        
        ex) `[[:upper:]]*` : 대문자로 시작하는 모든 파일
        
- mkdir : 디렉토리 생성
    
    ```bash
    mkdir directory
    mkdir dir1
    mkdir dir1 dir2 dir3
    ```
    
- cp : 파일과 디렉터리를 복사
    
    ```bash
    cp item1 item2 
    -- item1을 iem2라는 파일 또는 디렉토리로 복사
    cp item ... 
    --다수의 파일을 복사
    
    cp --help
    ```
    
    `-a, —archive` 
    
    파일 및 디렉토리뿐만 아니라 소유자 및 권한 정보와 같은 속성까지 모두 복사한다. 반면, 일반적으로는 복사를 하는 사용자의 기본적인 성을 복사
    
    `-i, —interactive`
    
    기존 파일을 덮어쓰기 전에 확인 메시지를 보여주는 옵션이다. 이 옵션 없이 cp 명령어를 사용하면 확인 과정 없이 그대로 파일을 덮어쓰게 됨
    
    ex) cp -i filel file2 
    
    `-r, —recursive`
    
    디렉토리와 그 안의 내용까지 복사할 때 쓰는 옵션. 이 옵션(또는 -a 옵션)은 디렉토리를복사할 때 필요
    
    ex) cp -r dirl dir2
    
    dir1 디렉토리와 그 안에 있는 든 내용을 dir2 디렉토리로 복사. dir2 가 없으면 새로 생성될 것이고 dir1 디렉토리에 있는 모든 내용들이 복사
    
    `-u, —update`
    
    어떤 디렉토리에 있는 파일을 다른 디렉토리로 복사 , 그 디렉토리에는 없거나 최신 버전인 파일만을 복사하기 위해서 이 옵션을 사용
    
    `-v, —verbose`
    
    복사가 완료되었다는 메시지를 보여주는 옵션<br/><br/>
    
- mv : 파일 이동과 이름 변경
    
    `i, - -interactive` : 기존 파일을 덮어쓰기 전에 확인 메시지를 보여주는 옵션. 이 옵션 없이 mv 명령어률 사용하면 확인 없이 그대로 파일을 덮어쓰게 됨.
    
    ex) mv -i filel file2 : file2파일이 있다면 사용자에게 덮어쓰기 여부를 확인   
    `u, - -update` : 디렉토리에는 없거나 또는 최신 버전인 파일만을 이동하기 위해 사용   
    `v, - -verbose` : 이동이 완료되었다는 메시지를 보여주는 옵션<br/><br/>
    
- rm : 파일 및 디렉토리 삭제    
    4-9) rm 사용예제   
    `rm file1` : file1/ 파일을 완전히 삭제   
    `rm -i file1` : fiie1 파일을 삭제하기 전에 사용자 확인 메시지를 보여줌   
    `rm -r file1 dir1` : file1 파일과 dir1 디렉토리 및 하위 내용까지 모두 삭제함   
    `rm -rf file1 dir1` :  file1 과 dir1모두 다 삭제하되 file1 이나 dir1 이 존재하지 않더라도 rm 영령어가 실행됨<br/><br/>
- ln : 링크생성   
    `ln file1 Link` : **하드링크** 만들 때 사용하는 것   
    `ln -s item Link` : item 파일 또는 디렉토리에 **심볼릭 링크**를 생성<br/><br/>
    
- 하드링크는 링크를 생성하는 기존 유닉스 방식
    
    - 파일시스템 외부에는 파일을 참조할 수 없음. 
    - 하드 링크는 디스크 파티션에 있는 파일이 아니면 조작할 수 없음.
    - 하드 링크는 디렉토리를 참조할 수 없음.
    - 하드 링크는 파일 그 자체만으로 구분해내기 어려움.
    - 하드 링크를 포함한 디렉토리 목록은 해당 링크가 가리키고 있는 것이 무엇인지 보여 주지 않음.
    - 하드 링크가 삭제될 때, 링크도 함께 사라지지만 파일 내용은 그 파일의 모든 링크가 삭제될 때까지 계속 남아 있음   
    (즉, 파일에 할당된 공간이 그대로 남게 된다는 것임)
    <br/><br/>
- 심볼릭 링크는 하드링크의 한계를 극복하기 위해 탄생
    - 윈도우 바로가기 기능과 유사
    - 원본파일의 정보가 포함되어 있지 않고, 원본파일의 위치정보만 포함
    - 참조될 파일이나 디렉토리를 가리키는 텍스트 포인터가 포함된 특수한 파일을 생성   
    <br/><br/>
    
-> 하드링크는 원본 파일이 사라지더라도 데이터만 살아 있다면 원본 파일에 접근이 가능하고, 심볼릭링크는 원본 파일이 사라지면 해당 데이터에 접근할 수 없음.
- 디렉토리 생성
    ```bash
    cd 
    mkdir playground
    cd playground
    mkdir dir1 dir2
    ```
    
- 파일복사
    ```bash
    cp /etc/passwd
    ls -l
    cp -v /etc/passwd
    cp -i /etc/passwd
    ```

- 파일이동 및 이름변경
    ```bash
    mv passwd fun
    mv fun dir1
    mv dir/fun dir2
    mv dir2/fun
    mv fun dir1
    mv dir1 dir2
    ls -l dir2
    ls -l dir2/dir1
    mv dir2/dir1
    mv dir1/fun
    ```

- 하드링크 생성
    ```bash
    ln fun fun-hard
    ln fun dir1/fun-hard
    ln fun dir2/fun-hard

    ls -l
    ls -li
    ```

- 심볼릭링크 생성
    ```bash
    ln -s fun fun-sym
    ln -s ../fun dir1/fun-sym
    ln -s ../fun dir2/fun-sym
    
    ls -l dir1
    ln -s /home/me/playground/fun dirl/fun-sym
    ln -s dirl dirl-sym
    ls -l
    ```
- 파일 및 디렉토리 삭제
    ```bash
    rm fun-hard
    ls -l
    rm -i fun
    ls-l
    ```
- 깨진 링크 사용하기
    ```bash
    less fun-sym
    ```
- 심볼릭 링크를 삭제해서 정리
    ```bash
    rm fun-sym
    ls -l
    cd
    rm -r playground
    ```