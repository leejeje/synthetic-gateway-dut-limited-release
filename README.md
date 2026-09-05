# Limited public release candidate

This repository contains the selected configuration files, fixed-seed protocol manifest, and manuscript-consistent aggregate summaries associated with the IEEE Access article **AI-Based Cross-Interface Attack Chain Generation and Optimization for Automotive Cybersecurity Penetration Testing**. The evaluation target is a synthetic or isolated Gateway-DUT environment.

## Release scope

Included materials are:

- paper-aligned, documentation-only reward and handoff parameter files (not executable result generators);
- fixed-seed and experiment-protocol manifests;
- manuscript-consistent Table VII, Supplementary S1/S2, and Appendix aggregate/transcribed CSV files;
- an offline schema and consistency smoke test; and
- license files and citation metadata.

This is a **limited public release**. It is not a raw-log archive and it is not presented as a complete independent reproduction package. The executable experiment source, raw SQLite/log files, and the original attempt-level log corresponding to the manuscript’s 2,000-attempt ASR denominator are not included because those materials are not available in the retained project files.

The YAML configuration files document parameters explicitly stated in the accepted manuscript; they do not generate or impute result data. The included CSV files are static aggregate/seed-level transcriptions. The Supplementary S2 CSV is an aggregate transcription of the values reported in the accepted manuscript. It is not regenerated attempt-level raw data, and no independent reconstruction of the missing 2,000-attempt log is claimed. Available 10,000-attempt materials and normalized-TTFF reconstructions are not substituted for the manuscript-consistent values.

## Safety and authorization

The materials are limited to an authorized synthetic or isolated Gateway-DUT environment. Do not connect them to a production vehicle, public network, or third-party system, and do not use them to probe, disrupt, bypass authentication on, or inject traffic into systems without explicit authorization.

## Paper linkage

The accepted article is the authoritative source for the reported scientific results. This release preserves the manuscript-consistent aggregate values and does not alter, recompute, or reinterpret the article’s conclusions.

## Citation and identifiers

The versioned public repository is: https://github.com/leejeje/synthetic-gateway-dut-limited-release

`CITATION.cff` records version 1.0.0 and the repository URL. The Zenodo DOI will be added after the v1.0.0 GitHub release is archived and published by Zenodo. No DOI is inferred or fabricated in this candidate.

Repository license scope: the data and documentation are released under CC BY 4.0 as described in `LICENSE-DATA-AND-DOCUMENTATION.md`; the MIT license file is retained for any future code scope, although this limited release contains no executable experiment source.

## Validation

Run the standard-library-only check from the repository root:

```text
python checks/offline_smoke_test.py
```

No included file generates, imputes, bootstraps, or simulates the scientific results. The check reads only the included manuscript-consistent CSV files and validates schema, row counts, policy/seed coverage, and S2 arithmetic. It does not access a DUT, open a network connection, read raw DB/log files, or establish independent reproduction of missing raw records.
