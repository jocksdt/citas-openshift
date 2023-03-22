use citas;
CREATE TABLE quotes (
	Id int AUTO_INCREMENT NOT NULL,
	quotation varchar(255) NULL,
	author varchar(50) NULL,
	PRIMARY KEY ( Id )
);
LOAD DATA INFILE '/tmp/citas.csv'
INTO TABLE quotes
FIELDS TERMINATED BY '|'
ENCLOSED BY '"'
LINES TERMINATED BY '\n';
