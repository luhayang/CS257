--Find all earthquakes with depth from 10 to 20 that are recorded by a seismic station with its code "tx"
SELECT * FROM earthquakes WHERE quakeDepth BETWEEN 10 AND 20 INTERSECT SELECT * FROM earthquakes WHERE seismicNet='tx';

--Find all earthquakes where it occured in "Panama" (containing Panama in its place)
SELECT * FROM earthquakes WHERE place LIKE '%Panama';

--Find all earthquakes with depth from 100 to 300 and magnitude greater than 4, then order them by descending magnitude order
SELECT * FROM earthquakes WHERE quakeDepth BETWEEN 100 AND 300 INTERSECT SELECT * FROM earthquakes WHERE magnitude>4 ORDER BY magnitude DESC;
