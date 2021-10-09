DROP DATABASE IF EXISTS spm_proj;
CREATE DATABASE spm_proj;

USE spm_proj;

DROP TABLE IF EXISTS STAFF;
CREATE TABLE STAFF
(
    staffID int(11) NOT NULL AUTO_INCREMENT,
    staffUsername varchar(255) NOT NULL,
    staffName varchar(255) NOT NULL,
    department varchar(255) NOT NULL,
    CONSTRAINT staff_pk PRIMARY KEY (staffID)
);

DROP TABLE IF EXISTS COURSE;
CREATE TABLE COURSE
(
    courseID int(11) NOT NULL AUTO_INCREMENT,
    courseName varchar(255) NOT NULL,
    courseCategory varchar(255) NOT NULL,
    noOfClasses int(11) NOT NULL,
    CONSTRAINT course_pk PRIMARY KEY (courseID)
);

DROP TABLE IF EXISTS CLASS;
CREATE TABLE CLASS
(
    classID int(11) NOT NULL,
    courseID int(11) NOT NULL,
    startDate date NOT NULL,
    endDate date NOT NULL,
    startTime time NOT NULL,
    endTime time NOT NULL,
    classSize int(11) NOT NULL,
    trainerName varchar(255) NOT NULL,
    staffID int(11) NOT NULL,
    CONSTRAINT class_pk PRIMARY KEY (courseID, classID),
    CONSTRAINT class_fk FOREIGN KEY (courseID) REFERENCES COURSE(courseID),
    CONSTRAINT class_fk2 FOREIGN KEY (staffID) REFERENCES STAFF(staffID)
);

DROP TABLE IF EXISTS QUIZ;
CREATE TABLE QUIZ
(
    quizID int(11) NOT NULL AUTO_INCREMENT,
    startDate date NOT NULL,
    endDate date NOT NULL,
    CONSTRAINT quiz_pk PRIMARY KEY (quizID)
);

DROP TABLE IF EXISTS QUESTION;
CREATE TABLE QUESTION
(
    questionID int(11) NOT NULL AUTO_INCREMENT,
    question varchar(255) NOT NULL,
    answer varchar(255) NOT NULL,
    CONSTRAINT question_pk PRIMARY KEY (questionID)
);

DROP TABLE IF EXISTS CHAPTER;
CREATE TABLE CHAPTER
(
    chapterID int(11) NOT NULL AUTO_INCREMENT,
    chapterName varchar(255) NOT NULL,
    quizID int(11) NOT NULL,
    CONSTRAINT chapter_pk PRIMARY KEY (chapterID),
    CONSTRAINT chapter_fk FOREIGN KEY (quizID) REFERENCES QUIZ(quizID)
);

DROP TABLE IF EXISTS GRADEDQUIZ;
CREATE TABLE GRADEDQUIZ 
(
    quizID int(11) NOT NULL,
    quizScore int(11) NOT NULL,
    passingScore int(11) NOT NULL,
    CONSTRAINT gradedquiz_pk PRIMARY KEY (quizID),
    CONSTRAINT gradedquiz_fk FOREIGN KEY (quizID) REFERENCES QUIZ(quizID)
);

DROP TABLE IF EXISTS CLASS_CHAPTER;
CREATE TABLE CLASS_CHAPTER  
(
    courseID int(11) NOT NULL,
    classID int(11) NOT NULL,
    chapterID int(11) NOT NULL,
    CONSTRAINT class_chapter_pk PRIMARY KEY (courseID, classID, chapterID),
    CONSTRAINT class_chapter_fk FOREIGN KEY (courseID, classID) REFERENCES CLASS(courseID, classID),
    CONSTRAINT class_chapter_fk2 FOREIGN KEY (chapterID) REFERENCES CHAPTER(chapterID)
);

DROP TABLE IF EXISTS TRAINER;
CREATE TABLE TRAINER  
(
    staffID int(11) NOT NULL,
    numberOfClasses int(11) NOT NULL,
    CONSTRAINT trainer_pk PRIMARY KEY (staffID),
    CONSTRAINT trainer_fk FOREIGN KEY (staffID) REFERENCES STAFF(staffID)
);

DROP TABLE IF EXISTS LEARNER;
CREATE TABLE LEARNER  
(
    staffID int(11) NOT NULL,
    numberOfClassesPassed int(11) NOT NULL,
    CONSTRAINT learner_pk PRIMARY KEY (staffID),
    CONSTRAINT learner_fk FOREIGN KEY (staffID) REFERENCES STAFF(staffID)
);

DROP TABLE IF EXISTS TEACH_CLASS;
CREATE TABLE TEACH_CLASS   
(
    staffID int(11) NOT NULL,
    courseID int(11) NOT NULL,
    classID int(11) NOT NULL,
    CONSTRAINT teach_class_pk PRIMARY KEY (staffID, courseID, classID),
    CONSTRAINT teach_class_fk FOREIGN KEY (staffID) REFERENCES STAFF(staffID),
    CONSTRAINT teach_class_fk2 FOREIGN KEY (courseID, classID) REFERENCES CLASS(courseID, classID)
);

