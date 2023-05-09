CREATE TABLE urls (
    link_id char(7) CONSTRAINT firstkey PRIMARY KEY,
    long_link varchar(250) NOT NULL,
    deleted boolean NOT NULL DEFAULT false
);
