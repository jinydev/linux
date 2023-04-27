---
layout: home
---

# 1. locate - 손쉽게 파일 찾기

: locate 프로그램은 경로명에 대한 빠른 데이터베이스 검색을 수행하고 주어진 조건에 일치하는 모든 이름을 출력한다.

### 예시

```sql
[me@linuxbox ~]$ locate bin/zip
```

> /usr/bin/zip
/usr/ bin/zipcloak
/ usr/ bin/zipgrep
/usr/bin/zipinfo
/ usr/bin/zipnote
/ usr/ bin/z ipsplit
> 

```sql
[me@linuxbox ~]$ locate zip I grep bin
```

> / bin/ bunzip2
/bin/bzip2
/ bin/bzip2recover
/ bin/ gunzip
/ bin/gzip
/usr/bin/funzip
/usr/ bin/ gpg-zip
/usr/ bin/ preunzip
/usr/bin/prezip
/ usr/ bin/prezip-bin
/ usr/ bin/ unzip
/usr/ bin/ unzipsfx
/usr/ bin/zip
/ usr/ bin/zipcloak
/usr/bin/zipgrep
/usr/bin/zipinfo
/ usr/ bin/z ipnote
/ usr/ bin/zipsplit
> 

# 2. find - 다양한 방법으로 파일 찾기

: locate 프로그램은 오로지 파일명에 근거하여 파일을 찾을 수 있지만 find 프로그램은 다양한 속성에 근거하여 주어진 디렉토리(하위 디렉토리를 퐇마하여)를 검색하여 파일을 찾는다.

### 예시

```sql
[me@linuxbox ~)$ find ~ I we -1
```

> 47068
> 

```sql
[me@linuxbox ~)$ find ~ -type d I we -1
```

> 1695
> 

```sql
[me@linuxbox ~) $ find ~ -type f I we -1
```

> 38737
> 

### 표: 파일 형식 찾기

| 파일형식 | 설명 |
| --- | --- |
| b | 블록특수파일 |
| c | 문자특 파일 |
| d | 디렉토리 |
| f | 파일 |
| l | 심볼릭 링크파일 |

### 표: 파일 크기 단위

| 기호 | 크기 단위 |
| --- | --- |
| b | 512 바이트 단위의 블록 (기본값) |
| c | 바이트 |
| w | 2바이트 크기의 위도 |
| k | 킬로바이트 (1024바이트) |
| M | 메가바이트 (1,048,576바이트) |
| G | 기가바이트 (1,073,741,824바이트) |

### 표: find의 테스트 예제

<img src="images/s_01.png">

<img src="images/s_02.png">

# 3. 연산자

: find 명령어가 지원하는 모든 테스트들조차도 테스트 간의 논리적인 관계를 설명하기 부족할 때가 있다. 그럴 때 논리 연산자를 사용하여 테스트들을 결합하는 방법을 제공한다.

### 표: find의 논리 연산자

<img src="images/s_03.png">

### 예시

```sql
[me@linuxbox ~]$ find ~ \( -type f -not -perm 0600 \) -or \( -type d -not -perm 0700 \)
```

### 표: find 명령어의 AND/OR 연산자 로직

<img src="images/s_04.png">

# 4. 액션

: find 명령은 검색하여 결과 목록을 보여주지만, 액션을 통하여 결과 목록에 해당 항목을 동작 하는 것을 구현할 수 있다.

### 표: 미리 정의된 find 액션

<img src="images/s_05.png">

### 예시

```sql
find N -type f -name ' * . BAK ' -delete
```

→ 예를 들어 .BAK(백업파일) 확장자를 가진 파일을 삭제하고 싶다면 다음과 같이 명령어를 실행할 수 있다.

### 표: 논리 연산자 효과

<img src="images/s_06.png">

# 5. 옵션

: find의 검색 범위를 설정할 때 사용된다. find 표현식을 만들기 위해 다른 테스트와 액션과 함께 사용 될 수 있다.

### 표: find 옵션

<img src="images/s_07.png">