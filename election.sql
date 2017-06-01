CREATE TABLE account ( Handle varchar (16) NOT NULL PRIMARY KEY, BenutzerName varchar (15) NOT NULL);
CREATE TABLE tweet ( TweetID int NOT NULL PRIMARY KEY, Text varchar(140) NOT NULL, Zeitpunkt timestamp without time zone NOT NULL, AnzahlFavoriten int, AnzahlRetweets int, SourceURL varchar(2000), isRetweet boolean, Originalautor varchar(140), AnzahlLangeWoerter int );
CREATE TABLE twittert ( TweetID int NOT NULL PRIMARY KEY, Handle varchar(16) NOT NULL);
CREATE TABLE Hashtag (Tag varchar(139) NOT NULL PRIMARY KEY);
CREATE TABLE Erwähnt_account ( TweetID int NOT NULL, Handle varchar(16) NOT NULL, PRIMARY KEY (TweetID, Handle));
CREATE TABLE Enthält (TweetID int NOT NULL, Tag varchar(139) NOT NULL, PRIMARY KEY (TweetID, Tag));


 
