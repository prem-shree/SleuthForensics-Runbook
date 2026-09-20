# 13 — Security Architecture

> **Status — DRAFT / NEEDS SME VALIDATION.** Per Rule 1 of [`17-governing-constraints.md`](17-governing-constraints.md), nothing in this document is
> confirmed Sleuth practice. Procedures, tools, legal requirements and operational rules here are
> proposals for SME review, not internal SOP. Content drawn from the public website is
> `SITE-SUGGESTED` and carries no authority over internal method (Rule 6). Gaps are named rather
> than filled (Rule 2). Validation vocabulary: [`18-content-provenance-and-validation.md`](18-content-provenance-and-validation.md).
>
> **§6 is now a hard constraint (Rule 4), not a recommendation.** There is no field, anywhere in
> the schema, typed to hold a secret.


> This platform holds, in one place: every client's scope and known weaknesses, live incident details, forensic evidence, and unreleased findings. It is a higher-value target than most of the systems Sleuth is engaged to assess.
>
> That is the design premise. A compromise here is not an outage — it is a breach of every client simultaneously, and it would end the firm.

---

## 1. Threat model, stated plainly

| Threat | Why it is credible here | Primary control |
|---|---|---|
| Credential theft targeting consultants | Consultants are publicly identifiable and hold access to many clients | Phishing-resistant MFA (WebAuthn), short sessions, re-auth for sensitive acts |
| Targeted compromise of Sleuth itself | Attacking the assessor to reach the assessed is an established pattern | Network isolation, least privilege, hardened hosting, monitoring |
| Insider access beyond need | 20 people should not all see 60 clients' evidence | Engagement-scoped access; no standing firm-wide read |
| Evidence tampering (external or internal) | Undermines every report ever issued | Hashing, hash-chained append-only audit, immutable custody events |
| Accidental disclosure | Report to the wrong recipient; evidence in the wrong engagement | Release Gate with recipient verification; persistent classification bar |
| Client data in a non-production environment | The most common way real data leaks from an internal tool | Synthetic-only rule, enforced by a seeding guard |
| Physical evidence loss | Devices and drives move between people and sites | Custody events, seal numbers, storage medium tracking |

---

## 2. Authentication

- **SSO/OIDC** against Sleuth's identity provider where one exists *(Needs Confirmation)*; otherwise local accounts with the same policy.
- **MFA mandatory for every account, without exception.** No "remember this device" for privileged roles.
- **WebAuthn / hardware keys preferred over TOTP**, and required for Administrator and Management. TOTP is phishable; given the threat model above, that matters more here than the enrolment friction.
- **Session:** 8-hour absolute, 30-minute idle. **Step-up re-authentication** for: evidence download, disposition authorisation, gate override, report release, user/role changes, bulk export.
- No shared or service accounts for human activity. Automation uses scoped, attributable credentials.
- On an active incident, sessions may be extended by an explicit, logged action — because forcing a re-login at 4am mid-acquisition creates worse risks than it removes.

## 3. Authorisation

Per `02-users-and-roles.md`: `Role capability ∧ Engagement membership ∧ Object rule`.

- **No standing access to all engagements for anyone** — Management and Administrators included.
- Break-glass access is available, and is logged, notified to the Engagement Manager, visible on the Oversight dashboard, and time-boxed.
- **Row-level security at the database layer**, not only in application code. Application-layer-only scoping fails open on the first forgotten `WHERE` clause; defence in depth means the database refuses too.
- Engagement membership is time-bounded and lapses at closure by default.

## 4. Evidence protection

- Evidence content lives in object storage, **never in the application database**.
- **Per-engagement encryption keys** in a managed KMS. A single compromised key exposes one engagement, not the archive.
- Access via short-lived signed URLs, generated per request, logged as an `AccessEvent` with a selected purpose.
- No public endpoints on evidence storage, ever. No predictable paths.
- Bulk export requires Engagement Manager approval and is notified.
- Backups are encrypted, and **deletion propagates to backups** — otherwise a destruction certificate is a document asserting something untrue.
- **A destroyed item's record, hashes and custody chain are retained permanently.** Content is destroyed; provenance is not.

## 5. Audit

- Append-only, hash-chained (`prev_hash` → `hash`), with periodic anchoring to an external store so tampering is detectable rather than merely prohibited.
- **No role can modify or delete an audit event.** Enforced by table permissions, not application logic.
- Logged: authentication, all authorisation decisions including denials, every evidence access, every gate evaluation and override, every state change with before/after, every export, every break-glass, every admin action.
- Retention aligned to the longest applicable obligation *(Needs Confirmation — Decision D7)*.
- Engagement-scoped audit views are available to the Engagement Manager, because "who touched this engagement" is an operational question, not only a forensic one.

