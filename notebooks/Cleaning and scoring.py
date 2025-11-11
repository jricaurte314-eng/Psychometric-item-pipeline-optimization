# =========================================================
#  Psychometric Item Pipeline — Athena → Cleaning → Scoring
# =========================================================

import pandas as pd
from pyathena import connect
from src.cleaning_psych import clean_and_score

# -----------------------------------------------
# 1️⃣ AWS Athena Connection
# -----------------------------------------------

ATHENA_S3_STAGING = "s3://your-staging-bucket/athena/results/"
ATHENA_REGION = "us-east-1"
ATHENA_DB = "psych"

conn = connect(s3_staging_dir=ATHENA_S3_STAGING, region_name=ATHENA_REGION)

# -----------------------------------------------
# 2️⃣ Query analytic data (responses + items)
# -----------------------------------------------
query = f"""
WITH base AS (
  SELECT r.respondent_id, r.session_id, r.item_id, r.response, r.response_ts, r.response_time_ms,
         p.email, p.consent, p.cohort, p.started_at,
         i.scale_id, i.key_correct, i.reverse_scored, i.time_limit_sec
  FROM {ATHENA_DB}.responses r
  LEFT JOIN {ATHENA_DB}.participants p USING (respondent_id)
  LEFT JOIN {ATHENA_DB}.items i USING (item_id)
  WHERE r.dt BETWEEN '2025-10-01' AND '2025-10-31'
)
SELECT *
FROM base
WHERE consent = 'yes'
"""

print("⏳ Executing Athena query...")
df_raw = pd.read_sql(query, conn)
print(f"✅ Retrieved {len(df_raw):,} rows")

# -----------------------------------------------
# 3️⃣ Load items (optional: local CSV or Athena)
# -----------------------------------------------
# If items are stored in the same DB, you can reuse:
items = pd.read_sql("SELECT * FROM psych.items", conn)
print(f"✅ Loaded {len(items):,} items")

# -----------------------------------------------
# 4️⃣ Clean & score psychometric data
# -----------------------------------------------
out = clean_and_score(df_raw=df_raw, items=items, drop_cols=["email"])

print("\n📊 Summary:")
print(f"- Cleaned dataset: {len(out['long_scored']):,} responses")
print(f"- Items analyzed: {out['item_stats'].shape[0]}")
print(f"- Cronbach's α: {out['alpha']:.3f}")

# -----------------------------------------------
# 5️⃣ Save outputs to CSV
# -----------------------------------------------
out["item_stats"].to_csv("output/item_stats.csv", index=False)
out["respondent_scores"].to_csv("output/respondent_scores.csv")
out["wide_scored"].to_csv("output/wide_scored.csv")

print("\n✅ Exported results to /output/")
