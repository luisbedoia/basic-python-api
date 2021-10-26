CREATE DATABASE users;
GRANT ALL PRIVILEGES ON DATABASE users TO bob;
\c users;

CREATE TABLE users (
	id serial PRIMARY KEY,
	username VARCHAR ( 50 ) UNIQUE NOT NULL,
	ts float NOT NULL,
	cumulative_steps int NOT NULL,
	created_at timestamp DEFAULT CURRENT_TIMESTAMP,
	modified_at timestamp DEFAULT CURRENT_TIMESTAMP
);


INSERT INTO users(id,username, ts, cumulative_steps)
VALUES (1,'jenna', 1503256778463.0, 12323);

INSERT INTO users(id,username, ts, cumulative_steps)
VALUES (2,'james', 1503256824767.0, 587);