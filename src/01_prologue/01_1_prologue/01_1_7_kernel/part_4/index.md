---
layout: home
title: "시스템 호출 System Calls"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 시스템 호출 System Calls

## 시스템 호출 (System Calls)

### 1. 시스템 호출의 개념

시스템 호출은 사용자 프로그램이 커널의 기능을 사용할 수 있도록 제공하는 인터페이스입니다.

**주요 특징:**
- **권한 모드 전환**: 사용자 모드에서 커널 모드로 전환
- **안전한 인터페이스**: 사용자 프로그램의 직접적인 하드웨어 접근 방지
- **표준화된 API**: POSIX 표준을 따르는 시스템 호출

### 2. 주요 시스템 호출

**파일 조작:**
```c
int open(const char *pathname, int flags);
int close(int fd);
ssize_t read(int fd, void *buf, size_t count);
ssize_t write(int fd, const void *buf, size_t count);
int unlink(const char *pathname);
```

**프로세스 관리:**
```c
pid_t fork(void);
int execve(const char *pathname, char *const argv[], char *const envp[]);
pid_t wait(int *wstatus);
void exit(int status);
```

**메모리 관리:**
```c
void *mmap(void *addr, size_t length, int prot, int flags, int fd, off_t offset);
int munmap(void *addr, size_t length);
void *brk(void *addr);
void *sbrk(intptr_t increment);
```


---

[⬅️ 이전](../)
