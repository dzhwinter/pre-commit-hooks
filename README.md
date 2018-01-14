pre-commit-hooks
==========

Some out-of-the-box hooks for pre-commit.

See also: https://github.com/pre-commit/pre-commit


### Using pre-commit-hooks with pre-commit

Add this to your `.pre-commit-config.yaml`

    -   repo: git://github.com/dzhwinter/pre-commit-hooks
        sha: v1.0.0  # Use the ref you want to point at
        hooks:
        -   id: copyright_checker
        # -   id: ...

