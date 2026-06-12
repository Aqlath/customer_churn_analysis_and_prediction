--How many customers have churned and how many have not churned?

SELECT churn,count(churn)
from telco_churn
GROUP BY churn;