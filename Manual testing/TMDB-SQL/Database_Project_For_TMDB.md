<h1>Database Project for TMDB (The Movie Database)</h1>

The scope of this project is to use all the SQL knowledge gained throught the Software Testing course and apply them in practice.

Application under test: The Movie Database

Tools used: MySQL Workbench

Database description: The Movie Database is a platform dedicated to collecting, organizing, and managing information related to movies. Its main purpose is to provide users with quick and efficient access to various aspects of films, such as their ratings, genres, actors, and directors. With the help of this database, users can perform advanced searches, obtain relevant statistics, and make informed decisions regarding watching or managing movies.
By covering a wide range of information and relationships between entities, facilitates exploration and interaction with the expansive world of cinematography.
<ol>
<li>Database Schema </li>
<br>
You can find below the database schema that was generated through Reverse Engineer and which contains all the tables and the relationships between them.

The tables are connected in the following way:

<ul>
  <li> movies is connected with movie_rating through a many-to-many relationship which was implemented through movies.movie_id as a primary key and movie_rating.movie_id as a foreign key.</li>
  <li> movies is connected with movie_genre through a many-to-many relationship which was implemented through movies.movie_id as a primary key and movie_genre.movie_id as a foreign key.</li>
  <li> movies is connected with movie_actor through a many-to-many relationship which was implemented through movies.movie_id as a primary key and movie_actor.movie_id as a foreign key.</li>
  <li> movies is connected with movie_director through a many-to-many relationship which was implemented through movies.movie_id as a primary key and movie_director.movie_id as a foreign key.</li>
  <li> ratings is connected with movie_rating through a many-to-many relationship which was implemented through ratings.rating_id as a primary key and movie_rating.rating_id as a foreign key.</li>
  <li> genres is connected with movie_genres through a many-to-many relationship which was implemented through genres.genres_id as a primary key and movie_genre.g_id as a foreign key.</li>
  <li> actors is connected with movie_actor through a many-to-many relationship which was implemented through actorss.actor_id as a primary key and movie_actor.actor_id as a foreign key.</li>
  <li> director is connected with movie_director through a many-to-many relationship which was implemented through director.director_id as a primary key and movie_director.director_id as a foreign key.</li>
  
  ...........
</ul><br>

<li>Database Queries</li><br>

<ol type="a">
  <li>DDL (Data Definition Language)</li>

  The following instructions were written in the scope of CREATING the structure of the database (CREATE INSTRUCTIONS)

create database TMDB;

create table movies 
(
movie_id int auto_increment primary key,
title varchar(25) not null,
year int,
rating decimal,
release_date date);

create table actors (
actor_id int auto_increment primary key,
name varchar(50) not null,
birth_date date);

create table director (
director_id int auto_increment primary key,
name varchar(50) not null,
birth_date date);

create table genres (
genres_id int auto_increment primary key,
name varchar(50) not null);
select * from genres;

create table movie_genre (
movie_genre_id int auto_increment primary key,
movie_id int,
genres_id int,
foreign key (movie_id) references movies(movie_id),
foreign key (genres_id) references genres(genres_id)
);

create table movie_genre (
movie_genre_id int auto_increment primary key,
m_id int,
g_id int,
foreign key (m_id) references movies(movie_id),
foreign key (g_id) references genres(genres_id)
);

create table ratings (
rating_id int auto_increment primary key,
rating decimal ); 

create table movie_rating (
movie_rating_id int auto_increment primary key,
movie_id int,
rating_id int,
foreign key (movie_id) references movies(movie_id),
foreign key (rating_id) references ratings(rating_id)
);

create table movie_actor (
movie_actor_id int auto_increment primary key,
movie_id int,
actor_id int,
foreign key (movie_id) references movies(movie_id),
foreign key (actor_id) references actors(actor_id)
);

create table movie_director (
movie_director_id int auto_increment primary key,
movie_id int,
director_id int,
foreign key (movie_id) references movies(movie_id),
foreign key (director_id) references director(director_id)
);


  After the database and the tables have been created, a few ALTER instructions were written in order to update the structure of the database, as described below:

alter table movies
add column genre varchar(50);

alter table movies
drop column year;

alter table movies
drop column genre;

alter table movies 
modify column rating float;

alter table ratings
modify column rating float;

alter table movies
modify title varchar(100);

alter table movies
drop column rating;

  
  <li>DML (Data Manipulation Language)</li>

  In order to be able to use the database I populated the tables with various data necessary in order to perform queries and manipulate the data. 
  In the testing process, this necessary data is identified in the Test Design phase and created in the Test Implementation phase. 

  Below you can find all the insert instructions that were created in the scope of this project:

insert into movies (title, rating, release_date) values ("The Beekeeper", 0.73, "2024-01-19");

insert into movies (title, rating, release_date) values ("The Shawshank Redemption", 0.87, "1994-09-23");

insert into movies (title, rating, release_date) values ("Good Fellas", 0.85, "1990-09-19");

insert into movies (title, rating, release_date) values ("Mutant:Ghost War Girl", 0.52, "2022-06-26");

insert into movies (title, rating, release_date) values ("The Hunger Games:The Ballad of Songbirds & Snakes", 0.72, "2023-11-17");

insert into movies (title, rating, release_date) values ("Patriots Time", 0.83, "2022-04-28");

insert into movies (title, rating, release_date) values ("Genghis Khan ", 0.49, "2018-04-28");

insert into movies (title, rating, release_date) values ("The OctoGames", 0.59, "2024-01-19");

insert into movies (title, rating, release_date) values ("The Beekeeper", 0.73, "2022-07-10");

insert into movies (title, rating, release_date) values ("The Farm", 0.52, "2019-04-19");

insert into movies (title, rating, release_date) values ("Thanksgiving", 0.67, "2023-11-16");

insert into movies (title, rating, release_date) values ("The Hill", 0.75, "2023-08-18");

insert into movies (title, rating, release_date) values ("Schindler's List", 0.86, "1993-12-15");

insert into movies (title, rating, release_date) values ("Fury", 0.75, "2014-10-15");

insert into movies (title, rating, release_date) values ("TLift", 0.66, "2024-01-10");

insert into movies (title, rating, release_date) values ("Leo", 0.75, "2023-11-17");

insert into movies (title, rating, release_date) values ("Turning Red", 0.74, "2022-03-10");

insert into movies (title, rating, release_date) values ("Dune", 0.78, "2021-09-15");

insert into movies (title, rating, release_date) values ("Transformers: Rise of the Beasts", 0.74, "2023-01-06");

insert into movies (title, rating, release_date) values ("Mutant: Ghost War Girl", 0.52, "2022-09-26");

insert into movies (title, rating, release_date) values ("Foxtrot Six", 0.65, "2019-02-21");

insert into movies (title, rating, release_date) values ("The Creator", 0.71, "2023-09-27");

insert into movies (title, rating, release_date) values ("Meg 2: The Trench", 0.67, "2023-08-02");

insert into movies (title, rating, release_date) values ("Avatar: The Way of Water", 0.76, "2012-12-14");

insert into movies (title, rating, release_date) values ("Thanksgiving", 0.67, "2023-11-16");

insert into movies (title, rating, release_date) values ("Wish", 0.67, "2023-11-13");

