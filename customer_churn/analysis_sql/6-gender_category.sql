--What is the count of male and female customers?

SELECT gender,count(*) from telco_churn
GROUP BY gender