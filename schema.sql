DROP TABLE IF EXISTS user;

CREATE TABLE user ( id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, password_hash TEXT NOT NULL, description TEXT, api_secret TEXT NOT NULL, admin INTEGER);

CREATE TABLE invite_code ( id INTEGER PRIMARY KEY AUTOINCREMENT, code TEXT UNIQUE NOT NULL)