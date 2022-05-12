use pbl;

CREATE TABLE `pbl`.`student` (
  `PRN` INT(20) NOT NULL,
  `fname` VARCHAR(45) NOT NULL,
  `lname` VARCHAR(45) NOT NULL,
  `DOB` DATE NOT NULL,
  `grad_year` INT(5) NOT NULL,
  `city` VARCHAR(45) NOT NULL,
  `gender` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`PRN`));