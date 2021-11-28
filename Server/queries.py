#insertion query for new movie id, movie name and 
insert_movie = '''INSERT INTO MOVIES
(MovieID, Title, RatingID)
VALUES(%s, %s, %s);'''

select_all_movie = "SELECT * FROM MOVIES;"

select_all_movie_plus_rating = '''SELECT m.MovieID, m.Title, r.RatingID, r.Rating
FROM MOVIES m INNER JOIN RATING r ON m.RatingID = r.RatingID;'''

update_movie = '''UPDATE MOVIES
SET
Title=%s,
RatingID=%s
WHERE MovieID=%s;'''


delete_movie = '''DELETE FROM MOVIES
WHERE MovieID=%s;'''