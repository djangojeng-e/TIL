# Branch commands exercises 







```bash

mkdir tutorial 
cd tutorial 
git init

touch myfile.txt

git add myfile.txt 
git commit -m 'first commit'
```





# 브랜치 만들기 





```bash
git branch <branchname> 


# issue1 이라는 이름으로 브랜치 생성. 
git branch issue1

# git branch 명령어로 브랜치 목록 전체를 확인.  
git branch 

git branch 
issue1 
*master 

# * master 가 현재 선택된 브랜치를 표시 *로 표시

```





# 브랜치 전환하기 





```bash
git checkout <branch> 

# checkout 명령어 뒤에 사용할 브랜치 이름을 입력 
# 해당 브랜치로 이동 가능

git checkout issue1 

# checkout 명령에 -b 옵션을 넣으면, 브랜치 작성과 체크아웃을 한꺼번에 실행할수 있음. 

git checkout -b <branch> 

git add myfile.txt 
git commit -m 'add 설명을 추가'

# commit 명령에 -m 옵션을 넣으면 커밋 설명을 포함시킬수 있음. 


```





![현재 시점의 이력](https://backlog.com/git-tutorial/kr/img/post/stepup/capture_stepup2_3_2.png)





# 브랜치 병합





```bash
# 브랜치 병합은 merge 명령어로 실행 

# 1. 마스터 브랜치로 이동 

git checkout master 

# issue1 브랜치에서 파일 편집이 이루어져 있기 때문에 
# master 브랜치에서 myfile.txt 파일을 확인했을때, 그 내용이 변경되어 있지 않아야 함. 

# issue1 브랜치와 master 브랜치를 병합하기 


git merge issue1 


# master 브랜치가 가리키는 커밋이 issue1 브랜치와 같은 위치로 이동 
# 이런식의 병합을 fast-forward(빨리감기) 병합이라고 함. 

# myfile.txt 파일을 열어 내용을 확인해볼 경우 
# issue1 에서 추가된 내용이 파일에 추가되어 있는 것을 확인 할수 있음. 
```





![현재 시점의 이력](https://backlog.com/git-tutorial/kr/img/post/stepup/capture_stepup2_4_1.png)





# 브랜치 삭제하기 





```bash
# issue1 브랜치의 내용이 master에 통합 되었기 때문에 
# 더이상 issue1 브랜치가 필요 없게 됨. 

git branch -d <branchname> 

# issue1 브랜치를 삭제하기 위해 다음 명령어를 실행 
git branch -d issue1 

# issue1 브랜치는 삭제되었기 때문에, 삭제 된것을 확인 하기 위해 아래 명령어를 실행 

git branch 
*master 
```





![현재 시점의 이력](https://backlog.com/git-tutorial/kr/img/post/stepup/capture_stepup2_5_1.png)





# 동시에 여러 작업하기 



```bash
# 두개의 브랜치를 생성하여 동시에 여러 작업을 처리하는 상황 

git branch issue2 	# issue2 브랜치 생성 
git branch issue3 	# issue3 브랜치 생성 

git checkout issue2 # issue2 브랜치로 이동 

git branch 			# 현재 브랜치 목록 확인 
*issue2 
issue3
master 


```







![현재 시점의 이력](https://backlog.com/git-tutorial/kr/img/post/stepup/capture_stepup2_6_1.png)





```bash
# issue2 브랜치에서 myfile.txt 에 내용 추가후, commit 설명 추가 
git add myfile.txt
git commit -m 'commit의 설명 추가'
```



![현재 시점의 이력](https://backlog.com/git-tutorial/kr/img/post/stepup/capture_stepup2_6_2.png)





```bash
# issue3 브랜치로 전환 
git checkout issue3 

# myfile.txt 파일 실행후 내용 확인 
# commit 설명은 issue2 브랜치에서 추가했기 때문에 issue3 브랜치로 전환한 후에 myfile.txt 파일에는 

# Git 명령어 
# add : 변경 사항 만들고 인덱스에 등록 
# pull : 원격 저장소의 내용 가져옴 


git add myfile.txt 
git commit -m 'pull 설명 추가'


```





![현재 시점의 이력](https://backlog.com/git-tutorial/kr/img/post/stepup/capture_stepup2_6_3.png)



issue 2 브랜치에서 내용 추가  

issue 3 브랜치에서 내용 추가 



각각의 브랜치에서 독립적으로 처리된 작업을 브랜치 병합으로 myfile.txt 파일을 마무리 할수 있음. 





# 브랜치 병합 충돌 해결 





```
# master  브랜치로 이동 

git checkout master 

# issue2 브랜치를 병합 

git merget issue2 

```





![현재 시점의 이력](https://backlog.com/git-tutorial/kr/img/post/stepup/capture_stepup2_7_1.png)





```
# issue3 브랜치를 병합 

git merge issue3 

# 자동병합에 실패 coflict 가 남 
# 각각의 브랜치에서 변경한 내용이 myfile.txt의 같은 행에 포함되어 있기 때문. 

# 충돌이 있는 부분에 git 이 자동으로 충돌 정보를 포함하여 파일 내용을 변경함. 
# 어떤 브랜치에서 어떤 부분이 충돌되었는지 확인 할수 있음. 
# 충돌이 일어난 부분은 일일히 확인해서 수정해줘야 함. 

# 충돌 부분 모두 수정완료후, 다시 커밋 

git add myfile.txt 
git commit -m 'issue3 브랜치 병합'


```



충돌 부분을 수정했기 때문에, 그 변화를 기록하는 새로운 병합 커밋이 생성됨. 이 같은 방식을 non-fast-forward 병합이라고 함. 





![현재 시점의 이력](https://backlog.com/git-tutorial/kr/img/post/stepup/capture_stepup2_7_2.png)





# rebase 로 병합하기 







![rebase전의 기록 ](https://backlog.com/git-tutorial/kr/img/post/stepup/capture_stepup2_8_1_1.png)





```bash
git checkout issue3 

git rebase master 
# merge 때와 마찬가지로 myfile.txt 파일 내용에 충돌로 인하여, 문제가 발생함 
# 충돌난 파일 내용을 적절히 변경해 주어야함. 


# rebase 의 경우 충돌 부분을 수정 완료, commit이 아니라, 
# rebase 명령에 --continue 옵션을 지정하여 실행해야함. 

git add myfile.txt 
git rebase --continue 
```





![현재 시점의 이력](https://backlog.com/git-tutorial/kr/img/post/stepup/capture_stepup2_8_1.png)



rebase만 실행한 경우에는 issue3 브랜치가 두 브랜치의 앞쪽으로 위치가 옮겨졌을뿐, master 브랜치는 아직 issue3 의 변경 사항이 적용되지 못한 상태로 뒤에 남겨져 있음.



따라서, master 브랜치로 전환후 issue3 브랜치의 변경 사항을 모두 병합 하여야 함. 



```bash
git checkout master 

git merge issue3 


# myfile.txt 최종 내용은 merge 했을때와 동일하지만, 이력은 아래와 같이 달라짐. 
```





![현재 시점의 이력](https://backlog.com/git-tutorial/kr/img/post/stepup/capture_stepup2_8_2.png)