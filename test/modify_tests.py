from pysyntax import modify


def header_comments__no_comment_test():
    code = """import x\n"""
    comments = "# A comment"
    for empty_lines in range(4):
        new_code = modify.header_comments(code=code, new_comments=comments, empty_lines=empty_lines)
        assert new_code == f"# A comment\n{'\n' * empty_lines}import x\n"


def header_comments__existing_comment_test():
    code = """# Existing comment\n\nimport x\n"""
    comments = "# A comment"
    for empty_lines in range(4):
        new_code = modify.header_comments(code=code, new_comments=comments, empty_lines=empty_lines)
        assert new_code == f"# A comment\n{'\n' * empty_lines}import x\n"


def header_comments__existing_comments_test():
    code = """# Existing comment\n\n# Another comment\nimport x"""
    comments = "# A comment\n# Another new comment"
    for empty_lines in range(4):
        new_code = modify.header_comments(code=code, new_comments=comments, empty_lines=empty_lines)
        assert new_code == f"# A comment\n# Another new comment\n{'\n' * empty_lines}import x"