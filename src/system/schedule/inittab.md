---
layout: home
---

# inittab
`inittab`은 서 버가 시스템 부팅을 완료한 경우 바로 특정 프로세스를 자동으로 실행시키고자 할 때 해당 프로세스를 지정하여 실행시키는 데몬이다.

## 기본동작
`inittab`은 리눅스 시스템에서 기본 init 프로세스가 실행될 때 읽는 구성 파일입니다. 이 파일은 시스템 `부팅 과정` 중에 사용되며, `시스템 레벨`을 변경하고 `스크립트를 실행`하는 등의 작업을 수행합니다.

## 런레벨
inittab 파일에는 `6개의 레벨(runlevel)`이 정의되어 있으며, 각 레벨에는 실행될 작업이 지정됩니다. 리눅스 시스템의 기본 레벨은 3이며, 이는 다중 사용자 모드(multi-user mode)를 의미합니다. 다중 사용자 모드에서는 다수의 사용자가 시스템에 로그인하여 동시에 작업할 수 있습니다.

inittab 파일에서는 각 레벨에 대해 실행할 명령어를 정의할 수 있습니다. 예를 들어, 시스템 부팅 시 자동으로 실행되어야 하는 서비스나 데몬 등을 등록할 수 있습니다. 또한, 시스템 레벨을 변경할 때 실행되어야 하는 작업을 정의할 수도 있습니다.

## inittab의 변경이력
리눅스(우분투) 표준방식에 의거 `/etc/re.local `파일 맨 마지막 행에 시작 시 구동될 프로세스를 등록함.

`/etc/re.local` 파일 맨 마지막 행에 시작 시 구동될 프로세스를 등록

## 예시
다음은 ruby언어로 작성된 inittab 파일의 예시입니다

```ruby
# Default runlevel. The runlevels used by RHS are:
#   0 - halt (Do NOT set initdefault to this)
#   1 - Single user mode
#   2 - Multiuser, without NFS
#   3 - Full multiuser mode
#   4 - unused
#   5 - X11
#   6 - reboot (Do NOT set initdefault to this)
#
id:3:initdefault:

# Runlevel 0
# Halt the system
l0:0:wait:/sbin/init 0

# Runlevel 1
# Single user mode
l1:1:wait:/sbin/init 1

# Runlevel 6
# Reboot the system
l6:6:wait:/sbin/init 6

# Runlevel 3-5
# Start the system daemons
l3:3:wait:/sbin/init 3
l4:4:wait:/sbin/init 4
l5:5:wait:/sbin/init 5
```

이 예시에서는 시스템 기본 레벨이 3으로 설정되어 있으며, 각 레벨에 대해 실행할 명령어가 정의되어 있습니다. 예를 들어, 시스템 레벨이 3으로 변경될 때 실행되어야 하는 시스템 데몬들은 l3 라인에서 정의되어 있습니다.
