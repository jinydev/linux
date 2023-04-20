---
layout: home
---

# JAM stack

---

<img src = "https://velog.velcdn.com/images%2Fkysung95%2Fpost%2F47d6a8af-37bb-457d-b4ef-f7094bdef34b%2Fimage.png">

JAM stack은 JavaScript와 API, 그리고 Markup(HTML)만으로 이루어진 웹의 구성을 이야기

# 0418 리눅스 프로그래밍



### JAM Stack이란?


- JavaScript
    - client의 모든 처리는 Javascript가 처리
    - 동적인 요소 처리
    - API 요청
- API
    - 모든 기능 및 비즈니스 로직은 재사용 가능한 API로 추상화
    - 서버 또는 DB에서 담당하던 역할
- Markup
    - SSG(Static Site Generator)나 Template Engine(Webpack 등)을 이용하여 Markup을 미리 생성
    - 문서 내용의 시각적 표현
    - 빌드시 페이지 생성



### Markup 만드는 방법



- HTML 직접 작성
- Template Engine과 같은 툴 사용
- 정적 사이트 생성기 (static site generator, SSG)를 사용하여 Static HTMl 생성
    - Gatsby, Next.js, Gridsome, Nuxt.js, Jekyll 등
- 이렇게 만들어진 Static HTML은 웹 서버의 리소스를 사용할 필요 없이 사용자에게 HTML만을 전달해주면 됨
- Static HTML은 CDN을 통해서 Cache를 배포하여 빠른 속도를 유지하면 됨
- 따로 동적으로 HTML을 생성하지 않기 때문에 웹서버가 필요없어서 서버 비용이 크지 않음

### JAM stack과 기존 Web 사이트와의 동작 방식

<img src ="https://user-images.githubusercontent.com/42582516/107994487-0def8f00-7020-11eb-8eec-2092e8b36f01.png">

- 기존 Web 사이트
    - 대부분 서버의 데이터베이스로부터 추출한 데이터를 프론트엔드에 뿌려주는 방식으로 동작
    - 클라이언트에 데이터를 보여주기 위해 많은 절차를 거쳐야 함
- JAM Stack
    - 다양한 API를 통해 만든 정적 웹 사이트를 Pre-Render 한 것
    - CDN(Content Delivery Network)을 통해 웹 사이트를 열람

### JAM stack 장점

<img src ="https://www.bottlehs.com/assets/jamstack-advantage-2.png">

1. 기존 방식보다 더 빠르게 웹 사이트를 제공
    1. JAM Stack은 렌더링할 화면들을 모두  Pre-Render하여 제공
    2. 사용자에게 화면을 보여주기 위해 준비하는 시간 단축할 수 있음
    
    → 배포타임에 생성해도 되는 페이지들을 요청시마다 생성할 필요가 없음,  CDN에서 받은 것 만큼 시간을 절약할 수 있음
    
<img src = "https://www.bottlehs.com/assets/jamstack-advantage-1.png">
    
2. 안전한 웹 사이트를 제공
    1. JAM Stack은 API를 통해 정적 사이트를 생성
    2. 여기서 사용되는 API는 JAM Stack을 활용한 각 프레임워크에서의 마이크로 서비스
    3. 사이트 생성을 위한 프로세스가 추상화되어 있음 
    4. 공격 노출 범위가 감소
    →  API들은 마이크로 서비스로 추상화되어 외부로부터 공격영역이 줄어들어 안정성이 높다.

<img src ="https://www.bottlehs.com/assets/jamstack-advantage-3.png">

3. 스케일링하기 쉬운 웹 사이트를 제공
    1. 미리 빌드된 파일 제공을 담당하는 CDN 서버를 구축하여 비용을 줄일 수 있음
    
<img src ="https://www.bottlehs.com/assets/jamstack-advantage-4.png">
    
4. 쉬운 자동화
    1. Netlify, AWS Lambda를 활용하면 배포를 자동화할 수 잇음

### JAM stack 단점

<img src ="https://www.bottlehs.com/assets/jamstack-grenze-1.png">

- 빌드 속도
    - JAM stack 구조상 정적인 페이지가 많아질수록 빌드 속도가 오래 걸림

<img src ="https://www.bottlehs.com/assets/jamstack-grenze-2.png">

- 실시간 변경 콘텐츠
    - 정적인 서비스를 하다보니 URL 구조들이나 컨텐츠 내용이 변화될 때 관련된 링크나 검색엔진들의 인덱싱 정보까지 변경되려면 오래 걸림
    


### GitHub Pages와 Jekyll

https://poiemaweb.com/jekyll-basics

- Jekyll은 markdown으로 작성된 문법을 HTML로 변환하여 웹사이트를 구축할 수 있도록 돕는 Static Website generator로 Ruby로 작성됨
- GitHub Pages는 GitHub에서 제공하는 Static Website로 GitHub repository에 리소스를 push하는 것만으로 간단히 웹 사이트를 만들 수 있음
- Static Website이므로 Database는 사용할 수 없으나 무료로 유지보수가 간편한 Website를 호스팅할 수 있다는 장점이 있음
- GitHub Pages는 HTML, CSS, Javascript만으로도 웹사이트를 구축할 수 있으나 markdown을 사용하여 웹사이트를 generate하기 위해 Jelyll을 지원
- 로컬 환경에서 Jelyll을 사용하여 웹사이트를 작성/테스트하고 GitHub repository에 웹리소스를 push하면 매우 간단히 Website를 Hosting할 수 있는 구조