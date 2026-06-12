--What percentage of customers have churned

SELECT (SELECT count(*) from telco_churn 
        WHERE churn='Yes') * 100 / count(*) from telco_churn