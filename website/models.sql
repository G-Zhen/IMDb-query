CREATE DATABASE IF NOT EXISTS `imdb_DB`;
USE `imdb_DB`;

CREATE TABLE `users` (
	`id` int AUTO_INCREMENT NOT NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE `page1_responses` (
	`id` int NOT NULL,
    `q1` varchar(100),
    `q2` varchar(100),
    `q3` varchar(100),
    FOREIGN KEY (`id`) REFERENCES users(`id`),
    PRIMARY KEY (`id`)
);