DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quakeTime timestamp with time zone,
  latitude real,
  longitude real,
  quakeDepth real,
  magnitude real,
  seismicNet char,
  place text,
  quakeType text
);
