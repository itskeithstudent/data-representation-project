DROP DATABASE G00387816_DataRepProject;
CREATE DATABASE G00387816_DataRepProject;

USE G00387816_DataRepProject;

CREATE TABLE Movies(
    MovieID int NOT NULL PRIMARY KEY,
    Title varchar(255) NULL,
    RatingID int NOT NULL
);

INSERT Movies(MovieID,Title,RatingID) VALUES(1, "7 Samurai", 1);
INSERT Movies(MovieID,Title,RatingID) VALUES(2, "Rashomon", 1);
INSERT Movies(MovieID,Title,RatingID) VALUES(3, "12 Angry Men", 1);
INSERT Movies(MovieID,Title,RatingID) VALUES(4, "The Lighthouse", 1);
INSERT Movies(MovieID,Title,RatingID) VALUES(5, "Rocky Horror Picture Show", 3);
INSERT Movies(MovieID,Title,RatingID) VALUES(6, "Blade Runner 2049", 2);
INSERT Movies(MovieID,Title,RatingID) VALUES(7, "The Room", 7);
INSERT Movies(MovieID,Title,RatingID) VALUES(8, "The Phantom Menace", 5);
INSERT Movies(MovieID,Title,RatingID) VALUES(9, "The Force Awakens", 6);





CREATE TABLE Genre(
    MovieID int NOT NULL,
    Genre varchar(255) NULL
);

INSERT Genre(MovieID, Genre) VALUES(1, "Action");
INSERT Genre(MovieID, Genre) VALUES(2, "Horror");
INSERT Genre(MovieID, Genre) VALUES(3, "Thriller");
INSERT Genre(MovieID, Genre) VALUES(4, "Noir");
INSERT Genre(MovieID, Genre) VALUES(5, "Science Fiction");
INSERT Genre(MovieID, Genre) VALUES(6, "Existentialism");
INSERT Genre(MovieID, Genre) VALUES(7, "Indie");
INSERT Genre(MovieID, Genre) VALUES(7, "Absurdist");
INSERT Genre(MovieID, Genre) VALUES(7, "Space Opera");

CREATE TABLE Rating(
    RatingID int NOT NULL,
    Rating varchar(255) NULL
);

INSERT Rating(RatingID, Rating) VALUES(1, "Classic");
INSERT Rating(RatingID, Rating) VALUES(2, "Excellent");
INSERT Rating(RatingID, Rating) VALUES(3, "Cult-Classic");
INSERT Rating(RatingID, Rating) VALUES(4, "Good");
INSERT Rating(RatingID, Rating) VALUES(5, "Bad");
INSERT Rating(RatingID, Rating) VALUES(6, "Meh");
INSERT Rating(RatingID, Rating) VALUES(7, "Drivel");
INSERT Rating(RatingID, Rating) VALUES(7, "So bad it's good!");