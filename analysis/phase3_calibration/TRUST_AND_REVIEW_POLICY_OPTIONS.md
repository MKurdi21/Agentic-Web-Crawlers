# Trust and Review Policy Options

Status: recommendation pending owner approval.

## Non-aliasing review classes

```text
MODEL_VERIFICATION
INDEPENDENT_MODEL_VERIFICATION
HUMAN_REVIEW
TRUSTED_HUMAN_APPROVAL
```

Model agreement can locate disagreements and estimate automation suitability. It is not human approval or duplicate human extraction.

## Options

- **Human-only:** humans perform and authorize all scientific verification.
- **Human plus model assistance:** models prepare evidence checks; humans authorize scientific acceptance.
- **Risk-tiered:** low-risk structural fields may pass deterministic validation; scientific claims receive model checks and trusted-human authorization at the approved threshold.

## Recommendation

Use risk-tiered review. Permit deterministic acceptance only for exact hashes and low-risk structural facts. Require trusted-human approval for production `SOURCE_VERIFIED`, quantitative conclusions, security threat models, contribution/version adjudication, synthesis eligibility, contradictions, and policy-sensitive decisions.

No software identity may satisfy `TRUSTED_HUMAN_APPROVAL`. Until an authenticated reviewer registry exists, that state is unavailable and dependent transitions fail closed. Test identities use `TEST_FIXTURE_NOT_A_HUMAN` and are rejected by production import paths.