insert into movies (title, rating, release_date) values ("The Boy and the Heron", 0.75, "2023-07-14");

insert into movies (title, rating, release_date) values ("Elemental", 0.77, "2023-06-14");

insert into movies (title, rating, release_date) values ("Puss in Boots: The Last Wish", 0.83, "2022-12-07");

insert into movies (title, rating, release_date) values ("Minions: The Rise of Gru", 0.73, "2022-07-29");

insert into movies (title, rating, release_date) values ("Trolls Band Together", 0.73, "2023-10-12");

insert into movies (title, rating, release_date) values ("Sing 2", 0.79, "2021-12-01");

insert into movies (title, rating, release_date) values ("Maestro", 0.65, "2023-11-22");

insert into movies (title, rating, release_date) values ("La La Land", 0.79, "2016-11-29");

insert into movies (title, rating, release_date) values ("Bohemian Rhapsody", 0.80, "2018-10-24");

insert into movies (title, rating, release_date) values ("Magic Mike's Last Dance", 0.67, "2023-02-09");

insert into movies (title, rating, release_date) values ("Django", 0.63, "2017-04-26");

insert into movies (title, rating, release_date) values ("CODA", 0.79, "2021-08-11");

insert into movies (title, rating, release_date) values ("Lyle, Lyle, Crocodile", 0.72, "2022-10-07");

insert into movies (title, rating, release_date) values ("Pitch Perfect 2", 0.69, "2015-05-07");

insert into movies (title, rating, release_date) values ("The Magic Flute", 0.64, "2022-09-30");

insert into movies (title, rating, release_date) values ("Alvin and the Chipmunks: The Squeakquel", 0.56, "2009-12-21");

insert into movies (title, rating, release_date) values ("Alvin and the Chipmunks: Chipwrecked", 0.57, "2011-12-14");

insert into movies (title, rating, release_date) values ("Whitney Houston: I Wanna Dance with Somebody", 0.70, "2022-12-20");

insert into movies (title, rating, release_date) values ("The Sound of Music", 0.77, "1965-03-29");

insert into movies (title, rating, release_date) values ("Descendants 2", 0.74, "2017-07-21");

insert into movies (title, rating, release_date) values ("An Audience With Kylie", 0.50, "2023-12-10");

insert into movies (title, rating, release_date) values ("Hotel Transylvania:Transformania", 0.70, "2022-02-25");

insert into movies (title, rating, release_date) values ("The Lord of the Rings: The Fellowship of the Ring", 0.84, "2001-12-18");

insert into movies (title, rating, release_date) values ("Pirates of the Caribbean: At World's End", 0.72, "2007-05-19");

insert into movies (title, rating, release_date) values ("Shortcut", 0.55, "2020-09-25");

insert into movies (title, rating, release_date) values ("The Moosehead Chronicles: Fate of the Moosehead", 1.0, "2018-08-03");

insert into movies (title, rating, release_date) values ("The Cabbage-Patch Fairy", 0.52, "1896-05-31");

insert into movies (title, rating, release_date) values ("Cinderella", 0.63, "1898-08-01");

insert into movies (title, rating, release_date) values ("The Human Fly", 0.58, "1902-01-01");

insert into movies (title, rating, release_date) values ("Ted", 0.64, "2012-06-29");

insert into movies (title, rating, release_date) values ("Shang-Chi and the Legend of the Ten Rings", 0.76, "2021-09-01");

insert into movies (title, rating, release_date) values ("How to Train Your Dragon", 0.78, "2010-03-18");

insert into movies (title, rating, release_date) values ("Teddy's Christmas", 0.72, "2022-11-05");

insert into movies (title, rating, release_date) values ("Alice in Wonderland", 0.66, "2010-03-03");

insert into movies (title, rating, release_date) values ("Zuhause", 0, "2015-06-06");

insert into movies (title, rating, release_date) values ("The Hardest Hour", 0, "2024-02-10");

insert into genres ( name ) values ("comedy");<br>
insert into genres ( name ) values ("science fiction");<br>
insert into genres ( name ) values ("action");<br>
insert into genres ( name ) values ("horror");<br>
insert into genres ( name ) values ("music");<br>
insert into genres ( name ) values ("animation");<br>
insert into genres ( name ) values ("history");<br>
insert into genres ( name ) values ("fantasy");<br>
insert into genres ( name ) values ("adventure");<br>
insert into genres ( name ) values ("documentary");<br>
insert into genres ( name ) values ("drama");<br>
insert into genres ( name ) values ("family");<br>
insert into genres ( name ) values ("mystery");<br>
insert into genres ( name ) values ("romance");<br>
insert into genres ( name ) values ("science fiction");<br>
insert into genres ( name ) values ("thriller");<br>
insert into genres ( name ) values ("war");<br>
insert into genres ( name ) values ("western");<br>
insert into genres ( name ) values ("crime");<br>

