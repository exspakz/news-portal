1. Создать двух пользователей (с помощью метода `User.objects.create_user('username'))`.
```bash
User.objects.create_user('Rick')
User.objects.create_user('Morty')
```


2. Создать два объекта модели `Author`, связанные с пользователями.
```bash
Author.objects.create(authorUser=User.objects.get(id=1))
Author.objects.create(authorUser=User.objects.get(id=2))
```


3. Добавить 4 категории в модель `Category`.
```bash
Category.objects.create(name='Fantastic')
Category.objects.create(name='Science')
Category.objects.create(name='Sport')
Category.objects.create(name='Crime')
```

4. Добавить 2 статьи и 1 новость.
```bash
text_ar1 = ["Adipisicing pig frankfurter consequat.  Quis swine sirloin, minim..."]
text_ar2 = ["T-bone adipisicing occaecat, ad jowl biltong veniam fatback..."]
text_nw1 = ["In pig venison, chuck meatloaf bacon commodo ut drumstick..."]
Post.objects.create(title="I'm first article", text=text_ar1, postAuthor=Author.objects.get(id=1))
Post.objects.create(title="I'm second article", text=text_ar2, postAuthor=Author.objects.get(id=1))
Post.objects.create(title="I'm first news", text=text_nw1, categoryType=Post.NEWS, postAuthor=Author.objects.get(id=2))
```

5. Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
```bash 
PostCategory.objects.create(postThrough=Post.objects.get(id=1), categoryThrough=Category.objects.get(name='Sport'))
PostCategory.objects.create(postThrough=Post.objects.get(id=1), categoryThrough=Category.objects.get(name='Crime'))
PostCategory.objects.create(postThrough=Post.objects.get(id=2), categoryThrough=Category.objects.get(name='Fantastic'))
PostCategory.objects.create(postThrough=Post.objects.get(id=2), categoryThrough=Category.objects.get(name='Science'))
PostCategory.objects.create(postThrough=Post.objects.get(id=3), categoryThrough=Category.objects.get(name='Science'))
PostCategory.objects.create(postThrough=Post.objects.get(id=3), categoryThrough=Category.objects.get(name='Sport'))
```

6. Создать как минимум 4 комментария к разным объектам модели `Post` (в каждом объекте должен быть как минимум один комментарий).
```bash 
Comment.objects.create(text="I'm first comment", commentPost=Post.objects.get(id=1), commentUser=User.objects.get(username='Rick'))
Comment.objects.create(text="I'm second comment", commentPost=Post.objects.get(id=1), commentUser=User.objects.get(username='Morty'))
Comment.objects.create(text="I'm third comment", commentPost=Post.objects.get(id=2), commentUser=User.objects.get(username='Morty'))
Comment.objects.create(text="I'm fourth comment", commentPost=Post.objects.get(id=3), commentUser=User.objects.get(username='Rick'))
```

7. Применяя функции `like()` и `dislike()` к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
```bash
Post.objects.get(id=1).like()
Post.objects.get(id=1).like()
Post.objects.get(id=1).like()
Post.objects.get(id=1).like()
Post.objects.get(id=1).dislike()
Post.objects.get(id=2).like()
Post.objects.get(id=2).like()
Post.objects.get(id=3).like()
Comment.objects.get(id=4).like()
Comment.objects.get(id=4).like()
Comment.objects.get(id=4).like()
Comment.objects.get(id=4).like()
Comment.objects.get(id=4).like()
Comment.objects.get(id=4).like()
Comment.objects.get(id=4).dislike()
Comment.objects.get(id=3).like()
Comment.objects.get(id=3).like()
Comment.objects.get(id=2).like()
Comment.objects.get(id=1).like()
```

8. Обновить рейтинги пользователей.
```bash
Author.objects.get(authorUser__username='Rick').update_rating()
Author.objects.get(authorUser__username='Morty').update_rating()
```

9. Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
```bash
Author.objects.order_by('-rating').values('authorUser__username')[0]
```

10. Вывести дату добавления, `username` автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
```bash
Post.objects.order_by('-rating').values('dateCreation', 'postAuthor__authorUser__username', 'rating', 'title')[0]
Post.objects.order_by('-rating')[0].preview()
```

11. Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
```bash
Post.objects.order_by('-rating')[0].comment_set.all().values('dateCreation', 'commentUser__username', 'rating', 'text')
```