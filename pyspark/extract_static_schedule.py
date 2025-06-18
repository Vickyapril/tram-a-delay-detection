from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.functions import lit

# Initialize Spark session
spark = SparkSession.builder.appName("GTFS Analysis").getOrCreate()

routes_df = spark.read.option("header", "true").csv(f'{gtfs_path}routes.txt')
tram_a = routes_df.filter(routes_df.route_short_name == 'A')
stops_df = spark.read.option("header", "true").csv(f'{gtfs_path}stops.txt')

# Filter for Peychotte stop
peychotte_stop = stops_df.filter(stops_df.stop_name.contains('Peychotte'))
tram_a_trips = trips_df.filter(col('route_id')=='74')
stop_times_df = spark.read.option("header", "true").csv(f'{gtfs_path}stop_times.txt')
peychotte_stop_times = stop_times_df.filter(col('stop_id') == '5230')
tram_a_peychotte = peychotte_stop_times.join(tram_a_trips, on='trip_id')
tram_a_peychotte.select('trip_id', 'arrival_time', 'departure_time', 'stop_id').show()