insert into ratings (rating) values (1.0);<br>
insert into ratings (rating) values (0.99);<br>
insert into ratings (rating) values (0.98);<br>
insert into ratings (rating) values (0.97);<br>
insert into ratings (rating) values (0.96);<br>
insert into ratings (rating) values (0.95);<br>
insert into ratings (rating) values (0.94);<br>
insert into ratings (rating) values (0.93);<br>
insert into ratings (rating) values (0.92);<br>
insert into ratings (rating) values (0.91);<br>
insert into ratings (rating) values (0.90);<br>
insert into ratings (rating) values (0.89);<br>
insert into ratings (rating) values (0.88);<br>
insert into ratings (rating) values (0.87);<br>
insert into ratings (rating) values (0.86);<br>
insert into ratings (rating) values (0.85);<br>
insert into ratings (rating) values (0.84);<br>
insert into ratings (rating) values (0.83);<br>
insert into ratings (rating) values (0.82);<br>
insert into ratings (rating) values (0.81);<br>
insert into ratings (rating) values (0.80);<br>
insert into ratings (rating) values (0.79);<br>
insert into ratings (rating) values (0.78);<br>
insert into ratings (rating) values (0.77);<br>
insert into ratings (rating) values (0.76);<br>
insert into ratings (rating) values (0.75);<br>
insert into ratings (rating) values (0.74);<br>
insert into ratings (rating) values (0.73);<br>
insert into ratings (rating) values (0.72);<br>
insert into ratings (rating) values (0.71);<br>
insert into ratings (rating) values (0.70);<br>
insert into ratings (rating) values (0.69);<br>
insert into ratings (rating) values (0.68);<br>
insert into ratings (rating) values (0.67);<br>
insert into ratings (rating) values (0.66);<br>
insert into ratings (rating) values (0.65);<br>
insert into ratings (rating) values (0.64);<br>
insert into ratings (rating) values (0.63);<br>
insert into ratings (rating) values (0.62);<br>
insert into ratings (rating) values (0.61);<br>
insert into ratings (rating) values (0.60);<br>
insert into ratings (rating) values (0.59);<br>
insert into ratings (rating) values (0.71);<br>
insert into ratings (rating) values (0.70);<br>
insert into ratings (rating) values (0.69);<br>
insert into ratings (rating) values (0.68);<br>
insert into ratings (rating) values (0.67);<br>
insert into ratings (rating) values (0.66);<br>
insert into ratings (rating) values (0.65);<br>
insert into ratings (rating) values (0.64);<br>
insert into ratings (rating) values (0.63);<br>
insert into ratings (rating) values (0.62);<br>
insert into ratings (rating) values (0.61);<br>
insert into ratings (rating) values (0.60);<br>
insert into ratings (rating) values (0.59);<br>
insert into ratings (rating) values (0.58);<br>
insert into ratings (rating) values (0.57);<br>
insert into ratings (rating) values (0.56);<br>
insert into ratings (rating) values (0.55);<br>
insert into ratings (rating) values (0.54);<br>
insert into ratings (rating) values (0.53);<br>
insert into ratings (rating) values (0.52);<br>
insert into ratings (rating) values (0.51);<br>
insert into ratings (rating) values (0.50);<br>
insert into ratings (rating) values (0.49);<br>
insert into ratings (rating) values (0.48);<br>
insert into ratings (rating) values (0.47);<br>
insert into ratings (rating) values (0.46);<br>
insert into ratings (rating) values (0.45);<br>
insert into ratings (rating) values (0.44);<br>
insert into ratings (rating) values (0.43);<br>
insert into ratings (rating) values (0.42);<br>
insert into ratings (rating) values (0.41);<br>
insert into ratings (rating) values (0.40);<br>
insert into ratings (rating) values (0.39);<br>
insert into ratings (rating) values (0.38);<br>
insert into ratings (rating) values (0.37);<br>
insert into ratings (rating) values (0.36);<br>
insert into ratings (rating) values (0.35);<br>
insert into ratings (rating) values (0.34);<br>
insert into ratings (rating) values (0.33);<br>
insert into ratings (rating) values (0.44);<br>
insert into ratings (rating) values (0.43);<br>
insert into ratings (rating) values (0.42);<br>
insert into ratings (rating) values (0.41);<br>
insert into ratings (rating) values (0.40);<br>
insert into ratings (rating) values (0.39);<br>
insert into ratings (rating) values (0.38);<br>
insert into ratings (rating) values (0.37);<br>
insert into ratings (rating) values (0.36);<br>
insert into ratings (rating) values (0.35);<br>
insert into ratings (rating) values (0.34);<br>
insert into ratings (rating) values (0.33);<br>
insert into ratings (rating) values (0.32);<br>
insert into ratings (rating) values (0.31);<br>
insert into ratings (rating) values (0.30);<br>
insert into ratings (rating) values (0.29);<br>
insert into ratings (rating) values (0.28);<br>
insert into ratings (rating) values (0.27);<br>
insert into ratings (rating) values (0.26);<br>
insert into ratings (rating) values (0.25);<br>
insert into ratings (rating) values (0.24);<br>
insert into ratings (rating) values (0.23);<br>
insert into ratings (rating) values (0.22);<br>
insert into ratings (rating) values (0.21);<br>
insert into ratings (rating) values (0.31);<br>
insert into ratings (rating) values (0.30);<br>
insert into ratings (rating) values (0.29);<br>
insert into ratings (rating) values (0.28);<br>
insert into ratings (rating) values (0.27);<br>
insert into ratings (rating) values (0.26);<br>
insert into ratings (rating) values (0.25);<br>
insert into ratings (rating) values (0.24);<br>
insert into ratings (rating) values (0.23);<br>
insert into ratings (rating) values (0.22);<br>
insert into ratings (rating) values (0.21);<br>
insert into ratings (rating) values (0.31);<br>
insert into ratings (rating) values (0.30);<br>
insert into ratings (rating) values (0.29);<br>
insert into ratings (rating) values (0.28);<br>
insert into ratings (rating) values (0.27);<br>
insert into ratings (rating) values (0.26);<br>
insert into ratings (rating) values (0.25);<br>
insert into ratings (rating) values (0.24);<br>
insert into ratings (rating) values (0.23);<br>
insert into ratings (rating) values (0.22);<br>
insert into ratings (rating) values (0.21);<br>
insert into ratings (rating) values (0.20);<br>
insert into ratings (rating) values (0.19);<br>
insert into ratings (rating) values (0.18);<br>
insert into ratings (rating) values (0.17);<br>
insert into ratings (rating) values (0.16);<br>
insert into ratings (rating) values (0.15);<br>
insert into ratings (rating) values (0.14);<br>
insert into ratings (rating) values (0.13);<br>
insert into ratings (rating) values (0.12);<br>
insert into ratings (rating) values (0.11);<br>
insert into ratings (rating) values (0.10);<br>
insert into ratings (rating) values (0.23);<br>
insert into ratings (rating) values (0.22);<br>
insert into ratings (rating) values (0.21);<br>
insert into ratings (rating) values (0.20);<br>
insert into ratings (rating) values (0.19);<br>
insert into ratings (rating) values (0.18);<br>
insert into ratings (rating) values (0.17);<br>
insert into ratings (rating) values (0.16);<br>
insert into ratings (rating) values (0.15);<br>
insert into ratings (rating) values (0.14);<br>
insert into ratings (rating) values (0.13);<br>
insert into ratings (rating) values (0.12);<br>
insert into ratings (rating) values (0.11);<br>
insert into ratings (rating) values (0.10);<br>
insert into ratings (rating) values (0.09);<br>
insert into ratings (rating) values (0.08);<br>
insert into ratings (rating) values (0.07);<br>
insert into ratings (rating) values (0.06);<br>
insert into ratings (rating) values (0.05);<br>
insert into ratings (rating) values (0.04);<br>
insert into ratings (rating) values (0.03);<br>
insert into ratings (rating) values (0.02);<br>
insert into ratings (rating) values (0.01);<br>
insert into ratings (rating) values (0);<br>

insert into actors (name, birth_date) values ("Jason Statham", "1967-07-26");

insert into actors (name, birth_date) values ("Jason Momoa", "1979-08-01");

insert into actors (name, birth_date) values ("Nicole Kidman", "1967-06-20");

insert into actors (name, birth_date) values ("Kevin Hart", "1979-07-06");

insert into actors (name, birth_date) values ("Ursula Corbero", "1989-08-11");

insert into actors (name, birth_date) values ("Emma Stone", "1988-11-06");

insert into actors (name, birth_date) values ("Willem Dafoe", "1955-07-22");

insert into actors (name, birth_date) values ("Mark Ruffalo", "1967-11-22");

insert into actors (name, birth_date) values ("John Brungot", "1977-01-16");

insert into actors (name, birth_date) values ("Mariann Hole", "1981-10-29");

insert into actors (name, birth_date) values ("Kai Remlov", "1946-12-30");

insert into actors (name, birth_date) values ("Nader Khademi", "1986-09-17");

insert into actors (name, birth_date) values ("Jonah Hill", "1969-11-13");

insert into actors (name, birth_date) values ("Gerard Butler", "1969-11-13");

insert into actors (name, birth_date) values ("America Ferrera", "1984-04-18");

insert into actors (name, birth_date) values ("Simu Liu", "1989-04-19");

insert into actors (name, birth_date) values ("Meng'er Zhang", "1987-04-22");

insert into actors (name, birth_date) values ("Florian Munteanu", "1990-10-13");

insert into actors (name, birth_date) values ("Benedict Wong", "1971-06-03");

