# Write your MySQL query statement below
SELECT e.name, ee.unique_id
FROM Employees e
left JOIN EmployeeUNI ee
ON e.id = ee.id;

