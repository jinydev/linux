---
layout: home
typora-copy-images-to: ./img
---

# Java8 (Yum)
yum 패키지 관리자를 사용하여 Linux 시스템에 Java 8을 설치하려면 다음 단계를 따르십시오.

* 먼저 시스템의 패키지 인덱스를 업데이트하고 다음 명령을 실행하여 설치된 모든 패키지가 최신인지 확인합니다.

```bash
sudo yum update
```

* 다음으로 다음 명령을 사용하여 Java 리포지토리를 시스템에 추가합니다.
```bash
sudo yum install java-1.8.0-openjdk-devel
```

* 리포지토리가 추가되면 다음 명령을 사용하여 Java 8을 설치할 수 있습니다.
```bash
sudo yum install java-1.8.0-openjdk
```

설치가 완료되면 다음 명령을 실행하여 Java 8이 성공적으로 설치되었는지 확인합니다.

```bash
java -version
```

이 명령은 시스템에 설치된 Java 버전을 표시합니다.


참고: 특정 패키지 이름은 사용 중인 Linux 배포판에 따라 다를 수 있습니다. 또한 헤드리스 서버에 Java를 설치하는 경우 JRE(Java Runtime Environment) 대신 JDK(Java Development Kit)를 설치할 수 있습니다. JDK에는 Java 개발에 필요한 추가 도구 및 라이브러리가 포함되어 있습니다.

