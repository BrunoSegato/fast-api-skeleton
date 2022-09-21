-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema zoo
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema zoo
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `zoo` DEFAULT CHARACTER SET utf8mb4 ;
USE `zoo` ;

-- -----------------------------------------------------
-- Table `zoo`.`animal`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `zoo`.`animal` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(80) NOT NULL,
  `type` ENUM('MAMMAL', 'BIRD', 'FISH', 'REPTILE', 'AMPHIBIAN', 'INSECT') NOT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_at` TIMESTAMP NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

CREATE INDEX `animal_created_at_idx` ON `zoo`.`animal` (`created_at` ASC) VISIBLE;

CREATE INDEX `animal_updated_at_idx` ON `zoo`.`animal` (`updated_at` ASC) VISIBLE;

CREATE INDEX `animal_deleted_at_idx` ON `zoo`.`animal` (`deleted_at` ASC) VISIBLE;

CREATE INDEX `animal_name_idx` ON `zoo`.`animal` (`name` ASC) VISIBLE;

CREATE UNIQUE INDEX `animal_unq` ON `zoo`.`animal` (`name` ASC) VISIBLE;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
