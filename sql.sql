/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 10.4.28-MariaDB : Database - easy_learn
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`easy_learn` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `easy_learn`;

/*Data for the table `auth_group` */

/*Data for the table `auth_group_permissions` */

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add login',7,'add_login'),
(26,'Can change login',7,'change_login'),
(27,'Can delete login',7,'delete_login'),
(28,'Can view login',7,'view_login'),
(29,'Can add subject',8,'add_subject'),
(30,'Can change subject',8,'change_subject'),
(31,'Can delete subject',8,'delete_subject'),
(32,'Can view subject',8,'view_subject'),
(33,'Can add user',9,'add_user'),
(34,'Can change user',9,'change_user'),
(35,'Can delete user',9,'delete_user'),
(36,'Can view user',9,'view_user'),
(37,'Can add uploads',10,'add_uploads'),
(38,'Can change uploads',10,'change_uploads'),
(39,'Can delete uploads',10,'delete_uploads'),
(40,'Can view uploads',10,'view_uploads'),
(41,'Can add stategovernment',11,'add_tutor'),
(42,'Can change stategovernment',11,'change_tutor'),
(43,'Can delete stategovernment',11,'delete_tutor'),
(44,'Can view stategovernment',11,'view_tutor'),
(45,'Can add reviews',12,'add_reviews'),
(46,'Can change reviews',12,'change_reviews'),
(47,'Can delete reviews',12,'delete_reviews'),
(48,'Can view reviews',12,'view_reviews'),
(49,'Can add notes',13,'add_notes'),
(50,'Can change notes',13,'change_notes'),
(51,'Can delete notes',13,'delete_notes'),
(52,'Can view notes',13,'view_notes'),
(53,'Can add feedback',14,'add_feedback'),
(54,'Can change feedback',14,'change_feedback'),
(55,'Can delete feedback',14,'delete_feedback'),
(56,'Can view feedback',14,'view_feedback'),
(57,'Can add doubt',15,'add_doubt'),
(58,'Can change doubt',15,'change_doubt'),
(59,'Can delete doubt',15,'delete_doubt'),
(60,'Can view doubt',15,'view_doubt'),
(61,'Can add complaints',16,'add_complaints'),
(62,'Can change complaints',16,'change_complaints'),
(63,'Can delete complaints',16,'delete_complaints'),
(64,'Can view complaints',16,'view_complaints');

/*Data for the table `auth_user` */

/*Data for the table `auth_user_groups` */

/*Data for the table `auth_user_user_permissions` */

/*Data for the table `django_admin_log` */

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(16,'myapp','complaints'),
(15,'myapp','doubt'),
(14,'myapp','feedback'),
(7,'myapp','login'),
(13,'myapp','notes'),
(12,'myapp','reviews'),
(8,'myapp','subject'),
(11,'myapp','stategovernment'),
(10,'myapp','uploads'),
(9,'myapp','user'),
(6,'sessions','session');

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2024-01-10 04:07:51.710042'),
(2,'auth','0001_initial','2024-01-10 04:07:52.092264'),
(3,'admin','0001_initial','2024-01-10 04:07:52.190795'),
(4,'admin','0002_logentry_remove_auto_add','2024-01-10 04:07:52.199741'),
(5,'admin','0003_logentry_add_action_flag_choices','2024-01-10 04:07:52.207418'),
(6,'contenttypes','0002_remove_content_type_name','2024-01-10 04:07:52.267910'),
(7,'auth','0002_alter_permission_name_max_length','2024-01-10 04:07:52.309525'),
(8,'auth','0003_alter_user_email_max_length','2024-01-10 04:07:52.322943'),
(9,'auth','0004_alter_user_username_opts','2024-01-10 04:07:52.330631'),
(10,'auth','0005_alter_user_last_login_null','2024-01-10 04:07:52.360696'),
(11,'auth','0006_require_contenttypes_0002','2024-01-10 04:07:52.363713'),
(12,'auth','0007_alter_validators_add_error_messages','2024-01-10 04:07:52.371822'),
(13,'auth','0008_alter_user_username_max_length','2024-01-10 04:07:52.384075'),
(14,'auth','0009_alter_user_last_name_max_length','2024-01-10 04:07:52.395905'),
(15,'auth','0010_alter_group_name_max_length','2024-01-10 04:07:52.410440'),
(16,'auth','0011_update_proxy_permissions','2024-01-10 04:07:52.419701'),
(17,'auth','0012_alter_user_first_name_max_length','2024-01-10 04:07:52.432364'),
(18,'myapp','0001_initial','2024-01-10 04:07:52.960085'),
(19,'sessions','0001_initial','2024-01-10 04:07:52.986951'),
(20,'myapp','0002_auto_20240111_1200','2024-01-11 06:30:45.402762'),
(21,'myapp','0003_rename_notes_notes_note','2024-01-11 07:02:28.592610'),
(22,'myapp','0004_auto_20240111_1439','2024-01-11 09:09:48.314528'),
(23,'myapp','0005_rename_feedback_feedback_feedbacks','2024-01-11 09:55:03.680289'),
(24,'myapp','0006_auto_20240111_1529','2024-01-11 09:59:39.907953'),
(25,'myapp','0007_doubt_status','2024-01-12 03:26:02.517912');

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('yx6yxjqf1zn54dabdnffj3k604hmtfd5','eyJsaWQiOjd9:1rNnC5:hyWK0Wja11fSF04em2HN1ZC0wtnQXCeuo3F-9hlqgU0','2024-01-25 05:01:29.255723');

