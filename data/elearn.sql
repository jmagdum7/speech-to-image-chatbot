-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 15, 2018 at 11:56 AM
-- Server version: 10.1.26-MariaDB
-- PHP Version: 7.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `elearn`
--

-- --------------------------------------------------------

--
-- Table structure for table `cources`
--

CREATE TABLE `cources` (
  `id` varchar(3) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL,
  `year` int(1) DEFAULT NULL,
  `dept` varchar(8) DEFAULT NULL,
  `language` varchar(7) DEFAULT NULL,
  `keywords` int(1) DEFAULT NULL,
  `clicks` int(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `cources`
--

INSERT INTO `cources` (`id`, `title`, `year`, `dept`, `language`, `keywords`, `clicks`) VALUES
('c01', 'TOC', 3, 'Computer', 'English', 0, 0),
('c02', 'DBMS', 3, 'Computer', 'English', 0, 0),
('c03', 'SEPM', 3, 'Computer', 'English', 0, 0),
('c04', 'Information Systems & Engineering Economics', 3, 'Computer', 'English', 0, 0),
('c05', 'Computer Networks', 3, 'Computer', 'English', 0, 0),
('c06', 'DAA', 3, 'Computer', 'English', 0, 0),
('c07', 'SPOS', 3, 'Computer', 'English', 0, 0),
('c08', 'Embedded Systems & Internet of Things', 3, 'Computer', 'English', 0, 0),
('c09', 'Software Modeling and Design', 3, 'Computer', 'English', 0, 0),
('c10', 'Web Technology', 3, 'Computer', 'English', 0, 0),
('i01', 'Theory of Computation', 3, 'IT', 'English', 0, 0),
('i02', 'Database Management Systems', 3, 'IT', 'English', 0, 0),
('i03', 'Software Engineering & Project Management', 3, 'IT', 'English', 0, 0),
('i04', 'Operating Systems', 3, 'IT', 'English', 0, 0),
('i05', 'Human-Computer Interaction', 3, 'IT', 'English', 0, 0),
('i06', 'Computer Network Technology', 3, 'IT', 'English', 0, 0),
('i07', 'Systems Programming', 3, 'IT', 'English', 0, 0),
('i08', 'Design & Analysis of Algorithms', 3, 'IT', 'English', 0, 0),
('i09', 'Cloud Computing', 3, 'IT', 'English', 0, 0),
('i10', 'Data Science & Big Data Analytics', 3, 'IT', 'English', 0, 0),
('e01', 'Digital Communication', 3, 'ENTC', 'English', 0, 0),
('e02', 'Digital Signal processing', 3, 'ENTC', 'English', 0, 0),
('e03', 'Electromagnetics', 3, 'ENTC', 'English', 0, 0),
('e04', 'Microcontrollers', 3, 'ENTC', 'English', 0, 0),
('e05', 'Mechatronics', 3, 'ENTC', 'English', 0, 0),
('e06', 'Power Electronics', 3, 'ENTC', 'English', 0, 0),
('e07', 'Information Theory', 3, 'ENTC', 'English', 0, 0),
('e08', 'Business Management', 3, 'ENTC', 'English', 0, 0),
('e09', 'Advanced Processors', 3, 'ENTC', 'English', 0, 0),
('e10', 'System Programming & Operating System', 3, 'ENTC', 'English', 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `globalhist`
--

CREATE TABLE `globalhist` (
  `rollno` int(1) DEFAULT NULL,
  `id` varchar(3) DEFAULT NULL,
  `status` int(2) DEFAULT NULL,
  `rating` int(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `globalhist`
--

INSERT INTO `globalhist` (`rollno`, `id`, `status`, `rating`) VALUES
(1, 'i01', 25, 5),
(1, 'i02', 75, 4),
(2, 'i05', 100, 4),
(2, 'c02', 50, 5),
(1, 'i08', 100, 2),
(1, 'i04', 25, 3);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `rollno` int(1) DEFAULT NULL,
  `name` varchar(12) DEFAULT NULL,
  `year` int(1) DEFAULT NULL,
  `dept` varchar(8) DEFAULT NULL,
  `language` varchar(7) DEFAULT NULL,
  `interest` varchar(2) DEFAULT NULL,
  `password` varchar(8) DEFAULT NULL,
  `email` varchar(21) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`rollno`, `name`, `year`, `dept`, `language`, `interest`, `password`, `email`) VALUES
(0, 'admin', 0, '0', '0', '0', 'admin', 'admin@admin.com'),
(1, 'Chetan Chaku', 3, 'IT', 'English', 'OS', 'password', 'chetanchaku@gmail.com'),
(2, 'testuser2', 3, 'Computer', 'English', '0', 'pwd', 'testuser2@gmail.com'),
(3, 'testuser3', 3, 'ENTC', 'English', '0', 'pwd', 'testuser3@gmail.com');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
