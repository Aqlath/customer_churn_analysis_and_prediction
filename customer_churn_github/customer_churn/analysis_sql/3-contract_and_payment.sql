--What are the unique types of contracts available and count of users?

SELECT DISTINCT(contract),count(*)  from telco_churn
GROUP BY contract;


--What are the different payment methods used by customers?

SELECT  DISTINCT(paymentmethod)  payment from telco_churn;
