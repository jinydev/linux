---
layout: home
typora-copy-images-to: ./img
---

# Spring Boot
Spring Boot 다운로드 및 설치: 공식 웹 사이트(https://spring.io/projects/spring-boot)에서 Spring Boot JAR 파일을 다운로드하거나 Maven 또는 Gradle과 같은 패키지 관리자를 사용할 수 있습니다. 여기에서는 Maven을 사용하여 Spring Boot를 설치합니다.


## Maven을 설치합니다.

```
sudo apt install maven
```

다음으로 Spring Boot 프로젝트를 위한 새 디렉터리를 만들고 해당 디렉터리로 이동합니다.

```
mkdir spring-boot-project
cd spring-boot-project
```

Maven을 사용하여 새 Spring Boot 프로젝트를 만듭니다.

```
mvn archetype:generate -DgroupId=com.example -DartifactId=my-spring-boot-app -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
```

그러면 pom.xml 파일과 src 디렉토리가 있는 기본 Spring Boot 프로젝트가 생성됩니다.

Maven을 사용하여 프로젝트를 빌드합니다.

```
mvn package
```

target 디렉토리에 Spring Boot 애플리케이션용 JAR 파일이 생성됩니다.

Tomcat에 Spring Boot 애플리케이션 배포: Spring Boot 애플리케이션을 빌드한 후에는 JAR 파일을 Tomcat 설치의 'webapps' 디렉터리에 복사하여 Tomcat에 배포할 수 있습니다.

Spring Boot 프로젝트의 target 디렉토리로 이동합니다.

```
cd target
```

JAR 파일을 Tomcat 설치의 webapps 디렉터리에 복사합니다.

```
sudo cp my-spring-boot-app-1.0-SNAPSHOT.jar /var/lib/tomcat9/webapps/
```

Tomcat을 다시 시작하여 Spring Boot 애플리케이션을 배포합니다.

```
sudo systemctl restart tomcat10
```

이제 Spring Boot 애플리케이션이 Tomcat에서 실행되고 있어야 합니다! 웹 브라우저에서 http://localhost:8080/my-spring-boot-app-1.0-SNAPSHOT/으로 이동하여 액세스할 수 있습니다.