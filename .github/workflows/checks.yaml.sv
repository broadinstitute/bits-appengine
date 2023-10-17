---
name: 'checks'

'on':
  pull_request:
    branches:
      - 'main'

jobs:
  linting:
    uses: broadinstitute/shared-workflows/.github/workflows/poetry-linting.yml@v1.4.0
