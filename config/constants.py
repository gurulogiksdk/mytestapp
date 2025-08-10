NAME = "ABC XYZ"

TITLE = f"{NAME} Resilience Assessment"

WELCOME_MESSAGE = f"Thank you for choosing {NAME} for your Resilience Assessment"




PROMPT_TEMPLATE_PATH = "config/prompt.txt"



file_types_allowed_list = ['pdf', 'docx', 'txt', 'csv', 'json']




placeholder_response = """
📄 **Resilience Architecture Assessment Summary**

**Application Name:** [PlaceholderApp]  
**Tier Level:** Tier 0 (Near-zero RTO/RPO, 99.99% availability)  
**Detected Platforms:** AWS, Azure

---

### 🧭 Domain Review Summary

| Domain | Current Design | Gap | Target Pattern | Risk |
|--------|----------------|-----|----------------|------|
| Global Traffic Management | Route 53 with basic failover | No health-based routing across regions | Use Route 53 + health checks + Global Accelerator | 🔴 |
| Compute Tier HA | EC2 with ASG in single AZ | AZ single-point-of-failure | Use ASG across multiple AZs | 🔴 |
| State & Data Layer | RDS Single-AZ, no cross-region | RPO > acceptable | RDS Multi-AZ + cross-region read replica | 🟡 |
| Backup Strategy | Daily snapshots, no immutability | Ransomware vulnerability | S3 Object Lock + AWS Backup + Vault Lock | 🔴 |

---

### 🛡️ Platform-Specific Recommendations

**AWS:**
- Implement Global Accelerator for cross-region failover
- Configure S3 Object Lock (compliance mode) with lifecycle rules
- Use RDS Multi-AZ with auto-failover and backup validation
- Integrate Route 53 ARC for resilience readiness tracking

**Azure:**
- Consider Azure Front Door + App Gateway for application routing
- Implement SQL MI Failover Groups
- Enable immutable backups on Blob storage

---

### 🧪 DR Testing & Recovery

- Last DR test not found in uploads — **Not evidenced**
- No runbook automation or synthetic DR scripts provided
- Recommendation: Implement scripted runbooks with idempotency and DR failover simulation logs

---

### 🧠 Risk Index (RRI) Summary

| Metric | Score | Weight | Risk |
|--------|-------|--------|------|
| Multi-AZ Topology | 2/5 | 15% | 🟡 |
| Backup Immutability | 1/5 | 10% | 🔴 |
| DR Testing Evidence | 0/5 | 10% | 🔴 |
| Monitoring Automation | 3/5 | 5% | 🟡 |

🧮 **Total RRI Score:** 45.2 / 100  
📉 **Readiness Level:** LOW

---

📌 **Note:** Several controls and standards were not evidenced in uploaded documents, including DR Runbooks, RCA reports, and chaos testing. Please upload those to improve assessment coverage.

"""
