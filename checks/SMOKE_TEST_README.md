# Offline check

`offline_smoke_test.py` verifies the included manuscript-consistent CSV schemas, seven-policy set, 20-seed appendix structure, and 2,000-attempt aggregate denominator shown in the S2 transcription. It uses only the Python standard library and does not contact a network or DUT. Passing this check is a packaging/schema check, not independent reproduction of missing raw logs.
