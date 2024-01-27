
# SQL

```bash
INSERT INTO users_tb (id, name, create_date) VALUES (
  'marieuig', 'euiyoung hwnag', '2022-01-01'
)

DROP TABLE users_test

CREATE TABLE users_test
(
    id serial primary key,
    name varchar(30) NOT NULL,
    email varchar(30) NOT NULL UNIQUE,
    bio text
);

INSERT INTO users_test (name, email, bio) VALUES
('Angelika Bartlett', 'angelika.bartlett@example.com', 'Lorem ipsum dolor sit amet, 
  consectetur adipisicing elit'),
('Roger Scott', 'roger.scott@example.com', 
 'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'),
('Malia Murray', 'malia.murray@example.com', 'Ut enim ad minim veniam, 
  quis nostrud exercitation ullamco laboris');
```