- Easiest vs. Hardest Fixes

    The easiest fixes were removing unused imports and replacing eval() with a direct print() statement. These changes were straightforward and risk-free.
    The hardest part was addressing the bare try/except and modifying file operations to use with open(..., encoding="utf-8"). These required careful handling to preserve program behavior and prevent unintended side effects.

- False Positives

    No major false positives were observed. However, the warning about using the global statement was contextually acceptable, as the variable was intentionally shared across functions.

- Integration of Static Analysis Tools

    - Tools like pylint, flake8, and bandit can be integrated into the workflow through:

    - Pre-commit hooks to catch issues before commits.

    - Continuous Integration (CI) pipelines to ensure quality checks run automatically on every push or pull request.

    - Editor integration (e.g., VS Code linters) for real-time feedback during coding.

- Improvements Observed

    - After applying the fixes, the code became cleaner, safer, and more consistent with PEP 8 standards.

    - Using with statements improved file handling and resource safety.

    - Adding docstrings and formatting lines enhanced readability.

    - Avoiding dangerous defaults and eval() increased reliability and security.