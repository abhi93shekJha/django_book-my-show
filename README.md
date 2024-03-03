# django_book-my-show
Requirements for bookmyshow

1. Select a city.
2. A city will have multiple theaters.
3. A theatre will have multiple halls.
2. Show list of movies being shown in the city.
3. We can search a movie.
3. Filter the movies based on language, Genres, Format (2D, 3D, IMAX), Theaters
4. We can book tickets by first selecting a movie then clicking on book tickets.
5. When clicking on booktickets, I can see a list of theaters with show timings. With prices.
6. Clicking on a show takes us to seat selection.
7. After seat selection go to payment page.
8. We can add coupon/promo code on the payment page.
9. We can pay using various payment options.

## Entities
### City
- id: int
- theaters: Theater[]
### Theater
- id: int
- halls: Hall[]
### Hall
- id: int
- shows: Show[]
- seats: Seat[]
### Seat
- id: int
- seat_type: SeatType (RECLINER, GOLD, VIP)
### Show
- id: int
- movie: Movie
- showSeats: ShowSeat[]
### ShowSeat
- id: int
- seat: Seat
- seatStatus: SeatStatus (AVAILABLE, LOCKED, UNAVAILABLE)
### Conceptual entities
#### Payment
- id: int
- amount: double
- payment_mode: PaymentMode
- payment_status: PaymentStatus (PENDING, PAYED, NOT_PAYED)
- pay_strategy: PaymentStrategy
#### Ticket
- id: int
- ticket_status: TicketStatus (BOOKED, CANCELLED)
- payment: Payment
- show: Show
- seats: Seat[]
- user: User
#### User
- id: int
- name: String
- password: String
- email: String

### APIs needed
### For admin
- Django admin for creating cities, movies, Genres.  (http://127.0.0.1:8000/admin/)
- Post /api/v1/theater - for creating a theater.  (http://127.0.0.1:8000/api/v1/theater/)
```json
{
  "city_id": 1,
  "name": "Raj Theater",
  "halls":[{
      "seats":{
          "number_of_sections":3,
          "sections":[
              {
                  "number_of_seats":10,
                  "seat_type":"RECLYNER"
              },
              {
                  "number_of_seats":40,
                  "seat_type":"PLATINUM"
              },
              {
                  "number_of_seats":80,
                  "seat_type":"GOLD"
              }
          ]
      }
   },
   {"seats":{
          "number_of_sections":2,
          "sections":[
                {
                "number_of_seats":10,
                "seat_type":"RECLYNER"
                },
                {
                "number_of_seats":90,
                "seat_type":"PLATINUM"
                }
          ]
      }
  }]
}
```
- Admin can CRUD shows.
- API for creating show - POST api/v1/show  (http://127.0.0.1:8000/api/v1/show)
```json
{
    "hall":39,
    "movie":4
}
```
- API for getting shows by hall_id - GET api/v1/show/<int:hall_id> (http://127.0.0.1:8000/api/v1/show/39)
```json
[
    {
        "hall": 39,
        "movie": 1,
        "movie_name": "Mission Impossible"
    },
    {
        "hall": 39,
        "movie": 3,
        "movie_name": "Lagaan"
    }
}
```
- API for updating show by show_id, PUT api/v1/show/<int:show_id>
- 
### APIs for user
- Show list of movies by city_id, GET /api/v1/city/{city_id}/movies. (http://127.0.0.1:8000/api/v1/city/1/movies)
- Output looks like below.
```json
[
    {
        "id": 7,
        "created_at": "2024-02-19T17:53:19.759573Z",
        "modified_at": "2024-02-27T14:48:48.341478Z",
        "name": "Bhool Bhulaaiya",
        "language": "HINDI",
        "format": "THREE_D",
        "genres": [
            "HORROR",
            "SUSPENSE"
        ]
    },
    {
        "id": 4,
        "created_at": "2024-02-19T17:52:30.340887Z",
        "modified_at": "2024-02-27T14:49:06.766746Z",
        "name": "Sholey",
        "language": "HINDI",
        "format": "TWO_D",
        "genres": [
            "THRILLER",
            "ACTION"
        ]
    }
]
```
### Few points to remember
- For retrieve, put, GenericAPIView will automatically take in the id from url and get or update the data. No need to add any code other than creating a simple serializer.
```python
class MySerializer(serializers.Serializer):
    my_field = serializers.CharField()

class AnotherSerializer(serializers.Serializer):
    my_models = MySerializer(many=True)
{
  "my_models": [
    {"my_field": "value1"},
    {"my_field": "value2"},
    {"my_field": "value3"}
  ]
}
```
- We override 'to_representation' and 'to_internal_value' inside a serializer. Former helps us modify the json being sent in response, while latter is used to modify incoming json payload in request.
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
- ManyToMany do not have on_delete, it is taken care by django internally for the mapping table. If any of the entity in manyToMany field is deleted, django deletes the corresponding rows in intermidiate (mapping) table.
- We can specify our own mapping table using "through" kwarg, when creating a manyToMany field.
- When creating a post body, we can subclass from ModelSerializer to directly convert a model to json body. For more customization we can subclass from serializers.Serializer and specify our own custom fields.
### Points to remember for views
- APIViews should be used when there is an specific task and gives the developer full control to customise the response, with code etc.
- GenericAPIViews along with mixins removes the boilerplates of creating response object, explicit validation etc. It should be used when CRUD operations are related on a particular model.
- create(self, validate_data) method can be overridden in serializer which is called when serializer.save() is called after validation (is_valid()).
- update(self, validate_data, instance) method can be overridden in serializer which is called when serializer.save() is called after validation (is_valid()). instance is the model of the serializer.
- ListAPIView inherits from GenericAPIView and internally uses ListModelMixin to implement get method(internally). We simply will have to specify queryset and serializer.
- Similarly there are other classes (CreateAPIView(post), RetrieveUpdateDestroyAPIView(get, put/patch and delete) ) subclassing GenericAPIView, for readymade usage.
