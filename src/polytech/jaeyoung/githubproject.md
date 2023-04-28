---
layout : home
---

Github Projects
======================

# Github Projects

먼저 [Github](https://github.com/)에 들어가서 자신의 레포지토리 아무거나 들어가보면 아래와 같은 화면을 볼 수 있다.

![https://blog.kakaocdn.net/dn/b8OhKQ/btqLFTg1pru/zCMeKvKKGqNZ6IDzqK0GMK/img.png](https://blog.kakaocdn.net/dn/b8OhKQ/btqLFTg1pru/zCMeKvKKGqNZ6IDzqK0GMK/img.png)

그림에서 볼 수 있듯이 Github에서는 **Issue**와 **Project**를 제공해주는데 하나씩 무엇이고 어떻게 사용하는지 알아보자.

# 1. Projects란?

프로젝트는 작업 현황과 진행도를 볼 수 있는 메뉴이다. 이슈, PR(풀 리퀘스트)들을 하나의 작업으로 구분해 그 작업이 현재 어느 정도 진행되었는지 확인할 수 있다.

- To Do : 해야 할 작업
- In Progress : 진행 중인 작업
- Done : 완료된 작업

그리고 Projects를 사용하면 위와 같이 **To do, In Progress, Done**과 같은 기능을 제공해주는데 이것을 통해 프로젝트의 진행상황을 한번에 파악하기가 수월하다는 장점이 있다. 또한 프로젝트에서 일어나는 모든 일을 추적할 수 있고, 마지막으로 본 이후에 어떤 일이 생겼는지 확인할 수 있다. 이제 하나씩 어떤 의미인지 알아보자.

![https://blog.kakaocdn.net/dn/dL90pn/btqLDO2AoAB/ukw5AS5a6h5WzfO1MdAmxK/img.png](https://blog.kakaocdn.net/dn/dL90pn/btqLDO2AoAB/ukw5AS5a6h5WzfO1MdAmxK/img.png)

Projects 탭을 누르면 위와 같은 화면을 볼 수 있다. 여기서 "Create a project"를 눌러보자.

![https://blog.kakaocdn.net/dn/v2NB1/btqLDOaoiTv/MUrafCfkl7ib1HrRCBkoq0/img.png](https://blog.kakaocdn.net/dn/v2NB1/btqLDOaoiTv/MUrafCfkl7ib1HrRCBkoq0/img.png)

그러면 위와 같은 화면을 볼 수 있는데 필자는 Project board name에는 Week1, Description에는 간단한 프로젝트의 설명을 적었다.

그리고 밑에 보면 Project template가 보일 것이다. 이것을 눌러 하나씩 의미를 알아보자.

![https://blog.kakaocdn.net/dn/cO85OE/btqLIGuIx3e/0wUzufCeGV94h2xh2thgd1/img.png](https://blog.kakaocdn.net/dn/cO85OE/btqLIGuIx3e/0wUzufCeGV94h2xh2thgd1/img.png)

- None : 아무 것도 없이 프로젝트만 생성하는 것이다.
- Basic Kanban : To Do, In Progress, Done 이 생성된다.
- Automated kanban : To Do, In Progress, Done이 생성된다. (위에와 다른 것은 **자동화**를 지원한다. 자동화가 무엇인지는 아래에서 자세히 설명한다)
- Automated kanban with reviews : To Do, In Progress, Review In Progress, Reviewer Approved Done 이 생성된다.
- Bug triage : Needs triage, High priority, Low priority, Close가 생성이 된다.

이번 글에서는 **Automated kanban**이라는 것을 이용해서 실습을 할 것이기 때문에 체크를 하고 프로젝트를 만들어 보자.

![https://blog.kakaocdn.net/dn/kGkl0/btqLEk0ZunY/xj9wrNFc1KiLkmFnsPYDmk/img.png](https://blog.kakaocdn.net/dn/kGkl0/btqLEk0ZunY/xj9wrNFc1KiLkmFnsPYDmk/img.png)

Automated kanban을 체크한 후에 프로젝트를 만들면 위와 같이 To Do, In Progress, Done이 생성된 것을 확인할 수 있다. 의미는 아래와 같다.

- To do
    - 새로 추가 되는 모든 이슈가 해당(해야할 것, 새로운 기능 추가, 기능 수정 등등)
    - 새로 추가 되는 모든 PR이 해당
- In Progress
    - 작업이 진행중 이라는 것을 의미
    - 새로 열린 모든 PR이 해당
    - 새로 열린 모든 이슈가 해당
- Done
    - 이슈가 Close되면 해당
    - Merge가 된 PR이 해당

위에서 말한 **자동화**가 여기에서 적용된다. 만약 새로운 이슈를 만들었다면 To do에 해당되기 때문에 이슈가 To do로 이동한다. 그리고 이슈가 close가 되면 자동으로 Done으로 이동하게 된다. 그래서 Project를 통해서 프로젝트의 진행을 한 눈에 보기 쉽다는 것이다.

# 2. Issues란?

**이슈는 작업의 버그 수정, 새로운 추가될 기능, 개선해야하는 기능 등등 모든 것**이 될 수 있다. 모든 활동 내역에 대해 이슈를 등록하고 그 이슈를 기반으로 작업을 진행한다. 그리고 이슈를 만들면 이슈를 열었다(open)라고 하고, 작업이 끝나 이슈를 정리하면 이슈를 닫았다(close)라고 말한다.

### 이슈 만들기(New Issue)

![https://blog.kakaocdn.net/dn/O0Jgz/btqLFnCE9QH/cj9yAXMMOXdqrVm7PNhH8K/img.png](https://blog.kakaocdn.net/dn/O0Jgz/btqLFnCE9QH/cj9yAXMMOXdqrVm7PNhH8K/img.png)

위와 같이 "**New Issue**"를 누르면 이슈를 만들 수 있다.

![https://blog.kakaocdn.net/dn/cg4Udt/btqLEkzV2cV/90qXU134He7XLtoFEivAR1/img.png](https://blog.kakaocdn.net/dn/cg4Udt/btqLEkzV2cV/90qXU134He7XLtoFEivAR1/img.png)

그러면 위와 같은 화면을 볼 수 있다. 여기서 현재 본인이 이슈를 발생시키는 제목을 적어주고 내용에 이슈에 대한 설명을 상세히 적어주면 된다. (내용에 마크다운을 사용할 수 있기 때문에 참고하자)  그리고 여기서 **Assigneers, Labels, Projects, Milestone**을 볼 수 있는데 이것이 의미하는 것이 무엇인지는 아래와 같다.

- Assigneers : 해당 작업의 담당자 (즉, 이슈의 작업자이다)
- Labels : 해당 작업의 성격
- Project : 위에서 만든 Projects 중에서 하나를 선택하면 된다. ex) Week1, Week2, Week3
- Milestone : 프로젝트가 도달해야 하는 목표 지점을 정해두는 것이다.

여기서 Labels을 직접 만들어 커스텀하게 사용할 수 있는데 라벨에 대해 좀 더 정리하고 가보자.

![https://blog.kakaocdn.net/dn/cV4gQC/btqLFSoUKS8/bFLKYkCHygiR0MSuvM3k50/img.png](https://blog.kakaocdn.net/dn/cV4gQC/btqLFSoUKS8/bFLKYkCHygiR0MSuvM3k50/img.png)

Labels를 누르면 위의 그림과 같이 Github에서 기본으로 제공해주는 것들이 있다. 하지만 본인이 원하는 Labels로 커스텀 하고 싶기 때문에 Edit labels를 클릭해보자.

![https://blog.kakaocdn.net/dn/bl6o4D/btqLE2Mknyg/5oHWmfetj6uelawak5hNSK/img.png](https://blog.kakaocdn.net/dn/bl6o4D/btqLE2Mknyg/5oHWmfetj6uelawak5hNSK/img.png)

그리고 "New label" 버튼을 누르면 위와 같은 화면을 볼 수 있다. 그리고 Label name에 필자는 **Server, Gyunny**를 만들었다. 본인이 프로젝트에 필요한 것을 커스텀해서 만들면 된다.

![https://blog.kakaocdn.net/dn/kA9Sf/btqLFnbA7Yg/Szbq6WBDr40IQ1DKz7TQN0/img.png](https://blog.kakaocdn.net/dn/kA9Sf/btqLFnbA7Yg/Szbq6WBDr40IQ1DKz7TQN0/img.png)

그리고 다시 아까 이슈를 만드는 화면으로 돌아와서 위와 같이 이슈에 알맞게 선택 해주면 된다. 이슈 내용에는 마크다운 문법을 사용할 수 있고,  본인이 이슈를 만드는 목적에 맞는 내용을 적어주면 된다.

![https://blog.kakaocdn.net/dn/RYpG8/btqLFSiaAXs/NmggFxUwv9WwKAcKRktPD0/img.png](https://blog.kakaocdn.net/dn/RYpG8/btqLFSiaAXs/NmggFxUwv9WwKAcKRktPD0/img.png)

그리고 위에서 만들었던 Week1의 Projects를 들어가서 보면 자동으로 To do에 이슈가 들어가 있는 것을 알 수 있다.  이렇게 프로젝트를 **Automated kanban**으로 만들었기 때문에 Github에서 제공하는 **자동화**가 진행되는 것을 볼 수 있다.

### 이슈 닫기(Closed)

![https://blog.kakaocdn.net/dn/IwHxh/btqLD1ghmF5/g8mglJ7MMycoRFy8kUlRtK/img.png](https://blog.kakaocdn.net/dn/IwHxh/btqLD1ghmF5/g8mglJ7MMycoRFy8kUlRtK/img.png)

이슈를 닫는 법은 위와 같이 "Close Issue"를 누르면 끝이다. 그리고 나서 다시 Projects 가서 확인하면 아래와 같이 To do에 있던 이슈가 Done으로 자동으로 이동한 것도 확인할 수 있다.

![https://blog.kakaocdn.net/dn/cvLZU6/btqLFS3uoIw/ggKZeDjkpoNn91ohCZEVlK/img.png](https://blog.kakaocdn.net/dn/cvLZU6/btqLFS3uoIw/ggKZeDjkpoNn91ohCZEVlK/img.png)

# Milestone이란?

마일스톤이란 **프로젝트가 도달해야 하는 목표지점을 지정해두는 것**이다. 예를 들어, 3주동안의 프로젝트라면 Projects를 만든 것과 같이 주 단위의 목표를 나눠서 Week1, Week2, Week3로 할 수도 있고, 어떤 A라는 기능을 만들어야 한다면 그 기능에 대한 마일스톤을 만들 수도 있다. 그래서 진행상황을 표현할 수 있다.

![https://blog.kakaocdn.net/dn/b796qq/btqLGZg1pGj/JylBSMGrX66hBI87lJM8k1/img.png](https://blog.kakaocdn.net/dn/b796qq/btqLGZg1pGj/JylBSMGrX66hBI87lJM8k1/img.png)

그리고 Issue 탭에서 보면 위와 같이 Milestones 버튼을 눌러보자.

![https://blog.kakaocdn.net/dn/6W15f/btqLGZg1pMi/XvqPKmP9DtHT92eeykG9V1/img.png](https://blog.kakaocdn.net/dn/6W15f/btqLGZg1pMi/XvqPKmP9DtHT92eeykG9V1/img.png)

그리고 **제목, 기간을 언제까지 설정할 것**인지를 적어주면 된다. (필자는 일주일동안의 진행상황을 보기 위해서 Week1의 마일스톤을 만들었다.)

![https://blog.kakaocdn.net/dn/wxbTz/btqLENV65VW/Spi0CS1GEuKOiUwuWoXjEK/img.png](https://blog.kakaocdn.net/dn/wxbTz/btqLENV65VW/Spi0CS1GEuKOiUwuWoXjEK/img.png)

그러면 위와 같이 만들어지게 되고 해당 마일스톤에 담긴 이슈들의 진행상황을 퍼센트로 보기 좋게 확인할 수 있다.

![https://blog.kakaocdn.net/dn/GOO5g/btqLDNo0Tn6/2Ez9oEQ7Jk8yJS5l4wBVfk/img.png](https://blog.kakaocdn.net/dn/GOO5g/btqLDNo0Tn6/2Ez9oEQ7Jk8yJS5l4wBVfk/img.png)

만들었던 이슈 or 새로운 이슈를 들어가서 Milestone에 위에서 만들었던 Week1을 적용해보자. 그리고 마일스톤의 퍼센트를 확인해보기 위해서 이슈를 2개정도 만들어서 마일스톤을 Week1으로 적용해보고, 하나를 만들자마자 바로 Close 해보겠다.

![https://blog.kakaocdn.net/dn/cjM8kS/btqLD0n9Sbk/3vk5D11XM6o7Z9qi6kfJMk/img.png](https://blog.kakaocdn.net/dn/cjM8kS/btqLD0n9Sbk/3vk5D11XM6o7Z9qi6kfJMk/img.png)

2개의 이슈를 Week1 마일스톤으로 지정하고 바로 1개를 Closed 하니까 진행상황이 0퍼에서 50퍼로 바뀐 것을 확인할 수 있다.