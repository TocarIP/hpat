import hpat
import pandas as pd
import numpy as np
import time

#SELECT cab_type,
#       count(*)
#FROM trips
#GROUP BY cab_type;
#@hpat.jit fails with Invalid use of Function(<ufunc 'isnan'>) with argument(s) of type(s): (StringType), even when dtype is provided
def q1():
    df = pd.read_csv('trips_xaa.csv.gz',compression='gzip',header=None,names=['trip_id','vendor_id','pickup_datetime','dropoff_datetime','store_and_fwd_flag',
    'rate_code_id','pickup_longitude','pickup_latitude','dropoff_longitude','dropoff_latitude','passenger_count','trip_distance','fare_amount','extra',
    'mta_tax','tip_amount','tolls_amount','ehail_fee','improvement_surcharge','total_amount','payment_type','trip_type','pickup','dropoff','cab_type',
    'precipitation','snow_depth','snowfall','max_temperature','min_temperature','average_wind_speed','pickup_nyct2010_gid','pickup_ctlabel','pickup_borocode',
    'pickup_boroname','pickup_ct2010','pickup_boroct2010','pickup_cdeligibil','pickup_ntacode','pickup_ntaname','pickup_puma','dropoff_nyct2010_gid',
    'dropoff_ctlabel','dropoff_borocode','dropoff_boroname','dropoff_ct2010','dropoff_boroct2010','dropoff_cdeligibil','dropoff_ntacode','dropoff_ntaname','dropoff_puma'],
# We need dtypes for hpat, but it currently fails with:
#    Integer column has NA values in column 21
# because some Integer columns have missing values
#    dtype={'trip_id':int,'vendor_id':str,'pickup_datetime':str,'dropoff_datetime':str,'store_and_fwd_flag':str,'rate_code_id':int,'pickup_longitude':float,
#    'pickup_latitude':float,'dropoff_longitude':float,'dropoff_latitude':float,'passenger_count':int,'trip_distance':float,'fare_amount':float,'extra':float,'mta_tax':float,
#    'tip_amount':float,'tolls_amount':float,'ehail_fee':float,'improvement_surcharge':float,'total_amount':float,'payment_type':str,'trip_type':int,'pickup':str,'dropoff':str,
#    'cab_type':str,'precipitation':int,'snow_depth':int,'snowfall':int,'max_temperature':int,'min_temperature':int,'average_wind_speed':int,'pickup_nyct2010_gid':int,
#    'pickup_ctlabel':str,'pickup_borocode':int,'pickup_boroname':str,'pickup_ct2010':str,'pickup_boroct2010':str,'pickup_cdeligibil':str,'pickup_ntacode':str,'pickup_ntaname':str,
#    'pickup_puma':str,'dropoff_nyct2010_gid':int,'dropoff_ctlabel':str,'dropoff_borocode':int,'dropoff_boroname':str,'dropoff_ct2010':str,'dropoff_boroct2010':str,'dropoff_cdeligibil':str,
#    'dropoff_ntacode':str,'dropoff_ntaname':str,'dropoff_puma':str},
#    parse_dates = ['pickup_datetime','dropoff_datetime'],
    )
    return df.groupby('cab_type')['cab_type'].count() 

#SELECT passenger_count,
#       avg(total_amount)
#FROM trips
#GROUP BY passenger_count;
def q2():
    df = pd.read_csv('trips_xaa.csv.gz',compression='gzip',header=None,names=['trip_id','vendor_id','pickup_datetime','dropoff_datetime','store_and_fwd_flag',
    'rate_code_id','pickup_longitude','pickup_latitude','dropoff_longitude','dropoff_latitude','passenger_count','trip_distance','fare_amount','extra',
    'mta_tax','tip_amount','tolls_amount','ehail_fee','improvement_surcharge','total_amount','payment_type','trip_type','pickup','dropoff','cab_type',
    'precipitation','snow_depth','snowfall','max_temperature','min_temperature','average_wind_speed','pickup_nyct2010_gid','pickup_ctlabel','pickup_borocode',
    'pickup_boroname','pickup_ct2010','pickup_boroct2010','pickup_cdeligibil','pickup_ntacode','pickup_ntaname','pickup_puma','dropoff_nyct2010_gid',
    'dropoff_ctlabel','dropoff_borocode','dropoff_boroname','dropoff_ct2010','dropoff_boroct2010','dropoff_cdeligibil','dropoff_ntacode','dropoff_ntaname','dropoff_puma'],
    )
    return df.groupby('passenger_count',as_index=False).mean()[['passenger_count','total_amount']]

