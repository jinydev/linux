---
layout : home
---

# 윈도우11 Virtualbox 어댑터 브릿지 설정



## Virtualbox 어댑터 브릿지가 안돼요  ㅠ

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FlgvrZ%2FbtrzL9V6iKP%2FtJHHD08LHKiQqCpswjGy4k%2Fimg.png)



### 1. 원인을 찾아보자!  

1. 어댑터의 속성을 확인해보자!
   ![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fpwzvr%2FbtrzMaU2Zbr%2FcR2Md2wUZ4Gp1KiW2CTMe1%2Fimg.png)

2. 보면  Vmware Bridge protocol은 있는데 VirtualBox가 없네용

   

### 2. 없으면 만들어야지 

1. **[설치]** 버튼을 누르고 **[서비스]** 를 선택하고 **[추가]** 버튼을 눌러줍니다.|
   ![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FNmspd%2FbtrzKutcvCB%2FIlaaZpGHVSyz60W4pNxIKK%2Fimg.png)

2. ### 여기서 부터 중요!
   
   1. 아래와 같이 **[네트워크 서비스 선택]** 창이 나오는데요. 여기서 **[디스크 있음]** 버튼을 눌러줍니다.

   2. **C:\Program Files\Oracle\VirtualBox\drivers\network\netlwf\VBoxNetLwf.inf** 경로에 있는 **VBoxNetLwf.inf** 라는 파일을 찾아주면됩니다.
      -> 보통은 저렇게 VritualBox 폴더 밑에 drivers 의 network 폴더를 뒤적이다보면 찾을 수 있습니다.
   
      ![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbfFL7Y%2FbtrzMvkeF42%2F2zhjMlhkvSKQrxyL4sQHZK%2Fimg.png)
   
   
   
3.  **[열기]** 버튼을 눌러서 열어주고 **[확인]** 버튼을 눌러서 확인해줍니다.
   ![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fd1NJUb%2FbtrzKa9wlXU%2FImAJrTSoyVqizUyX8YvWM0%2Fimg.png)

4.  이제 아래와 같이 네트워크 서비스가 선택되어 집니다. 이제 다시 **[확인]** 버튼을 눌러줍니다.
   ![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbIvbW1%2FbtrzGhF8uK5%2FbVbK64zCapg0Pod9pQdK91%2Fimg.png)
5. ![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fnmlgm%2FbtrzKbADtIs%2FQRKd6yKUIxnU5ZV3TKvj90%2Fimg.png)

6. 이 상태로 다시 VirtualBox 의 네트워크 설정에 들어가서 어댑터에 브릿지를 선택하면 아래와 같이 어댑터 이름과 목록이 잘 나오는 것을 확인할 수 있습니다!
   ![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fb3gUFW%2FbtrzKt17WAo%2FgEtETO2KK5NIgz4dA92e4k%2Fimg.png)



7. 그럼 아래처럼 자동으로 할당받은 IP주소를 가지고 있는 것을 볼 수 있습니다.
   ![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FA6us4%2FbtrzIsCRqQO%2FUYv08KjyA7zNWpxK5Ozhq1%2Fimg.png)