/*Data for the table `myapp_complaints` */

insert  into `myapp_complaints`(`id`,`Compliant`,`Date`,`Status`,`Replay`,`LOGIN_id`) values 
(1,'sdf','2024-01-10','Cleared','zzz',1),
(2,'admin','2024-01-11','pending','pending',7);

/*Data for the table `myapp_doubt` */

insert  into `myapp_doubt`(`id`,`Doubt`,`Date`,`Reply`,`TUTOR_id`,`USER_id`,`Status`) values 
(1,'bhmjjbhn','2024-01-12','zzz',8,1,'Cleared');

/*Data for the table `myapp_feedback` */

insert  into `myapp_feedback`(`id`,`Date`,`Feedbacks`,`LOGIN_id`) values 
(1,'2024-01-10','sdf',1);

/*Data for the table `myapp_login` */

insert  into `myapp_login`(`id`,`Name`,`Password`,`Usertype`) values 
(1,'admin@gmail.com','Admin@12','Admin'),
(2,'xxx','xxx','stategovernment'),
(3,'yyy','yyy','pending'),
(4,'zzz','zzz','stategovernment'),
(5,'iuy@gmail.com','111','User'),
(6,'nayanzz@gmail.com','123','pending'),
(7,'zzz@123','123','Tutor');

/*Data for the table `myapp_notes` */

/*Data for the table `myapp_reviews` */

insert  into `myapp_reviews`(`id`,`Review`,`Date`,`Rating`,`USER_id`) values 
(1,'lhjk','2024-01-10','4.5',1),
(2,'fdvx','2024-01-10','4',1);

/*Data for the table `myapp_subject` */

insert  into `myapp_subject`(`id`,`Subject_name`) values 
(3,'maths');

/*Data for the table `myapp_tutor` */

insert  into `myapp_tutor`(`id`,`Name`,`Photo`,`Phone_number`,`DOB`,`Gender`,`Qualification`,`Email`,`District`,`State`,`Status`,`LOGIN_id`) values 
(1,'xxx','',765567886,'2024-01-10','m','xxx','xxx','xxx','xxx','approved',2),
(3,'yyy','',45632,'2024-02-09','f','yyy','yyy','yyy','yyy','rejected',3),
(7,'yyy','',3452342352,'2024-03-01','o','zzz','zzz','zzz','zzz','pending',4),
(8,'Nayana','/media/2024-01-11%2010-17-53.jpg',9987675661,'2024-01-11','on','xx','nayanzz@gmail.com','www','kerala','rejected',6),
(9,'zzz','/media/2024-01-11%2011-53-12.jpg',5643655234,'2024-01-10','Female','cvv','zzz@gmail.com','www','gfds','approved',7);

/*Data for the table `myapp_uploads` */

/*Data for the table `myapp_user` */

insert  into `myapp_user`(`id`,`Name`,`Photo`,`Dob`,`Gender`,`Class`,`Email`,`Phone`,`House_name`,`Place`,`Post`,`Pin`,`District`,`State`,`LOGIN_id`) values 
(1,'jh','','2024-01-10','kjhf',',jhjg',',khg',0,'kj','jkhg','jmhg',76,'mh','jhg',5);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
