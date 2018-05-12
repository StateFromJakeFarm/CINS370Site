SELECT SUM(Goals) AS allGoals, Country
FROM PLAYERS
GROUP BY Country
ORDER BY allGoals DESC
