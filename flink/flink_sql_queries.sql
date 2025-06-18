CREATE TABLE tram_stream (
  trip_id STRING,
  route_id STRING,
  start_date STRING,
  stop_id STRING,
  arrival_delay INT,
  departure_delay INT,
  arrival_time BIGINT,
  departure_time BIGINT,
  `event_time` AS TO_TIMESTAMP_LTZ(arrival_time * 1000, 3),
  WATERMARK FOR `event_time` AS `event_time` - INTERVAL '30' SECOND
) WITH (
  'connector' = 'kafka',
  'topic' = 'gtfs_json',
  'properties.bootstrap.servers' = '127.0.0.1:9092',
  'format' = 'json',
  'scan.startup.mode' = 'latest-offset'
);

SELECT *
FROM tram_stream
WHERE route_id = '74' AND stop_id IN ('5230', '5231', '5284', '5815', '9128');