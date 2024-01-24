SELECT * FROM earthquakes WHERE quakeDepth BETWEEN 10 AND 20 INTERSECT SELECT * FROM earthquakes WHERE seismicNet='tx';
SELECT * FROM earthquakes WHERE place LIKE '%Panama';
SELECT * FROM earthquakes WHERE quakeDepth BETWEEN 100 AND 300 INTERSECT SELECT * FROM earthquakes WHERE magnitude>4 ORDER BY magnitude DESC;
