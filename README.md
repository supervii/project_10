# Django 종합 프로젝트 구현 

### 1. 프로젝트 소개 📃

본 프로젝트는 github의 organizations를 이용하여 협업하여 Django의 기본 CRD 를 구현하고 데이터베이스 설계와 Seed Data를 구성하는 과정입니다. 이를 Accounts 와 Movies App을 구현하였습니다. 
프로젝트를 진행하는데 있어 협업의 방법을 체계적으로 이해할 수 있는 프로젝트입니다.



### 2. 과정 및 파일에 대한 설명

- 데이터베이스 설계

  각각의 models.py에 필요한 class를 테이블 관계에 맞게 작성합니다. 

  ```python
  #/movies/models.py
  class Genre(models.Model):
      name = models.CharField(max_length=20)
  
      def __str__(self):
          return self.name
      
  
  class Movie(models.Model):
      title = models.CharField(max_length=30)
      audience = models.IntegerField()
      poster_url = models.CharField(max_length=140)
      description = models.TextField()
      like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)
      genres = models.ManyToManyField(Genre, blank=True)
  
      def __str__(self):
          return self.title
  
  
  class Review(models.Model):
      content = models.CharField(max_length=140)
      score = models.IntegerField()
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  
      class Meta:
          ordering = ('-pk',)
      
      def __str__(self):
          return self.content
       
  #/accounts/models.py      
  class User(AbstractUser):
      followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')
  ```

  - Seed Data 구성

    임의의 데이터를 직접 추가하여 더미데이터를 fixture폴더 안에 json 파일로 작성합니다.

    ```json
    // movie.json
    [
    {
      "model": "movies.movie",
      "pk": 1,
      "fields": {
        "title": "\ube14\ub799\uba38\ub2c8",
        "audience": 1275187,
        "poster_url": "https://movie-phinf.pstatic.net/20191113_203/1573610067050zNCj1_JPEG/movie_image.jpg",
        "description": "\uc904\uac70\ub9ac\r\n\uace0\ubc1c\uc740 \uc758\ubb34! \uc218\uc0ac\ub294 \uc9c1\uc9c4!\r\n\ud560\ub9d0\uc740 \ud558\uace0 \uae54 \uac74 \uae50\ub2e4!\r\n\uc77c\uba85 \uc11c\uc6b8\uc9c0\uac80 \u2018\ub9c9\ud504\ub85c\u2019! \uac80\ucc30 \ub0b4\uc5d0\uc11c \uac70\uce68\uc5c6\uc774 \ub9c9 \ub098\uac00\ub294 \ubb38\uc81c\uc801 \uac80\uc0ac\ub85c\r\n \uc774\ub984\uc744 \ub0a0\ub9ac\ub294 \u2018\uc591\ubbfc\ud601\u2019\uc740 \uc790\uc2e0\uc774 \uc870\uc0ac\ub97c \ub2f4\ub2f9\ud55c \ud53c\uc758\uc790\uac00 \uc790\uc0b4\ud558\ub294 \uc0ac\uac74\uc73c\ub85c \uc778\ud574\r\n \ud558\ub8e8 \uc544\uce68\uc5d0 \ubcbc\ub791 \ub05d\uc5d0 \ub0b4\ubab0\ub9b0\ub2e4. \uc5b5\uc6b8\ud55c \ub204\uba85\uc744 \ubc97\uae30 \uc704\ud574 \ub0b4\ub9c9\uc744 \ud30c\ud5e4\uce58\ub358 \uadf8\ub294\r\n \ud53c\uc758\uc790\uac00 \ub300\ud55c\uc740\ud589 \ud5d0\uac12 \ub9e4\uac01\uc0ac\uac74\uc758 \uc911\uc694 \uc99d\uc778\uc774\uc5c8\uc74c\uc744 \uc54c\uac8c \ub41c\ub2e4.\r\n \r\n \uadfc\uac70\ub294 \uc758\ubb38\uc758 \ud329\uc2a4 5\uc7a5! \uc790\uc0b0\uac00\uce58 70\uc870 \uc740\ud589\uc774 1\uc870 7\ucc9c\uc5b5\uc6d0\uc5d0 \ub118\uc5b4\uac04\r\n \ud76c\ub300\uc758 \uc0ac\uac74 \uc55e\uc5d0\uc11c \u2018\uc591\ubbfc\ud601\u2019 \uac80\uc0ac\ub294 \uae08\uc735\uac10\ub3c5\uc6d0, \ub300\ud615 \ub85c\ud38c, \ud574\uc678\ud380\ub4dc \ud68c\uc0ac\uac00 \ub4a4\uc5bd\ud78c\r\n \uac70\ub300\ud55c \uae08\uc735 \ube44\ub9ac\uc758 \uc2e4\uccb4\uc640 \ub9c8\uc8fc\ud558\uac8c \ub418\ub294\ub370\u2026\r\n \r\n \ub300\ud55c\ubbfc\uad6d \ucd5c\ub300\uc758 \uae08\uc735\uc2a4\uce94\ub4e4, \uc0ac\uac74\uc740 \uc544\uc9c1 \ub05d\ub098\uc9c0 \uc54a\uc558\ub2e4!",
        "like_users": [],
        "genres": [
          1,
          6
        ]
      }
    },
    {
      "model": "movies.movie",
      "pk": 2,
      "fields": {
        "title": "\uc2e0\uc758 \ud55c \uc218: \uadc0\uc218\ud3b8",
        "audience": 1926844,
        "poster_url": "https://movie-phinf.pstatic.net/20191029_52/15723135180872xOKy_JPEG/movie_image.jpg",
        "description": "\u201c\uc138\uc0c1\uc740 \ub458 \uc911 \ud558\ub098\uc57c\r\n\ub180\uc774\ud130\uac00 \ub418\ub358\uac00, \uc0dd\uc9c0\uc625\uc774 \ub418\ub358\uac00\u201d\r\n\ubc14\ub451\uc73c\ub85c \ubaa8\ub4e0 \uac83\uc744 \uc783\uc740 \uc544\uc774 \u2018\uadc0\uc218\u2019\r\n \uc720\uc77c\ud558\uac8c \uae30\ub300\ub358 \uc2a4\uc2b9 \ud5c8\uc77c\ub3c4\ub9c8\uc800 \uc783\uace0 \ud640\ub85c \uc0b4\uc544\ub0a8\uc544\r\n \uc138\uc0c1\uc744 \ud5a5\ud55c \ubcf5\uc218\ub97c \uacc4\ud68d\ud55c\ub2e4.\r\n \uc6b4\uba85\uc758 \uc120\ud0dd\uc740 \u795e\uc758 \ub180\uc74c\ud310\uc5d0 \uc788\ub2e4!\r\n \uc790\uc2e0\uc744 \uc0ac\uc9c0\ub85c \ub0b4\ubaac \ub0c9\ud639\ud55c \ub0b4\uae30\ubc14\ub451\ud310\uc73c\ub85c \ub6f0\uc5b4\ub4e0 \uadc0\uc218(\uad8c\uc0c1\uc6b0)\ub294\r\n \uc804\uad6d\uc744 \ub3cc\uc544\ub2e4\ub2c8\uba70 \uadc0\uc2e0 \uac19\uc774 \ubc14\ub451\uc744 \ub450\ub294 \uc790\ub4e4\uacfc \ub300\uacb0\uc744 \ud3bc\uce58\ub294\ub370\u2026\r\n \r\n \uc0ac\ud65c\uc744 \uac74 \ub300\uacb0!\r\n \uc2e0\uc758 \ud55c \uc218\ub97c \ub2e4\uc2dc \ub450\uc2dc\uaca0\uc2b5\ub2c8\uae4c?",
        "like_users": [],
        "genres": [
          2,
          6
        ]
      }
    },
    {
      "model": "movies.movie",
      "pk": 3,
      "fields": {
        "title": "82\ub144\uc0dd \uae40\uc9c0\uc601",
        "audience": 3536715,
        "poster_url": "https://movie-phinf.pstatic.net/20191024_215/1571900079078PNazL_JPEG/movie_image.jpg",
        "description": "\uc904\uac70\ub9ac\r\n1982\ub144 \ubd04\uc5d0 \ud0dc\uc5b4\ub098\r\n \ub204\uad70\uac00\uc758 \ub538\uc774\uc790 \uc544\ub0b4, \ub3d9\ub8cc\uc774\uc790 \uc5c4\ub9c8\ub85c\r\n 2019\ub144 \uc624\ub298\uc744 \uc0b4\uc544\uac00\ub294 \u2018\uc9c0\uc601\u2019(\uc815\uc720\ubbf8).\r\n \ub54c\ub860 \uc5b4\ub518\uac00 \uac07\ud78c \ub4ef \ub2f5\ub2f5\ud558\uae30\ub3c4 \ud558\uc9c0\ub9cc\r\n \ub0a8\ud3b8 \u2018\ub300\ud604\u2019(\uacf5\uc720)\uacfc \uc0ac\ub791\uc2a4\ub7ec\uc6b4 \ub538,\r\n \uadf8\ub9ac\uace0 \uc790\uc8fc \ub9cc\ub098\uc9c0 \ubabb\ud574\ub3c4 \ud56d\uc0c1 \ub4e0\ub4e0\ud55c \uac00\uc871\ub4e4\uc774 \u2018\uc9c0\uc601\u2019\uc5d0\uac90 \ud070 \ud798\uc774\ub2e4.\r\n \r\n \ud558\uc9c0\ub9cc \uc5b8\uc820\uac00\ubd80\ud130 \ub9c8\uce58 \ub2e4\ub978 \uc0ac\ub78c\uc774 \ub41c \uac83\ucc98\ub7fc \ub9d0\ud558\ub294 \u2018\uc9c0\uc601\u2019.\r\n \u2018\ub300\ud604\u2019\uc740 \uc544\ub0b4\uac00 \uc0c1\ucc98 \uc785\uc744\uae4c \ub450\ub824\uc6cc \uadf8 \uc0ac\uc2e4\uc744 \ud138\uc5b4\ub193\uc9c0 \ubabb\ud558\uace0\r\n \u2018\uc9c0\uc601\u2019\uc740 \uc774\ub7f0 \u2018\ub300\ud604\u2019\uc5d0\uac8c \uc5b8\uc81c\ub098 \u201c\uad1c\ucc2e\ub2e4\u201d\ub77c\uba70 \uc6c3\uc5b4 \ubcf4\uc774\uae30\ub9cc \ud558\ub294\ub370\u2026\r\n \r\n \ubaa8\ub450\uac00 \uc54c\uc9c0\ub9cc \uc544\ubb34\ub3c4 \ubab0\ub790\ub358\r\n \ub2f9\uc2e0\uacfc \ub098\uc758 \uc774\uc57c\uae30",
        "like_users": [],
        "genres": [
          1
        ]
      }
    },
    {
      "model": "movies.movie",
      "pk": 4,
      "fields": {
        "title": "\ud130\ubbf8\ub124\uc774\ud130: \ub2e4\ud06c \ud398\uc774\ud2b8",
        "audience": 2339794,
        "poster_url": "https://movie-phinf.pstatic.net/20191030_118/1572411669676j0Arb_JPEG/movie_image.jpg",
        "description": "\uc2ec\ud310\uc758 \ub0a0 \uadf8 \ud6c4, \ubaa8\ub4e0 \uac83\uc774 \ub2e4\uc2dc \uc2dc\uc791\ub41c\ub2e4!\r\n\uc2ec\ud310\uc758 \ub0a0 \uadf8 \ud6c4, \ub4a4\ubc14\ub010 \ubbf8\ub798\r\n \uc0c8\ub85c\uc6b4 \uc778\ub958\uc758 \ud76c\ub9dd \u2018\ub300\ub2c8\u2019(\ub098\ud0c8\ub9ac\uc544 \ub808\uc774\uc988)\ub97c \uc9c0\ud0a4\uae30 \uc704\ud574 \uc288\ud37c \uc194\uc838 \u2018\uadf8\ub808\uc774\uc2a4\u2019(\ub9e5\ucf04\uc9c0 \ub370\uc774\ube44\uc2a4)\uac00\r\n \ubbf8\ub798\uc5d0\uc11c \ucc3e\uc544\uc624\uace0, \u2018\ub300\ub2c8\u2019\ub97c \uc81c\uac70\ud558\uae30 \uc704\ud55c \ud130\ubbf8\ub124\uc774\ud130 \u2018Rev-9\u2019(\uac00\ube0c\ub9ac\uc5d8 \ub8e8\ub098)\uc758 \ucd94\uaca9\uc774 \uc2dc\uc791\ub41c\ub2e4.\r\n \r\n \ucd5c\ucca8\ub2e8 \uae30\uc220\ub825\uc73c\ub85c \ubb34\uc7a5\ud55c \ucd5c\uac15\uc758 \uc801 \ud130\ubbf8\ub124\uc774\ud130 \u2018Rev-9\u2019\uc758 \ubb34\ucc28\ubcc4\uc801\uc778 \uacf5\uaca9\uc5d0 \ucad3\uae30\uae30 \uc2dc\uc791\ud558\ub358\r\n \u2018\uadf8\ub808\uc774\uc2a4\u2019\uc640 \u2018\ub300\ub2c8\u2019 \uc55e\uc5d0 \ud130\ubbf8\ub124\uc774\ud130 \ud5cc\ud130 \u2018\uc0ac\ub77c \ucf54\ub108\u2019(\ub9b0\ub2e4 \ud574\ubc00\ud134)\uac00 \ub098\ud0c0\ub098 \ub3c4\uc6c0\uc744 \uc900\ub2e4.\r\n \r\n \uc778\ub958\uc758 \uc218\ud638\uc790\uc774\uc790 \uae30\uacc4\ub85c \uac15\ud654\ub41c \uc288\ud37c \uc194\uc838 \u2018\uadf8\ub808\uc774\uc2a4\u2019\uc640 \u2018\uc0ac\ub77c \ucf54\ub108\u2019\ub294 \u2018\ub300\ub2c8\u2019\ub97c \uc9c0\ud0a4\uae30 \uc704\ud574\r\n \uc0c8\ub85c\uc6b4 \uc870\ub825\uc790\ub97c \ucc3e\uc544 \ub098\uc11c\uace0, \ud130\ubbf8\ub124\uc774\ud130 \u2018Rev-9\u2019\uc740 \uadf8\ub4e4\uc758 \ub4a4\ub97c \ub048\uc9c8\uae30\uac8c \ucd94\uaca9\ud558\ub294\ub370...\r\n \r\n \ub354 \uc774\uc0c1 \uc815\ud574\uc9c4 \ubbf8\ub798\ub294 \uc5c6\ub2e4\r\n \uc9c0\ud0a4\ub824\ub294 \uc790 VS \uc81c\uac70\ud558\ub824\ub294 \uc790, \uc0c8\ub85c\uc6b4 \uc6b4\uba85\uc774 \uaca9\ub3cc\ud55c\ub2e4!",
        "like_users": [],
        "genres": [
          2,
          7
        ]
      }
    },
    {
      "model": "movies.movie",
      "pk": 5,
      "fields": {
        "title": "\uc544\ub2f4\uc2a4 \ud328\ubc00\ub9ac",
        "audience": 322762,
        "poster_url": "https://movie-phinf.pstatic.net/20191011_62/1570758276142YxXEz_JPEG/movie_image.jpg",
        "description": "\ud3c9\ubc94\ud568\uc740 \uac70\uc808\ud55c\ub2e4!\r\n\uc138\uc0c1\uc5d0\uc11c \uac00\uc7a5 \ubb34\uc12d\uace0 \uc0ac\ub791\uc2a4\ub7ec\uc6b4 \uac00\uc871 \uc5b4\ub4dc\ubca4\ucc98!\r\n\uc5b8\uc81c\ub098 \ucfe8\ud55c \uad34\uc9dc \uc5c4\ub9c8 \u2018\ubaa8\ud2f0\uc2dc\uc544\u2019\ubd80\ud130\r\n \uc0ac\uace0\uce58\ub294 \uc544\uc774\ub4e4\uc774 \uc790\ub791\uc2a4\ub7ec\uc6b4 \uc544\ube60 \u2018\uace0\uba54\uc988\u2019,\r\n \ubd80\ubaa8\ub2d8\uc774 \ubaa8\ub974\ub294 \ub9ce\uc740 \uac78 \uac00\uc9c4 \uc18c\ub140 \u2018\uc6ec\uc988\ub370\uc774\u2019,\r\n \ud3ed\ubc1c\ubb3c \uc2e4\ud5d8\uc774 \ucde8\ubbf8\uc778 \ub9c9\ub0b4 \u2018\ud37d\uc2ac\ub9ac\u2019\uae4c\uc9c0!\r\n \ud3c9\ubc94\uce58 \uc54a\uc740 \u2018\uc544\ub2f4\uc2a4 \ud328\ubc00\ub9ac\u2019\uac00 \ud3c9\ubc94\ud55c \ub3d9\ub124\uc5d0 \ub098\ud0c0\ub0ac\ub2e4.\r\n \uc9c0\uae08\uaecf \ubcf8 \uc801 \uc5c6\ub294 \uac00\uc871\uc758 \ub4f1\uc7a5\uc5d0 \ub9c8\uc744 \uc0ac\ub78c\ub4e4\uc740\r\n \u2018\uc544\ub2f4\uc2a4 \ud328\ubc00\ub9ac\u2019\ub97c \uad34\ubb3c\ub85c \ubab0\uc544\uac00\uae30 \uc2dc\uc791\ud558\ub294\ub370\u2026",
        "like_users": [],
        "genres": [
          3,
          5,
          8
        ]
      }
    }
    ]
    
    //genre.json
    [
    {
      "model": "movies.genre",
      "pk": 1,
      "fields": {
        "name": "\ub4dc\ub77c\ub9c8"
      }
    },
    {
      "model": "movies.genre",
      "pk": 2,
      "fields": {
        "name": "\uc561\uc158"
      }
    },
    {
      "model": "movies.genre",
      "pk": 3,
      "fields": {
        "name": "\uc560\ub2c8\uba54\uc774\uc158"
      }
    },
    {
      "model": "movies.genre",
      "pk": 4,
      "fields": {
        "name": "\uba5c\ub85c/\ub85c\ub9e8\uc2a4"
      }
    },
    {
      "model": "movies.genre",
      "pk": 5,
      "fields": {
        "name": "\ucf54\ubbf8\ub514"
      }
    },
    {
      "model": "movies.genre",
      "pk": 6,
      "fields": {
        "name": "\ubc94\uc8c4"
      }
    },
    {
      "model": "movies.genre",
      "pk": 7,
      "fields": {
        "name": "SF"
      }
    },
    {
      "model": "movies.genre",
      "pk": 8,
      "fields": {
        "name": "\uac00\uc871"
      }
    }
    ]
    
    ```

    - `accounts app` 

      > 유저의 회원 가입과 로그인 로그아웃 기능을 구현해야 합니다.
      >
      > 1. 유저목록(/accounts/)
      >
      >    사용자의 목록을 표시해주고 username을 클릭하면 유저 상세보기 페이지로 이동
      >
      > 2. 유저 상세보기 (/accounts/{user_pk}/)
      >
      >    해당 유저가 작성한 평점 정보 , 좋아하는 영화 정보 및 유저를팔로우한사람의수,팔로잉 한 사람의 수를 출력합니다.  

      - 어려웠던 점 .

        서로가 각각 만든 파일이 바로바로 업데이트 및 적용되지 않아서 연결된 작업을 확인하는데 있어서 어려운 점이 많았습니다. 또한 변수 명이 통일되지 않아서 시간을 소비하였습니다. 

    - `movies app`

      >1. 영화목록(/movies/) 
      >
      >    영화의 이미지를 클릭하면 영화 상세보기 페이지로 넘어갑니다. 
      >
      >2. 영화상세보기(/movies/{movie_pk}/) 
      >
      >   영화 관련 정보가 모두 나열되며 로그인한 사람만 영화평점을 남길 수 있습니다. 영화가 존재 하지 않는 경우 404 페이지를 보여줍니다. 
      >
      >3. 평점생성 
      >
      >​	영화평점은 로그인 한 사람만 남길 수 있습니다. 
      >
      >​	검증을 통해 유효한 경우 데이터베이스에 저장을 하며,아닌경우 영화 정보 조회 	페이지로 Redirect 합니다. 데이터베이스에 저장되면, 해당하는 영화의 영화 	상세보기 페이지로 Redirect 합니다.  영화가 존재 하지 않는 경우 404 페이지	를 보여줍니다. 
      >
      >4. 평점삭제 
      >
      >​	 영화 평점 삭제는 본인만 가능하며,  동적으로 할당되는 부분이 존재합니다. 데	이터 베이스에서 삭제되면, 해당하는 영화의 영화 상세보기 페이지로 Redirect 	합니다. 영화가 존재 하지 않는 경우 404 페이지를 보여줍니다. 
      >
      >5. 영화좋아요기능구현 
      >
      >    좋아하는 영화를 담아 놓을 수 있도록 구현합니다. 로그인한 유저만 해당 기능을사용할 수 있으며,  영화가 존재 하지 않는 경우 404 페이지를 보여줍니다. 

      

      - 어려웠던 점 .

        git hub에 파일을 push 및 pull 하는 과정에서 개인 프로젝트와 달리 request 및 branch 활용을 통해 하는 과정에서 이해가 부족하여 오랜 시간을 소비하였습니다. 

        또한 더미데이터를 생성하는 과정에서 해당 부분의 자료를 찾아보고 문제를 해결하였습니다. 

        

    ### 결과물

    Movies 메인 페이지 

    ![01](https://user-images.githubusercontent.com/52685245/69300707-55d60980-0c57-11ea-8696-79503756a20f.PNG)

    Movies Detail 페이지 

    <img width="254" alt="Screen Shot 2019-11-21 at 12 03 08 PM" src="https://user-images.githubusercontent.com/52685245/69300756-8453e480-0c57-11ea-9909-4a408121b1ab.png">

    Accounts 메인 페이지

    <img width="759" alt="Screen Shot 2019-11-21 at 12 03 28 PM" src="https://user-images.githubusercontent.com/52685245/69300804-a77e9400-0c57-11ea-8a2c-981a4ed3d40e.png">

    

    Accounts Profile  페이지

    ![02](https://user-images.githubusercontent.com/52685245/69300872-caa94380-0c57-11ea-89b5-71644f08749f.PNG)

    

    

### 3. 프로젝트를 통해 느낀 점

처음으로 github을 통해 진행하는 프로젝트임에 구현하는 시간보다 push 와 pull , full request, branch 등 여러 가지 설정에 있어 시간을 너무 많이 소비하게 되었습니다. 최종 프로젝트의 준비과정에 있어서 팀원과의 협업과 방법에 대해서 워밍업할 수 있는 과정이었으며, Django 복습을 통해 전에 학습했던 내용을 돌아볼 수 있었습니다. 