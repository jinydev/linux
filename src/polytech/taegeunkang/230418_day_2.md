
# 리눅스에서 사용되는 에디터의 종류

리눅스 운영 체제에서 CLI(Command Line Interface) 기반으로 사용 가능한 에디터의 종류는 다음과 같다.

- **vi**:
리눅스에서 가장 많이 사용되는 텍스트 에디터 중 하나이다. 사용법이 다소 복잡하고 익숙하지 않은 사용자에게는 불편할 수 있지만, 강력한 기능을 제공하며 시스템 리소스를 적게 사용한다는 장점이 있다.
- **nano**:
사용하기 쉽고 간단한 기능만을 제공하는 텍스트 에디터이다. 기본적인 편집 작업을 수행하는 데는 적합하지만, vi와 같이 강력한 기능을 제공하지는 않는다.
- **emacs**:
vi와 함께 리눅스에서 가장 유명한 에디터 중 하나이다. 다양한 기능과 확장성을 제공하며, 사용자는 자신의 필요에 따라 에디터의 동작을 변경하고 확장할 수 있다.
- **pico**:
nano와 매우 유사한 기능을 제공하는 텍스트 에디터이다. BSD 라이선스로 배포되며, 무료로 사용할 수 있다.
- **joe**:
vi와 비슷한 사용자 인터페이스를 제공하면서도, 사용하기 쉽고 초보자들도 쉽게 익힐 수 있는 에디터이다. 다양한 편집 모드와 매크로 기능을 제공한다.

위에서 언급한 에디터들은 모두 CLI(Command Line Interface) 기반으로 동작하며, 사용자의 텍스트 편집 요구에 따라 선택하여 사용할 수 있다.

### 일반적인 사용

```bash
에이터이름 파일명
nano test.txt
vi test.txt
```

### vi 실행화면

![Untitled](https://user-images.githubusercontent.com/53002135/232693060-0f4014b3-130c-490a-b201-ae1b4ef58e24.png)

### nano 실행화면

![Untitled](https://user-images.githubusercontent.com/53002135/232693187-816455c8-b84c-40ea-b448-dd2e43079571.png)

### Vim(Vi improved)

 vi는 **v**isual **e**ditor의 약자이고, Vim은 **Vi** I**m**proved(향상된 vi)의 약자이다. 향상된 vi라는 말에서부터 알 수 있듯이 Vim이 vi보다 더 편하다. 그렇기 때문에 대부분의 리눅스에서는 vi를 호출해도 Vim이 실행되도록 내부적으로 alias 설정을 해두었다. 실제로 Vim을 vim으로 호출하기보다 vi으로 호출하는 사용자가 더 많다.

vi와 Vim의 가장 큰 차이점은, Vim은 에디터에서 화살표 방향키로 커서의 이동이 되지만 vi는 이 방법으로는 커서의 이동이 되지 않는다는 것이다. 순수하게 vi만 설치되어 있다면 화살표 방향키가 아닌 h, j, k ,l로 커서를 이동할 수 있다.

### vim 설치 및 사용

```bash
sudo apt-get install vim

vi 파일명 (vi를 호출해도 vim이 설치되어 있으면 vim이 실행된다)
```

## GUI editor(외부 접속)

cli기반의 리눅스에서 외부 접속을 통한 gui 에디터를 사용할 수 있는 방법

### VScode extension

![Untitled](https://user-images.githubusercontent.com/53002135/232692089-bac968f5-3d68-41e0-aa12-1f42dcf6d5c3.png)

![Untitled](https://user-images.githubusercontent.com/53002135/232692187-f980336f-9cb4-46dc-bd9d-3d81dc8d58ae.png)

![Untitled](https://user-images.githubusercontent.com/53002135/232692265-3e4bc56c-b74d-41c4-acf9-25cb21ba62af.png)

### code-server

vscode를 웹상에서 실행 가능하게 해주는 오픈 소스 프로젝트

리눅스 서버에 설치하여 외부에서 접속 가능하다. 

[https://github.com/coder/code-server](https://github.com/coder/code-server)


![](https://user-images.githubusercontent.com/53002135/232692844-6bccc9db-e252-4f7f-bc6b-d10c1e63f330.png)