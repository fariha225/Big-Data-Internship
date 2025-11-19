#  Big Data Security & Compliance Framework (GDPR / HIPAA-Aligned)

*COMPANY* : CODTECH IT SOLUTIONS

*NAME* : Syeda Fariha Fatima 

*INTERN ID* : CT04DR818

*DOMAIN* : Big Data

*DURATION*: 4 weeks

*MENTOR* : Neela Santhosh Kumar

## 📄 Task 4 – Security & Compliance Report

---

##  **1. Introduction**

Big data systems handle massive volumes of information, including sensitive *PII (Personally Identifiable Information)*.  
To comply with global data protection laws, a structured security framework is required.

This report outlines a practical framework aligned with:

- **GDPR** (EU General Data Protection Regulation)  
- **HIPAA** (US Health Insurance Portability and Accountability Act)  
- **ISO 27001** (Information Security Management Standard)

---

##  **2. Objectives of the Framework**

- Ensure **Confidentiality** → prevent unauthorized access  
- Maintain **Integrity** → avoid tampering or corruption  
- Guarantee **Availability** → systems must stay operational  
- Provide **Compliance** → follow global standards  
- Enable **Auditability** → track all actions and access  

---

##  **3. Big Data Architecture Overview**

A secure pipeline includes:

1. **Data Ingestion Layer** – ETL, batch loads, streaming inputs  
2. **Storage Layer** – Data Lake, Data Warehouse, HDFS  
3. **Processing Layer** – Spark, Hadoop  
4. **Analytics Layer** – BI dashboards, ML pipelines  
5. **Access Layer** – Analysts, APIs, applications  

Security controls apply to *each* layer.

---

## **4. Security Framework Components**

---

###  **4.1 Identity & Access Management (IAM)**

- Enforce **Role-Based Access Control (RBAC)**  
- Roles:  
  - **Analyst** → masked/anonymized data  
  - **Manager** → full data  
  - **Admin** → infrastructure access  
- Apply **Least Privilege Access**  
- Require **Multi-Factor Authentication (MFA)**  
- Conduct **Periodic Access Reviews**

**Compliance Mapping:**

- GDPR → Article 32  
- HIPAA → Access Control (164.312)

---

###  **4.2 Data Encryption**

#### **Encryption at Rest**
- AES-256 encryption  
- Encrypted cloud volumes (AWS KMS, Azure Key Vault)

#### **Encryption in Transit**
- TLS/SSL for API + Spark cluster communication

**Compliance Mapping:**

- GDPR → Article 32  
- HIPAA → Transmission Security

---

###  **4.3 Data Masking & Anonymization**

Required when exposing data to non-privileged roles.

Techniques:

- Masking → `***123`  
- Tokenization  
- Hashing (SHA-256)  
- Static or Dynamic Data Masking (SDM / DDM)

**Compliance Mapping:**

- GDPR → “Data Protection by Design”  
- HIPAA → De-identification Standard

---

###  **4.4 Logging & Audit Trails**

Every data operation must be logged:

- User identity  
- Action  
- Timestamp  
- Data accessed  

Common tools:
- Splunk  
- ELK Stack  
- AWS CloudWatch  
- Azure Monitor  

**Compliance Mapping:**

- GDPR → Article 30  
- HIPAA → Audit Controls

---

### **4.5 Data Minimization & Purpose Limitation**

Core principles:

- Collect only what is necessary  
- Store only as long as needed  
- Remove or prune unused PII fields  

Reduces overall risk.

---

### **4.6 Secure Data Processing (Spark / Hadoop)**

Security best practices:

- Cluster isolation  
- Encrypted node-to-node traffic  
- Signed Spark job submissions  
- Secured notebook environments  
- Manage secure temporary Spark shuffle storage  

---

###  **4.7 Backup & Disaster Recovery**

- Daily incremental backups  
- Weekly full backups  
- Multi-region redundancy  
- Routine restore testing  

**Compliance Mapping:**

- HIPAA → Contingency Plan  
- ISO 27001 → Backup Controls

---

## 🧾 **5. Compliance Checklist**

| **Control Area**      | **GDPR**      | **HIPAA**              | **Status**      |
|-----------------------|---------------|-------------------------|-----------------|
| Role-Based Access     | ✔ Art. 32     | ✔ 164.312               | Implemented     |
| Data Masking          | ✔ Art. 25     | ✔ De-identification     | Implemented     |
| Audit Logging         | ✔ Art. 30     | ✔ 164.312               | Implemented     |
| Encryption            | ✔ Art. 32     | ✔ 164.312               | Designed        |
| Data Minimization     | ✔ Art. 5      | —                       | Designed        |
| Backup & DR           | —             | ✔ 164.308               | Designed        |

---

## 🛠 **6. Prototype Implemented in This Task**

This project demonstrates practical implementations of core security controls:

### **a. Role-Based Access Control (RBAC)**  
- **Analyst** → receives *masked* CustomerID  
- **Manager** → receives *full* CustomerID  

### **b. Data Masking**
CustomerID masking function used in the prototype:

```python```
```def mask_customer_id(cid):```
    ```return "***" + str(cid)[-2:]```

  ###  **c. Audit Logging**

All data access and processing actions are recorded in an audit log.

**Example audit log entry:**
```2025-11-19 18:15:25,147 – actor=system action=load_dataset details=rows=5 file=sample_data/cleaned_retail_sample.csv```

---

### **d. Secure Output Files**

The prototype generates multiple secure output files showing different access levels and logs:

- `demo_masked.csv` — Masked analyst view  
- `demo_manager.csv` — Full-access manager view  
- `task4_audit_log.txt` — Complete audit log  
- `terminal_output.txt` — Raw terminal execution logs

 ###  **7. Conclusion**

This security framework ensures that a modern Big Data system is:

- 🔒 **Secure**
- 📜 **Compliant** with GDPR & HIPAA
- 🧾 **Auditable** through detailed logs
- 📈 **Scalable** for large datasets and distributed pipelines
- 🛡 **Privacy-preserving** via masking & RBAC

The implemented prototype — **data masking**, **role-based access control**, and **audit logging** — closely reflects real-world enterprise security practices used in production-grade big data systems.

<img width="1464" height="512" alt="Image" src="https://github.com/user-attachments/assets/fd34476d-f9c4-4ce1-b711-8c6d1c904f56" />





 


