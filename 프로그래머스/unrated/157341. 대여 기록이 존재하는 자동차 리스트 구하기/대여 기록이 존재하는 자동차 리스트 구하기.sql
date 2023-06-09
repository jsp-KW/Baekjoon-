SELECT DISTINCT CAR_RENTAL_COMPANY_CAR.CAR_ID
FROM CAR_RENTAL_COMPANY_CAR
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY ON CAR_RENTAL_COMPANY_CAR.CAR_ID = CAR_RENTAL_COMPANY_RENTAL_HISTORY.CAR_ID
WHERE CAR_TYPE = '세단' AND CAR_RENTAL_COMPANY_RENTAL_HISTORY.START_DATE BETWEEN TO_DATE('2022-10-01', 'YYYY-MM-DD') AND TO_DATE('2022-10-31', 'YYYY-MM-DD')
ORDER BY CAR_RENTAL_COMPANY_CAR.CAR_ID DESC;
