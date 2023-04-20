---
layout : home
---

GITHUB-FLOW 전략
======================

## **GITHUB-FLOW 전략**

![https://blog.kakaocdn.net/dn/70a1a/btrAAZMILka/BwnRKBTeZX1UWI8sddApdK/img.png](https://blog.kakaocdn.net/dn/70a1a/btrAAZMILka/BwnRKBTeZX1UWI8sddApdK/img.png)

- Git flow가 좋은 방식이지만 GitHub에 적용하기에는 **복잡**하다는 Scott Chacon의 판단에 따라 만들어진 새로운 깃 관리 방식이다.
- **자동화 개념이 들어가 있다**라는 큰 특징이 존재하며 만일 자동화가 적용되어 있지 않은 곳에서만 수동으로 진행하면 된다.
- Git flow에 비해 흐름이 해졌다.
    
    **단순해짐에 따라 그 규칙도 단순**
    
- 기본적으로 master branch에 대한 규칙만 정확하게 정립되어 있다면 나머지 가지들에 대해서는 특별한 관여를 하지 않으며 pull request기능을 사용하도록 권장한다.

---

### **GitHub-Flow 특징**

- release branch가 명확하게 구분되지 않은 시스템에서의 사용이 유용하다.
- GitHub 자체의 서비스 특성상 배포의 개념이 없는 시스템으로 되어있기 때문에 이 flow가 유용하다.
- 웹 서비스들에 배포의 개념이 없어지고 있는 추세이기 때문에 앞으로도 Git flow에 비해 사용하기에 더 수월할 것이다.
- hotfix와 가장 작은 기능을 구분하지 않는다.모든 구분사항들도 결국 개발자가 전부 수정하는 일들 중 하나이기 때문이다.이 대신 구분하는 것은 우선 순위가 어떤 것이 더 높은지에 대한 것이다.

---

## **Github-Flow 흐름**

**1. 브랜치 생성**

![https://blog.kakaocdn.net/dn/sartC/btrlFbgVPdm/sZbc064FclDUVwNIWjebuk/img.png](https://blog.kakaocdn.net/dn/sartC/btrlFbgVPdm/sZbc064FclDUVwNIWjebuk/img.png)

Github-flow 전략은 기능 개발, 버그 픽스 등 어떤 이유로든 **새로운 브랜치를 생성**하는 것으로 시작된다.

단, 이때 체계적인 분류 없이 브랜치 하나에 의존하게 되기 때문에 **브랜치 이름을 통해 의도를 명확하게** 드러내는 것이 매우 중요하다.

- master 브랜치는 항상 최신 상태며, stable 상태로 product에 배포되는 브랜치다. 이 브랜치에 대해서는 엄격한 role과 함께 사용한다
- **새로운 브랜치는 항상 master 브랜치에서 만든다**
- Git-flow와는 다르게 feature 브랜치나 develop 브랜치가 존재하지 않는다.
- 그렇지만, 새로운 기능을 추가하거나 버그를 해결하기 위한 **브랜치 이름은 자세하게** 어떤 일을 하고 있는지에 대해서 작성해주도록 하자

**2. 개발 & 커밋 & 푸쉬**

![https://blog.kakaocdn.net/dn/CvHSI/btrlD3QSnw0/areYgHfDrZOp9GvHsKK1hK/img.png](https://blog.kakaocdn.net/dn/CvHSI/btrlD3QSnw0/areYgHfDrZOp9GvHsKK1hK/img.png)

개발을 진행하면서 커밋을 남긴다.이때도 브랜치와 같이 커밋 메세지에 의존해야 하기 때문에, 커밋 메세지를 최대한 상세하게 적어주는 것이 중요하다.

- **커밋메시지를 명확하게 작성하자**
- 원격지 브랜치로 **수시로 push** 하자
- Git-flow와 상반되는 방식
- 항상 원격지에 자신이 하고 있는 일들을 올려 다른 사람들도 확인할 수 있도록 해준다
- 이는 하드웨어에 문제가 발생해 작업하던 부분이 없어지더라도, 원격지에 있는 소스를 받아서 작업할 수 있도록 해준다

**3. PR(Pull Request) 생성**

![https://blog.kakaocdn.net/dn/XDeFC/btrlFmhSJ7Y/fx1cePcEtg57k04pd8MuLK/img.png](https://blog.kakaocdn.net/dn/XDeFC/btrlFmhSJ7Y/fx1cePcEtg57k04pd8MuLK/img.png)

피드백이나 도움이 필요할 때, 그리고 merge 준비가 완료되었을 때는 pull request를 생성한다

- pull request는 **코드 리뷰**를 도와주는 시스템
- 이것을 이용해 자신의 코드를 공유하고, 리뷰받는다.
- merge 준비가 완료되었다면 master 브랜치로 반영을 요구한다.

**4. 리뷰 & 토의**

![https://blog.kakaocdn.net/dn/bJXi8B/btrlDAVImKv/dsrlw9Nc1YZkNxogdRSRB0/img.png](https://blog.kakaocdn.net/dn/bJXi8B/btrlDAVImKv/dsrlw9Nc1YZkNxogdRSRB0/img.png)

Pull-Request가 master 브랜치 쪽에 합쳐진다면 곧장 라이브 서버에 배포되는 것과 다름 없으므로, 상세한 리뷰와 토의가 이루어져야 한다.

**5. 테스트**

![https://blog.kakaocdn.net/dn/N7QbA/btrlJNF6YVy/PkLcqZ8Kjr9tzyFZdPCoDk/img.png](https://blog.kakaocdn.net/dn/N7QbA/btrlJNF6YVy/PkLcqZ8Kjr9tzyFZdPCoDk/img.png)

리뷰와 토의가 끝났다면 해당 내용을 라이브 서버(혹은 테스트 환경)에 배포해본다.

배포시 문제가 발생한다면 곧장 master 브랜치의 내용을 다시 배포하여 초기화 시킨다.

**6. 최종 Merge**

![https://blog.kakaocdn.net/dn/cpGa8k/btrlJNMRC3m/miaSfApRLc64KSm2JJPWZ1/img.png](https://blog.kakaocdn.net/dn/cpGa8k/btrlJNMRC3m/miaSfApRLc64KSm2JJPWZ1/img.png)

라이브 서버(혹은 테스트 환경)에 배포했음에도 문제가 발견되지 않았다면 **그대로 master 브랜치에 푸시를 하고, 즉시 배포**를 진행한다.

대부분의 Github-flow 에선 master 브랜치를 최신 브랜치라고 가정하기 때문에 배포 자동화 도구를 이용해서 Merge 즉시 배포를 시킨다.

**master로 merge되고 push 되었을 때는, 즉시 배포되어야한다**

- GitHub-flow의 핵심
- master로 merge가 일어나면 자동으로 배포가 되도록 설정해놓는다. (CI / CD)