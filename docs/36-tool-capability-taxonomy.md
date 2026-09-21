# 36 — Tool Capability Taxonomy

> **Status — `PROPOSED`, Draft / Needs SME Validation.**
> **The tool catalogue ships empty.** The website names no tools, so populating it with an assumed
> stack would invent a capability claim. This document supplies the *vocabulary* only — vendor-neutral
> capability names that procedures reference, so the catalogue can be seeded by Sleuth with what they
> actually own, license and have validated.

---

## In plain terms

Runbooks never say "use tool X". They say "this step needs the ability to image a disk with
verification hashing". The analyst then picks from whatever approved tools provide that ability, and
**their choice is recorded against the evidence**.

Two reasons this matters more than it sounds:

1. **Tools get replaced.** If a tool name appears in 200 procedures, replacing it is a 200-edit job
   that will be done incompletely. Capability references make it one catalogue change.
2. **Tools get found faulty.** When a specific version of a forensic imager turns out to have a
   defect, Sleuth needs to answer "which of our engagements used it?" in seconds. That is only
   possible if the tool and version were recorded per evidence item.

---

## 1. Capability naming

`CAP-<CATEGORY>-<nn>`. A procedure declares `capability_refs[]`. A tool record declares
`capabilities[]`. The platform resolves approved tools at execution time.

| Category | Code | Scope |
|---|---|---|
| Acquisition | `ACQ` | Getting data out of a source, forensically |
| Processing | `PRC` | Parsing, normalising, indexing |
| Analysis | `ANL` | Examining processed data |
| Discovery | `DSC` | Finding what exists |
| Testing | `TST` | Active security testing |
| Monitoring | `MON` | Continuous observation |
| Integrity | `INT` | Hashing, verification, custody |
| Reporting | `RPT` | Output production |
| Utility | `UTL` | Supporting functions |

---

## 2. The taxonomy

### Acquisition — `CAP-ACQ`
| Ref | Capability | Used by |
|---|---|---|
| `ACQ-01` | Physical disk imaging with verification hashing | `EV-03`, `DFE-04` |
| `ACQ-02` | Logical / file-system acquisition | `EV-03` |
| `ACQ-03` | Targeted collection — specified artefacts only | `IRE-05` |
| `ACQ-04` | Live-response collection from a running host | `IRE-05`, `A3-04` |
| `ACQ-05` | Volatile memory capture | `A3-05`, `DT-09` |
| `ACQ-06` | Mobile device acquisition — iOS | `SPY-06` |
| `ACQ-07` | Mobile device acquisition — Android | `SPY-06` |
| `ACQ-08` | Cloud and SaaS evidence export | `DFE`, `IRE` |
| `ACQ-09` | Network traffic capture | `IRE`, `SPY-10` |
| `ACQ-10` | Log export and preservation | `IRE`, `CTH` |
| `ACQ-11` | Configuration extraction — cloud | `TCR-02` |
| `ACQ-12` | Configuration extraction — directory services | `TCR-02`, `ATP-01` |
| `ACQ-13` | Configuration extraction — endpoint / OS | `TCR-02` |
| `ACQ-14` | Configuration extraction — network devices | `TCR-02` |
| `ACQ-15` | **Hardware write-blocking** | `A3-06` — *device, not software* |
| `ACQ-16` | Verified software write-blocking | `A3-06` |

### Integrity — `CAP-INT`
| Ref | Capability |
|---|---|
| `INT-01` | Cryptographic hashing — SHA-256 minimum |
| `INT-02` | Hash verification and comparison |
| `INT-03` | Verified image duplication |
| `INT-04` | Container sealing and seal-number tracking *(physical)* |

### Processing — `CAP-PRC`
| Ref | Capability |
|---|---|
| `PRC-01` | File system parsing and enumeration |
| `PRC-02` | Deleted file recovery and carving |
| `PRC-03` | Registry / configuration hive parsing |
| `PRC-04` | Email container parsing |
| `PRC-05` | Browser and application artefact parsing |
| `PRC-06` | Log normalisation and parsing |
| `PRC-07` | Memory image processing |
| `PRC-08` | Full-text indexing and keyword search |
| `PRC-09` | Timeline generation and normalisation *(with timezone handling)* |
| `PRC-10` | Mobile backup and filesystem parsing |
| `PRC-11` | Archive and container extraction |

### Analysis — `CAP-ANL`
| Ref | Capability |
|---|---|
| `ANL-01` | Timeline correlation across multiple sources |
| `ANL-02` | Static binary analysis |
| `ANL-03` | Dynamic / sandboxed execution analysis |
| `ANL-04` | Network protocol and C2 analysis |
| `ANL-05` | Malware unpacking and deobfuscation |
| `ANL-06` | IOC matching against a corpus |
| `ANL-07` | YARA-style pattern matching and rule authoring |
| `ANL-08` | Attack path graphing |
| `ANL-09` | Authentication and access pattern analysis |
| `ANL-10` | Spyware and stalkerware indicator matching |
| `ANL-11` | Diff and delta comparison *(A4 cycles)* |
| `ANL-12` | Detection coverage mapping to ATT&CK |

