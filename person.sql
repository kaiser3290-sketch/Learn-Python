create table Students(
    first_name varchar(255),
    last_name varchar(255),
    age int,
    grade int
);
insert into Students(first_name,last_name,age,grade)
values
("Himansh","Keswani",10,5),
("Avi","Jain",11,5),
("Jas","Wadhwani",11,6);

select * from Students
where age=11;

drop table Students;