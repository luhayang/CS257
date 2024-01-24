DROP TABLE IF EXISTS states;
CREATE TABLE states {
  state char,
  abbreviation char
};

DROP TABLE IF EXISTS cities;
CREATE TABLE cities {
  city char,
  state char,
  population int,
  lat double,
  lon double
};
