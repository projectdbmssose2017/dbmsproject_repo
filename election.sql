CREATE TABLE Account (Handle varchar (140) NOT NULL PRIMARY KEY, BenutzerName varchar (15) NOT NULL);
CREATE TABLE Tweet (TweetID int NOT NULL PRIMARY KEY, Text varchar(140) NOT NULL, Zeitpunkt timestamp without time zone, AnzahlFavoriten int, AnzahlRetweets int, SourceURL varchar(2000), isRetweet boolean, Originalautor varchar(140), AnzahlLangeWoerter int);
CREATE TABLE Hashtag (Tag varchar(139) NOT NULL PRIMARY KEY);
CREATE TABLE Twittert (TweetID int NOT NULL PRIMARY KEY, Handle varchar(140) NOT NULL);
CREATE TABLE Erwaehnt_account (TweetID int NOT NULL, Handle varchar(140) NOT NULL, PRIMARY KEY (TweetID, Handle));
CREATE TABLE Enthaelt (TweetID int NOT NULL, Tag varchar(139) NOT NULL, PRIMARY KEY (TweetID, Tag));
CREATE TABLE Gemeinsam_getwittert_mit (Tag1 varchar(139), Tag2 varchar(139), TweetID int[], PRIMARY KEY (Tag1, Tag2));

 
