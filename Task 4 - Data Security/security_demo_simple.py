# security_demo_simple.py
"""
Simple demo for Task 4: Data Masking + Two-Role Access (Analyst vs Manager)
Usage:
  1) Put a small sample CSV at sample_data/cleaned_retail_sample.csv
  2) Run: python security_demo_simple.py
Outputs:
  - sample_data/demo_masked.csv (what analyst can see)
  - sample_data/demo_manager.csv (what manager can see)
  - task4_audit_log.txt (access log)
"""

import os
import logging
import pandas as pd
from datetime import datetime

# ---------- CONFIG ----------
SAMPLE_CSV = "sample_data/cleaned_retail_sample.csv"
OUT_MASKED = "sample_data/demo_masked.csv"
OUT_MANAGER = "sample_data/demo_manager.csv"
AUDIT_LOG = "task4_audit_log.txt"

# Setup simple audit logger
logging.basicConfig(filename=AUDIT_LOG, level=logging.INFO,
                    format="%(asctime)s - %(message)s")

def audit(actor, action, details=""):
    msg = f"actor={actor} action={action} details={details}"
    logging.info(msg)
    print("AUDIT:", msg)

# ---------- MASKING ----------
def mask_customer_id(cid):
    """Mask CustomerID except last 2 digits. If invalid, return 'MASKED'."""
    try:
        s = str(int(cid))
    except Exception:
        return "MASKED"
    if len(s) <= 2:
        return "*" * len(s)
    return "*"*(len(s)-2) + s[-2:]

# ---------- ROLE VIEWS ----------
def analyst_view(df):
    """Return dataframe with masked PII for analyst role."""
    df_copy = df.copy()
    if "CustomerID" in df_copy.columns:
        df_copy["CustomerID"] = df_copy["CustomerID"].apply(mask_customer_id)
    return df_copy

def manager_view(df):
    """Full view (manager) — no masking. In real life manager would be RBAC-protected."""
    return df.copy()

# ---------- MAIN ----------
def main():
    if not os.path.exists(SAMPLE_CSV):
        print(f"Error: sample CSV not found at {SAMPLE_CSV}")
        print("Create a small sample CSV (5-50 rows) with columns: InvoiceNo, Description, CustomerID, TotalPrice")
        return

    # Load
    df = pd.read_csv(SAMPLE_CSV)
    print("Loaded sample rows:", len(df))
    audit("system", "load_dataset", f"rows={len(df)} file={SAMPLE_CSV}")

    # Create views
    df_analyst = analyst_view(df)
    audit("system", "masking_applied", "CustomerID masked for analyst view")

    df_manager = manager_view(df)
    audit("system", "manager_view_prepared", "Full access view for manager")

    # Save outputs
    df_analyst.to_csv(OUT_MASKED, index=False)
    audit("system", "save_masked_view", OUT_MASKED)
    print(f"Analyst view saved -> {OUT_MASKED}")

    df_manager.to_csv(OUT_MANAGER, index=False)
    audit("system", "save_manager_view", OUT_MANAGER)
    print(f"Manager view saved -> {OUT_MANAGER}")

    # Simulate role access action examples
    print("\n--- SIMULATED ACCESS: Analyst requests data ---")
    audit("analyst_user", "request_data", "requested analyst view")
    print(df_analyst.head(5).to_string(index=False))

    print("\n--- SIMULATED ACCESS: Manager requests data ---")
    audit("manager_user", "request_data", "requested manager view")
    print(df_manager.head(5).to_string(index=False))

    print("\nDemo complete. Inspect", AUDIT_LOG)

if __name__ == "__main__":
    main()
