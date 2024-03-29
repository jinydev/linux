---
layout: home
---
# SSR 과 CSR

### 1. 렌더링의 의미

HTML, CSS, 자바스크립트 등 개발자가 작성한 문서가 브라우저에서 출력되는 과정을 의미한다. 이 과정에서는 HTML, CSS, JavaScript 등을 해석하여 브라우저에서 사용자가 볼 수 있는 UI를 생성한다.

따라서, 렌더링은 입력된 데이터를 사용자가 볼 수 있는 형태로 변환하는 과정을 의미한다.
<br/><br/>
### 2.  SSR의 정의와 설명

> Server Side Rendering의 약자.
> 
> 
> 말 그대로 서버쪽에서 렌더링 준비를 끝마친 상태로 클라이언트에 전달하는 방식이다.
> 

<br/><br/>
![ssr1](https://user-images.githubusercontent.com/127702320/234141064-033d54ee-ea37-4295-9960-a0cee4a099b4.png)

위의 사진은 **SSR**의 단계를 설명한다.

1. User가 Website 요청을 보냄.
2. Server는 'Ready to Render'. 즉, 즉시 렌더링 가능한 html파일을 만든다.(리소스 체크, 컴파일 후 완성된 HTML 컨텐츠로 만든다.)
3. 클라이언트에 전달되는 순간, 이미 렌더링 준비가 되어있기 때문에 HTML은 즉시 렌더링 된다. 그러나 사이트 자체는 조작 불가능하다. (Javascript가 읽히기 전이다.)
4. 클라이언트가 자바스크립트를 다운받는다.
5. 다운 받아지고 있는 사이에 유저는 컨텐츠는 볼 수 있지만 사이트를 조작 할 수는 없다. 이때의 사용자 조작을 기억하고 있는다.
6. 브라우저가 Javascript 프레임워크를 실행한다.
7. JS까지 성공적으로 컴파일 되었기 때문에 기억하고 있던 사용자 조작이 실행되고 이제 웹 페이지는 상호작용 가능해진다.

<br/><br/>
아래의 사진은 SSR을 설명하는 좀 더 간단한 사진이다.

![ssr2](https://user-images.githubusercontent.com/127702320/234141073-bb535866-e220-4259-ace7-38c8d9e91402.png)


즉. 서버에서 이미 '렌더 가능한' 상태로 클라이언트에 전달되기 때문에, JS가 다운로드 되는 동안 사용자는 **무언가**를 보고 있을 수 있다.
<br/><br/>
### CSR의 정의와 설명

> Client Side Rendering의 약자.
> 
> 
> 말 그대로 SSR과 달리 렌더링이 클라이언트 쪽에서 일어난다.즉, 서버는 요청을 받으면 클라이언트에 HTML과 JS를 보내준다. 클라이언트는 그것을 받아 렌더링을 시작한다.
> 

![csr1](https://user-images.githubusercontent.com/127702320/234141072-3d68faaf-f3ce-44ec-ae0b-0940c2991c2a.png)

위의 사진은 **CSR**의 단계를 설명한다.

1. User가 Website 요청을 보낸다
2. CDN이 HTML 파일과 JS로 접근할 수 있는 링크를 클라이언트로 보낸다.

> CDN : 엔드 유저의 요청에 '물리적'으로 가까운 서버에서 요청에 응답하는 방식이다
> 
3. 클라이언트는 HTML과 JS를 다운로드 받는다.(이때 SSR과 달리 유저는 아무것도 볼 수 없다.)
4. 클라이언트가 JS를 다운 받는다. 
5. 다운이 완료된 JS가 실행된다. 데이터를 위한 API가 호출된다.(이때 유저들은 placeholder를 보게된다.)

> Placeholder : 웹 페이지에서 폼에 입력될 값이나 내용이 미리 예상되어 있을 때, 해당 입력 필드의 힌트 또는 예시로 사용되는 텍스트를 의미한다.
> 
> 
> 예를 들어, 검색 창에 "검색어를 입력하세요" 라는 Placeholder 텍스트가 있으면, 사용자는 검색어를 입력할 때 이 텍스트를 보고 어떤 검색어를 입력해야 하는지 알 수 있다. 
> 
6. 서버가 API로부터의 요청에 응답한다.
7. API로부터 받아온 data를 placeholder 자리에 넣어준다. 이제 페이지는 상호작용이 가능해진다.
<br/><br/>
아래의 사진은 CSR을 설명하는 좀 더 간단한 사진이다.

![csr2](https://user-images.githubusercontent.com/127702320/234141068-7e4c8950-10b0-485a-82d2-b1babb893500.png)

즉, 서버에서 처리 없이 클라이언트로 보내주기 때문에 자바스립트가 모두 다운로드 되고 실행이 끝나기 전까지 사용자는 볼수 있는게 없다.
<br/><br/>
### 3. 각각의 차이

1) 웹페이지를 로딩하는 시간

웹 페이지 로딩의 종류는 두 가지로 나눌 수 있다.하나는 웹 사이트의 가장 **첫 페이지**를 로딩하는 것.다른 하나는 **나머지**를 로딩하는 것

- 첫 페이지 로딩시간.

CSR의 경우 HTML, CSS와 모든 스크립트들을 한 번에 불러온다. 반면 SSR은 필요한 부분의 HTML과 스크립트만 불러오게 된다. 따라서 평균적으로 SSR이 더 빠르다.

- 나머지 로딩 시간

첫 페이지를 로딩한 후, 사이트의 다른 곳으로 이동하는 식의 동작을 가정하자. CSR은 이미 첫 페이지 로딩할 때 나머지 부분을 구성하는 코드를 받아왔기 때문에 빠르다. 반면, SSR은 첫 페이지를 로딩한 과정을 **정확하게** 다시 실행한다. 그래서 더 느리다.
<br/><br/>
2) SEO 대응

SEO는 검색 엔진에서 웹사이트를 검색하여 노출시키는 것을 의미한다. 검색 엔진 크롤러는 일반적으로 HTML 코드를 읽어들여 페이지의 내용을 파악하는데, CSR 방식에서는 페이지 내용이 자바스크립트에 의해 동적으로 생성되기 때문에 크롤러가 자바스크립트를 실행시키지 않으면 페이지의 내용이 완전히 노출되지 않는다. 이에 따라 검색 엔진에서 CSR 방식으로 작성된 페이지를 인식하지 못하고 검색 노출이 떨어질 수 있다.

반면, SSR 방식에서는 서버에서 HTML을 미리 렌더링하여 브라우저로 전송하기 때문에 페이지 내용이 이미 포함되어 있어 크롤러에서 쉽게 읽어들일 수 있다. 따라서, 검색 엔진 최적화를 위해선 CSR 방식보다는 SSR 방식이 더 유리하다.
<br/><br/>
3) 서버 자원 사용

SSR이 서버 자원을 더 많이 사용한다. 매번 서버에 요청을 하기 때문이다. 반면 CSR은 클라이언트에 작업을 몰아주기 때문에 서버에 부하가 적다.

---

### 4. 사용 권장 예시

SSR을 사용할 때 

- 네트워크가 느릴 때 (CSR은 한번에 모든 것을 불러오지만 SSR은 각 페이지마다 나눠불러오기 때문)
- SEO(serach engine optimization : 검색 엔진 최적화)가 필요할 때.
- 최초 로딩이 빨라야하는 사이트를 개발 할 때
- 메인 스크립트가 크고 로딩이 매우 느릴 때 CSR은 메인스크립트가 로딩이 끝나면 API로 데이터 요청을 보낸다. 하지만 SSR은 한번의 요청에 아예 렌더가 가능한 페이지가 돌아온다.
- 웹 사이트가 상호작용이 별로 없을 때.

CSR을 사용할 때

- 네트워크가 빠를 때
- 서버의 성능이 좋지 않을 때
- 사용자에게 보여줘야 하는 데이터의 양이 많을 때.(로딩창을 띄울 수 있는 장점이 있다.)
- 메인 스크립트가 가벼울 때
- 웹 어플리케이션에 사용자와 상호작용할 것들이 많을 때. (아예 렌더링 되지 않아서 사용자의 행동을 막는 것이 경험에 오히려 유리함.)