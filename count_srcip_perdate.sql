select t1.srcip,
case when t2.srcip is not null then 1 else 0 end date_171221,
case when t3.srcip is not null then 1 else 0 end date_020122,
case when t4.srcip is not null then 1 else 0 end date_020621,
case when t5.srcip is not null then 1 else 0 end date_020721,
case when t6.srcip is not null then 1 else 0 end date_020821,
case when t7.srcip is not null then 1 else 0 end date_020921,
case when t8.srcip is not null then 1 else 0 end date_021021,
case when t9.srcip is not null then 1 else 0 end date_021121,
case when t10.srcip is not null then 1 else 0 end date_021221,
case when t11.srcip is not null then 1 else 0 end date_170621,
case when t12.srcip is not null then 1 else 0 end date_170721,
case when t13.srcip is not null then 1 else 0 end date_170821,
case when t14.srcip is not null then 1 else 0 end date_170921,
case when t15.srcip is not null then 1 else 0 end date_171021,
case when t16.srcip is not null then 1 else 0 end date_171121
from(
select distinct srcip
from public."NTP_reflector_171221"
union all
select distinct srcip
from public."NTP_reflector_020122"
)as t1 left join public."NTP_reflector_171221" t2 on t1.srcip=t2.srcip
left join public."NTP_reflector_020122" t3 on t1.srcip=t3.srcip
left join public."NTP_reflector_020621" t4 on t1.srcip=t4.srcip
left join public."NTP_reflector_020721" t5 on t1.srcip=t5.srcip
left join public."NTP_reflector_020821" t6 on t1.srcip=t6.srcip
left join public."NTP_reflector_020921" t7 on t1.srcip=t7.srcip
left join public."NTP_reflector_021021" t8 on t1.srcip=t8.srcip
left join public."NTP_reflector_021121" t9 on t1.srcip=t9.srcip
left join public."NTP_reflector_021221" t10 on t1.srcip=t10.srcip
left join public."NTP_reflector_170621" t11 on t1.srcip=t11.srcip
left join public."NTP_reflector_170721" t12 on t1.srcip=t12.srcip
left join public."NTP_reflector_170821" t13 on t1.srcip=t13.srcip
left join public."NTP_reflector_170921" t14 on t1.srcip=t14.srcip
left join public."NTP_reflector_171021" t15 on t1.srcip=t15.srcip
left join public."NTP_reflector_171121" t16 on t1.srcip=t16.srcip
limit 10

