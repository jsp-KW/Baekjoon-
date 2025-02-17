SELECT  I.ANIMAL_ID, I.ANIMAL_TYPE, I.NAME FROM ANIMAL_INS  I INNER JOIN ANIMAL_OUTS O ON I.ANIMAL_ID = O.ANIMAL_ID WHERE ( (O.SEX_UPON_OUTCOME LIKE '%Neutered%' OR O.SEX_UPON_OUTCOME LIKE '%Spayed%') AND I.SEX_UPON_INTAKE  LIKE '%Intact%')
ORDER BY O.ANIMAL_ID ASC;