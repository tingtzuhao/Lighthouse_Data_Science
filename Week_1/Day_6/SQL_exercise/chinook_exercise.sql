/* SQL Exercise
====================================================================
We will be working with database chinook.db
You can download it here: https://drive.google.com/file/d/0Bz9_0VdXvv9bWUtqM0NBYzhKZ3c/view?usp=sharing

 The Chinook Database is about an imaginary video and music store. Each track is stored using one of the digital formats and has a genre. The store has also some playlists, where a single track can be part of several playlists. Orders are recorded for customers, but are called invoices. Every customer is assigned a support employee, and Employees report to other employees.
*/


-- MAKE YOURSELF FAIMLIAR WITH THE DATABASE AND TABLES HERE





--==================================================================
/* TASK I
Which artists did not make any albums at all? Include their names in your answer.
*/
SELECT Name, Title
FROM artists
LEFT JOIN albums ON artists.ArtistId = albums.ArtistId
WHERE Title IS NULL

/* TASK II
Which artists recorded any tracks of the Latin genre?
*/
SELECT artists.Name FROM tracks
JOIN albums ON albums.AlbumId = tracks.AlbumId
JOIN artists ON artists.ArtistId = albums.AlbumId
JOIN genres ON genres.GenreId = tracks.GenreId
WHERE genres.Name = 'Latin'
GROUP BY artists.Name

/* TASK III
Which video track has the longest length?
*/
SELECT tracks.Name, MAX(Milliseconds) FROM tracks
JOIN media_types ON tracks.MediaTypeId = media_types.MediaTypeId
WHERE media_types.Name LIKE '%video%'

/* TASK IV
Find the names of customers who live in the same city as the top employee (The one not managed by anyone).
*/
SELECT customers.FirstName, customers.LastName FROM employees
JOIN customers ON customers.City = employees.City
WHERE ReportsTo IS NULL

/* TASK V
Find the managers of employees supporting Brazilian customers.
*/
SELECT b.FirstName, b.LastName FROM employees a
JOIN customers ON customers.SupportRepId = a.EmployeeId
JOIN employees b ON a.ReportsTo = b.EmployeeId
WHERE customers.Country = 'Brazil'
GROUP BY b.FirstName, b.LastName

/* TASK VI
Which playlists have no Latin tracks?
*/
SELECT playlists.Name FROM playlist_track
JOIN playlists ON playlists.PlaylistId = playlist_track.PlaylistId
JOIN tracks ON tracks.TrackId = playlist_track.TrackId
JOIN genres ON genres.GenreId = tracks.GenreId
WHERE genres.Name != 'Latin'
GROUP BY playlists.Name