---
layout : home
---

Merge의 3가지 방식
======================

# Merge의 3가지 방식

Merge에는 다음 3가지 방식이 있다.

- `Merge Commit`
- `Squash Merging`
- `Rebase Merging`

프로젝트 방향에 맞는 merge 방법을 사용하면 보다 효과적으로 git 이력을 관리할 수 있다.

![https://velog.velcdn.com/images%2Finjoon2019%2Fpost%2F64b1e97a-5e44-40a3-a2ff-9cc642a1e90a%2Fimage.png](https://velog.velcdn.com/images%2Finjoon2019%2Fpost%2F64b1e97a-5e44-40a3-a2ff-9cc642a1e90a%2Fimage.png)

```
$ git checkout my-branch
```

![https://velog.velcdn.com/images%2Finjoon2019%2Fpost%2F7781a348-2ec7-404f-a449-ed92bb74458c%2Fimage.png](https://velog.velcdn.com/images%2Finjoon2019%2Fpost%2F7781a348-2ec7-404f-a449-ed92bb74458c%2Fimage.png)

## Merge

![https://velog.velcdn.com/images%2Finjoon2019%2Fpost%2F8f8c596a-440d-4128-82c7-d05cd24cd6f6%2Fimage.png](https://velog.velcdn.com/images%2Finjoon2019%2Fpost%2F8f8c596a-440d-4128-82c7-d05cd24cd6f6%2Fimage.png)

하나의 브랜치와 다른 브랜치의 변경 이력 전체를 합치는 방법이다.

commit a, b, c를 refer하는 m이 생성되고 m을 통해 a + b + c가 master에 추가된다.

m은 2개의 parent를 가진다.

```
$ git checkout master
$ git merge my-branch
```

## Squash and Merge

![https://velog.velcdn.com/images%2Finjoon2019%2Fpost%2F65da9e89-060e-4903-a174-4ace14a29ec6%2Fimage.png](https://velog.velcdn.com/images%2Finjoon2019%2Fpost%2F65da9e89-060e-4903-a174-4ace14a29ec6%2Fimage.png)

commit a + b + c를 합쳐서 새로운 commit, abc를 만들어지고 master에 추가된다.

abc는 1개의 parent를 가진다.

feature 브랜치의 commit history를 합쳐서 깔끔하게 만들기 위해 사용한다.

```
$ git checkout master
$ git merge --squash my-branch
$ git commit -m "your-commit-message"
```

## Rebase and Merge

![https://velog.velcdn.com/images%2Finjoon2019%2Fpost%2F563848eb-dafb-42d7-a42b-a524b63b8408%2Fimage.png](https://velog.velcdn.com/images%2Finjoon2019%2Fpost%2F563848eb-dafb-42d7-a42b-a524b63b8408%2Fimage.png)

모든 commit들이 합쳐지지 않고 각각 master 브랜치에 추가된다.

각 commit은 모두 하나의 parent를 가진다.

```
$ git checkout my-branch
$ git rebase master
$ git checkout master
$ git merge my-branch
```

Merge는 Merge commit 기록이 추가로 남게 되지만 Rebase의 경우에는 branch 병합 시 Merge commit 기록이 남지 않는다. 따라서 마치 하나의 브랜치에서 작업한 것처럼 보여진다.