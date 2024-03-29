# 텍스트 편집

### 텍스트의 응용 범위
1. 문서 작성 : markup language
2. 웹 페이지 : HTML 또는 XML
3. 이메일
4. 프린터 출력
5. 프로그램 소스 코드

### 텍스트 명령어
- cat : 파일과 표준 출력을 연결
```
옵션 : -A(텍스트 조회) -n, -s(텍스트 수정)
      -ns(공백 제거 + 번호 매기기) 등등
```
- sort : 텍스트 파일의 행 정렬
```
옵션 : -f(대소문자 무시), -n(수치 기준), -r(역순),
      -output=file(정렬 결과를 파일로 출력 등등)
```
- uniq : 중복된 행을 생략하거나 보고
```
중복 결과를 정리하기 위해 sort와 함께 종종 사용
sort foo.txt | uniq
옵션 : -c(중복 발생 횟수 같이 출력), -i(대소문자 무시),
      -u (유일한 행 출력, 기본값), -d(중복된 행 출력)
```
<br>

### 텍스트 자르고 붙이기 명령어
- cut : 행의 일부 영역 제거
```
옵션 : -c, -f, -d 등등
사실, cut이 텍스트를 추출하는 방법은 그리 좋지 않다.
사용자가 직접 입력한 텍스트보다 다른 프로그램이 생성한 파일의 텍슽트를 추출하는게 적합하다.
```
- paste : 행 합치기
```
cut의 반대 명령어
텍스트 열을 추출하는 대신 파일에 하나 이상의 텍스트 열을 추가한다.
```
- join : 공통 필드로 두 파일의 행 합치기
```
join은 paste와 같아 보이지만, 공유키 필드로 복수의 테이블에서 
자료를 가져와 원하는 결과의 형태로 합치는 관계형 데이터베이스와 관련된 작업이다.
join은 공유키 필드 기반으로 복수의 파일로부터 자료를 합친다.
```
<br>

### 텍스트 비교 명령어
- comm : 정렬된 두 파일을 행 단위로 비교 
```
옵션 : -n[1, 2, 3] (제거할 열을 지정, 
오직 두 파일의 공통된 행만 출력되기 원한다면 나머지 행을 제거해서 출력할 수 있다.)
```
- diff : 행 단위로 파일들을 비교
```
comm처럼 파일 간 차이점을 찾을 때 사용
변경 명령 범위 : r1cr2 (r1 위치에 있는 행을 두 번째 파일의 r2 위치의 행으로 변경)
r1ar2 (두 번째 파일의 r2 위치에 있는 행을 첫 번째 파일이 r1 위치에 추가)
r1drc (두 번째 파일의 r2 범위에 있어야 할 행을 첫 번째 파일의 r1 위치에서 삭제)
변경 지시자 : 없음 (문맥 표시 행 두 파일 간의 차이점을 나타내지 않음)
+ (추가된 행, 두 번째 파일에는 나타나지만 첫 번째 파일에는 나타나지 않음)
- (삭제된 행, 첫 번째 파일에는 나타나지만 두 번째 파일에는 나타나지 않음)
| (변경된 행, 두 파일 모두의 각자 영역에 각각 표시된다.)
통합 방식 변경 지시자 : - (첫 번째 파일에서 삭제되었음), + (첫 번째 파일에 추가되었음)
```
- patch : 원본에 diff 적용
```
diff 파일은 전체 소스 트리의 크기에 비해 매우 작으며,
diff 파일은 변경 내역을 간결하게 보여 주기 때문에 원본 파일에 diff를 적용한다면
검토자가 평가를 빠르게 할 수 있다.
```
### 신속한 편집 명령어
- tr : 문자들을 변환하거나 삭제
```
"lowercase letters" | tr a-z A-Z
-> LOWERCASE LETTERS
"lowercase letters" | tr [:lower]
-> AAAAAAAAA AAAAAAA
옵션 : -s(반복 문자 삭제)
```
- sed : 텍스트의 필터링과 반환을 위한 스트림 편집기
```
"front" | sed \s/front/back/
-> back
"front" | sed \1(주소)s/fron/back/'
-> back
주소 표기법 : n(양수인 행 번호), $(마지막 행), addr!(addr을 제외한 모든 행) 등등
옵션 : =(현재 행 번호 출력), a(현재 행 뒤에 텍스트 추가), d(현재 행 삭제) 등등
s/regexp/replacement/ : regexp가 발견될 때마다 replacement의 내용으로 치환
y/set1/set2 : set1 문자들을 set2의 상응하는 문자들로 변환, tr과 달리 동일한 길이이 집합들이 필요
```
- aspell : 대화형 맞춤법 검사기
```
cat > foot.txt
The quick brown fox jimped over the laxy dog.
aspell check foo.txt
The quick brown fox "jimped" over the laxy dog.
-> 문제가 되는 단어를 강조 표시하고, 문제가 되는 단어 대신 추천 철자와 가능한 동작 목록을 표시한다.
The quick brown fox "jumped" over the laxy dog.
```