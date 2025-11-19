# ⭐ Task 4 – Big Data Security (Focused: Masking + Two-Role Access)

This task demonstrates two core security controls for a Big Data pipeline:
1. **Data Masking** (PII minimization)  
2. **Two-role access simulation** (Analyst vs Manager)

A compact prototype shows how masked views are produced for analysts while managers can access full data (simulated). An audit log records accesses.

---

## ✅ Objective

- Implement minimal, practical controls to protect PII in datasets.
- Show role-based views: analyst (masked) and manager (full).
- Provide an easy-to-run prototype and logs as evidence.

---

## 📂 Files in this folder

- `security_demo_simple.py` — Prototype (masking + two-role access + audit)    
- `sample_data/cleaned_retail_sample.csv` — Small sample input (safe subset)  
- `sample_data/demo_masked.csv` — Generated analyst view (after run)  
- `sample_data/demo_manager.csv` — Generated manager view (after run)  
- `task4_audit_log.txt` — Generated audit log (after run)

---

## 🧾 How masking works

- `CustomerID` is masked so only the **last two digits** are visible; e.g., `13448` → `***48`.
- Masking reduces risk if dataset or BI exports are viewed by non-authorized users.

---

## 🔐 Role behaviour

- **Analyst**: receives masked dataset (cannot see raw CustomerID). This is the default safe view for analytics.
- **Manager**: receives full dataset (simulated privileged access). In production this should be enforced using RBAC/IAM.

All views are produced as separate CSVs to demonstrate separation of duties.

---

## 📘 How to run (exact steps)

1. Ensure Python and pip are installed.  
2. Install dependencies:
   ```bash```
   ```pip install pandas```
3. Run the script 
   ```py security_demo_simple.py```


