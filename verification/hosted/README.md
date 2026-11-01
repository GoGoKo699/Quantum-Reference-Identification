# Checking the hosted mathematical account

The read-only [verification workflow](../../.github/workflows/verify.yml) captures the actual commit-pinned GitHub rendering of every tracked Markdown page at widths 1440 and 760 pixels. It compares each inline and display expression, including table cells, with MathML compiled from the same pinned source. A source hash and complete expression count bind every page; headline expressions also have explicit text contracts.

The collector and source checker are a matched copy of version 0.10.0 of the Merlin–Arthur verification helpers. The collector opens an anonymous browser and requires public pinned pages. It does not request credentials or change repository settings.

To reproduce with Node.js 18 or newer, Python 3.10 or newer, Git, Playwright 1.56.1, MathJax 3.2.1 and Chromium installed:

```bash
NODE_PATH=/absolute/dependency-directory/node_modules node verification/hosted/capture_hosted_math.cjs \
  --root /absolute/repository-checkout \
  --repository GoGoKo699/Quantum-Reference-Identification \
  --revision FULL_COMMIT_SHA \
  --contract verification/hosted/math-contract.json \
  --output /absolute/new-evidence-directory
```

Replace the paths and commit with the actual checkout and inspected revision. The output directory must be new or empty so earlier failures remain available. The report includes exact source and page identities, both viewport results, captured host counts, structural comparisons, screenshot hashes and any failures.

A passing report checks source-to-host correspondence and bounded equation geometry. It does not establish proof validity, priority, full page legibility or future renderer behavior. Inspect the saved screenshots, all flagged or repaired formulas, ordinary tables and navigation separately. The finite scientific checks have their own [reproduction route](../README.md). Workflow artifacts expire; the durable review record preserves the report and its source pin separately.
