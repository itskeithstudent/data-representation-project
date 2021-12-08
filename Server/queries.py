#insertion query for new movie id, movie name and rating id (RatingID joins with Rating table)
insert_movie = '''INSERT INTO Movies
(MovieID, Title, RatingID)
VALUES(%s, %s, %s);'''

#query not currently used, retrieves all rows from movies table
select_all_movie = "SELECT * FROM Movies;"

#retrieves all fields from movie table and joins in rating, populates table displayed in html page
select_all_movie_plus_rating = '''SELECT m.MovieID, m.Title, r.RatingID, r.Rating
FROM Movies m INNER JOIN Rating r ON m.RatingID = r.RatingID;'''

#updates a movie with new title and ratingid, doesn't update movieid as this is primary key
update_movie = '''UPDATE Movies
SET
Title=%s,
RatingID=%s
WHERE MovieID=%s;'''

#delete's single movie from table
delete_movie = '''DELETE FROM Movies
WHERE MovieID=%s;'''

#used when populating dropdown in html page, for updating or adding movie rating
select_all_ratings = "SELECT * FROM Rating;"