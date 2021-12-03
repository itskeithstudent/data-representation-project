#insertion query for new movie id, movie name and 
insert_movie = '''INSERT INTO Movies
(MovieID, Title, RatingID)
VALUES(%s, %s, %s);'''

select_all_movie = "SELECT * FROM Movies;"

select_all_movie_plus_rating = '''SELECT m.MovieID, m.Title, r.RatingID, r.Rating
FROM Movies m INNER JOIN Rating r ON m.RatingID = r.RatingID;'''

update_movie = '''UPDATE Movies
SET
Title=%s,
RatingID=%s
WHERE MovieID=%s;'''

delete_movie = '''DELETE FROM Movies
WHERE MovieID=%s;'''

select_all_ratings = "SELECT * FROM Rating;"