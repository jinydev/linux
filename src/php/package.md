---
layout: home
---

# php 설치
PHP는 소스를 컴파일 하여 설치하는 방법과 패티지를 이용하는 설치하는 방법이 있습니다.

패키지의 경우 운영체제에 최적화 되어 있다는 점과, 쉽게 설치를 할 수 있는 점에서 많이 선호 합니다.




## 01.설치하기

우분투 운영체제에서 패키지를 이용하여 간단하게 설치를 합니다.

```
# sudo apt install php -y
```

ubuntu 20.04의 경우 php 7.4가 기본적으로 설치됩니다. 그이상의 버젼은 별도의 패키지 저장소를 등록하거나 컴파일 하여 설치를 해야 합니다.



#### 실행

php는 별도의 데몬이 실행되지 않습니다. 터미널 콘솔 또는 웹서버스 확장모듈 형태로 동작을 합니다.

터미널에서 `php -v`명령을 통하여 설치 버젼을 확인해 봅니다. 

```
test@test:~$ php -v
PHP 7.4.3 (cli) (built: Oct  6 2020 15:47:56) ( NTS )
Copyright (c) The PHP Group
Zend Engine v3.4.0, Copyright (c) Zend Technologies
    with Zend OPcache v7.4.3, Copyright (c), by Zend Technologies
```