insert into actors (name, birth_date) values ("Georges Méliès", "1938-01-21");

insert into actors (name, birth_date) values ("Lily James", "1989-04-05");

insert into actors (name, birth_date) values ("Meng'er Zhang", "1987-04-22");

insert into actors (name, birth_date) values ("Cate Blanchett", "1969-05-14");

insert into actors (name, birth_date) values ("Holliday Grainger", "1988-03-27");

insert into actors (name, birth_date) values ("Alice Guy-Blaché", "1873-07-01");

insert into actors (name) values ("Andrew Gerber");

insert into actors (name) values ("Joshua Pitt");

insert into actors (name) values ("Jack Kane");

insert into actors (name, birth_date) values ("Johnny Depp", "1963-06-09");

insert into actors (name, birth_date) values ("Orlando Bloom", "1977-01-13");

insert into actors (name, birth_date) values ("Keira Knightley", "1985-03-26");

insert into actors (name, birth_date) values ("Bill Nighy", "1949-12-12");

insert into actors (name, birth_date) values ("Elijah Wood", "1981-01-28");

insert into actors (name, birth_date) values ("Ian McKellen", "1939-05-25");

insert into actors (name, birth_date) values ("Viggo Mortensen", "1958-10-20");

insert into actors (name, birth_date) values ("Sean Bean", "1959-04-17");

insert into actors (name, birth_date) values ("Billy Boyd", "1968-08-28");

insert into actors (name, birth_date) values ("Dominic Monaghan", "1976-12-08");

insert into actors (name, birth_date) values ("Ian Holm", "1931-09-12");

insert into actors (name, birth_date) values ("Brian Hull", "1991-08-28");

insert into actors (name, birth_date) values ("Selena Gomez", "1992-07-22");

insert into actors (name, birth_date) values ("Kylie Minogue", "1968-05-28");

insert into actors (name, birth_date) values ("Andrew Scott", "1976-10-21");

insert into actors (name, birth_date) values ("Dove Cameron", "1996-01-15");

insert into actors (name, birth_date) values ("Julie Andrews", "1935-10-01");

insert into actors (name, birth_date) values ("Christopher Plummer", "1929-12-13");

insert into actors (name, birth_date) values ("Naomi Ackie", "1992-11-02");

insert into actors (name, birth_date) values ("Jason Lee", "1970-04-25");

insert into actors (name, birth_date) values ("Zachary Levi", "1980-09-29");

insert into actors (name, birth_date) values ("F. Murray Abraham", "1939-10-24");

insert into actors (name, birth_date) values ("Anna Kendrick", "1985-08-09");

insert into actors (name, birth_date) values ("Shawn Mendes", "1998-08-08");

insert into actors (name, birth_date) values ("Emilia Jones", "2002-02-23");

insert into actors (name, birth_date) values ("Franco Nero", "1941-11-23");

insert into actors (name, birth_date) values ("Channing Tatum", "1980-04-26");

insert into actors (name, birth_date) values ("Salma Hayek Pinault", "1966-09-02");

insert into actors (name, birth_date) values ("Rami Malek", "1981-05-12");

insert into actors (name, birth_date) values ("Ryan Gosling", "1980-11-12");

insert into actors (name, birth_date) values ("Bradley Cooper", "1975-01-05");

insert into actors (name, birth_date) values ("Matt Bomer", "1977-10-11");
insert into actors (name, birth_date) values ("Matthew McConaughey", "1969-11-04");
insert into actors (name, birth_date) values ("Anna Kendrick", "1985-08-09");
insert into actors (name, birth_date) values ("Steve Carell", "1962-08-16");
insert into actors (name, birth_date) values ("Antonio Banderast", "1960-08-10");
insert into actors (name, birth_date) values ("Leah Lewis", "1996-12-09");
insert into actors (name, birth_date) values ("Soma Santoki", "2005-06-06");
insert into actors (name, birth_date) values ("Ariana DeBose", "1991-01-25");
insert into actors (name, birth_date) values ("Zendaya Maree Stoermer Coleman", "1996-09-01");
insert into actors (name, birth_date) values ("Mark Wahlberg", "1971-06-05");
insert into actors (name) values ("Nora Yessayan");
insert into actors (name, birth_date) values ("Chris Pine", "1980-08-26");
insert into actors (name, birth_date) values ("Patrick Dempsey", "1966-01-13");
insert into actors (name, birth_date) values ("Sam Worthington", "1976-08-02");
insert into actors (name, birth_date) values ("Zoe Saldaña", "1978-06-19");
insert into actors (name, birth_date) values ("Sigourney Weaver", "1949-10-08");
insert into actors (name, birth_date) values ("Wu Jing", "1974-04-03");
insert into actors (name, birth_date) values ("John David Washington", "1984-07-28");
insert into actors (name, birth_date) values ("Oka Antara", "1981-07-08");
insert into actors (name, birth_date) values ("Miya Muqi", "1987-05-24");
insert into actors (name, birth_date) values ("Peter Dinklagey", "1969-06-11");
insert into actors (name, birth_date) values ("Anthony Ramos", "1991-11-01");
insert into actors (name, birth_date) values ("Timothée Chalamet", "1995-12-27");
insert into actors (name, birth_date) values ("Stellan Skarsgård", "1951-06-13");
insert into actors (name, birth_date) values ("Sandra Oh", "1971-07-20");
insert into actors (name, birth_date) values ("Adam Sandler", "1966-09-09");
insert into actors (name, birth_date) values ("Brad Pitt", "1963-12-18");
insert into actors (name, birth_date) values ("Liam Neeson", "1952-06-07");
insert into actors (name, birth_date) values ("Colin Ford", "1996-09-12");
insert into actors (name, birth_date) values ("Lacy Hartselle", "1993-03-09");
insert into actors (name, birth_date) values ("William Chan Wai-Ting", "1985-11-21");
insert into actors (name, birth_date) values ("Daniyar Alshinov", "1987-11-23");
insert into actors (name, birth_date) values ("Tom Blyth", "1995-02-02");
insert into actors (name, birth_date) values ("Jamshid Mashayekhi", "1934-11-26");
insert into actors (name, birth_date) values ("Morgan Freeman", "1937-06-01");
insert into actors (name, birth_date) values ("Jerry Lee", "1978-11-24");
insert into actors (name, birth_date) values ("Grégoire Colin", "1975-07-25");
insert into actors (name, birth_date) values ("Sean Connery", "1930-08-25");
insert into actors (name) values ("Anna Striesow");
insert into actors (name, birth_date) values ("Konstantin Khabenskiy", "1972-01-11");