DROP TABLE IF EXISTS MATERIAL;
CREATE TABLE MATERIAL   
(
    materialID int(11) NOT NULL AUTO_INCREMENT,
    materialName varchar(255) NOT NULL,
    materialType varchar(255) NOT NULL,
    materialLink varchar(255) NOT NULL,
    materialLinkBody varchar(255) NOT NULL,
    chapterID int(11) NOT NULL,
    CONSTRAINT material_pk PRIMARY KEY (materialID),
    CONSTRAINT material_fk FOREIGN KEY (chapterID) REFERENCES CHAPTER(chapterID)

);

DROP TABLE IF EXISTS TAKE_CLASS;
CREATE TABLE TAKE_CLASS   
(
    staffID int(11) NOT NULL,
    courseID int(11) NOT NULL,
    classID int(11) NOT NULL,
    CONSTRAINT take_class_pk PRIMARY KEY (staffID, courseID, classID),
    CONSTRAINT take_class_fk FOREIGN KEY (staffID) REFERENCES STAFF(staffID),
    CONSTRAINT take_class_fk2 FOREIGN KEY (courseID, classID) REFERENCES CLASS(courseID, classID)
);

DROP TABLE IF EXISTS QUIZ_QUESTION;
CREATE TABLE QUIZ_QUESTION    
(
    quizID int(11) NOT NULL,
    questionID int(11) NOT NULL,
    CONSTRAINT quiz_question_pk PRIMARY KEY (quizID, questionID),
    CONSTRAINT quiz_question_fk FOREIGN KEY (quizID) REFERENCES QUIZ(quizID),
    CONSTRAINT quiz_question_fk2 FOREIGN KEY (questionID) REFERENCES QUESTION(questionID)
);

INSERT INTO STAFF VALUES
(1, 'gerry', 'Geraldine', 'Learner'),
(2, 'ly', 'Ley Yi', 'Learner'),
(3, 'gellybear', 'Haoyue', 'Trainer'),
(4, 'jewel', 'Jewel', 'Trainer'),
(5, 'wesley', 'Wesley', 'Administrator'),
(6, 'AAA', 'AAAAA', 'Learner'),
(7, 'BBB', 'BBBBB', 'Learner'),
(8, 'CCC', 'CCCCCC', 'Learner'),
(9, 'DDD', 'DDDDDDD', 'Learner'),
(10, 'EEE', 'EEEEEE', 'Administrator');

INSERT INTO COURSE VALUES
(1, 'IBM 101', 'IBM', 2),
(2, 'IBM 102', 'IBM', 4),
(3, 'HP 101', 'HP', 1),
(4, 'HP 102', 'HP', 3),
(5, 'Xerox 101', 'Xerox', 2),
(6, 'Xerox 102', 'Xerox', 2),
(7, 'Canon 101', 'Canon', 3),
(8, 'Canon 102', 'Canon', 1);

INSERT INTO CLASS VALUES
(1, 1, '2021-01-01', '2021-01-03', '22:30:00', '23:30:00', 4, 'Haoyue', 3),
(2, 1, '2021-01-01', '2021-01-03', '12:30:00', '01:30:00', 4, 'Haoyue', 3),
(3, 2, '2021-01-01', '2021-01-03', '01:30:00', '02:30:00', 4, 'Haoyue', 3),
(4, 2, '2021-01-01', '2021-01-03', '02:30:00', '03:30:00', 4, 'Haoyue', 3),
(5, 2, '2021-01-03', '2021-02-07', '22:30:00', '23:30:00', 4, 'Jewel', 4),
(6, 2, '2021-01-03', '2021-02-07', '12:30:00', '02:30:00', 4, 'Jewel', 4),
(7, 3, '2021-01-03', '2021-02-07', '01:30:00', '02:30:00', 4, 'Jewel', 4),
(8, 4, '2021-01-03', '2021-02-07', '02:30:00', '03:30:00', 4, 'Haoyue', 3),
(9, 4, '2021-01-03', '2021-02-07', '02:00:00', '03:30:00', 4, 'Haoyue', 3),
(10, 4, '2021-02-07', '2021-12-21', '22:30:00', '23:30:00', 1, 'Haoyue', 3),
(11, 5, '2021-02-07', '2021-12-21', '12:30:00', '13:30:00', 1, 'Jewel', 4),
(12, 5, '2021-02-07', '2021-12-21', '01:30:00','02:30:00', 1, 'Jewel', 4),
(13, 6, '2021-02-07', '2021-12-21', '02:00:00', '02:30:00', 1, 'Jewel', 4),
(14, 6, '2021-02-07', '2021-12-21', '02:30:00', '03:30:00', 1, 'Jewel', 4),
(15, 7, '2021-02-07', '2021-12-21', '04:30:00', '05:30:00', 1, 'Haoyue', 3),
(16, 7, '2021-12-21', '2022-02-28', '22:30:00', '23:30:00', 2, 'Haoyue', 3),
(17, 7,  '2021-12-21', '2022-02-28', '12:30:00', '13:30:00', 2, 'Haoyue', 3),
(18, 8, '2021-12-21', '2022-02-28', '22:30:00', '23:30:00', 2, 'Jewel', 4);