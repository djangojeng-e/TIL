## Django 의 MVC 패턴 

<br>

MVC  패턴이란, Model, View, Controller 로 이루어진 구조를 의미. 

<br>웹 프로그래밍만을 위한 내용이 아닌, 소프트웨어 개발 방법 methodology 이다. 

특정 소프트웨어를 아래 3 단계로 나누어서 개발한다는 방법이다. 

<br>

- Model 
- View
- Controller 

<br>

많은 웹사이트와 웹 프레임워크들이 MVC패턴을 기반으로 만들어져 있고, 웹 프로그래밍 개발자들에게는 친숙한 개발 패턴이다. 

<br>

각, Model, View, 그리고 Controller 부분들이 의미하는바는 아래와 같이 요약할수 있다. 

<br>

- Model - 웹에서 백앤드에 존재하는 데이터베이스를 의미, 알고리즘이나 쿼리 등도 의미하지만, 어떤것을 이루는 데이터라고 보는것이 편함 
- View - 사용자에게 보여지는 것, 웹에서는 당연히 화면을 이야기 할것이고, HTML 파일을 사용자에게 보여주었다면, 화면에 나타나는 겨로가물이 View 가 될것이다. 
- Controller - Model 과 View 를 제어하는 역할을 하는데. 사용자가 view 를 통해 controller 에 요청을 보내면, Controller 는 특정한 프로세스를 처리한다. 예를들면, model 에서 데이터를 가져오거나, 처리된 결과를 View  로 다시 보내어, 사용자에게 표시하는것. 





<br>실제 Django 에서는, MVC 패턴이 이루어 지는데. 

<br>

| 파일      | 패턴       |
| --------- | ---------- |
| models.py | Model      |
| views.py  | Controller |
| templates | View       |

<br>

<br>

## Model 에 대한 정리 

<br>

데이터베이스는, 데이터가 저장되는 테이블로, models.py 파일에서 정의가 된다. 

<br>데이터는 특정 테이블에 저장되고, 테이블을 만들 때 설정한 데이터의 형태를 따르고. 데이터베이스는 이렇게 특정 테이블들의 집합으로 이루어진다. 

<br>

데이터베이스에 저장된 테이블에 있는 데이터들을 저장하거나, 필요한 데이터를 꺼내어 사용하는데. 

<br>

<br>

Django 에서 데이터를 사용하기위해 설정해야 할것은 크게 2가지이다. 

<br>

1. 어떤 데이터베이스를 사용할것인지 설정해 준다.<br>예) SQLite, Oracle, PostgreSQL 등등 
2. 테이블에 대한 형태를 정의해 준다 <br>



<br>

하나의 모델은, 하나의 클래스로 되어 있으며, models.py  파일에 데이터에 대한 정보를 정의해 주었으면, 

<br>Django 서버에 실제로 적용을 해주어야 한다. models.py 에 작성된 모델을 바탕으로 동일한 테이블을 데이터베이스에 만들어 주기 위해서, python manage.py makemigrations 커맨드를 사용한다. 

<br>

makemigrations 명령어를 입력하면, migrations 이란것을 만들어서, 데이터베이스에 대한 초안을 만들어 낸다. 이때 생성되는 파일이 0001_initial.py 같은 파일이다. 

<br>

이 생성된 migrations 를 진짜로 데이터베이스 테이블로 만들어 내려면, 아래 명령어를 실행 해 주어야 한다. 

<br>

python manage.py migrate 

<br>

위 명령어를 사용하면, 데이터베이스가 생성이 되는데. 

<br>제대로 만들어졌는지 확인하기 위해서, dbshell 에 접근해 볼수 있다. 

<br>

<br>

```shell
python manage.py dbshell
```

<br>* 해당 Db 프로그램이 경로에 깔려 있어야 작동한다. 

<br>

## Views 에 대한 정리 

<br>

views.py 파일은, 들어온 요청을 내부적으로 어떻게 처리할지에 대한 함수와 클래스가 존재한다. 

<br>URL 을 통하여 요청이 들어오면, views.py 파일에 존재하는 적절한 함수나 클래스를 호출하여 작업을 수행한후에. 결과물을 templates 에 돌려준다. 

<br>



<br>

## Templates 에 대한 정리 

<br>

Django 에서 templates 는, views 가 처리한 내용을 전달받아 표시하는 파일이다. 

<br>보통은, html 파일로 되어 있어서. 웹에 표시가 된다. 

<br>

<br>



## MVC 페턴 

<br>

<br>

MVC 는 소프트웨어 공학적으로 하나의 디자인 페턴으로. 오랜 기간동안 많은 개발자들에 의해서 생겨난 방법론이다. 사용자에게 보이는 화면 로직, 내부적으로 실행되는 비지니스 로직 들이 서로 영향 없이 시스템 개발이 가능하고, 따로 유지 보수 할수 있다는 장점이 존재한다. 

<br>

웹 프로그래밍 특성상, 사용자에게 보여지는 화면과 내부 로직이 존재하므로, 많은 웹프레임워크가 MVC 패턴을 따르고 있다. 

<br>

크게 아래 별도의 두가지 패턴으로 나누어서, 개발하는 방법론이다. 

<br>

- 사용자에게 보여지는 화면 
- 내부적으로 사용되는 비지니스 로직 

<br>

이를 Django 에 적용해보면, 사용자에게 보여지는 화면은, templates 폴더안에 있는 html 파일들이 될것이고, 

<br>내부적으로 계산되는 로직은, views.py 에서 진행 할수 있다.<br>

