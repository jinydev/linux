---
layout : home
---

GIT-FLOW 전략
======================

## **GitLab Flow**

Github에서 말하는 flow는 너무나도 간단하여 배포, 환경 구성, 릴리즈, 통합에 대한 이슈를 남겨둔 것이 많았다. 
그것을 보안하기 위해 GitLab에서 관련 내용들을 추가적으로 덧붙여 설명한 것을 일컫는다.

### **Production branch with GitLab flow**

![https://blog.kakaocdn.net/dn/cpFS3u/btrswUeKUIu/0VzMlqENM1oD2SKo8kPlZ0/img.png](https://blog.kakaocdn.net/dn/cpFS3u/btrswUeKUIu/0VzMlqENM1oD2SKo8kPlZ0/img.png)

pre-production 브랜치가 없는 전략

## ****Environment branches with GitLab flow****

![https://blog.kakaocdn.net/dn/cKg4cN/btrsC9Iih0f/Xl7RoK2KfrzWVkWttjfKNk/img.png](https://blog.kakaocdn.net/dn/cKg4cN/btrsC9Iih0f/Xl7RoK2KfrzWVkWttjfKNk/img.png)

pre-production 브랜치를 두어 staging 단계를 가지는 전략

Gitlab flow의 브랜치는 아래와 같이 사용을 한다.

## **브랜치 설명**

### feature

모든 기능 구현은 feature 브랜치에서 시작한다. feature 브랜치는 master 브랜치에서 분기되고 머지된다.

### master

gitlab flow의 master 브랜치 역할은 git flow의 develop 브랜치와 동일하다. 

master 브랜치는 feature 브랜치에서 병합된 기능에 대해 test를 진행합니다. 
전체적인 테스트가 진행되어 기능에 대한 보장이 되었다면 production 브랜치로 머지한다.

만약 staging 단계를 원한다면 pre-production 브랜치로 머지를 진행한다.

### production

gitlab flow의 production 브랜치 역할은 git flow의 master 브랜치와 동일하다. 

테스트가 끝난 기능에 대해 배포를 하기 위한 브랜치이다.

### pre-production

master → production 브랜치 사이에 pre-production 브랜치를 두어 변경사항을 바로 production에 배포하지 않고 
test server에 배포하여 통합 테스트를 진행하거나 시간을 두고 반영하는 브랜치다.

## **Release branches with GitLab flow**

![https://about.gitlab.com/images/git_flow/release_branches.png](https://about.gitlab.com/images/git_flow/release_branches.png)

`release`한 브런치를 두고서 보안상 문제가 발생한 것이나 백 포트를 위해서 작업을 할 경우, cherry-pick을 이용해서 작업을 진행할 수 도 있다. 
아니면 해당 릴리즈에서 발생하는 버그들을 묶어서 수정하는 방식으로 작업한다. 일반적으로 말하는 ‘upstream first’ 정책이다.