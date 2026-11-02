# Evidence updates and publication

This repository contains published clinical research only, not patient information. Source data: data/trials.json, data/meta.json and data/coverage.json. Build with Python 3: `python scripts/validate.py` then `python scripts/build.py`. Copy dist/ to docs/ for GitHub Pages (main branch, /docs).

Review primary publications, registry updates, corrections and retractions daily; page through the search period and record failed sources. Review at most 10 priority candidates per run and retain unresolved candidates outside the verified dataset. Confirm population, treatment arms, analysis denominator, endpoint/timepoint, effect and confidence interval before changing a trial. Preserve negative findings and previous sources. Do not infer survival curves, pool unrelated trials or rank treatments across trials.

Record source-fetch time separately from clinical-verification time. Update verified records and version history, validate and rebuild, then commit source and docs together using an authenticated maintainer connection. Verify exact remote revision and public readback. No public write endpoint or credentials belong in this repository. Keep the prior functioning revision on failure. Daily review is not enabled merely by publishing this repository; activation requires a verified recurring authenticated maintenance run.
