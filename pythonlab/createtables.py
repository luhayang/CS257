DROP TABLE IF EXISTS states;
CREATE TABLE states {
  state text,
  abbreviation text
};

DROP TABLE IF EXISTS cities;
CREATE TABLE cities {
  city text,
  state text,
  population int,
  lat double,
  lon double
};
