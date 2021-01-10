1. 在 Linux 环境下，安装 MySQL5.6 以上版本，修改字符集为 UTF8mb4 并验证，新建一个数据库 testdb，并为该数据库增加远程访问的用。

将修改字符集的配置项、验证字符集的 SQL 语句作为作业内容提交
将增加远程用户的 SQL 语句作为作业内容提交

答：
修改字符集，/etc/my.cnf 增加如下配置：
[client]
default_character_set = utf8mb4
	
[mysql]
default_character_set = utf8mb4

[mysqld]
character_set_server = utf8mb4   #mysql字符集设置
init_connect = 'SET NAMES utf8mb4'

验证字符集sql：show variables like '%character%';
增加远程用户sql：
create user 'testuser'@'%' identified by 'testpass';
grant all on testdb.* to 'testuser'@'%';


3、sql之前标号为执行顺序：
 5   SELECT DISTINCT player_id, player_name, count(*) as num 
 1   FROM player JOIN team ON player.team_id = team.team_id 
 2   WHERE height > 1.80 
 3   GROUP BY player.team_id 
 4   HAVING num > 2 
 6   ORDER BY num DESC 
 7   LIMIT 2

4、inner join：
select table1.id,table1.name,table2.id,table2.name from table1 inner join table2 on table1.id = table2.id;
+------+---------------+------+---------------+
| id   | name          | id   | name          |
+------+---------------+------+---------------+
|    1 | table1_table2 |    1 | table1_table2 |
+------+---------------+------+---------------+

left join:
mysql> select table1.id,table1.name,table2.id,table2.name from table1 left join table2 on table1.id = table2.id;
;
+------+---------------+------+---------------+
| id   | name          | id   | name          |
+------+---------------+------+---------------+
|    1 | table1_table2 |    1 | table1_table2 |
|    2 | table1        | NULL | NULL          |
+------+---------------+------+---------------+

right join:
mysql> select table1.id,table1.name,table2.id,table2.name from table1 right join table2 on table1.id = table2.id
d;
+------+---------------+------+---------------+
| id   | name          | id   | name          |
+------+---------------+------+---------------+
|    1 | table1_table2 |    1 | table1_table2 |
| NULL | NULL          |    3 | table2        |
+------+---------------+------+---------------+

5、create index id_name on table1(id,name);
create index id_name on table2(id,name);

