--What is the average monthly charge?

SELECT avg(monthlycharges) as avg_monthly_charge from telco_churn;

--What are the maximum and minimum tenure values?

SELECT min(tenure) , max(tenure) from telco_churn;