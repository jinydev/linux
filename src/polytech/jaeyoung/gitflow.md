# 제목 없음

## **GIT-FLOW 전략**

![https://blog.kakaocdn.net/dn/UwrHH/btrAAcyJxeV/xkIF2PeoqBSQESWcivaxb0/img.png](https://blog.kakaocdn.net/dn/UwrHH/btrAAcyJxeV/xkIF2PeoqBSQESWcivaxb0/img.png)

- 기본적인 가지의 이름은 아래의 5가지로 구분하곤 한다.
- **feature > develop > release > hotfix > master**
- 위 순서들은 왼쪽으로 갈수록 포괄적인 가지이며 master branch를 병합할 경우 그 왼쪽에 있는 hotfix 등 모든 가지들에 있는 커밋들도 병합하도록 구성하게 된다.
- 5가지 중, **항시 유지되는 메인 브랜치 master, develop** 2가지와 **merge 되면 사라지는 보조 브랜치 feature, release, hotfix** 3가지로 구성된다.

---

### **Git-flow 브랜치 구조**

![https://blog.kakaocdn.net/dn/bQA8c1/btrACMzkbRN/0fFHCPKTR1LhKZUKSPSti1/img.jpg](https://blog.kakaocdn.net/dn/bQA8c1/btrACMzkbRN/0fFHCPKTR1LhKZUKSPSti1/img.jpg)

- **master** : 라이브 서버에 제품으로 되는 브랜치.
    
    **출시**
    
- **develop** : 다음 출시 버전을 대비하여 하는 브랜치.
    
    **개발**
    
- **feature** :  개발 브랜치. develop 브랜치에 들어간다.
    
    **추가 기능**
    
- **release** :  출시를 준비하는 브랜치. develop 브랜치를 release 브랜치로 옮긴 후 QA, 테스트를 진행하고 master 브랜치로 합친다.
    
    **다음 버전**
    
- **hotfix** : master 브랜치에서 발생한 하는 브랜치.
    
    **버그를 수정**
    

### **메인 브랜치**

메인 브랜치는 **master 브랜치**와 **develop 브랜치** 두 종류를 말한다.

![https://blog.kakaocdn.net/dn/ltmzh/btrlPn0RYiX/qSivFQwoY63XkW28XuBmWK/img.png](https://blog.kakaocdn.net/dn/ltmzh/btrlPn0RYiX/qSivFQwoY63XkW28XuBmWK/img.png)

master 브랜치는 **배포 가능한 상태**만을 관리하는 브랜치를 말하며,

develop브랜치는 다음에 **배포할 것을 개발**하는 브랜치이다.

즉 develop 브랜치는 통합 브랜치의 역할을 하며, 평소에는 이 브랜치를 기반으로 개발을 진행한다.

### **보조 브랜치**

보조 브랜치는 **피처 브랜치(feature branch)** 또는 **토픽 브랜치(topic branch)를** 말한다.

![https://blog.kakaocdn.net/dn/l7ghN/btrlEIzgZhO/Yr4Bq3K2Rdmo37VhmG9KBk/img.png](https://blog.kakaocdn.net/dn/l7ghN/btrlEIzgZhO/Yr4Bq3K2Rdmo37VhmG9KBk/img.png)

- **가지가 뻗어나오는 곳** : develop
- **뻗어나갔던 가지가 다시 합쳐지는 곳** : develop
- **이름 설정** : master, develop, release-*, hotfix-*를 제외하기만 하면 자유롭게 이름 설정이 가능하다.
- **새로운 기능을 추가**할 때 주로 사용하는 가지이다.

master 브랜치에서 develop 브랜치를 만들었고,

develop 브랜치에서 다시 **feature 브랜치를 나눠 작업**을 하고 있는 것을 그림을 통해 알 수 있다.

**develop 브랜치에는 기존에 잘 작동하는 개발코드**가 담겨있으며,

**보조 브랜치는 새로 변경될 개발코드를 분리하고 각각 보존하는 역할**을 한다.

즉, 보조 브랜치는 **기능을 다 완성할 때까지 유지하고, 다 완성되면 develop 브랜치로 merge 하고 결과가 좋지 못하면 버리는 방향**을 취한다.

보조 브랜치는 보통 개발자 저장소에만 있는 브랜치고, origin에는 push하지 않는다.

### **릴리즈 브랜치(release branch)**

**릴리즈 브랜치**는 **배포를 위한 최종적인 버그 수정** 등의 개발을 **수행**하는 브랜치를 말한다.

![https://blog.kakaocdn.net/dn/bfrnW4/btrlKeQT8mr/Tw2TZEkr39sZIeoKUJES8k/img.png](https://blog.kakaocdn.net/dn/bfrnW4/btrlKeQT8mr/Tw2TZEkr39sZIeoKUJES8k/img.png)

- **가지가 뻗어나오는 곳** : develop
- **뻗어나갔던 가지가 다시 합쳐지는 곳** : develop, master
- **이름 설정** : release-*
- 새로운 **제품을 배포**하고자 할 때 사용하는 가지이다.

develop 브랜치에 버전에 포함되는 기능이 merge 되었다면 QA를 위해 develop 브랜치에서부터 release 브랜치를 생성한다.

**배포 가능한 상태가 되면 master 브랜치로 병합**시키고, **출시된 master 브랜치에 버전 태그(ex, v1.0, v0.2)를 추가**한다.

release 브랜치에서 기능을 점검하며 발견한 버그 수정 사항은 develop 브랜치에도 적용해줘야 한다.

그러므로 배포 완료 후 develop 브랜치에 대해서도 merge 작업을 수행해야 한다.

### **핫픽스 브랜치(hotfix branch)**

**핫픽스 브랜치**는 **배포한 버전에서 긴급하게 수정**할 필요가 있을 때 master 브랜치에서 분리하는 브랜치를 말한다.

![https://blog.kakaocdn.net/dn/ct9FBn/btrlGJqMMST/JgZHcI2gO5IkcXwwMNckA0/img.png](https://blog.kakaocdn.net/dn/ct9FBn/btrlGJqMMST/JgZHcI2gO5IkcXwwMNckA0/img.png)

- **가지가 뻗어나오는 곳** : master
- **뻗어나갔던 가지가 다시 합쳐지는 곳** : develop, master
- **이름 설정** : hotfix-*
- 제품에서 버그가 발생했을 경우에는 처리를 위해 이 가지로 해당 정보들을 모아준다. 버그에 대한 수정이 완료된 후에는 develop, master에 곧장 반영해주며 tag를 통해 관련 정보를 기록해둔다.

버그를 잡는 사람이 일하는 동안에도 다른 사람들은 develop 브랜치에서 하던 일을 계속할 수 있다.

이 때 만든 hotfix 브랜치에서의 변경 사항은 develop 브랜치에도 merge 하여 문제가 되는 부분을 처리해줘야 한다.

release 가지가 생성되어 관리되고 있는 상태라면 해당 가지에 hotfix정보를 병합시켜 다음번 배포 시 반영이 정상적으로 이루어질 수 있도록 해준다.

Hotfix는 보통 다급하게 버그를 고치기 위해 생성되는 가지이기 때문에 버그를 해결하면 보통 제거하는 일회성 가지다.

---

### **Git flow 흐름**

- 앞에서 적었던 기본 구조 5개 중 가장 많이 사용되는 가지는 master와 develop가 되며 정상적인 프로젝트를 진행하기 위해서는 둘 모두를 운용해야 한다.
- 나머지 feature, release, hotfix branch는 사용하지 않는다면 지우더라도 오류가 발생하지 않기 때문에 깔끔한 프로젝트 진행을 원한다면 지워뒀다가 해당 가지를 활용해야 할 상황이 왔을 때 만들어줘도 괜찮다.
- 대부분의 작업은 develop에서 취합한다 생각하면 되며 테스트를 통해 정말 확실하게 더 이상 변동사항이 없다 싶을 때 master로의 병합을 진행하게 된다.
- master가 아닌 가지들은 master의 변동사항을 꾸준히 주시해야 한다.

**1. 신규 기능 개발**

![https://blog.kakaocdn.net/dn/c4oHhU/btrlEsJEeue/Cao2ePzB1Bdx8OAH9eAKk0/img.png](https://blog.kakaocdn.net/dn/c4oHhU/btrlEsJEeue/Cao2ePzB1Bdx8OAH9eAKk0/img.png)

1. 개발자는 develop 브랜치로부터 본인이 신규 개발할 기능을 위한 feature 브랜치를 생성한다.
2. feature 브랜치에서 기능을 완성하면 develop 브랜치에 merge를 진행하게 된다.

**2. 라이브 서버로 배포**

![https://blog.kakaocdn.net/dn/bLxHoz/btrlPoeoynz/U795uDv8y9GkT4tHtLdykK/img.png](https://blog.kakaocdn.net/dn/bLxHoz/btrlPoeoynz/U795uDv8y9GkT4tHtLdykK/img.png)

1. feature 브랜치들이 모두 develop 브랜치에 merge 되었다면 QA를 위해 release 브랜치를 생성한다.
2. release 브랜치를 통해 오류가 확인된다면 release 브랜치 내에서 수정을 진행한다.
3. QA와 테스트를 모두 통과했다면, 배포를 위해 release 브랜치를 master 브랜치 쪽으로 merge하며,
4. 만일 release 브랜치 내부에서 오류 수정이 진행되었을 경우 동기화를 위해 develop 브랜치 쪽에도 merge를 진행한다.

**3. 배포 후 관리**

![https://blog.kakaocdn.net/dn/bw4I9Q/btrlOVXIxW0/zf8ol3GOUpRdUAEfyduKZ0/img.png](https://blog.kakaocdn.net/dn/bw4I9Q/btrlOVXIxW0/zf8ol3GOUpRdUAEfyduKZ0/img.png)

1. 만일 배포된 라이브 서버(master)에서 버그가 발생된다면, hotfix 브랜치를 생성하여 버그 픽스를 진행한다.
2. 그리고 종료된 버그 픽스를 master와 develop 양 쪽에 merge하여 동기화 시킨다.