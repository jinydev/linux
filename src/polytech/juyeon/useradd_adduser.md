---
layout : home
---

# **useradd / adduser 명령어 차이점**

## **useradd / adduser 명령어 차이점**

### **useradd로 계정 생성하면 발생하는 현상**

useradd 로 test라는 사용자를 생성하고 비밀번호까지 정상적으로 지정해 주었다.

BASH

```
$ sudo useradd test$ sudo passwd 123123Copy
```
<br/><br/>
그런데 이상하게 OS 로그인 화면에서 정상적으로 비밀번호를 입력해도, 화면이 한번 깜빡이더니 다시 **로그인창 루프**에 빠져버린다. 계정 자체는 문제는 없을텐데 무슨 일일까?


우선 계정 정보를 가진 파일은 /etc/passwd 를 조회해보았다. 정상적으로 유저명과 UID, GID, 유저디렉토리가 명시 되어 있었다.

이번에는 직접 /home 디렉토리를 조회해 보았다. 그런데 이게 왠걸, test라는 새로 **생성한 유저 디렉토리가 없는 것**이다.
<br/><br/>

![https://blog.kakaocdn.net/dn/dOoSHE/btrs5z2yXTw/eqsN8ljjcjaG7xliQqBKsk/img.png](https://blog.kakaocdn.net/dn/dOoSHE/btrs5z2yXTw/eqsN8ljjcjaG7xliQqBKsk/img.png)

---
<br/><br/>
### **useradd vs adduser 기능 차이**

문제는 useradd로 아무 옵션 없이 유저를 새로 생성해서 였다.

### **useradd 명령어**

useradd의 매뉴얼을 보면 **a low level utility**라는 표현이 있다. 정리하자면 **계정을 생성할 때 필요한 모든 옵션들을 명시해줘야 한다.**

adduser로 사용자를 추가할때, UID나 GID는 자동생성된다. 하지만 **홈 디렉토리는 직접 옵션을 명시**해줘야 한다.

BASH

```
# 사용자는 생성하되 홈 디렉토리는 미생성$ useradd testuser# 사용자 홈 디렉토리를 /home/testuser으로 자동 생성$ useradd -m testuserCopy
```
<br/><br/>
### **adduser 명령어**

adduser의 매뉴얼을 보면 **configuration information in /etc/adduser.conf**라고 적혀있다. 또한 useradd로 사용자를 생성하면 아무런 IO없이 바로 명령 처리가 되는 반면, adduser로 사용자를 추가하면, 다음과 같이 무언갈 쭉쭉 추가 정보를 써야되는 걸 경험할 수 있다.

![https://blog.kakaocdn.net/dn/d2j6lf/btrtk988I4f/neWMJ3mwMvEaxNR2iKuGgK/img.png](https://blog.kakaocdn.net/dn/d2j6lf/btrtk988I4f/neWMJ3mwMvEaxNR2iKuGgK/img.png)

---

### **CentOS vs Ubuntu OS 차이**

이와 같은 특징은, **리눅스 계열간의 차이**에서 발생한다.
<br/><br/>
CentOS에서는 adduser가 useradd에 대한 **링크 파일**이다. 즉, CentOS에서는 '**useradd = adduser**'이다.

![https://blog.kakaocdn.net/dn/dzr6bS/btrs9hONxSL/Qwr45KjwZRaU8NKpTjCjCk/img.png](https://blog.kakaocdn.net/dn/dzr6bS/btrs9hONxSL/Qwr45KjwZRaU8NKpTjCjCk/img.png)

반면에 우분투를 살펴보면 이렇다.

useradd의 심볼릭 링크로 adduser가 존재했던 CentOS에서와 달리, **별개의 파일**로 존재하는 것을 알 수 있다.

![https://blog.kakaocdn.net/dn/cTjwJ1/btrs8aoh7Wf/tDkm2Nep5TytGPKfKUcEk1/img.png](https://blog.kakaocdn.net/dn/cTjwJ1/btrs8aoh7Wf/tDkm2Nep5TytGPKfKUcEk1/img.png)
<br/><br/>
따라서 정리해 보면 CentOS는 두 명령어는 차이가 없지만, 우분투에선

- useradd : 순수하게 '계정만' 생성해주고, 기본 쉘인 sh가 할당된다. 홈 디렉터리나 비밀번호 등은 따로 설정이 필요하다.
- adduser : 계정 생성 시 비밀번호와 사용자의 기타 정보를 입력받는다. 옵션을 통해 기본 쉘이나 로그인 옵션 등도 설정할 수 있다. 홈 디렉토리도 자동 생성된다.

명령어의 구체적인 기능 차이가 있으니, 왠만하면 우분투는 adduser 명령어를 사용하는게 좋다.