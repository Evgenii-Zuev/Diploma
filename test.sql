﻿--
-- Script was generated by Devart dbForge Studio 2020 for MySQL, Version 9.0.791.0
-- Product home page: http://www.devart.com/dbforge/mysql/studio
-- Script date 02.02.2022 12:01:39
-- Server version: 8.0.28
-- Client version: 4.1
--

-- 
-- Disable foreign keys
-- 
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;

-- 
-- Set SQL mode
-- 
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- 
-- Set character set the client will use to send SQL statements to the server
--
SET NAMES 'utf8';

--
-- Set default database
--
USE test;

--
-- Drop table `the_beatles`
--
DROP TABLE IF EXISTS the_beatles;

--
-- Set default database
--
USE test;

--
-- Create table `the_beatles`
--
CREATE TABLE the_beatles (
  kind varchar(13) DEFAULT NULL,
  collectionName varchar(60) DEFAULT NULL,
  trackName varchar(60) DEFAULT NULL,
  collectionPrice varchar(5) DEFAULT NULL,
  trackPrice varchar(5) DEFAULT NULL,
  primaryGenreName varchar(25) DEFAULT NULL,
  trackCount varchar(2) DEFAULT NULL,
  trackNumber varchar(2) DEFAULT NULL,
  releaseDate datetime DEFAULT NULL
)
ENGINE = INNODB,
AVG_ROW_LENGTH = 655,
CHARACTER SET latin1,
COLLATE latin1_swedish_ci;

--
-- Create index `IDX_the_beatles` on table `the_beatles`
--
ALTER TABLE the_beatles
ADD INDEX IDX_the_beatles (collectionName, releaseDate);

-- 
-- Dumping data for table the_beatles
--
INSERT INTO the_beatles VALUES
(' ', 'The Beatles', ' ', '22.99', ' ', 'Biographies & Memoirs', '1', ' ', '2010-03-18 07:00:00'),
('song', 'SremmLife 2 (Deluxe)', 'Black Beatles (feat. Gucci Mane)', '10.99', '1.29', 'Hip-Hop/Rap', '14', '5', '2016-08-12 12:00:00'),
('song', 'The Beatles 1967-1970 (The Blue Album)', 'Hey Jude', '19.99', '1.29', 'Rock', '14', '13', '1968-08-26 12:00:00'),
('song', 'Cripple Crow', 'The Beatles', '9.99', '1.29', 'Alternative', '22', '10', '2005-09-13 12:00:00'),
('song', 'The Beatles (The White Album)', 'While My Guitar Gently Weeps', '19.99', '1.29', 'Rock', '17', '7', '1968-11-22 12:00:00'),
('song', 'The Beatles 1967-1970 (The Blue Album)', 'Revolution', '19.99', '1.29', 'Rock', '14', '14', '1968-08-26 12:00:00'),
('song', 'Abbey Road (2019 Mix)', 'Here Comes the Sun', '9.99', '1.29', 'Rock', '17', '7', '1969-09-26 12:00:00'),
('song', 'The Beatles (The White Album)', 'Dear Prudence', '19.99', '1.29', 'Pop', '17', '2', '1968-11-22 12:00:00'),
('song', 'The Beatles 1967-1970 (The Blue Album)', 'Strawberry Fields Forever', '19.99', '1.29', 'Rock', '14', '1', '1967-02-13 12:00:00'),
('song', 'The Beatles (The White Album)', 'I Will', '19.99', '1.29', 'Rock', '17', '16', '1968-11-22 12:00:00'),
(' ', 'The Beatles: The Pocket Essential Guide', ' ', '6.99', ' ', 'Nonfiction', '1', ' ', '2016-03-15 07:00:00'),
('song', 'Liquid Love', 'The Beatles', '6.99', '0.99', 'Dance', '11', '5', '2010-03-15 12:00:00'),
('song', 'The Beatles 1967-1970 (The Blue Album)', 'Across the Universe', '19.99', '1.29', 'Rock', '14', '13', '1969-12-12 12:00:00'),
('song', 'The Beatles 1962-1966 (The Red Album)', 'I Want to Hold Your Hand', '19.99', '1.29', 'Rock', '13', '5', '1963-11-29 12:00:00'),
('song', 'Let It Be (2021 Mix)', 'Let It Be', '9.99', '1.29', 'Rock', '12', '6', '2021-08-28 07:00:00'),
('song', 'The Beatles (The White Album)', 'Mother Nature''s Son', '19.99', '1.29', 'Rock', '13', '3', '1968-11-22 12:00:00'),
('song', 'The Beatles 1967-1970 (The Blue Album)', 'With a Little Help From My Friends', '19.99', '1.29', 'Rock', '14', '4', '1967-06-01 12:00:00'),
('song', 'The Beatles 1967-1970 (The Blue Album)', 'Lucy In the Sky with Diamonds', '19.99', '1.29', 'Rock', '14', '5', '1967-06-01 12:00:00'),
('music-video', 'The Beatles (The White Album)', 'The Beatles', '19.99', '1.99', 'Pop', '32', '1', '2019-05-22 07:00:00'),
('song', 'The Beatles (The White Album)', 'Martha My Dear', '19.99', '1.29', 'Rock', '17', '9', '1968-11-22 12:00:00'),
('song', 'The Beatles (The White Album)', 'Why Don''t We Do It In the Road?', '19.99', '1.29', 'Pop', '17', '15', '1968-11-22 12:00:00'),
('song', 'The Beatles (The White Album)', 'Cry Baby Cry', '19.99', '1.29', 'Rock', '13', '11', '1968-11-22 12:00:00'),
('song', 'The Beatles (The White Album)', 'Sexy Sadie', '19.99', '1.29', 'Rock', '13', '5', '1968-11-22 12:00:00'),
('song', 'The Beatles 1967-1970 (The Blue Album)', 'Get Back', '19.99', '1.29', 'Pop', '14', '4', '1969-04-11 12:00:00'),
('song', 'The Beatles (The White Album)', 'Yer Blues', '19.99', '1.29', 'Rock', '13', '2', '1968-11-22 12:00:00');

-- 
-- Restore previous SQL mode
-- 
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;

-- 
-- Enable foreign keys
-- 
/*!40014 SET FOREIGN_KEY_CHECKS = @OLD_FOREIGN_KEY_CHECKS */;