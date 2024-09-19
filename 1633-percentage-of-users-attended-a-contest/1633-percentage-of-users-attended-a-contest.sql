# Write your MySQL query statement below
select r.contest_id, round((count(r.contest_id) / (select count(*) from Users)) * 100, 2) as percentage
from Users as u, Register as r
where u.user_id = r.user_id
group by r.contest_id
order by percentage desc, contest_id asc;