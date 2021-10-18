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
    prereqCourse varchar(255) NOT NULL,
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
    chapterDetails varchar(255) NOT NULL,
    quizID int(11) NOT NULL,
    CONSTRAINT chapter_pk PRIMARY KEY (chapterID),
    CONSTRAINT chapter_fk FOREIGN KEY (quizID) REFERENCES QUIZ(quizID)
);

DROP TABLE IF EXISTS GRADEDQUIZ;
CREATE TABLE GRADEDQUIZ
(
    quizID int(11) NOT NULL,
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

DROP TABLE IF EXISTS LEARNER_QUIZ;
CREATE TABLE LEARNER_QUIZ
(
    quizID int(11) NOT NULL,
    staffID int(11) NOT NULL,
    quizScore int(11) NOT NULL,
    CONSTRAINT learner_quiz_pk PRIMARY KEY (quizID, staffID),
    CONSTRAINT learner_quiz_fk FOREIGN KEY (quizID) REFERENCES QUIZ(quizID),
    CONSTRAINT learner_quiz_fk2 FOREIGN KEY (staffID) REFERENCES LEARNER(staffID)
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
(1, 'IBM 101', 'IBM', 'None', 2),
(2, 'IBM 102', 'IBM', 'IBM 101', 4),
(3, 'HP 101', 'HP', 'None', 1),
(4, 'HP 102', 'HP', 'HP 101', 3),
(5, 'Xerox 101', 'Xerox', 'None', 2),
(6, 'Xerox 102', 'Xerox', 'Xerox 101', 2),
(7, 'Canon 101', 'Canon', 'None', 3),
(8, 'Canon 102', 'Canon', 'Canon 101', 1);

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

INSERT INTO QUIZ VALUES
(1, '2021-01-01', '2021-01-03'),
(2, '2021-01-01', '2021-01-03'),
(3, '2021-01-01', '2021-01-03'),
(4, '2021-01-01', '2021-01-03'),
(5, '2021-01-03', '2021-02-07'),
(6, '2021-01-03', '2021-02-07'),
(7, '2021-01-03', '2021-02-07'),
(8, '2021-01-03', '2021-02-07'),
(9, '2021-01-03', '2021-02-07'),
(10, '2021-02-07', '2021-12-21'),
(11, '2021-02-07', '2021-12-21'),
(12, '2021-02-07', '2021-12-21'),
(13, '2021-02-07', '2021-12-21'),
(14, '2021-02-07', '2021-12-21'),
(15, '2021-02-07', '2021-12-21'),
(16, '2021-12-21', '2022-02-28'),
(17, '2021-12-21', '2022-02-28'),
(18, '2021-12-21', '2022-02-28');

INSERT INTO QUESTION VALUES
(1, 'Is cat cute?', 'True'),
(2, 'Is dog cute?', 'True'),
(3, 'Is turtle cute?', 'True'),
(4, 'Is life cute?', 'False'),
(5, 'Is foetus cute?', 'False'),
(6, 'Is baby cute?', 'True'),
(7, 'Is diluc cute?', 'True'),
(8, 'Is zhongli cute?', 'True'),
(9, 'Which cat is cutest?', 'B'),
(10, 'Which dog is cuter?', 'C'),
(11, 'AAA', 'D'),
(12, 'BBB', 'B'),
(13, 'BBV', 'C'),
(14, 'CCC', 'True'),
(15, 'DDD', 'F'),
(16, 'EEE', 'E'),
(17, 'FFF', 'False'),
(18, 'GGG', 'G');

INSERT INTO CHAPTER VALUES
(1, 'CAT', 'A cat is running away', 1),
(2, 'DOG', 'A dog is running away',2),
(3, 'TURTLE', 'A turtle is running away', 3),
(4, 'LIFE', 'My life is great', 4),
(5, 'foetus', 'A foetus is growing', 5),
(6, 'baby', 'A baby is crawling away', 6),
(7, 'diluc', 'yay diluc', 7),
(8, 'zhongli', 'yay zhongli', 8),
(9, 'cutest', 'yay cutest', 9),
(10, 'cuter', 'yay cuter', 10),
(11, 'AAA', 'AAA yummy', 11),
(12, 'BBB', 'BBB happy', 12),
(13, 'BBV', 'BBV bumble bee', 13),
(14, 'CCC', 'CCC bumble bee', 14),
(15, 'DDD', 'DDD bumble bee', 15),
(16, 'EEE', 'EEE bumble bee', 16),
(17, 'FFF', 'FFF bumble bee', 17),
(18, 'GGG', 'GGG bumble bee', 18);

INSERT INTO GRADEDQUIZ VALUES
(1, 50),
(2, 50),
(3, 50),
(4, 50),
(5, 50),
(6, 50),
(7, 50);

INSERT INTO CLASS_CHAPTER VALUES
(1, 1, 1),
(1, 1, 2);

INSERT INTO TRAINER VALUES
(3, 10),
(4, 8);

INSERT INTO LEARNER VALUES
(1, 1),
(2, 1),
(6, 1),
(7, 1),
(8, 1),
(9, 1);

INSERT INTO TEACH_CLASS VALUES
(3, 1, 1),
(3, 1, 2),
(3, 2, 3),
(3, 2, 4),
(4, 2, 5),
(4, 2, 6),
(4, 3, 7),
(3, 4, 8),
(3, 4, 9),
(3, 4, 10),
(4, 5, 11),
(4, 5, 12),
(4, 6, 13),
(4, 6, 14),
(3, 7, 15),
(3, 7, 16),
(3, 7, 17),
(4, 8, 18);

INSERT INTO MATERIAL VALUES
(1, "aaa", "document", "https://cseweb.ucsd.edu/classes/sp15/cse190-c/reports/sp15/048.pdf", "Info", 1),
(2, "bbb", "link", "www.google.com", "Website", 2),
(3, "bbb", "video", "https://www.youtube.com/watch?v=mFFXuXjVgkU&ab_channel=DevOpsJourney", "Vid", 3);

INSERT INTO TAKE_CLASS VALUES
(1, 1, 1),
(2, 1, 2),
(6, 2, 3),
(7, 2, 4),
(8, 2, 5),
(9, 2, 6);

INSERT INTO QUIZ_QUESTION VALUES
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(2, 1),
(2, 2),
(2, 3),
(2, 4),
(3, 1);

INSERT INTO LEARNER_QUIZ VALUES
(1, 1, 23),
(2, 1, 14),
(3, 1, 46),
(1, 2, 22),
(2, 2, 45),
(3, 2, 23),
(3, 6, 24),
(2, 7, 15),
(1, 8, 50);





