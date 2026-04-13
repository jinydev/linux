---
layout: home
---

# VirtualBox 설치



## 다운로드

VirtualBox 사이트로 접속합니다. https://www.virtualbox.org/ 

![image-20230328185525241](D:\jinydev\linux\src\setup\virtual\virtualbox\img\image-20230328185525241.png)

다운로드 버튼을 클립합니다. 다양한 운영체제에서 사용 가능한 설치 프로그램을 제공합니다.

![image-20230328185717658](D:\jinydev\linux\src\setup\virtual\virtualbox\img\image-20230328185717658.png)





## 설치

자신의 호스트 컴퓨터에 VirtualBox를 설치합니다. 다음은 windows 운영체제 에서의 설치 방법입니다.

![image-20230328185923655](D:\jinydev\linux\src\setup\virtual\virtualbox\img\image-20230328185923655.png)



![image-20230328185947784](D:\jinydev\linux\src\setup\virtual\virtualbox\img\image-20230328185947784.png)



![image-20230328190007687](D:\jinydev\linux\src\setup\virtual\virtualbox\img\image-20230328190007687.png)

네트워크 설정이 변경될 수 있어 네트워크가 끊길수 있답니다.

특별한 상황이 아니라면 "Yes"를 눌러 다음으로 진행합니다.



![image-20230328190042040](D:\jinydev\linux\src\setup\virtual\virtualbox\img\image-20230328190042040.png)

VirtualBox 설치를 위해서는 Python Core / win32api 가 의존성으로 필요합니다. 필요시 나중에 설치를 진행하겠냐고 물어봅니다. 



Linux를 설치하는데 는 필요가 없으니 "Yes" 버튼을 선택합니다. 

만약 이 메시지를 보고 싶지 않다면 pywin32를 설치하시고 다시 설치하면 됩니다.

![image-20230328190122767](D:\jinydev\linux\src\setup\virtual\virtualbox\img\image-20230328190122767.png)



![image-20230328190543504](D:\jinydev\linux\src\setup\virtual\virtualbox\img\image-20230328190543504.png)



![image-20230328190647225](D:\jinydev\linux\src\setup\virtual\virtualbox\img\image-20230328190647225.png)



설치가 완료되었습니다.



## 실행

VirtualBox를 설치하였다면, 바탕화면에 아이콘이 생성됩니다. 클릭하여 VirtualBox를 실행합니다.



![image-20230328190803554](D:\jinydev\linux\src\setup\virtual\virtualbox\img\image-20230328190803554.png)



## 네트워크

VirtualBox를 설치하게 되면 윈도우에 새로운 네트워크가 추가 됩니다.

![image-20230328191005753](D:\jinydev\linux\src\setup\virtual\virtualbox\img\image-20230328191005753.png)



제어판->네트워크연결 탭을 확인해 보면 `VirtualBox Host-Only`가 추가된 것을 확인확인합니다.

## OVA 출력
VirtualBox에서 OVA는 "Open Virtualization Appliance"의 약자로, 가상 머신을 저장, 전송 및 배포하기 위한 개방형 표준 파일 형식입니다. OVA 파일은 가상 머신의 `디스크 이미지`, 설정 및 메타 데이터를 포함하며, 다른 가상화 소프트웨어, 클라우드 환경 또는 다른 시스템에서 가상 머신을 쉽게 배포하고 공유할 수 있습니다.

### OVA 파일을 생성하는 방법은 다음과 같습니다:

* VirtualBox에서 해당 가상 머신을 선택하고 "Export"를 클릭합니다.
* OVA 파일로 내보낼 디스크 이미지와 설정을 선택합니다.
* OVA 파일을 저장할 위치와 이름을 지정하고, "Next"를 클릭합니다.
* OVA 파일이 생성될 때까지 대기합니다.  

### OVA 파일을 가져오는 방법은 다음과 같습니다:

* VirtualBox에서 "Import Appliance"를 선택하고, OVA 파일을 선택합니다.
* OVA 파일의 설정을 선택하고, 새 가상 머신의 이름과 위치를 지정합니다.
* OVA 파일이 가져와진 가상 머신을 시작합니다. 

이렇게 OVA 파일을 사용하면 가상 머신을 쉽게 공유하고 이식성이 높은 가상 머신을 만들 수 있습니다.

### vmware 이식
OVA 파일은 VMware와 같은 다른 가상화 소프트웨어에서도 사용할 수 있습니다. OVA는 개방형 표준 파일 형식으로, 가상 머신을 저장, 전송 및 배포하기 위한 표준 방법을 제공합니다. 이것은 OVA 파일이 가상화 소프트웨어와 관계없이 사용할 수 있도록 만들어진 것입니다.

따라서, OVA 파일을 VMware나 다른 가상화 소프트웨어에서 가져오려면 해당 소프트웨어에서 OVA 파일을 열고 가져오는 작업을 수행하면 됩니다. 그러나 OVA 파일에서 지원하지 않는 기능이나 설정이 있을 수 있으므로, 이식 전에 이러한 부분을 확인해야 합니다.

즉, OVA 파일을 사용하면 가상 머신을 쉽게 이식할 수 있으며, 다양한 가상화 소프트웨어에서 호환됩니다.




