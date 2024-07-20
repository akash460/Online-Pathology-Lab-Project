CREATE DATABASE project;
USE project;

CREATE TABLE `aregister` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `specialnote` text DEFAULT NULL,
  `way` varchar(20) NOT NULL,
  `day` varchar(20) NOT NULL,
  `time` varchar(20) NOT NULL,
  `did` int(11) NOT NULL
);

CREATE TABLE `booked` (
  `bid` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `email` varchar(255) NOT NULL,
  `tid` varchar(20) NOT NULL,
  `testname` varchar(255) NOT NULL,
  `testprice` decimal(10,2) NOT NULL
);

CREATE TABLE `dregister` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `qualification` varchar(255) NOT NULL,
  `specialisation` varchar(255) NOT NULL
);

CREATE TABLE `pregister` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `password` varchar(255) NOT NULL
);

CREATE TABLE `test` (
  `tid` int(11) NOT NULL,
  `testname` varchar(255) NOT NULL,
  `description` text DEFAULT NULL,
  `price` decimal(10,2) NOT NULL
);