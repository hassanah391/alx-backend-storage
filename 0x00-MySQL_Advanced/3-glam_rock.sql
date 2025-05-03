-- This script lists all bands with Glam rock as their main style,
-- ranked by their longevity
-- Requirements:
-- Column names must be: band_name and lifespan (in years until 2022)
SELECT
  band_name,
  CASE
    WHEN split IS NULL THEN 2022 - formed
    ELSE split - formed
  END AS lifespan
FROM
  metal_bands
WHERE
  style LIKE '%Glam_rock%'
ORDER BY
  lifespan DESC;