insert into movie_genre (m_id, g_id) values ( 45, 7), (45, 11), (45, 8);
insert into movie_genre (m_id, g_id) values ( 46, 2), (45, 10), (45, 15);
insert into movie_genre (m_id, g_id) values ( 47, 10), (45, 18);
insert into movie_genre (m_id, g_id) values (45, 10), (45, 15);
insert into movie_genre (m_id, g_id) values (46, 10), (46, 15);
insert into movie_genre (m_id, g_id) values ( 47, 10), (47, 18);
insert into movie_genre (m_id, g_id) values ( 48, 10), (48, 16);
insert into movie_genre (m_id, g_id) values ( 49, 14), (49, 2);
insert into movie_genre (m_id, g_id) values ( 50, 2), (50, 14), (50, 10);
insert into movie_genre (m_id, g_id) values ( 51, 2), (51, 16);
insert into movie_genre (m_id, g_id) values ( 52, 7), (52, 2), (52, 8);
insert into movie_genre (m_id, g_id) values ( 53, 15), (53, 2), (53, 3);
insert into movie_genre (m_id, g_id) values ( 55, 3);
insert into movie_genre (m_id, g_id) values ( 56, 10);
insert into movie_genre (m_id, g_id) values ( 57, 10), (57, 16);
insert into movie_genre (m_id, g_id) values ( 58, 1);
insert into movie_genre (m_id, g_id) values ( 59, 2), (59, 10), (59, 16);
insert into movie_genre (m_id, g_id) values ( 60, 18), (60, 1), (60, 2);
insert into movie_genre (m_id, g_id) values ( 61, 5), (45, 1), (45,11);
insert into movie_genre (m_id, g_id) values ( 62, 5), (62, 1), (62, 11), (62,7);
insert into movie_genre (m_id, g_id) values ( 63, 14), (63, 8);
insert into movie_genre (m_id, g_id) values ( 64, 8), (64, 2), (64, 14);
insert into movie_genre (m_id, g_id) values ( 66, 2), (66, 14);
insert into movie_genre (m_id, g_id) values ( 67, 2), (67, 8), (67, 14);
insert into movie_genre (m_id, g_id) values ( 68, 2), (68, 14), (68, 3);
insert into movie_genre (m_id, g_id) values ( 69,14), (69, 8), (69, 2);
insert into movie_genre (m_id, g_id) values ( 70, 3), (70, 12), (70, 15);
insert into movie_genre (m_id, g_id) values ( 71, 5), (71, 11), (71, 7), (71, 8);
insert into movie_genre (m_id, g_id) values ( 72, 5), (72, 8), (72, 7);
insert into movie_genre (m_id, g_id) values ( 73, 5), (73, 1), (73, 7), (73, 13), (73, 8);
insert into movie_genre (m_id, g_id) values ( 74, 8), (74, 7), (73, 1), (73, 11), (73, 2);
insert into movie_genre (m_id, g_id) values ( 75, 1), (75, 5), (75, 11);
insert into movie_genre (m_id, g_id) values ( 76, 5), (76, 11), (76, 4), (76, 7), (76, 1);
insert into movie_genre (m_id, g_id) values ( 77, 1), (77, 11), (77, 4), (77, 5);
insert into movie_genre (m_id, g_id) values ( 78, 10), (78, 13), (78, 4);
insert into movie_genre (m_id, g_id) values ( 79, 1), (79, 10), (79, 13), (79, 4);
insert into movie_genre (m_id, g_id) values ( 80, 4), (80, 10);
insert into movie_genre (m_id, g_id) values ( 81, 1), (81, 10), (81, 13);
insert into movie_genre (m_id, g_id) values ( 82, 2), (82, 17);
insert into movie_genre (m_id, g_id) values ( 83, 10), (83, 4), (83, 13);
insert into movie_genre (m_id, g_id) values ( 84, 1), (84, 11), (84, 4);
insert into movie_genre (m_id, g_id) values ( 85, 1), (85, 4);
insert into movie_genre (m_id, g_id) values ( 86, 8), (86, 7), (86, 4), (86, 11);
insert into movie_genre (m_id, g_id) values ( 87, 1), (87, 11), (87, 5), (87, 7), (87, 4);
insert into movie_genre (m_id, g_id) values ( 88, 1), (88, 11), (88, 8), (88, 7), (88, 4);
insert into movie_genre (m_id, g_id) values ( 89, 4), (89, 6), (89, 10);
insert into movie_genre (m_id, g_id) values ( 90, 10), (90, 11), (90, 4), (90, 13);
insert into movie_genre (m_id, g_id) values ( 91, 4), (91, 11), (91, 7), (91, 8), (91, 2), (91, 13);
insert into movie_genre (m_id, g_id) values ( 92, 4);
insert into movie_genre (m_id, g_id) values ( 93, 1), (93, 5), (93, 11), (93, 8), (93, 7);
insert into movie_genre (m_id, g_id) values ( 94, 8), (94, 7), (94, 2);
insert into movie_genre (m_id, g_id) values ( 95, 7), (95, 8), (95, 2);
insert into movie_genre (m_id, g_id) values ( 96, 3), (96, 8), (96, 7);
insert into movie_genre (m_id, g_id) values ( 97, 11), (97, 8), (97, 1), (97, 7);
insert into movie_genre (m_id, g_id) values ( 98, 7), (98, 11);
insert into movie_genre (m_id, g_id) values ( 99, 13), (99, 7), (99, 11), (99, 10);
insert into movie_genre (m_id, g_id) values ( 100, 7);
insert into movie_genre (m_id, g_id) values ( 101, 7), (101, 1);
insert into movie_genre (m_id, g_id) values ( 102, 2), (102, 8), (102, 7);
insert into movie_genre (m_id, g_id) values ( 103, 7), (103, 8), (103, 5), (103, 11);
insert into movie_genre (m_id, g_id) values ( 104, 8), (104, 7), (104, 11);
insert into movie_genre (m_id, g_id) values (105, 10);
insert into movie_genre (m_id, g_id) values ( 106, 10);

