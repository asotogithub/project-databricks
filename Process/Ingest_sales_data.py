# Databricks notebook source
dbutils.widgets.removeAll()

# COMMAND ----------

from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DateType
from pyspark.sql.functions import current_timestamp, to_timestamp, concat, col, lit

# COMMAND ----------

dbutils.widgets.text("container", "raw")
dbutils.widgets.text("catalogo", "catalog_smartdata")
dbutils.widgets.text("esquema", "bronze")

# COMMAND ----------

container = dbutils.widgets.get("container")
catalogo = dbutils.widgets.get("catalogo")
esquema = dbutils.widgets.get("esquema")

ruta = f"abfss://{container}@adlssmartdatasvar0912.dfs.core.windows.net/DataAgua/rep_ventas_2025.csv"

# COMMAND ----------

sales_schema = StructType(fields=[  StructField("default_code", StringType(), True),
                                    StructField("sales_id", IntegerType(), False),
                                    StructField("product_id", IntegerType(), False), 
                                    StructField("product_uom", StringType(), True),
                                    StructField("product_uom_qty", IntegerType(), True),
                                    StructField("qty_delivered", IntegerType(), False),
                                    StructField("qty_invoiced", IntegerType(), False),
                                    StructField("qty_to_invoice", IntegerType(), True),
                                    StructField("price_total", DoubleType(), True),
                                    StructField("price_subtotal", DoubleType(), True),
                                    StructField("nbr", IntegerType(), True),
                                    StructField("name", StringType(), True),
                                    StructField("date", DateType(), True),
                                    StructField("state", StringType(), True),
                                    StructField("partner_id", IntegerType(), True),
                                    StructField("user_id", IntegerType(), True),
                                    StructField("company_id", IntegerType(), True),
                                    StructField("delay", StringType(), True),
                                    StructField("categ_id", IntegerType(), True),
                                    StructField("pricelist_id", IntegerType(), True),
                                    StructField("analytic_account_id", IntegerType(), True),
                                    StructField("team_id", IntegerType(), True),
                                    StructField("product_tmpl_id", IntegerType(), True),
                                    StructField("country_id", IntegerType(), True),
                                    StructField("commercial_partner_id", IntegerType(), True),
                                    StructField("weight", IntegerType(), True),
                                    StructField("volume", IntegerType(), True),
                                    StructField("warehouse_id", IntegerType(), True)
                                ])

# COMMAND ----------

sales_df = spark.read \
            .option("header", True) \
            .schema(sales_schema) \
            .csv(ruta)

# COMMAND ----------

sales_with_timestamp_df = sales_df.withColumn("ingestion_date", current_timestamp())

# COMMAND ----------

races_selected_df = races_with_timestamp_df.select(col('sales_id'), 
                                                   col('default_code').alias('product_code'), 
                                                   col('product_id'), 
                                                   col('circuitId').alias('circuit_id'),
                                                   col('qty_delivered'), 
                                                   col('qty_invoiced'), 
                                                   col('qty_to_invoice'),
                                                   col('price_total'), 
                                                   col('price_subtotal'), 
                                                   col('name') ,
                                                   col('date').alias('sales_date'),
                                                   col('ingestion_date'))

# COMMAND ----------

sales_selected_df.write.mode('overwrite').saveAsTable(f'{catalogo}.{esquema}.sales')
