/*
Write a SQL query to get the nth highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the nth highest salary where n = 2 is 200. If there is no nth highest salary, then the query should return null.

+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
*/

CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    RETURN (
        /* Write your T-SQL query statement below. */
        SELECT MAX(CASE WHEN salaryrank=@N THEN Salary ELSE NULL END)
        FROM
          (SELECT
              Salary,
              DENSE_RANK() OVER(ORDER BY Salary DESC) AS salaryrank
          FROM Employee
          ) temp

    );
END