insert into director (name, birth_date) values ("David Ayer", "1968-01-18");
insert into movie_director (movie_id, director_id) values (46, 1);
insert into director (name, birth_date) values ("Frank Darabont", "1959-01-28");
insert into movie_director (movie_id, director_id) values (47, 3);
insert into director (name) values ("Liu Binjie");
insert into movie_director (movie_id) values (48);
insert into director (name, birth_date) values ("Francis Lawrence", "1971-03-26");
insert into movie_director (movie_id, director_id) values (49, 4);
insert into director (name) values ("Serikbol Utepbergenov");
insert into movie_director (movie_id, director_id) values (50, 5);
insert into director (name, birth_date) values ("David Ayer", "1968-01-18");
insert into movie_director (movie_id) values (51);
insert into director (name) values ("Hasi Chaolu");
insert into director (name) values ("AAron Mirtes");
insert into director (name) values ("Hans Stjernsward");
insert into movie_director (movie_id, director_id) values (52, 7);
insert into movie_director (movie_id, director_id) values (53, 8);
insert into movie_director (movie_id, director_id) values (55, 5);
insert into director (name, birth_date) values ("Tim Burton", "1958-08-25");
insert into movie_director (movie_id, director_id) values (45, 10);
insert into director (name, birth_date) values ("Sidney Lumet", "1924-06-25");
insert into movie_director (movie_id, director_id) values (57, 11);
insert into movie_director (movie_id) values (56);
insert into director (name, birth_date) values ("Steven Spielberg", "1946-12-18");
insert into movie_director (movie_id, director_id) values (58, 12);
insert into director (name, birth_date) values ("David Ayer", "1968-01-18");
insert into movie_director (movie_id, director_id) values (59, 13);
insert into director (name, birth_date) values ("F. Gary Gray", "1969-07-17");
insert into movie_director (movie_id, director_id) values (60, 14);
insert into director (name, birth_date) values ("Robert Smigel", "1960-02-07");
insert into director (name) values ("David Wachtenheim");
insert into director (name) values ("Robert Marianetti");
insert into movie_director (movie_id, director_id) values (61, 15), (61, 16), (61,17);
insert into director (name, birth_date) values ("Domee Shi", "1989-09-08");
insert into movie_director (movie_id, director_id) values (62, 18);
insert into director (name, birth_date) values ("Denis Villeneuve", "1967-10-03");
insert into movie_director (movie_id, director_id) values (63, 19);
insert into director (name, birth_date) values ("Steven Caple Jr.", "1988-01-01");
insert into movie_director (movie_id, director_id) values (64, 20);
insert into director (name) values ("Randy Korompis");
insert into movie_director (movie_id, director_id) values (66, 21);
insert into director (name, birth_date) values ("Gareth Edwards", "1975-06-01");
insert into movie_director (movie_id, director_id) values (67, 22);
insert into director (name, birth_date) values ("Ben Wheatley", "1972-05-07");
insert into movie_director (movie_id, director_id) values (68, 23);
insert into director (name, birth_date) values ("James Cameron", "1954-08-16");
insert into movie_director (movie_id, director_id) values (69, 24);
insert into director (name, birth_date) values ("Eli Roth", "1972-04-18");
insert into movie_director (movie_id, director_id) values (70, 25);
insert into director (name) values ("Fawn Veerasunthorn");
insert into director (name, birth_date) values ("Chris Buck", "1958-02-24");
insert into movie_director (movie_id, director_id) values (71, 26), (71, 27);
insert into director (name, birth_date) values ("Hayao Miyazaki", "1941-01-05");
insert into movie_director (movie_id, director_id) values (72, 28);
insert into director (name, birth_date) values ("Peter Sohn", "1975-06-21");
insert into movie_director (movie_id, director_id) values (73, 29);
insert into director (name) values ("Joel Crawford");
insert into movie_director (movie_id, director_id) values (74, 30);
insert into director (name, birth_date) values ("Kyle Balda", "1971-03-09");
insert into movie_director (movie_id, director_id) values (75, 31);
insert into director (name, birth_date) values ("Walt Dohrn", "1970-12-05");
insert into movie_director (movie_id, director_id) values (76, 32);
insert into director (name, birth_date) values ("Garth Jennings", "1972-03-04");
insert into movie_director (movie_id, director_id) values (77, 33);
insert into director (name, birth_date) values ("Bradley Cooper", "1975-01-05");
insert into movie_director (movie_id, director_id) values (78, 34);
insert into director (name, birth_date) values ("Damien Chazelle", "1965-09-17");
insert into movie_director (movie_id, director_id) values (80, 36);
insert into director (name, birth_date) values ("Bryan Singer", "1965-09-17");
insert into movie_director (movie_id, director_id) values (80, 37);
insert into director (name, birth_date) values ("Steven Soderbergh", "1963-01-14");
insert into movie_director (movie_id, director_id) values (81, 38);
insert into director (name, birth_date) values ("Sergio Corbucci", "1926-12-06");
insert into movie_director (movie_id, director_id) values (82, 39);
insert into director (name, birth_date) values ("Siân Heder", "1977-06-23");
insert into movie_director (movie_id, director_id) values (83, 40);
insert into director (name) values ("Josh Gordon");
insert into director (name, birth_date) values ("Will Speck", "1969-12-31");
insert into movie_director (movie_id, director_id) values (83, 41), (83, 42);
insert into director (name, birth_date) values ("Elizabeth Banks", "1974-02-10");
insert into movie_director (movie_id, director_id) values (85, 43);
insert into director (name) values ("Florian Sigl");
insert into movie_director (movie_id, director_id) values (86, 44);
insert into director (name, birth_date) values ("Betty Thomas", "1947-07-27");
insert into movie_director (movie_id, director_id) values (87, 45);
insert into director (name, birth_date) values ("Mike Mitchell", "1970-10-18");
insert into movie_director (movie_id, director_id) values (88, 46);
insert into director (name, birth_date) values ("Kasi Lemmons", "1961-02-24");
insert into movie_director (movie_id, director_id) values (89, 47);
insert into director (name, birth_date) values ("Robert Wise", "1914-09-10");
insert into movie_director (movie_id, director_id) values (90, 48);
insert into director (name, birth_date) values ("Kenny Ortega", "1950-04-18");
insert into movie_director (movie_id, director_id) values (91, 49);
insert into director (name) values ("Julia Knowles");
insert into movie_director (movie_id, director_id) values (92, 50);
insert into director (name, birth_date) values ("Derek Drymon", "1968-11-19");
insert into movie_director (movie_id, director_id) values (93, 51);
insert into director (name) values ("Jennifer Kluska");
insert into movie_director (movie_id, director_id) values (93, 52);
insert into director (name, birth_date) values ("Peter Jackson", "1961-10-31");
insert into movie_director (movie_id, director_id) values (94, 53);
insert into director (name, birth_date) values ("Gore Verbinski", "1964-03-16");
insert into movie_director (movie_id, director_id) values (95, 54);
insert into director (name, birth_date) values ("Alessio Liguori", "1981-01-01");
insert into movie_director (movie_id, director_id) values (96, 55);
insert into director (name) values ("Grant Wilkinson");
insert into movie_director (movie_id, director_id) values (97, 56);
insert into director (name, birth_date) values ("Alice Guy-Blaché", "1873-07-01");
insert into movie_director (movie_id, director_id) values (98, 57);
insert into director (name, birth_date) values ("Kenneth Branagh", "1960-12-10");
insert into movie_director (movie_id, director_id) values (99, 58);
insert into director (name, birth_date) values ("Georges Méliès", "1861-12-09");
insert into movie_director (movie_id, director_id) values (100, 59);
insert into director (name, birth_date) values ("Seth MacFarlane", "1973-10-26");
insert into movie_director (movie_id, director_id) values (101, 60);
insert into director (name, birth_date) values ("Destin Daniel Cretton", "1978-11-23");
insert into movie_director (movie_id, director_id) values (102, 61);
insert into director (name, birth_date) values ("Chris Sanders", "1962-03-12"), ("Dean DeBlois", "1970-06-07");
insert into movie_director (movie_id, director_id) values (103, 62), (103, 63);
insert into director (name, birth_date) values ("Alf Prøysen", "1944-07-23");
insert into movie_director (movie_id, director_id) values (104, 64);
insert into director (name, birth_date) values ("Max Gleschinski", "1993-12-30");
insert into movie_director (movie_id, director_id) values (105, 65);
insert into movie_director (movie_id) values (106);


