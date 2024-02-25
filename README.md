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
