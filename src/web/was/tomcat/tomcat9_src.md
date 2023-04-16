---
layout: home
typora-copy-images-to: ./img
---

# tomcat9 수동설치
공식사이트에서 tomcat9을 다운로드 받아 설치를 합니다.

## 다운로드 및 준비
압축 파일은 임시 파일이므로 관리를 위해 /tmp/lib 폴더에 다운받는다
```
$ cd /tmp/lib
```

wget을 통해 톰켓을 다운로드 받습니다.
```
$ wget http://archive.apache.org/dist/tomcat/tomcat-9/v9.0.4/bin/apache-tomcat-9.0.4.tar.gz 
```

압축 파일 해제
```
tar -xvf apache-tomcat-9.0.4.tar.gz
```

## Tomcat 설치

사용자 로컬 폴더에 Tomcat 디렉토리 생성
```bash
# /usr/local 폴더는 애플리케이션 컴파일 설치 시 사용
sudo mkdir /usr/local/tomcat  
```

Tomcat을 사용자 해당 폴더로 이동합니다.
```bash
sudo mv apache-tomcat-9.0.4/ /usr/local/tomcat
```

## Tomcat 실행
스크립트를 통하여 톰켓을 실행합니다.

```
/usr/local/tomcat/apache-tomcat-9.0.4/bin/startup.sh
```

+ 아래와 같은 `ERROR` 가 표시될 경우.
```

```
* java 를 설치하지 않았고 JAVA_HOME 환경변수를 지정하지 않았기 떄문
* OpenJDK 설치 및 JAVA_HOME 환경변수 등록하면 해결

* Tomcat 실행 확인

Tomcat에서 기본 포트인 8080 LISTEN 확인
```
netstat -an | grep 8080
```