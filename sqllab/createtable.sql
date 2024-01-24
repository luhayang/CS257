DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quakeTime timestamp with time zone,
  latitude float,
  longitude float,
  quakeDepth float,
  magnitude float,
  seismicNet char,
  place text,
  quakeType char
);
