# project_databricks
Projecto del curso databricks

<div align="center">

### Arquitectura Medallion en Azure Databricks

[![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=for-the-badge&logo=databricks&logoColor=white)](https://databricks.com/)
[![Azure](https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white)](https://azure.microsoft.com/)
[![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=for-the-badge&logo=apache-spark&logoColor=white)](https://spark.apache.org/)
[![Delta Lake](https://img.shields.io/badge/Delta_Lake-00ADD8?style=for-the-badge&logo=delta&logoColor=white)](https://delta.io/)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Power BI]()](https://powerbi.com/)
*Pipeline automatizado de datos para análisis de ventas de una empresa de produccion de derivados de Agua con arquitectura de tres capas y despliegue continuo*

</div>

---

## 🎯 Descripción

Pipeline ETL enterprise-grade que transforma datos crudos de ventas (sales) diferentes años , implementando la **Arquitectura Medallion** (Bronze-Silver-Gold) en Azure Databricks con **CI/CD completo** y power BI para desplegar los datos en dashboards.

### ✨ Características Principales
El Projecto contendra los sigueintes aspectos
- 🏗️ **Arquitectura Medallion** - Separación clara de capas Bronze → Silver → Gold
- 🔄 **ETL Automatizado** - Pipeline completo con despliegue automático via GitHub Actions
- 📊 **Modelo Dimensional** - Star Schema optimizado para análisis de negocio
- 🚀 **CI/CD Integrado** - Deploy automático en cada push a master
- 📈 **Power BI** - Visualización
- 🔔 **Monitoreo** - Notificaciones automáticas y logs detallados

---

## 🏛️ Arquitectura

### Flujo de Datos

```
📄 CSV (Raw Data)
    ↓
🥉 Bronze Layer (Ingesta de datos del sistema transacciona sin transformación)
    ↓
🥈 Silver Layer (Limpieza de datos antes de enviarlos a la capa golden y almacenarlos en el modelo dimensional)
    ↓
🥇 Gold Layer (Alamcenamiento de todos los datos en el modelo dimencional)
    ↓
📊 Databricks Dashboards (Visualización)
```

![Texto descriptivo](Arquitectura.png)


### 📦 Capas del Pipeline

<table>
<tr>
<td width="33%" valign="top">

#### 🥉 Bronze Layer
**Propósito**: Zona de almacenamiento de datos sin procesar, tal cual son obtenidos del proveedor.

**Tablas**: 
- `Partners` 
- `sales`

**Características**:
- ✅ Datos tal como vienen de origen
- ✅ Timestamp de ingesta
- ✅ Sin validaciones

</td>
<td width="33%" valign="top">

#### 🥈 Silver Layer
**Propósito**: Limpieza de datos

**Tablas**:
- `partners`
- `products`
- `sales`

**Características**:
- ✅ catalog_smartdata Schema
- ✅ Datos normalizados
- ✅ Validaciones completas

</td>
<td width="33%" valign="top">

#### 🥇 Gold Layer
**Propósito**: Analytics-ready

**Tablas**:
- dim_parents    : Tabla dimension Parents
- dim_products   : Tabla Dimension Productos
- kpi_sales      : Tabla KPI Sales

**Características**:
- ✅ Cargado Total de la data despues de su transformacion
- ✅ Optimizado para BI
- ✅ Performance máximo
- ✅ Tablas y datos listos para explotarlos en Power BI

</td>
</tr>
</table>

---

## 📁 Estructura del Proyecto

```
project_databricks/
│
├── 📂 .github/
│   └── 📂 workflows/
│       └── 📄 script0.yml    # Pipeline CI/CD deploy de todo el proceso in PROD
├── 📂 Process/
│   ├── 🐍 Ingest_partner_data.py           # Bronze layer
│   ├── 🐍 Ingest_sales_data.py             # Bronze Layer
│   └── 🐍 Load.ipynb                       # Gold Layer
│   └── 🐍 Transform.ipynb                  # Gold Layer
├── 📂 Scrips/
|   ├── 🐍 Enviroment_preparation.ipynb    # Create Schema, Tables, External location
├── 📂 Security/
|   ├── 🐍 Permissions.ipynb               # Sql Grants
├── 📂 Reversion/
|   ├── 🐍 Revoke.ipynb                    # Revoke permissions
├── 📂 dashboards/                         # Databricks Dashboards 
|   ├── 📊 Dashboard_v2.pbix               # Dashboads
|   ├── 📊 Sashboard_v1.pbix               # Dasboards
├── 📂 DataSet/                            # Data Set usados para este proyecto 
|   ├── 📊 res_partner_2025.csv            # partners de la empresa
|   ├── 📊 rep_ventas_2025.csv             # Sales desde 2017 - 2025
└── 📄 README.md
```

---

## 🛠️ Tecnologías

<div align="center">

| Tecnología | Propósito |
|:----------:|:----------|
| ![Databricks](https://img.shields.io/badge/Azure_Databricks-FF3621?style=flat-square&logo=databricks&logoColor=white) | Motor de procesamiento distribuido Spark |
| ![Delta Lake](https://img.shields.io/badge/Delta_Lake-00ADD8?style=flat-square&logo=delta&logoColor=white) | Storage layer con ACID transactions |
| ![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=flat-square&logo=apache-spark&logoColor=white) | Framework de transformación de datos |
| ![ADLS](https://img.shields.io/badge/ADLS_Gen2-0078D4?style=flat-square&logo=microsoft-azure&logoColor=white) | Data Lake para almacenamiento persistente |
| ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=github-actions&logoColor=white) | Automatización CI/CD |
| ![Databricks Dashboards](https://img.shields.io/badge/Databricks Dashboards-F2C81?style=for-the-badge&logo=databricks&logoColor=black) |  Visualización |

</div>

---

## ⚙️ Requisitos Previos

- ☁️ Cuenta de Azure con acceso a Databricks
- 💻 Workspace de Databricks configurado
- 🖥️ Cluster activo (nombre: `Cluster_SD`)
- 🐙 Cuenta de GitHub con permisos de administrador
- 📊 Power BI Desktop (opcional para visualización)

---

## 🚀 Instalación y Configuración

### 1️⃣ Clonar el Repositorio

```bash
git clone https://github.com/guaru/project-databricks.git
cd project-databricks
```

### 2️⃣ Configurar Databricks Token

1. Ir a Databricks Workspace
2. **User Settings** → **Developer** → **Access Tokens**
3. Click en **Generate New Token**
4. Configurar:
   - **Comment**: `GitHub CI/CD`
   - **Lifetime**: `90 days`
5. ⚠️ Copiar y guardar el token

### 3️⃣ Configurar GitHub Secrets

En tu repositorio: **Settings** → **Secrets and variables** → **Actions**

| Secret Name | Valor Ejemplo |
|------------|---------------|
| `DATABRICKS_HOST` | `https://adb-xxxxx.azuredatabricks.net` |
| `DATABRICKS_TOKEN` | `dapi_xxxxxxxxxxxxxxxx` |
| `DATABRICKS_HOST` | `https://adb-xxxxx.azuredatabricks.net` |
| `DATABRICKS_TOKEN` | `dapi_xxxxxxxxxxxxxxxx` |

### 4️⃣ Verificar Storage Configuration

```python
storage_path = "abfss://raw@adlssmartdatasvar0912.dfs.core.windows.net"
```

<div align="center">

✅ **¡Configuración completa!**

</div>

---

## 💻 Uso

### 🔄 Despliegue Automático (Recomendado)

```bash
git add .
git commit -m "✨ feat: mejoras en pipeline"
git push origin dev
```

**GitHub Actions ejecutará**:
- 📤 Deploy de notebooks a `/Production/ETL-AGUA`
- 🔧 Creación del workflow `WF_PROD_ETL_AGUA_SALES`
- ▶️ Ejecución completa:  Bronze → Silver → Gold
- 📧 Notificaciones de resultados

### 🖱️ Despliegue Manual desde GitHub

1. Ir al tab **Actions** en GitHub
2. Seleccionar **Deploy ETL Apple Sales And Warranty**
3. Click en **Run workflow**
4. Seleccionar rama `dev`
5. Click en **Run workflow**

### 🔧 Ejecución Local en Databricks

Navegar a `/Production/ETL-APPLE` y ejecutar en orden:

```
- Enviroment preparation.py         → Crear esquema
- ingest_catalogs.py                → Bronze Layer
- ingest_sales.py                   → Bronze Layer
- ingest_warranty.py                → Bronze Layer
- transform_sales.py                → Silver Layer
- transform_warranty.py             → Silver Layer
- load_sales.py                     → Gold Layer
- load_warranty.py                  → Gold Layer
```

---


## 🔄 CI/CD

### Pipeline de GitHub Actions

```yaml
Workflow: Deploy ETL Apple Sales And Warranty
├── Deploy notebooks → /Production/ETL-APPLE
├── Eliminar workflow antiguo (si existe)
├── Buscar cluster configurado
├── Crear nuevo workflow con 4 tareas
├── Ejecutar pipeline automáticamente
└── Monitorear y notificar resultados
```

### 🔄  Workflow Databricks
![Texto descriptivo](CICD_ETL_APPLE.png)
```


⏰ Schedule: Diario 8:00 AM (Lima)
⏱️ Timeout total: 4 horas
 🔒 Max concurrent runs: 1
⏰ Notificaciones: 
      success: abel.soto2009@gmail.com
      failed:  abel.soto2009@gmail.com
```

---

## 📈 Dashboards
https://github.com/guaru/project-databricks/tree/dev/dashboards

## 🔍 Monitoreo

### En Databricks

**Workflows**:
- Ir a **Workflows** en el menú lateral
- Buscar `ETL_PROD_APPLE_SALES`
- Ver historial de ejecuciones

**Logs por Tarea**:
- Click en una ejecución específica
- Click en cada tarea para ver logs detallados
- Revisar stdout/stderr en caso de errores

### En GitHub Actions

- Tab **Actions** del repositorio
- Ver historial de workflows
- Click en ejecución específica para detalles
- Revisar logs de cada step

---

## 👤 Autor

<div align="center">

### Abel Rolando Soto Vera

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/oca-abel-rolando-soto-vera/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/asotogithub/prj_databricks)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:abel.soto2009@gmail.com)

**Data Engineering** | **Azure Databricks** | **Delta Lake** | **CI/CD**

</div>

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

---

<div align="center">

**Proyecto**: Data Engineering - Arquitectura Medallion  
**Tecnología**: Azure Databricks + Delta Lake + CI/CD  
**Última actualización**: 2025


</div>
