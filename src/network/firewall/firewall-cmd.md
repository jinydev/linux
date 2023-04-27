---
layout: home
---

# firewall-cmd
CentOS에서는 ufw(Uncomplicated Firewall)가 아닌 firewall-cmd 명령을 사용하여 방화벽을 설정합니다. ufw는 Debian 계열의 Linux 배포판에서 기본적으로 사용되는 방화벽 설정 도구입니다.

## firewall-cmd란?
firewall-cmd는 CentOS와 RHEL 계열의 Linux 배포판에서 기본적으로 사용되는 방화벽 설정 도구입니다. firewall-cmd 명령을 사용하여 방화벽 정책을 설정하고, 포트를 열거나 닫을 수 있습니다. 또한, 방화벽 설정을 수정하면서 실시간으로 적용할 수 있도록 firewall-cmd는 시스템에 대한 설정 변경을 즉시 적용합니다.

firewall-cmd 명령은 CentOS 7부터 사용 가능하며, 이전 버전의 CentOS에서는 iptables를 사용하여 방화벽을 설정하였습니다. 그러나 iptables는 복잡한 설정과 규칙 변경이 어려워, CentOS 7에서는 firewall-cmd를 사용하여 보다 쉽게 방화벽 설정을 할 수 있도록 개선되었습니다.

따라서, CentOS에서는 firewall-cmd 명령을 사용하여 방화벽 설정을 해주시면 됩니다.
