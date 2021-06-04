/* SQL Exercise
====================================================================
We will be working with database imdb.db
You can download it here: https://drive.google.com/file/d/1E3KQDdGJs4a0i1RoYb8DEq0PFxCgI6cN/view?usp=sharing
*/


-- MAKE YOURSELF FAIMLIAR WITH THE DATABASE AND TABLES HERE





--==================================================================
/* TASK I
 Find the id's of movies that have been distributed by “Universal Pictures”.
*/
SELECT movie_distributors.movie_id FROM movie_distributors
JOIN distributors ON distributors.distributor_id = movie_distributors.distributor_id
WHERE distributors.name = 'Universal Pictures'


/* TASK II
 Find the name of the companies that distributed movies released in 2006.
*/
SELECT name FROM movie_distributors
JOIN movies ON movies.movie_id = movie_distributors.movie_id
JOIN distributors ON distributors.distributor_id = movie_distributors.distributor_id
WHERE year = 2006


/* TASK III
Find all pairs of movie titles released in the same year, after 2010.
hint: use self join on table movies.
*/
SELECT * FROM movies a
JOIN movies b ON a.year = b.year
WHERE a.title != b.title AND
a.year > 2010 AND b.year > 2010

/* TASK IV
 Find the names and movie titles of directors that also acted in their movies.
*/
SELECT movies.title, people.name FROM directors
JOIN movies ON movies.movie_id = directors.movie_id
JOIN people ON people.person_id = directors.person_id
JOIN roles ON roles.person_id = people.person_id
WHERE roles.person_id = directors.person_id
GROUP BY movies.title

/* TASK V
Find ALL movies realeased in 2011 and their aka titles.
hint: left join
*/
SELECT movies.title, aka_titles.title FROM movies
LEFT JOIN aka_titles ON aka_titles.movie_id = movies.movie_id
WHERE movies.year = 2011

/* TASK VI
Find ALL movies realeased in 1976 OR 1977 and their composer's name.
*/
SELECT people.name FROM composers
LEFT JOIN movies ON movies.movie_id = composers.movie_id
LEFT JOIN people ON people.person_id = composers.person_id
WHERE movies.year = 1976 OR 
movies.year = 1977

/* TASK VII
Find the most popular movie genres.
*/
SELECT genres.label, COUNT() FROM movie_genres
JOIN genres ON genres.genre_id = movie_genres.genre_id
JOIN movies ON movies.movie_id = movie_genres.movie_id
GROUP BY genres.label
ORDER BY COUNT() DESC
LIMIT 1

/* TASK VIII
Find the people that achieved the 10 highest average ratings for the movies 
they cinematographed.
*/
SELECT people.name, AVG(rating) FROM cinematographers
JOIN movies ON movies.movie_id = cinematographers.movie_id
JOIN people ON people.person_id = cinematographers.person_id
GROUP BY people.name
ORDER BY AVG(rating)
LIMIT 10


/* TASK IX
Find all countries which have produced at least one movie with a rating higher than
8.5.
hint: subquery
*/
SELECT countries.name, COUNT(movies.title) FROM movie_countries
JOIN movies ON movies.movie_id = movie_countries.movie_id
JOIN countries ON countries.country_id = movie_countries.country_id
WHERE movies.rating > 8.5
GROUP BY countries.name;

/* TASK X
Find the highest-rated movie, and report its title, year, rating, and country. There
can be ties; if so, you should report for each of them.
*/
SELECT title, year, rating, name FROM movie_countries
JOIN movies ON movies.movie_id = movie_countries.movie_id
JOIN countries ON countries.country_id = movie_countries.country_id
ORDER BY movies.rating DESC
LIMIT 1



/* STRETCH BONUS
Find the pairs of people that have directed at least 5 movies and whose 
carees do not overlap (i.e. The release year of a director's last movie is 
lower than the release year of another director's first movie).
*/
