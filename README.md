[![Sponsor](https://img.shields.io/badge/Sponsor-GitHub-%23EA4AAA)](https://github.com/sponsors/jinydev)


# 개발자를 위한 리눅스
개발자라면 Linux 운영 체제를 함께 배우는 것이 좀더 나은 개발경험과 환경을 구축하는데 도움이 됩니다. 또한, 컴퓨팅 환경을 더 잘 제어하려는 개발자에게 매력적인 운영체제입니다.

## 풀 코스의 리눅스강의
본 저장소의 문서와 커리큘럼은 리눅스를 풀 코스로 학습을 하고자 하는 분들에게 적당합니다. 강사 및 학생들 모두 본 사이트를 통하여 리눅스를 시작하고 학습할 수 있습니다.

## 함께 만들어가는 학습공간
본 사이트는 여러사람들의 기여와 지식 나눔을 통하여 만들어지고 있습니다.

## 🚀 자동 배포 설정

이 프로젝트는 GitHub Actions를 통해 자동으로 빌드되고 배포됩니다.

### 배포 방법

1. **GitHub 저장소에 푸시**
   - `main` 또는 `master` 브랜치에 푸시하면 자동으로 빌드가 시작됩니다.
   - Pull Request를 생성해도 빌드가 실행됩니다.

2. **GitHub Pages 배포**
   - 빌드가 성공적으로 완료되면 자동으로 GitHub Pages에 배포됩니다.
   - 배포된 사이트는 `https://[username].github.io/[repository-name]`에서 확인할 수 있습니다.
   - **배포 경로**: `docs` 디렉토리

### 설정된 GitHub Actions

- **워크플로우 파일**: `.github/workflows/jekyll-gh-pages.yml`
- **트리거**: `main`/`master` 브랜치 푸시 및 Pull Request
- **환경**: Ubuntu 최신 버전
- **지원 언어**: Ruby 3.2, Node.js 18
- **빌드 대상**: `src` 디렉토리
- **배포 대상**: `docs` 디렉토리

### 로컬 개발 환경

로컬에서 개발하려면 다음 명령어를 실행하세요:

```bash
# 의존성 설치
bundle install
npm install

# 로컬 서버 실행
bundle exec jekyll serve
```

### 주의사항

- GitHub Pages는 `main`/`master` 브랜치의 `docs` 디렉토리를 자동으로 배포합니다.
- 빌드 과정에서 Node.js와 Ruby 의존성이 자동으로 설치됩니다.
- 배포 전에 Jekyll 빌드가 성공적으로 완료되어야 합니다.
- `docs` 디렉토리는 `.gitignore`에서 제외되지 않아야 합니다.
