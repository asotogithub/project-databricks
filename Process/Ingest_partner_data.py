# Databricks notebook source
# MAGIC %md
# MAGIC ### CARGADO DEL LOS PARNERTS DATA

# COMMAND ----------

dbutils.widgets.removeAll()

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

dbutils.widgets.text("container", "raw")
dbutils.widgets.text("catalogo", "catalog_smartdata")
dbutils.widgets.text("esquema", "bronze")

# COMMAND ----------

container = dbutils.widgets.get("container")
catalogo = dbutils.widgets.get("catalogo")
esquema = dbutils.widgets.get("esquema")
#https://adlssmartdatasvar0912.blob.core.windows.net/raw/DataAgua/res_partner_2025.csv
ruta = f"abfss://{container}@adlssmartdatasvar0912.dfs.core.windows.net/DataAgua/res_partner_2025.csv"

# COMMAND ----------

df_partners = spark.read.option('header', True)\
                        .option('inferSchema', True)\
                        .csv(ruta)

# COMMAND ----------

partner_schema = StructType(fields=[StructField("partner_Id", IntegerType(), False),
                                    StructField("name", StringType(), True),
                                    StructField("company_id", IntegerType(), False),
                                    StructField("comment", StringType(), True),
                                    StructField("website", StringType(), True),
                                    StructField("create_date",DateType(), False),
                                    StructField("color", StringType(), True),
                                    StructField("active", StringType(), True),
                                    StructField("street", StringType(), True),
                                    StructField("supplier", StringType(), True),
                                    StructField("city", StringType(), True),
                                    StructField("display_name", StringType(), True),
                                    StructField("zip", StringType(), True),
                                    StructField("title", StringType(), True),
                                    StructField("country_id", IntegerType(), False),
                                    StructField("commercial_company_name", StringType(), True),
                                    StructField("parent_id", IntegerType(), False),
                                    StructField("company_name", StringType(), True),
                                    StructField("employee", StringType(), True),
                                    StructField("ref", StringType(), True),
                                    StructField("email", StringType(), True),
                                    StructField("is_company", StringType(), True),
                                    StructField("function", StringType(), True),
                                    StructField("lang", StringType(), True),
                                    StructField("fax", StringType(), True),
                                    StructField("street2", StringType(), True),
                                    StructField("barcode", StringType(), True),
                                    StructField("phone", StringType(), True),
                                    StructField("write_date",DateType(), False),
                                    StructField("date", StringType(), True),
                                    StructField("tz", StringType(), True),
                                    StructField("write_uid", IntegerType(), False),
                                    StructField("customer", StringType(), True),
                                    StructField("create_uid", IntegerType(), False),
                                    StructField("credit_limit", DoubleType(), True),
                                    StructField("user_id", IntegerType(), False),
                                    StructField("mobile", StringType(), True),
                                    StructField("type", StringType(), True),
                                    StructField("partner_share", StringType(), True),
                                    StructField("vat", StringType(), True),
                                    StructField("state_id", IntegerType(), False),
                                    StructField("commercial_partner_id", IntegerType(), False),
                                    StructField("notify_email", StringType(), True),
                                    StructField("message_last_post", StringType(), True),
                                    StructField("opt_out", StringType(), True),
                                    StructField("message_bounce", StringType(), True),
                                    StructField("signup_type", StringType(), True),
                                    StructField("signup_expiration", StringType(), True),
                                    StructField("signup_token", StringType(), True),
                                    StructField("team_id", IntegerType(), False),
                                    StructField("debit_limit", StringType(), True),
                                    StructField("last_time_entries_checked", StringType(), True),
                                    StructField("invoice_warn_msg", StringType(), True),
                                    StructField("invoice_warn", StringType(), True),
                                    StructField("sale_warn", StringType(), True),
                                    StructField("sale_warn_msg", StringType(), True),
                                    StructField("picking_warn", StringType(), True),
                                    StructField("picking_warn_msg", StringType(), True),
                                    StructField("purchase_warn", StringType(), True),
                                    StructField("purchase_warn_msg", StringType(), True),
                                    StructField("code", StringType(), True),
                                    StructField("payment_type_id", IntegerType(), False),
                                    StructField("client_type_id", IntegerType(), False),
                                    StructField("record_type_id", IntegerType(), False),
                                    StructField("nit_name", StringType(), True),
                                    StructField("nit", StringType(), True),
                                    StructField("coordinates", StringType(), True),
                                    StructField("calendar_last_notif_ack", StringType(), True)
                                ])

# COMMAND ----------

# DBTITLE 1,Use user specified schema to load df with correct types
df_partner_final = spark.read\
.option('header', True)\
.schema(partner_schema)\
.csv(ruta)

# COMMAND ----------

# DBTITLE 1,select only specific cols
partner_selected_df = df_partner_final.select(col("partner_Id"), 
                                                col("par_name"), 
                                                col("create_date"), 
                                                col("display_name"), 
                                                col("par_email"), 
                                                col("mobile"), 
                                                col("coordinates"), 
                                                col("nit_name"),
                                                col("nit"))

# COMMAND ----------

partner_renamed_df = partner_selected_df.withColumnRenamed("name", "par_name") \
                                            .withColumnRenamed("color", "par_color") \
                                            .withColumnRenamed("active", "par_active") \
                                            .withColumnRenamed("email", "par_email") \
                                            .withColumnRenamed("function", "par_function") \
                                            .withColumnRenamed("lang", "par_lang") \
                                            .withColumnRenamed("date", "par_date") \
                                            .withColumnRenamed("tz", "par_tz") \
                                            .withColumnRenamed("type", "par_type") \
                                            .withColumnRenamed("code", "par_code") 

# COMMAND ----------

# DBTITLE 1,Add col with current timestamp 
partner_final_df = partner_renamed_df.withColumn("ingestion_date", current_timestamp())

# COMMAND ----------

partner_final_df.write.mode("overwrite").saveAsTable(f"{catalogo}.{esquema}.partners")
