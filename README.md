# django_book-my-show

### Few points to remember
- There is no need to specify id for models, django automatically provides 'id' column to all the models implicitly.
- If we assign a custom primary key, default id column is removed.
- AutoField, makes the column primary key with autoincreament.
- We generally choose 255 max_length for Charfield as it is 1 byte of size in case of string storage in most of the databases.
- Installing django-extension helps use see the sql query being run by django, using its shell_plus (python manage.py shell_plus).
- admin.site.register(Movie), this is how we register on admin.
- We can set various permissions on admin.

### Few syntax to remember when filling model objects (creating rows)
- Enums won't work with ManyToMany relation.
- Not helpful to have default field, when using an Enum with choices. See the code in Movie model in the repo.
```python
# directly create and save the object with this
genre_thriller = Genres.objects.create(genre=Genre.THRILLER)

# genres is a ManyTOMany field. We first saved movie, then added the objects
# Genres.objects.get(genre=Genre.ACTION), this will get me genre object using any column value (Genre.ACTION and Genre.THRILLER here as enums).
movie.genres.add(Genres.objects.get(genre=Genre.ACTION), Genres.objects.get(genre=Genre.THRILLER))

# few more syntax just to look at
>>> genre_comedy = Genres.objects.create(genre=Genre.COMEDY)
>>> genre_mystry = Genres.objects.create(genre=Genre.MYSTRY)
>>> genre_horror = Genres.objects.create(genre=Genre.HORROR)
>>> genre_suspense = Genres.objects.create(genre=Genre.SUSPENSE)
>>> genre_thriller = Genres.objects.get(genre=Genre.THRILLER)
>>> genre_action = Genres.objects.get(genre=Genre.ACTION)
```
