SELECT member_id, member_name, gender, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') AS DATE_OF_BIRTH
    FROM member_profile
    WHERE MONTH(DATE_OF_BIRTH) = 03 AND TLNO IS NOT NULL AND gender = 'W'

ORDER BY MEMBER_ID ASC;
