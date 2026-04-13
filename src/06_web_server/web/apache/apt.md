---
layout: home
---

# 아파치2 설치(APT)
`apt`명령을 통하여 아파치2를 설치합니다.


## 준비작업 및 패키지 검색
설치하기 전에 패키지 목록을 갱신합니다.

```bash
sudo apt update
```

apt 패키지 매니저를 사용하여 아파치2를 설치할 수 있는지 여부를 확인하려면 다음 명령어를 사용하십시오:

```bash
apt-cache search apache2
```

이 명령은 시스템에서 사용 가능한 모든 아파치2 관련 패키지를 검색합니다. 패키지 목록에서 "apache2"가 포함된 패키지를 찾으면 아파치2를 설치할 수 있습니다.

만약 검색된 목록에서 "apache2"가 없다면, 해당 패키지가 시스템에서 사용 가능하지 않은 것입니다. 이 경우, 다른 소스를 추가하여 설치할 수도 있습니다.


## 패키지 설치
우분투에서 아파치2를 설치하려면 다음 단계를 따르세요:

```bash
sudo apt install apache2 -y
```

패키지가 설치되면 자동적으로 아파치 데몬이 실행됩니다. `status` 명령을 통하여 상태를 확인할 수 있습니다.

```bash
service apache2 status
```
`systemctl` 로은 다음과 같이 실행해 볼 수 있습니다.

```
root@test:~# systemctl status apache2
● apache2.service - The Apache HTTP Server
     Loaded: loaded (/lib/systemd/system/apache2.service; enabled; vendor preset: ena>
     Active: active (running) since Sun 2021-01-03 03:36:41 UTC; 8s ago
       Docs: https://httpd.apache.org/docs/2.4/
    Process: 3366 ExecStart=/usr/sbin/apachectl start (code=exited, status=0/SUCCESS)
   Main PID: 3381 (apache2)
      Tasks: 55 (limit: 2282)
     Memory: 4.9M
     CGroup: /system.slice/apache2.service
             ├─3381 /usr/sbin/apache2 -k start
             ├─3382 /usr/sbin/apache2 -k start
             └─3383 /usr/sbin/apache2 -k start

Jan 03 03:36:41 test systemd[1]: Starting The Apache HTTP Server...
Jan 03 03:36:41 test apachectl[3380]: AH00558: apache2: Could not reliably determine >
Jan 03 03:36:41 test systemd[1]: Started The Apache HTTP Server.
```

## 아파치 실행하기
만일 설치된 아파치2가 실행되어 있지 않다면 다음과 같이 명령을 입력합니다.

```bash
sudo systemctl start apache2
```

이제 웹 브라우저를 열고, `http://localhost` 또는 서버의 IP 주소를 입력하여 아파치2 웹 페이지에 액세스할 수 있습니다. 웹 페이지가 표시되면, 아파치2가 성공적으로 설치되었다는 것을 의미합니다.


## 방화벽 허용

웹서버는 기본적으로 80번 포트를 사용합니다. 80번을 사용하기 위해서는 방화벽을 허용해 주어야 합니다.

```
test@test:~$ sudo ufw allow 80
[sudo] password for test:
Rules updated
Rules updated (v6)
```

방화벽을 재실행 합니다.

```
$ sudo ufw reload
```

## 포트포워딩

VirualBox와 같은 가상환경을 사용하는 경우 외부 접속을 위해서 포트 포워드를 같이 해주어야 합니다.

![image-20210102124523726](../../img/image-20210102124523726.png)



고급을 선택하여 항목을 확장 합니다.

![image-20210102124602576](../../img/image-20210102124602576.png)



추가를 선택하여 80번 포트를 입력합니다.

![image-20210102124648697](../../img/image-20210102124648697.png)



## 브라우저 접속하기

윈도우 또는 작업 PC에서 localhost로 접속을 해봅니다. 아파치 기본 페이지가 출력되는 것을 확인할 수 있습니다.

![image-20210102124719180](../../img/image-20210102124719180.png)



## 자동실행
만일 서버가 재부팅시 항상 apache2 데몬이 자동실행되기를 원하시면 활성화를 시켜 줍니다.

```bash
sudo systemctl enable apache2
```


## 문서경로
아파치는 기본 문서는 `/var/www/html` 입니다. 해당 경로의 index.html 파일이 실행됩니다.

