# Data Dictionary

## Overview
This dataset contains synthetic institutional records tracking admissions, billing, medication, and transfers.

## Columns

| Variable | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **record_id** | String | Unique identifier for the record | Format: `R` followed by digits. Duplicates may exist. |
| **date** | Date | Date of the event | **Inconsistent formats found**: `YYYY-MM-DD` and `DD/MM/YYYY`. |
| **category** | String | Type of event | Values include: `admission`, `billing`, `discharge`, `follow_up`, `imaging`, `lab_test`, `medication`, `transfer`. **Needs normalization** (mixed case/spelling). |
| **value** | Float | Quantitative measure of the event | **Data Quality Warning**: Contains negative values that should be positive. |
| **unit** | String | Unit of measurement | Examples: `USD`, `EUR`, `SEK` (billing); `mg`, `dose`, `ml` (medication); `points`, `count`, `min`. |
| **source_system** | String | Originating system | Values: `system_a`, `system_b`, `system_c`, `manual_entry`, `import_batch`. (Called `source` in 2022 data). |
| **status** | String | Workflow status | Values: `ok`, `cancelled`, `pending`, `review`, `rejected`. |
| **department** | String | Hospital department | **Available only in 2023 data**. Values: `ICU`, `ER`, `RAD`, `ADMIN`, `LAB`, `WARD_A/B`. |
| **priority** | String | Urgency level | **Available only in 2023 data**. Values: `high`, `medium`, `low`. |