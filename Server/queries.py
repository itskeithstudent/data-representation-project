#insertion query for new movie id, movie name and 
insert_movie = '''INSERT INTO MOVIES
(MovieID, Title, RatingID)
VALUES(%s, %s, %s);'''

select_all_movie = "SELECT * FROM MOVIES;"