### Discovery — `CAP-DSC`
| Ref | Capability |
|---|---|
| `DSC-01` | Passive reconnaissance from public sources |
| `DSC-02` | DNS and subdomain enumeration |
| `DSC-03` | Host discovery and port scanning |
| `DSC-04` | Service and version identification |
| `DSC-05` | Web application crawling and mapping |
| `DSC-06` | API endpoint discovery |
| `DSC-07` | Cloud resource inventory enumeration |
| `DSC-08` | Directory service enumeration |
| `DSC-09` | Wireless network discovery |
| `DSC-10` | External attack surface mapping |
| `DSC-11` | Credential exposure search *(result metadata only — Rule 4)* |
| `DSC-12` | Brand and domain impersonation detection |

### Testing — `CAP-TST`
| Ref | Capability | Ceiling note |
|---|---|---|
| `TST-01` | Vulnerability scanning — network | L1 |
| `TST-02` | Vulnerability scanning — web | L1 |
| `TST-03` | Configuration benchmark comparison | L1 |
| `TST-04` | Web request interception and manipulation | L2+ |
| `TST-05` | Injection testing | L2+ |
| `TST-06` | Authentication and session testing | L2+ |
| `TST-07` | Authorisation matrix testing | L2+ |
| `TST-08` | Mobile application dynamic instrumentation | L2+ |
| `TST-09` | Cloud IAM path analysis | L2+ |
| `TST-10` | Directory attack path validation | **L3 for domain-admin proof** |
| `TST-11` | Credential attack simulation *(lockout-safe)* | L2+ |
| `TST-12` | Exploitation framework | **L2 ceiling by default; L3 requires RoE authorisation** |
| `TST-13` | Post-exploitation and lateral movement | **L3 only** |
| `TST-14` | Command and control infrastructure | **L3, red team only** |
| `TST-15` | Phishing campaign delivery | `SF-A2-SES` — **must not store credentials** |
| `TST-16` | Detection validation / atomic testing | `SF-A1-SOA` — L1/L2 equivalent |
| `TST-17` | Wireless security testing | L2+, geographic boundary applies |

> **The ceiling column is enforceable.** A tool whose only capability is `TST-13` cannot be selected
> on an engagement set to Level 2. The intrusiveness policy (`32` §1) reaches the tool picker, not
> only the procedure text.

### Monitoring — `CAP-MON`
`MON-01` continuous asset discovery · `MON-02` exposure change detection · `MON-03` credential
exposure monitoring · `MON-04` dark web and forum monitoring · `MON-05` certificate transparency
monitoring · `MON-06` vulnerability intelligence feed.

### Reporting & Utility
`RPT-01` structured report generation · `RPT-02` evidence packaging and indexing · `RPT-03`
attack path visualisation · `RPT-04` spreadsheet export.
`UTL-01` secure file transfer · `UTL-02` isolated analysis environment · `UTL-03` virtualisation and
snapshot · `UTL-04` secure deletion with certificate · `UTL-05` case and evidence storage management.

---

## 3. Tool record — the fields that carry weight

Full schema at `07-tools-and-templates.md` §3. Three deserve restating:

**`limitations[]` is mandatory.** A catalogue entry listing only what a tool can do is marketing. The
operational value is knowing where it will let you down — which file systems it mis-parses, which
mobile OS versions it cannot reach, what it silently skips.

**`data_handling_notes` is mandatory.** *Does this tool transmit data externally?* This exists because
of one recurring, serious mistake: uploading a client's suspected-malicious file to a public
multi-scanner is a disclosure to third parties, and in a targeted-intrusion case it can alert the
adversary. `MAL-03` makes sharing permission a blocking question; this field makes the risk visible at
the point of use.

**Approval is per version, not per tool.** `approval_status` and `validation_date` attach to a
`ToolVersion`. "We approved that tool" is not an answer when a specific version is found defective.

---

## 4. Selection at execution time

```
PROCEDURE  EV-03 · Acquire and verify
  REQUIRES   CAP-ACQ-01  physical disk imaging with verification hashing
             CAP-ACQ-15  hardware write-blocking
             CAP-INT-01  SHA-256 hashing

  APPROVED AND IN VALIDATION DATE        ‹resolved from the catalogue›
  ENGAGEMENT CEILING  L2 — tools above the ceiling are not offered
  SELECTED            ‹examiner chooses›
  RECORDED            tool + version, against the evidence item
```

Where no approved tool provides a required capability, the procedure **blocks at the Readiness Gate**
with a specific message — *"no approved tool provides CAP-ACQ-06 (iOS acquisition)"* — rather than an
analyst discovering it on the day.

---

## 5. Placeholders

| Ref | Placeholder | Default applied |
|---|---|---|
| `‹PH-09›` | Sleuth's actual tool inventory | **Empty.** Seeded by Sleuth in Phase 1 |
| `‹PH-10›` | Tool validation method — what constitutes validating a forensic tool at Sleuth | Reference SWGDE / NIST CFTT practice: known-dataset test, documented result, dated, by a named examiner |
| `‹PH-11›` | Revalidation trigger | Annually, or on version change for acquisition and integrity tools |
| `‹PH-12›` | Whether client-provided tooling may be used | Assumed **yes with an exception record**; never for acquisition or integrity |

---

## 6. Counts

| | |
|---|---|
| Capabilities defined | **97** |
| Categories | 9 |
| Capabilities carrying an intrusiveness ceiling | 17 |
| Tools in catalogue | **0 — ships empty by design** |
| `SME-VALIDATED` | **0** |
