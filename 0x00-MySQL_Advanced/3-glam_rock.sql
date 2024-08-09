-- Lists all Glam rock bands ranked by longevity
SELECT band_name, 
       CASE 
           WHEN split IS NULL THEN (2022 - formed)
           ELSE (split - formed)
       END AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;