## 6. Secrets — a hard constraint

> **Rule 4 (binding).** No client credentials, secrets, API keys, passwords, private keys or similar
> access material in the platform. There is no field, anywhere in the schema, typed to hold one.

**The platform must not become a client credential store.**

Test accounts, API keys, VPN credentials and cloud access keys for client environments are among the most sensitive things a consultancy handles, and the temptation to keep them beside the engagement for convenience is strong. Resist it. A single compromise of this platform would then hand an attacker working credentials into dozens of client environments — converting a bad breach into a catastrophic one.

**What the platform records instead:**

```
Test account TA-02
  Purpose            Authenticated web application testing, "partner" role
  Status             ● Delivered and verified working
  Delivered via      Client's password manager, shared vault link
  Delivered by       J. Fernandes (client), 2026-09-19
  Verified by        P. Nair, 2026-09-19
  Expires            2026-09-27 (end of testing window + 1 day)
  Revocation         Confirmed by client 2026-09-28    ⓘ tracked at closure
  ─────────────────────────────────────────────────────────────
  Credential itself  NOT STORED IN THIS PLATFORM
```

This keeps every operationally useful fact — does it exist, does it work, when does it expire, was it revoked at closure — without holding the secret. Credential revocation at closure becomes a tracked Closure Gate condition, which is a genuine improvement on the status quo in most consultancies.

Platform secrets (database credentials, KMS references, integration keys) live in a managed secrets store, never in the repository, never in environment files committed anywhere.

## 7. Environments and data

```
Production    real client data · full controls · restricted access · MFA enforced
Staging       synthetic data only · production-like configuration
Development   synthetic data only · no production access of any kind
```

**Never any real client data outside production.** Not "anonymised", not "just this once for a bug". Anonymisation of forensic and incident data is unreliable — hostnames, IPs, timestamps and file paths re-identify a client trivially, and an incident narrative is identifying on its own.

**Enforced, not merely stated:** a seeding guard refuses to load data into non-production if it fails synthetic-data heuristics (real-looking domains, public IP ranges, plausible client names). Demo and test data is generated from a fixed synthetic fixture set — fictional companies, RFC 5737 documentation IP ranges, `.example` domains, generated hashes.

## 8. Application security

The obvious baseline applies and is not restated at length: parameterised queries, output encoding, CSRF protection, strict CSP, secure cookie flags, HSTS, no secrets in logs, dependency scanning, rate limiting on authentication.

Worth stating for this application specifically:

- **File upload is a primary attack surface**, because analysts will upload malware samples by design. Uploads are stored outside the web root, never executed, never rendered inline, scanned where appropriate, and served only with `Content-Disposition: attachment` and a non-executable content type. Malware samples are stored password-protected and clearly marked, and the UI makes accidental opening hard.
- **Server-side rendering of client-supplied content** (questionnaire answers, client document text) is a stored-XSS vector against Sleuth's own staff. Escape everywhere; no `innerHTML` paths.
- **The platform should be subject to Sleuth's own testing.** A security consultancy running an internal platform that has never been assessed is an uncomfortable position to be in. Recommend a full assessment before it holds real engagement data, and annually thereafter.

## 9. Availability and recovery

- Incident response engagements make this operationally sensitive: the platform being down during a client's ransomware incident is a serious failure.
- Encrypted backups, **restore tested on a schedule** — an untested backup is a hypothesis.
- Defined RTO/RPO *(Needs Confirmation)*.
- **An offline path for incident work.** The runbook for an active incident, the current engagement's stop conditions, escalation contacts and the chain-of-custody form must be exportable to PDF and usable without the platform. A tool that becomes a single point of failure during an incident has made things worse, not better.

## 10. Legal and regulatory — open, not assumed

The website states only that it operates under the laws of India and serves organisations across India. It names no specific legislation. The following are therefore recorded as questions for qualified counsel, **not** as requirements the platform assumes:

- Data residency: must all client data, including evidence, remain in India?
- Which incident-reporting obligations apply to Sleuth, and which apply to its clients with Sleuth advising?
- Personal-data obligations arising from holding forensic images that contain third parties' personal data — including people who are not the client.
- Whether Sleuth issues certificates for electronic records, or provides expert testimony; both would change the report format and the custody documentation materially.
- Retention: minimum and maximum periods for evidence, reports and audit logs.
- Cross-border transfer where a client's evidence originates outside India.
- Professional indemnity requirements that constrain record-keeping.

The platform is built so these are **configurable policy**, not hard-coded assumptions — retention periods, residency, disposition defaults and certificate templates are all settings. That is the correct engineering response to a set of questions that only counsel can answer.