<br>

Django 에서 따르는  MVC 패턴을 다시 복습하자면, 

<br>웹 프로그래밍만을 위한 내용이 아닌, 소프트웨어 개발 방법 methodology 이다. 

특정 소프트웨어를 아래 3 단계로 나누어서 개발한다는 방법이다. 

<br>

- Model 
- View
- Controller 

<br>

### Model

<br>

Model 의 역할은, 데이터에 대한 부분들이고, Django 에서 model 은 데이터베이스와 직접적으로 연관되는 개념으로. models.py 파일에 구현을 할수가 있고, 클래스들을 만들고, 변수로 데이터 타입등을 지정할수 있다. 

<br>makemigrations, migrate 명령어들을 통해, models.py 파일을 참조후 데이터베이스에 테이블을 생성한다. 

<br>

models.py 파일에 만든 모델들은, 데이터베이스에서 하나의 테이블이 되고, 테이블내의 데이터 속성들은, 클래스내부 변수와 속성으로 지정해준 이름과 데이터 타입으로 가지게 된다. 

<br>

주로 사용되는 데이터 타입은 아래 테이블에 정리한다. 

<br>

| 데이터 타입  | 설명                                                         |
| ------------ | ------------------------------------------------------------ |
| CharField    | 문자열을 정의하는데에 많이 사용되는 타입. 옵션으로, max_length 값을 지정하여, 최대길이를 지정할수 있다. max_length 를 주지 않는다면, default 값인 None 값을 갖게 된다. |
| DateField    | 날짜 양식에 맞게 저장되는 데이터 타입이다. 기본적으로, python 에서 제공하는 datetime 라이브러리 형태로 표현된다. 게시글의 등록시간 혹은 수정 시간을 기록하고, 데이터 자체에 대한 등록 및 수정 시간을 표시할때 유용하다. |
| EmailField   | 이메일 형식을 가지는 데이터 타입이다. EmailValidator 를 사용하여, 입력되는 문자열이 이메일 형식인지 자동으로 체크해준다. 만약 문자열이 이메일 형식이 아니라면, 데이터 저장 과정에서 오류가 발생한다. |
| FileField    | 파일을 저장할수 있는 데이터 타입으로, FileField 에 실질적으로 저장되는것은 저장되는 파일의 이름이고, upload_to 옵션을 지정하여, 특정위치에 저장한다. |
| TextField    | CharField 와 비슷하게 문자열을 저장하는 데이터 타입으로. CharField 는 varChar 와 매핑되고, TextField 는 textarea 와 매핑된다. TextField 에도 max_length 를 지정할수 있지만, TextField 에서 지정되는 max_length 는 실제 데이터베이스에는 적용되지 않는다. |
| IntegerField | 숫자를 지정하는 데이터 타입으로. 유효 범위는 -2147483648 ~ 2147483647. 조회수나 추천수 등 숫자들을 저장할때 사용되고, 그 외에 다양한 방법이 존재한다. |
| BooleanField | BooleanField 는 참 (True) 또는 거짓 (False) 를 저장하는 데이터 타입이다 |

<br>

<br>

### View

<br><br>

MVC 패턴의 View 에 대해서 생각해보면, view 의 역할은, 사용자에 보여지게 되는 화면이다. 

<br>Django에서 사용자에 보여지는 화면은, templates 폴더에 있는 html 파일들이 될수 있고.<br>

이 파일들은, Controller 에 의해서 데이터를 전달받거나, 전달하는 매개체로 사용된다. 

<br>

Controller 는 이따금씩, 어떤 요청에 의해서, 이 VIew 즉 화면에 보여지는 것의 방식을 바꿀수도 있고. 없앨수도 있다.<br>

<br>

### Controller

<br>

Django 에서 Controller 는 views.py 파일과 연관이 있다. 

<br>views.py 파일은, Controller 역할을 한다. Controller는 사용자에게 보여지는 화면에 대한것이 아니라. <br>뒤에서 진행되는 내부 비지니스 로직을 담당한다. 

<br>

사용자가 입력한 값이나, 누르는 버튼 등, 입력을 받아서 이를 변형하거나, 데이터베이스에 저장 혹은 입력한 값을 처리하는데에 사용하거나 다른 데이터를 꺼내오는 등의 다양한 작업등을 할수 있다.<br>

<br><br>

views.py 파일에는 함수들을 정의하고, 특정 함수내에서 특정 로직을 처리하도록 한다. 

<br>urls.py 파일에서, url 들을 지정할수 있고, 어떤 함수를 호출할지 결정할수 있다.<br>

보통, views.py 파일에 return 은 render 같은 함수를 이용해서, templates 폴더안에 있는 html 을 통하여, 사용자에게 보여질수 있도록, 로직의 처리 결과를 사용자에게 반환하는데에 사용된다. 

<br>

<br>

## MVC vs MTV 

<br>

MVC 패턴을, MTV (Model, Templates, View) 패턴으로 표현하는 경우도 있다. 

<br>

Django 는 구체적으로 얘기하면, MTV  패턴으로 보는것이 맞지만. MVC  패턴을 더 일반화된 개념으로 본다.<br><br>

| MVC        | Django 파일 및 폴더 | MTV      |
| ---------- | ------------------- | -------- |
| Model      | models.py           | Model    |
| View       | templates 폴더      | Template |
| Controller | views.py            | View     |

<br>

MTV 패턴도, MVC 패턴과 크게 다르지 않다.<br>