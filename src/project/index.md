---
layout: home
title: "리눅스 프로젝트 - 실습 가이드"
description: "리눅스 실습을 위한 프로젝트 가이드. Ubuntu 22.04와 Rocky 9를 활용한 마스터-슬레이브 구성, 테스트 계정 생성, 실습 환경 구축 방법을 학습합니다."
keywords: "리눅스 프로젝트, Ubuntu, Rocky Linux, 마스터-슬레이브, 실습, 테스트 계정, VM 설정"
author: "리눅스 강의 개발팀"
date: 2024-12-01
last_modified_at: 2024-12-01
categories: ["리눅스", "프로젝트", "실습"]
tags: ["리눅스", "프로젝트", "Ubuntu", "Rocky Linux", "마스터-슬레이브", "실습", "테스트 계정", "VM"]
og_title: "리눅스 프로젝트 - 실습 가이드"
og_description: "Ubuntu 22.04와 Rocky 9를 활용한 리눅스 실습 프로젝트 가이드"
og_type: "article"
og_image: "/assets/images/linux-project-og.jpg"
twitter_card: "summary"
twitter_title: "리눅스 프로젝트 - 실습 가이드"
twitter_description: "Ubuntu 22.04와 Rocky 9를 활용한 리눅스 실습 프로젝트"
canonical_url: "https://example.com/linux-project"
---

# 리눅스 프로젝트

## 1.VM 준비
2대의 서버를 준비합니다. 다양한 리눅스의 확습을 위하여 Ubuntu 리눅스와 Rocky 리눅스를 선택합니다. 
* Master : Ubuntu 22.04
* Slave : Rocky9

### 테스트 계정 생성
테스트를 위한 계정을 생성합니다.  

```bash
sudo useradd 계정 # 사용자를 추가합니다.
sudo passwd 계정  # 비밀번호를 변경합니다.
```



