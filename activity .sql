create table student(
    name_ varchar(255),
    age int,
    gender varchar(20),
    address_ varchar(250)
);
insert into student(
    name_,age,gender,address_
)
values
("Himansh",10,"male","144"),
("Shanaya",9,"female","3123"),
("Siddharth",10,"male","213"),
("Avi",10,"male","1232"),
("Kanishka",10,"female","312");

select* from student
WHERE age=10 or gender="female";

select * from student
where age=(select(MAX(age)from student));

update student set age=12 where name_="Himansh";
select * from student;

delete from student where name_="Himansh";
select * from student;

select * from student
where name_ like "S%";