#SELECT passenger_count,
#       EXTRACT(year from pickup_datetime) as year,
#       count(*)
#FROM trips
#GROUP BY passenger_count,
#         year;
def q3():
    df = pd.read_csv('trips_xaa.csv.gz',compression='gzip',header=None,names=['trip_id','vendor_id','pickup_datetime','dropoff_datetime','store_and_fwd_flag',
    'rate_code_id','pickup_longitude','pickup_latitude','dropoff_longitude','dropoff_latitude','passenger_count','trip_distance','fare_amount','extra',
    'mta_tax','tip_amount','tolls_amount','ehail_fee','improvement_surcharge','total_amount','payment_type','trip_type','pickup','dropoff','cab_type',
    'precipitation','snow_depth','snowfall','max_temperature','min_temperature','average_wind_speed','pickup_nyct2010_gid','pickup_ctlabel','pickup_borocode',
    'pickup_boroname','pickup_ct2010','pickup_boroct2010','pickup_cdeligibil','pickup_ntacode','pickup_ntaname','pickup_puma','dropoff_nyct2010_gid',
    'dropoff_ctlabel','dropoff_borocode','dropoff_boroname','dropoff_ct2010','dropoff_boroct2010','dropoff_cdeligibil','dropoff_ntacode','dropoff_ntaname','dropoff_puma'],
    )
    transformed = df[['passenger_count','pickup_datetime']].transform({'passenger_count':lambda x: x,'pickup_datetime':lambda x:  pd.DatetimeIndex(x).year})
    return transformed.groupby(['passenger_count','pickup_datetime'])[['passenger_count','pickup_datetime']].count()['passenger_count'] 

#SELECT passenger_count,
#       EXTRACT(year from pickup_datetime) as year,
#       round(trip_distance) distance,
#       count(*) trips
#FROM trips
#GROUP BY passenger_count,
#         year,
#         distance
#ORDER BY year,
#         trips desc;
def q4():
    df = pd.read_csv('trips_xaa.csv.gz',compression='gzip',header=None,names=['trip_id','vendor_id','pickup_datetime','dropoff_datetime','store_and_fwd_flag',
    'rate_code_id','pickup_longitude','pickup_latitude','dropoff_longitude','dropoff_latitude','passenger_count','trip_distance','fare_amount','extra',
    'mta_tax','tip_amount','tolls_amount','ehail_fee','improvement_surcharge','total_amount','payment_type','trip_type','pickup','dropoff','cab_type',
    'precipitation','snow_depth','snowfall','max_temperature','min_temperature','average_wind_speed','pickup_nyct2010_gid','pickup_ctlabel','pickup_borocode',
    'pickup_boroname','pickup_ct2010','pickup_boroct2010','pickup_cdeligibil','pickup_ntacode','pickup_ntaname','pickup_puma','dropoff_nyct2010_gid',
    'dropoff_ctlabel','dropoff_borocode','dropoff_boroname','dropoff_ct2010','dropoff_boroct2010','dropoff_cdeligibil','dropoff_ntacode','dropoff_ntaname','dropoff_puma'],
    )
    transformed = df[['passenger_count','pickup_datetime','trip_distance']].transform({'passenger_count':lambda x: x,'pickup_datetime':lambda x:  pd.DatetimeIndex(x).year,'trip_distance': lambda x: x.round()}).groupby(['passenger_count','pickup_datetime','trip_distance'])
    return transformed.size().reset_index().sort_values(by=['pickup_datetime',0],ascending=[True,False])

def time4q():
    t1 = time.time()
    print(q1())
    print(time.time()-t1)
    
    t2 = time.time()
    print(q2())
    print(time.time()-t2)
    
    t3 = time.time()
    print(q3())
    print(time.time()-t3)
    
    t4 = time.time()
    print(q4())
    print(time.time()-t4)



time4q()
