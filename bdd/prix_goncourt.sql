-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost
-- Généré le : mer. 16 sep. 2026 à 06:59
-- Version du serveur : 11.7.1-MariaDB
-- Version de PHP : 8.5.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `prix_goncourt`
--

-- --------------------------------------------------------

--
-- Structure de la table `author`
--

CREATE TABLE `author` (
  `id_author` int(10) UNSIGNED NOT NULL,
  `biography` varchar(500) DEFAULT NULL,
  `id_person` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `author`
--

INSERT INTO `author` (`id_author`, `biography`, `id_person`) VALUES
(1, 'Écrivain français né en 1992, auteur de romans et de textes liés à la jeunesse et à la scène.', 1),
(2, 'Écrivaine française, autrice notamment de romans explorant les relations familiales et la filiation.', 2),
(3, 'Écrivaine mauricienne francophone, autrice de nombreux romans consacrés à l\'identité, à la violence et aux héritages historiques.', 3),
(4, 'Journaliste et écrivaine française, autrice de récits mêlant histoire familiale, mémoire et enquête.', 4),
(5, 'Écrivaine française, autrice de romans à la construction narrative singulière.', 5),
(6, 'Écrivain français.', 6),
(7, 'Écrivain français, romancier et essayiste.', 7),
(8, 'Écrivaine et journaliste française.', 8),
(9, 'Écrivain français connu pour ses romans d\'enquête littéraire et historique.', 9),
(10, 'Écrivain et critique d\'art français.', 10),
(11, 'Écrivaine française.', 11),
(12, 'Écrivaine et artiste française.', 12),
(13, 'Écrivain québécois d\'origine haïtienne.', 13),
(14, 'Écrivain français.', 14),
(15, 'Écrivain et essayiste français.', 15),
(16, 'Écrivain, galeriste et dramaturge français.', 16);

-- --------------------------------------------------------

--
-- Structure de la table `book`
--

CREATE TABLE `book` (
  `isbn` char(13) NOT NULL,
  `title` varchar(100) NOT NULL,
  `summary` varchar(1500) DEFAULT NULL,
  `price` decimal(10,2) NOT NULL,
  `publishing_date` date DEFAULT NULL,
  `nb_pages` int(11) NOT NULL,
  `editor_price` decimal(10,2) DEFAULT NULL,
  `id_author` int(10) UNSIGNED NOT NULL,
  `id_editor` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `book`
--

INSERT INTO `book` (`isbn`, `title`, `summary`, `price`, `publishing_date`, `nb_pages`, `editor_price`, `id_author`, `id_editor`) VALUES
('9782073099945', 'Je', 'En Jamaïque en 1831, Antoinette Cosway s\'éprend d\'Edward Rochester. Inspiré de la première épouse de Rochester dans Jane Eyre, le roman donne une voix et une histoire à un personnage longtemps resté dans l\'ombre.', 21.00, '2026-08-20', 256, 21.00, 8, 7),
('9782073121349', 'La Guerre éternelle', 'Souvenirs de Troie', 20.00, '2026-08-20', 224, 20.00, 15, 7),
('9782073161925', 'La solitude des professeurs est infinie', 'Jean Deichel, jeune professeur de français stagiaire, découvre les difficultés et les joies de son métier dans un collège de la banlieue parisienne, tout en cherchant la beauté dans un quotidien marqué par la violence et la banalité.', 21.50, '2026-08-20', 320, 21.50, 7, 7),
('9782073162854', 'Choses que je croyais perdues', 'Une jeune femme qui s\'apprête à déménager rassemble ses affaires et voit surgir, à travers les objets du quotidien, des souvenirs, des histoires d\'amour, des désillusions et des fragments de son existence.', 19.00, '2026-08-20', 176, 19.00, 12, 7),
('9782080490896', 'L\'Inconnue du quai de Javel', 'En 1949, Louise Cansot est retrouvée morte quai de Javel à Paris. Soixante-quinze ans plus tard, Philippe Jaenada reprend l\'enquête à partir des archives afin de tenter de résoudre ce meurtre resté mystérieux.', 22.00, '2026-08-12', 528, 22.00, 9, 8),
('9782221286807', 'Le Fabuleux piano', 'Sonia Devillers enquête sur un piano à queue volé par les nazis en 1943 et retrace le destin de ses propriétaires juifs ainsi que celui de la famille d\'éditeurs de musique Enoch.', 21.00, '2026-08-27', 288, 21.00, 4, 4),
('9782226499523', 'Une forêt', 'Le capitaine Lenz enquête sur le destin d\'oiseaux allemands et se retrouve confronté à une affaire aussi étrange que mélancolique, dans un court roman marqué par la guerre et la mémoire.', 16.90, '2026-01-02', 112, 16.90, 10, 1),
('9782226511874', 'Minotaure', 'Une autofiction autour de la filiation, du désir et de la réinvention de l\'amour, dans laquelle Boris Bergmann explore les relations familiales et la figure du père.', 20.90, '2026-08-19', 256, 20.90, 1, 1),
('9782246846949', 'Chronique d\'un royaume perdu', 'Au Bouchon, petit village isolé de l\'île Maurice, quatre générations se succèdent depuis le temps de l\'esclavage. Une fresque familiale et mythologique où se mêlent histoire, violence, surnaturel et héritage.', 24.00, '2026-08-19', 464, 24.00, 3, 3),
('9782246847069', 'C\'était ça ou mourir', 'Jonas fuit Haïti et entreprend une longue traversée vers le Canada. Son parcours d\'exil est marqué par la faim, la peur, les blessures et les solidarités qui lui permettent de continuer à avancer.', 21.50, '2026-08-19', 272, 21.50, 13, 3),
('9782330225575', 'Nous aussi', 'Une famille parisienne vit dans un monde clos où les enfants, les frères, les sœurs et les cousins forment un ensemble indissociable. Lorsque cette unité se fissure, les certitudes familiales vacillent.', 21.00, '2026-08-19', 240, 21.00, 5, 5),
('9782378562953', 'N\'efface pas mes cercles', 'En remontant l\'histoire de sa famille, une narratrice cherche à comprendre le suicide d\'une femme en 1980 et les destins brisés de plusieurs générations marquées par le patriarcat, la guerre et la colonisation.', 19.50, '2026-08-20', 160, 19.50, 11, 9),
('9782378805975', 'Joseph dans la nuit', 'Un récit consacré à Joseph, confronté à l\'emprisonnement en Iran, qui interroge la liberté, la résistance et la capacité de l\'être humain à préserver une part de lui-même dans l\'adversité.', 19.90, '2026-08-20', 256, 19.90, 6, 6),
('9782707358233', 'De l\'autre côté du lac', 'Aux abords d\'un lac de haute montagne, une photographe découvre des signes étranges tandis qu\'un corps est retrouvé. Elle décide de rester seule dans cet environnement sauvage, où les disparitions se succèdent.', 22.00, '2026-01-01', 288, 22.00, 14, 10),
('9782818063583', 'Faire la peau', 'Une réflexion romanesque sur les relations entre les mères et leurs filles, la filiation et la violence qui peut se transmettre au sein d\'une famille.', 21.00, '2026-08-20', 288, 21.00, 2, 2),
('9782862316857', 'Bataille au procès', 'En 1956, Georges Bataille témoigne au procès de Jean-Jacques Pauvert, poursuivi pour avoir publié les œuvres de Sade. Cet épisode conduit Bataille à réfléchir aux rapports entre morale, littérature, création et transgression.', 19.00, '2026-08-21', 136, 19.00, 16, 11);

-- --------------------------------------------------------

--
-- Structure de la table `editor`
--

CREATE TABLE `editor` (
  `id_editor` int(10) UNSIGNED NOT NULL,
  `label` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `editor`
--

INSERT INTO `editor` (`id_editor`, `label`) VALUES
(1, 'Albin Michel'),
(2, 'P.O.L'),
(3, 'Grasset'),
(4, 'Robert Laffont'),
(5, 'Actes Sud'),
(6, 'L\'Iconoclaste'),
(7, 'Gallimard'),
(8, 'Flammarion'),
(9, 'Verdier'),
(10, 'Éditions de Minuit'),
(11, 'Éditions Maurice Nadeau');

-- --------------------------------------------------------

--
-- Structure de la table `jury_member`
--

CREATE TABLE `jury_member` (
  `id_jury_member` int(10) UNSIGNED NOT NULL,
  `id_person` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `jury_member`
--

INSERT INTO `jury_member` (`id_jury_member`, `id_person`) VALUES
(1, 17),
(2, 18),
(3, 19),
(4, 20),
(5, 21),
(6, 22),
(7, 23),
(8, 24),
(9, 25),
(10, 26);

-- --------------------------------------------------------

--
-- Structure de la table `main_character`
--

CREATE TABLE `main_character` (
  `id_main_character` int(10) UNSIGNED NOT NULL,
  `name` varchar(50) NOT NULL,
  `isbn` char(13) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `main_character`
--

INSERT INTO `main_character` (`id_main_character`, `name`, `isbn`) VALUES
(1, 'Jean Deichel', '9782073161925'),
(2, 'Antoinette Cosway', '9782073099945'),
(3, 'Edward Rochester', '9782073099945'),
(4, 'Louise Cansot', '9782080490896'),
(5, 'Inspecteur-chef Ferrière', '9782080490896'),
(6, 'Jacob Michael Lenz', '9782226499523'),
(7, 'Mia', '9782378562953'),
(8, 'Elsa', '9782378562953'),
(9, 'François', '9782378562953'),
(10, 'Émilie', '9782073162854'),
(11, 'Tristan', '9782073162854'),
(12, 'Paola', '9782707358233'),
(13, 'Georges Bataille', '9782862316857'),
(14, 'Jean-Jacques Pauvert', '9782862316857'),
(15, 'Jonas Dorléon', '9782246847069');

-- --------------------------------------------------------

--
-- Structure de la table `person`
--

CREATE TABLE `person` (
  `id_person` int(10) UNSIGNED NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `person`
--

INSERT INTO `person` (`id_person`, `first_name`, `last_name`) VALUES
(1, 'Boris', 'Bergmann'),
(2, 'Louise', 'Chennevière'),
(3, 'Ananda', 'Devi'),
(4, 'Sonia', 'Devillers'),
(5, 'Anne', 'Godard'),
(6, 'Olivier', 'Grondeau'),
(7, 'Yannick', 'Haenel'),
(8, 'Lilia', 'Hassaine'),
(9, 'Philippe', 'Jaenada'),
(10, 'Jean-Yves', 'Jouannais'),
(11, 'Emma', 'Marsantes'),
(12, 'Clémentine', 'Mélois'),
(13, 'Thélyson', 'Orélien'),
(14, 'Sylvain', 'Prudhomme'),
(15, 'Olivier', 'Rolin'),
(16, 'Patrice', 'Trigano'),
(17, 'Didier', 'Decoin'),
(18, 'Françoise', 'Chandernagor'),
(19, 'Tahar', 'Ben Jelloun'),
(20, 'Paule', 'Constant'),
(21, 'Philippe', 'Claudel'),
(22, 'Pierre', 'Assouline'),
(23, 'Éric-Emmanuel', 'Schmitt'),
(24, 'Camille', 'Laurens'),
(25, 'Pascal', 'Bruckner'),
(26, 'Christine', 'Angot');

-- --------------------------------------------------------

--
-- Structure de la table `president`
--

CREATE TABLE `president` (
  `id_president` int(10) UNSIGNED NOT NULL,
  `id_jury_member` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `president`
--

INSERT INTO `president` (`id_president`, `id_jury_member`) VALUES
(1, 5);

-- --------------------------------------------------------

--
-- Structure de la table `selection`
--

CREATE TABLE `selection` (
  `selection_nbr` int(10) UNSIGNED NOT NULL,
  `selection_date` date DEFAULT NULL,
  `id_president` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `selection`
--

INSERT INTO `selection` (`selection_nbr`, `selection_date`, `id_president`) VALUES
(1, '2026-09-02', 1);

-- --------------------------------------------------------

--
-- Structure de la table `selection_book`
--

CREATE TABLE `selection_book` (
  `selection_nbr` int(10) UNSIGNED NOT NULL,
  `isbn` char(13) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `selection_book`
--

INSERT INTO `selection_book` (`selection_nbr`, `isbn`) VALUES
(1, '9782073099945'),
(1, '9782073121349'),
(1, '9782073161925'),
(1, '9782073162854'),
(1, '9782080490896'),
(1, '9782221286807'),
(1, '9782226499523'),
(1, '9782226511874'),
(1, '9782246846949'),
(1, '9782246847069'),
(1, '9782330225575'),
(1, '9782378562953'),
(1, '9782378805975'),
(1, '9782707358233'),
(1, '9782818063583'),
(1, '9782862316857');

-- --------------------------------------------------------

--
-- Structure de la table `vote`
--

CREATE TABLE `vote` (
  `isbn` char(13) NOT NULL,
  `id_jury_member` int(10) UNSIGNED NOT NULL,
  `selection_nbr` int(10) UNSIGNED NOT NULL,
  `turn` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `vote`
--

INSERT INTO `vote` (`isbn`, `id_jury_member`, `selection_nbr`, `turn`) VALUES
('9782073121349', 1, 1, 2),
('9782073121349', 1, 1, 3),
('9782226511874', 1, 1, 1),
('9782073121349', 2, 1, 3),
('9782330225575', 2, 1, 1),
('9782818063583', 2, 1, 2),
('9782073121349', 3, 1, 2),
('9782818063583', 3, 1, 1),
('9782818063583', 3, 1, 3),
('9782073121349', 4, 1, 3),
('9782818063583', 4, 1, 1),
('9782818063583', 4, 1, 2),
('9782073121349', 5, 1, 1),
('9782073121349', 5, 1, 2),
('9782818063583', 5, 1, 3),
('9782073121349', 6, 1, 1),
('9782073121349', 6, 1, 3),
('9782818063583', 6, 1, 2),
('9782073121349', 7, 1, 1),
('9782073121349', 7, 1, 2),
('9782818063583', 7, 1, 3),
('9782073099945', 8, 1, 1),
('9782073121349', 8, 1, 3),
('9782818063583', 8, 1, 2),
('9782073121349', 9, 1, 2),
('9782073121349', 9, 1, 3),
('9782226499523', 9, 1, 1),
('9782818063583', 10, 1, 2),
('9782818063583', 10, 1, 3),
('9782862316857', 10, 1, 1);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `author`
--
ALTER TABLE `author`
  ADD PRIMARY KEY (`id_author`),
  ADD UNIQUE KEY `id_person` (`id_person`);

--
-- Index pour la table `book`
--
ALTER TABLE `book`
  ADD PRIMARY KEY (`isbn`),
  ADD KEY `id_author` (`id_author`),
  ADD KEY `id_editor` (`id_editor`);

--
-- Index pour la table `editor`
--
ALTER TABLE `editor`
  ADD PRIMARY KEY (`id_editor`);

--
-- Index pour la table `jury_member`
--
ALTER TABLE `jury_member`
  ADD PRIMARY KEY (`id_jury_member`),
  ADD UNIQUE KEY `id_person` (`id_person`);

--
-- Index pour la table `main_character`
--
ALTER TABLE `main_character`
  ADD PRIMARY KEY (`id_main_character`),
  ADD KEY `isbn` (`isbn`);

--
-- Index pour la table `person`
--
ALTER TABLE `person`
  ADD PRIMARY KEY (`id_person`);

--
-- Index pour la table `president`
--
ALTER TABLE `president`
  ADD PRIMARY KEY (`id_president`),
  ADD UNIQUE KEY `id_jury_member` (`id_jury_member`);

--
-- Index pour la table `selection`
--
ALTER TABLE `selection`
  ADD PRIMARY KEY (`selection_nbr`),
  ADD KEY `id_president` (`id_president`);

--
-- Index pour la table `selection_book`
--
ALTER TABLE `selection_book`
  ADD PRIMARY KEY (`selection_nbr`,`isbn`),
  ADD KEY `isbn` (`isbn`);

--
-- Index pour la table `vote`
--
ALTER TABLE `vote`
  ADD PRIMARY KEY (`isbn`,`id_jury_member`,`selection_nbr`,`turn`),
  ADD KEY `id_jury_member` (`id_jury_member`),
  ADD KEY `selection_nbr` (`selection_nbr`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `author`
--
ALTER TABLE `author`
  MODIFY `id_author` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT pour la table `editor`
--
ALTER TABLE `editor`
  MODIFY `id_editor` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT pour la table `jury_member`
--
ALTER TABLE `jury_member`
  MODIFY `id_jury_member` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT pour la table `main_character`
--
ALTER TABLE `main_character`
  MODIFY `id_main_character` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT pour la table `person`
--
ALTER TABLE `person`
  MODIFY `id_person` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT pour la table `president`
--
ALTER TABLE `president`
  MODIFY `id_president` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `author`
--
ALTER TABLE `author`
  ADD CONSTRAINT `author_ibfk_1` FOREIGN KEY (`id_person`) REFERENCES `person` (`id_person`);

--
-- Contraintes pour la table `book`
--
ALTER TABLE `book`
  ADD CONSTRAINT `book_ibfk_1` FOREIGN KEY (`id_author`) REFERENCES `author` (`id_author`),
  ADD CONSTRAINT `book_ibfk_2` FOREIGN KEY (`id_editor`) REFERENCES `editor` (`id_editor`);

--
-- Contraintes pour la table `jury_member`
--
ALTER TABLE `jury_member`
  ADD CONSTRAINT `jury_member_ibfk_1` FOREIGN KEY (`id_person`) REFERENCES `person` (`id_person`);

--
-- Contraintes pour la table `main_character`
--
ALTER TABLE `main_character`
  ADD CONSTRAINT `main_character_ibfk_1` FOREIGN KEY (`isbn`) REFERENCES `book` (`isbn`);

--
-- Contraintes pour la table `president`
--
ALTER TABLE `president`
  ADD CONSTRAINT `president_ibfk_1` FOREIGN KEY (`id_jury_member`) REFERENCES `jury_member` (`id_jury_member`);

--
-- Contraintes pour la table `selection`
--
ALTER TABLE `selection`
  ADD CONSTRAINT `selection_ibfk_1` FOREIGN KEY (`id_president`) REFERENCES `president` (`id_president`);

--
-- Contraintes pour la table `selection_book`
--
ALTER TABLE `selection_book`
  ADD CONSTRAINT `selection_book_ibfk_1` FOREIGN KEY (`selection_nbr`) REFERENCES `selection` (`selection_nbr`),
  ADD CONSTRAINT `selection_book_ibfk_2` FOREIGN KEY (`isbn`) REFERENCES `book` (`isbn`);

--
-- Contraintes pour la table `vote`
--
ALTER TABLE `vote`
  ADD CONSTRAINT `vote_ibfk_1` FOREIGN KEY (`isbn`) REFERENCES `book` (`isbn`),
  ADD CONSTRAINT `vote_ibfk_2` FOREIGN KEY (`id_jury_member`) REFERENCES `jury_member` (`id_jury_member`),
  ADD CONSTRAINT `vote_ibfk_3` FOREIGN KEY (`selection_nbr`) REFERENCES `selection` (`selection_nbr`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
