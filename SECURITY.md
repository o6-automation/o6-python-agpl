# Security Policy

The authoritative, always-current version of this policy is published at
**<https://www.o6-automation.com/security>**. 

## Reporting a Vulnerability

You are invited to disclose your findings privately with one of the following
mechanisms. **DO NOT OPEN PUBLIC GITHUB ISSUES FOR POTENTIAL VULNERABILITIES.**
This only gives the bad guys a head-start and does not speed up the
vulnerability handling.

- Via email to psirt@o6-automation.com
- Via the Github disclosure mechanism at
  https://github.com/o6-automation/o6-python-agpl/security/advisories

You can encrypt emails to us with the o6 PSIRT PGP key, available at
<https://www.o6-automation.com/security/o6-psirt.asc>:

```
C969 F334 7BA6 31BD 5686  9514 AE55 28D6 D703 B17C
```

Please include, as far as you can determine it:

1. **Affected product** -- name the product, release, commit or service,
   including the relevant configuration.
2. **Security impact** -- describe what an attacker could achieve and which
   assumptions or access are required.
3. **Reproduction** -- provide clear steps, a minimal proof of concept, and
   relevant logs or traces.
4. **Disclosure status** -- tell us whether anyone else knows, whether
   exploitation is suspected, and how you wish to be credited.

## Vulnerability Management Process

The disclosure of a potential vulnerability triggers our Vulnerability
Management Process. It comprises of the following steps:

1. Acknowledgement of receipt and setup of a private channel for follow-up
   questions
2. Evaluation of the disclosure (reproduction and CVSS score), and
   determination of the affected products and versions
3. If relevant, preparation of mitigations (patches) for the impacted
   o6\Python release families together with a non-public Vulnerability Advisory
4. Dissemination to commercial users and operators of critical infrastructure
5. Embargo time (typically 30 days)
6. Merge of the mitigations into the impacted o6\Python release family branches
7. Preparation of o6\Python patch releases for the impacted release families

## Acknowledgement and Public CVE

**We do not endorse public CVE advisories for o6\Python.** With todays AI-based
coding tools, a public CVE has roughly the same impact as releasing a working
exploit. Professional users and operators of critical installations receive
non-public Vulnerability Advisories via the Professional Support Services. Then,
after an embargo time to fix critical installations, we prepare public patch
releases for the impacted versions of o6\Python.

If the person disclosing a vulnerability wishes so, we can give a personal
acknowledgement of the disclosure both in the non-public Vulnerability Advisory
and in the commits that are eventually merged into the public git branches.