insert into movie_actor (movie_id, actor_id) values (45, 29);
insert into movie_actor (movie_id, actor_id) values (46, 1);
insert into movie_actor (movie_id, actor_id) values (47, 92);
insert into movie_actor (movie_id, actor_id) values (48, 93);
insert into movie_actor (movie_id, actor_id) values (49, 77);
insert into movie_actor (movie_id, actor_id) values (50, 90), (50, 78);
insert into movie_actor (movie_id, actor_id) values (51, 89);
insert into movie_actor (movie_id, actor_id) values (52, 88);
insert into movie_actor (movie_id, actor_id) values (53, 87);
insert into movie_actor (movie_id, actor_id) values (55, 94);
insert into movie_actor (movie_id, actor_id) values (56, 95);
insert into movie_actor (movie_id, actor_id) values (57, 96);
insert into movie_actor (movie_id, actor_id) values (58, 85);
insert into movie_actor (movie_id, actor_id) values (59, 84);
insert into movie_actor (movie_id, actor_id) values (60, 4), (60, 71), (60, 5);
insert into movie_actor (movie_id, actor_id) values (61, 83);
insert into movie_actor (movie_id, actor_id) values (62, 82);
insert into movie_actor (movie_id, actor_id) values (63, 80), (63, 97), (63, 81);
insert into movie_actor (movie_id, actor_id) values (64, 82), (64, 78);
insert into movie_actor (movie_id, actor_id) values (66, 76);
insert into movie_actor (movie_id, actor_id) values (67, 75);
insert into movie_actor (movie_id, actor_id) values (68, 74), (68, 1);
insert into movie_actor (movie_id, actor_id) values (69, 71), (69, 72), (69, 73);
insert into movie_actor (movie_id, actor_id) values (70, 70);
insert into movie_actor (movie_id, actor_id) values (71, 67), (71, 69);
insert into movie_actor (movie_id, actor_id) values (72, 66);
insert into movie_actor (movie_id, actor_id) values (73, 65);
insert into movie_actor (movie_id, actor_id) values (74, 64);
insert into movie_actor (movie_id, actor_id) values (75, 63);
insert into movie_actor (movie_id, actor_id) values (76, 62);
insert into movie_actor (movie_id, actor_id) values (77, 61);
insert into movie_actor (movie_id, actor_id) values (78, 59), (78, 60);
insert into movie_actor (movie_id, actor_id) values (79, 58);
insert into movie_actor (movie_id, actor_id) values (80, 57);
insert into movie_actor (movie_id, actor_id) values (81, 55), (81, 56);
insert into movie_actor (movie_id, actor_id) values (82, 54);
insert into movie_actor (movie_id, actor_id) values (83, 53);
insert into movie_actor (movie_id, actor_id) values (84, 52);
insert into movie_actor (movie_id, actor_id) values (85, 51);
insert into movie_actor (movie_id, actor_id) values (86, 50);
insert into movie_actor (movie_id, actor_id) values (87, 49);
insert into movie_actor (movie_id, actor_id) values (88, 48);
insert into movie_actor (movie_id, actor_id) values (89, 47);
insert into movie_actor (movie_id, actor_id) values (90, 45), (90, 46);
insert into movie_actor (movie_id, actor_id) values (91, 44);
insert into movie_actor (movie_id, actor_id) values (92, 42), (92, 43);
insert into movie_actor (movie_id, actor_id) values (93, 40), (93, 41);
insert into movie_actor (movie_id, actor_id) values (94, 33), (94, 34), (94, 35), (94, 36), (94, 37), (94, 38), (94, 39);
insert into movie_actor (movie_id, actor_id) values (95, 29), (95, 30), (95, 31);
insert into movie_actor (movie_id, actor_id) values (96, 28);
insert into movie_actor (movie_id, actor_id) values (97, 26), (97, 27);
insert into movie_actor (movie_id, actor_id) values (98, 25);
insert into movie_actor (movie_id, actor_id) values (99, 22), (99, 23), (99, 24);
insert into movie_actor (movie_id, actor_id) values (100, 21);
insert into movie_actor (movie_id, actor_id) values (101, 98);
insert into movie_actor (movie_id, actor_id) values (102, 19), (102, 18), (102, 17);
insert into movie_actor (movie_id, actor_id) values (103, 15), (103, 16);
insert into movie_actor (movie_id, actor_id) values (104, 12);
insert into movie_actor (movie_id, actor_id) values (105, 99);
insert into movie_actor (movie_id, actor_id) values (106, 100);


insert into movie_rating (movie_id, rating_id) values (45, 198);
insert into movie_rating (movie_id, rating_id) values (46, 191);
insert into movie_rating (movie_id, rating_id) values (47,177);
insert into movie_rating (movie_id, rating_id) values (48, 179);
insert into movie_rating (movie_id, rating_id) values (49, 225);
insert into movie_rating (movie_id, rating_id) values (50, 192);
insert into movie_rating (movie_id, rating_id) values (51, 181);
insert into movie_rating (movie_id, rating_id) values (52, 228);
insert into movie_rating (movie_id, rating_id) values (53, 205);
insert into movie_rating (movie_id, rating_id) values (55, 225);
insert into movie_rating (movie_id, rating_id) values (56, 197);
insert into movie_rating (movie_id, rating_id) values (57, 189);
insert into movie_rating (movie_id, rating_id) values (58, 178);
insert into movie_rating (movie_id, rating_id) values (59, 189);
insert into movie_rating (movie_id, rating_id) values (60, 198);
insert into movie_rating (movie_id, rating_id) values (61, 189);
insert into movie_rating (movie_id, rating_id) values (62, 190);
insert into movie_rating (movie_id, rating_id) values (63, 186);
insert into movie_rating (movie_id, rating_id) values (64, 190);
insert into movie_rating (movie_id, rating_id) values (66, 199);
insert into movie_rating (movie_id, rating_id) values (67, 193);
insert into movie_rating (movie_id, rating_id) values (68, 197);
insert into movie_rating (movie_id, rating_id) values (69, 188);
insert into movie_rating (movie_id, rating_id) values (70, 197);
insert into movie_rating (movie_id, rating_id) values (71, 197);
insert into movie_rating (movie_id, rating_id) values (72, 189);
insert into movie_rating (movie_id, rating_id) values (73, 187);
insert into movie_rating (movie_id, rating_id) values (74, 181);
insert into movie_rating (movie_id, rating_id) values (75, 191);
insert into movie_rating (movie_id, rating_id) values (76, 191);
insert into movie_rating (movie_id, rating_id) values (77, 185);
insert into movie_rating (movie_id, rating_id) values (78, 199);
insert into movie_rating (movie_id, rating_id) values (79, 185);
insert into movie_rating (movie_id, rating_id) values (80, 184);
insert into movie_rating (movie_id, rating_id) values (81, 197);
insert into movie_rating (movie_id, rating_id) values (82, 201);
insert into movie_rating (movie_id, rating_id) values (83, 185);
insert into movie_rating (movie_id, rating_id) values (84, 192);
insert into movie_rating (movie_id, rating_id) values (85, 195);
insert into movie_rating (movie_id, rating_id) values (86, 200);
insert into movie_rating (movie_id, rating_id) values (87, 221);
insert into movie_rating (movie_id, rating_id) values (88, 220);
insert into movie_rating (movie_id, rating_id) values (89, 194);
insert into movie_rating (movie_id, rating_id) values (90, 187);
insert into movie_rating (movie_id, rating_id) values (91, 190);
insert into movie_rating (movie_id, rating_id) values (92, 227);
insert into movie_rating (movie_id, rating_id) values (93, 194);
insert into movie_rating (movie_id, rating_id) values (94, 180);
insert into movie_rating (movie_id, rating_id) values (95, 192);
insert into movie_rating (movie_id, rating_id) values (96, 222);
insert into movie_rating (movie_id, rating_id) values (97, 164);
insert into movie_rating (movie_id, rating_id) values (98, 225);
insert into movie_rating (movie_id, rating_id) values (99, 201);
insert into movie_rating (movie_id, rating_id) values (100, 219);
insert into movie_rating (movie_id, rating_id) values (101, 200);
insert into movie_rating (movie_id, rating_id) values (102, 188);
insert into movie_rating (movie_id, rating_id) values (103, 186);
insert into movie_rating (movie_id, rating_id) values (104, 192);
insert into movie_rating (movie_id, rating_id) values (105, 325);
insert into movie_rating (movie_id, rating_id) values (106, 325);

  After the insert, in order to prepare the data to be better suited for the testing process, I updated some data in the following way:

