--118,054,742 (07-02-2022)
select distinct count(t1.srcip) from (
select distinct srcip
from public."NTP_reflector_170721" union all
select distinct srcip
from public."NTP_reflector_021121" union all
select distinct srcip
from public."NTP_reflector_171021" union all
select distinct srcip
from public."NTP_reflector_021021" union all
select distinct srcip
from public."NTP_reflector_170921" union all
select distinct srcip
from public."NTP_reflector_020921" union all
select distinct srcip
from public."NTP_reflector_170821" union all
select distinct srcip
from public."NTP_reflector_020821" union all
select distinct srcip
from public."NTP_reflector_020721" union all
select distinct srcip
from public."NTP_reflector_170621" union all
select distinct srcip
from public."NTP_reflector_020621" union all
select distinct srcip
from public."NTP_reflector_170521" union all
select distinct srcip
from public."NTP_reflector_020521" union all
select distinct srcip
from public."NTP_reflector_170421" union all
select distinct srcip
from public."NTP_reflector_020421" union all
select distinct srcip
from public."NTP_reflector_170321" union all
select distinct srcip
from public."NTP_reflector_020321" union all
select distinct srcip
from public."NTP_reflector_170221" union all
select distinct srcip
from public."NTP_reflector_020221" union all
select distinct srcip
from public."NTP_reflector_170121" union all
select distinct srcip
from public."NTP_reflector_020121" union all
select distinct srcip
from public."NTP_reflector_171220" union all
select distinct srcip
from public."NTP_reflector_021120" union all
select distinct srcip
from public."NTP_reflector_171020" union all
select distinct srcip
from public."NTP_reflector_171221" union all
select distinct srcip
from public."NTP_reflector_021220" union all
select distinct srcip
from public."NTP_reflector_171120" union all
select distinct srcip
from public."NTP_reflector_021020" union all
select distinct srcip
from public."NTP_reflector_170920" union all
select distinct srcip
from public."NTP_reflector_020920" union all
select distinct srcip
from public."NTP_reflector_170820" union all
select distinct srcip
from public."NTP_reflector_020122" union all
select distinct srcip
from public."NTP_reflector_021221" union all
select distinct srcip
from public."NTP_reflector_171121" union all
select distinct srcip
from public."NTP_reflector_020820" union all
select distinct srcip
from public."NTP_reflector_020720" union all
select distinct srcip
from public."NTP_reflector_170620" union all
select distinct srcip
from public."NTP_reflector_170520" union all
select distinct srcip
from public."NTP_reflector_020620" union all
select distinct srcip
from public."NTP_reflector_020520" union all
select distinct srcip
from public."NTP_reflector_170420" union all
select distinct srcip
from public."NTP_reflector_020420" union all
select distinct srcip
from public."NTP_reflector_170320") as t1


--SELECT table_name
--  FROM information_schema.tables
-- WHERE table_schema='public'
--   AND table_type='BASE TABLE';