UPDATE movies
SET title = 'Lift'
WHERE movie_id = '60';

update movie_genre 
set m_id = 61
where movie_genre_id = 45;

update movie_genre 
set m_id = 61
where movie_genre_id = 46;

update movie_genre 
set m_id = 74
where movie_genre_id = 84;

update movie_genre 
set m_id = 74
where movie_genre_id = 85;

update movie_genre 
set m_id = 74
where movie_genre_id = 86;

update movie_director 
set movie_id = 49
where movie_director_id = 4;

update movie_director 
set movie_id = 50
where movie_director_id = 4;

update movie_director
set movie_id = 84
where movie_director_id = 57;

update movie_director
set movie_id = 84
where movie_director_id = 5;

UPDATE movie_rating
SET rating_id = NULL
WHERE movie_rating_id = 61;

UPDATE movie_rating
SET rating_id = NULL
WHERE movie_rating_id = 62;
select * from movie_rating;


  <li>DQL (Data Query Language)</li>

After the testing process, I deleted the data that was no longer relevant in order to preserve the database clean: 

delete from movies where movie_id = 65;

delete from director 
where director_id = 2;

delete from movie_director;

delete from director
where director_id = 36;

delete from movies;

delete from ratings;

delete from ratings
where rating_id not in (    
    select rating_id     
    from (                 
		select min(rating_id) as rating_id  
		from ratings                  
		group by rating     
						)   
		as min_ratings )

select * from actors;
delete from actors where actor_id = 68;

delete from movie_genre where movie_genre_id = 8;
delete from movie_genre where movie_genre_id = 9;
delete from movie_genre where movie_genre_id = 10;
delete from movie_genre where movie_genre_id = 11;
delete from movie_genre where movie_genre_id = 13;
delete from movie_genre where movie_genre_id = 12;

delete from movies where movie_id = 54;
delete from movies where movie_id = 65;


In order to simulate various scenarios that might happen in real life I created the following queries that would cover multiple potential real-life situations:

select * from ratings;

select * from actors;

select * from movies;

select * from genres;

select * from movie_genre;

select * from movie_director;

select * from movie_actor;

select * from movie_rating;

select m.title
from movies m
join movie_rating mr on m.movie_id = mr.movie_id
join ratings r on mr.rating_id = r.rating_id
where r.rating > 0.8;

select * from movies where release_date < "2000-01-01";

select m.title as movie_title, g.name as genre_name
from movies m
join movie_genre mg on m.movie_id = mg.m_id
join genres g on mg.g_id = g.genres_id
where g.name = "Action";

select m.title as movie_title, g.name as genre_name 
from movies m
join movie_genre mg on m.movie_id = mg.m_id
join genres g on mg.g_id = g.genres_id
where g.name in ("drama", "history");


select m.title as movie_title, d.name as director_name
from movies m
inner join movie_director md on m.movie_id = md.movie_id
inner join director d on md.director_id = d.director_id;

select m.title, a.name as actor_name
from movies m
left join movie_actor ma on m.movie_id = ma.movie_id
left join actors a on ma.actor_id = a.actor_id;

select g.name as genre, count(m.movie_id) as nr_movies
from movies m
inner join movie_genre mg on m.movie_id = mg.m_id
inner join genres g on mg.g_id = g.genres_id
group by g.name;

select g.name as genre, count(m.movie_id) as nr_of_movies 
from movies m
inner join movie_genre mg on m.movie_id = mg.m_id
inner join genres g on mg.g_id = g.genres_id
group by g.name
order by nr_of_movies desc    
limit 1;

select m.title as movie_title, count(*) as number_of_actors
from movies m
join movie_actor ma on m.movie_id = ma.movie_id
group by m.title;


select m.title as movie_title, count(*) as number_of_actors
from movies m
join movie_actor ma on m.movie_id = ma.movie_id
group by m.title
order by number_of_actors desc
limit 1;

select m.title as movie_title, count(*) as number_of_directors
from movies m
join movie_director md on m.movie_id = md.movie_id
group by m.title;


select round(avg(r.rating), 2) as average_rating
from ratings r
join movie_rating mr on r.rating_id = mr.rating_id;

select g.name as genre, round(avg(r.rating), 2) as avg_rating
from movies m
inner join movie_genre mg on m.movie_id = mg.m_id
inner join genres g on mg.g_id = g.genres_id
inner join movie_rating mr on m.movie_id = mr.movie_id
inner join ratings r on mr.rating_id = r.rating_id
group by g.name
having avg(r.rating) > 0.7;


select m.* from movies m
inner join movie_rating mr on m.movie_id = mr.movie_id
inner join ratings r on mr.rating_id = r.rating_id
where m.release_date > '2000-01-01' and r.rating > 0.8 and m.title not like '%The%';


select * from movies
where title like '%the%';

select count(*) as m_with_the
from movies
where title Like'%the%';

select * from movies
where month(release_date) = 5;

select * from movies
where release_date like '%-05-%';

select count(*) as total_movies_in_may
from movies
where month(release_date) = 5;

select * from actors
where birth_date is null;

select m.* from movies m
left join movie_rating mr on m.movie_id = mr.movie_id
where mr.rating_id is null ;

select m.* from movies m
inner join movie_rating mr on m.movie_id = mr.movie_id
inner join ratings r on mr.rating_id = r.rating_id
inner join movie_genre mg on m.movie_id = mg.m_id
inner join genres g on mg.g_id = g.genres_id
where (m.release_date > '2020-01-01' and r.rating > 0.9) or g.name in ('drama');

select min(number_of_actors) as min_actors,
       max(number_of_actors) as max_actors
from (
    select count(*) as number_of_actors
    from movie_actor
    group by movie_id
) as actor_counts;


select sum(number_of_actors) as total_actors
from (
    select count(*) as number_of_actors
    from movie_actor
    group by movie_id
) as actor_number;

select sum(number_of_director) as total_directors
from (
    select count(*) as number_of_director
    from movie_director
    group by movie_id
) as director_number;


select sum(number_of_genres) as total_genres
from (
    select count(*) as number_of_genres
    from genres
    group by genres_id
) as genre_number;

<br>

</ol>

<li>Conclusions</li>

**Inserati aici o concluzie cu privire la ceea ce ati lucrat, gen lucrurile pe care le-ati invatat, lessons learned, un rezumat asupra a ceea ce ati facut si orice alta informatie care vi se pare relevanta pentru o concluzie finala asupra a ceea ce ati lucrat**

</ol>
