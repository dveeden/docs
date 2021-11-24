#!/bin/python3
import argparse
import glob
import re
import sys
import sqlparse
from pathlib import Path

SQL_RE = re.compile(
    r"^\s*(select .* from|update table|alter table|delete from|create user) .*?(;|$|\\G)"
)

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Check SQL formatting")
    parser.add_argument("file", nargs="*")
    args = parser.parse_args()
    returncode = 0

    files = [Path(x) for x in args.file]
    if not files:
        files = [Path(x) for x in glob.glob("**/*.md")]

    for file in files:
        with file.open() as fh:
            linenr = 0
            matches = []
            while line := fh.readline():
                linenr += 1
                if m := SQL_RE.search(line):
                    matches.append(f"  On line {linenr:4d}: {m[0][:70]}")
            if matches:
                returncode = 1
                print(
                    f"\nSQL in {file} needs to be changed to have uppercase keywords."
                )
                [print(x) for x in matches]

                fh.seek(0)
                suggestions = []
                if m := re.findall(
                    r"```sql\n(.*?)```", fh.read(), re.MULTILINE | re.DOTALL
                ):
                    for sql in m:
                        if re.search(
                            r"(mysql>|\+-{4}|\*{4}|rows affected|curl|Query_time|ERROR)",
                            sql,
                        ):
                            # Skip things that are not SQL, but output from SQL statements, etc
                            continue
                        for stmt in sqlparse.split(sql):
                            sqlfmt = sqlparse.format(
                                stmt, reindent=False, keyword_case="upper"
                            )
                            if stmt != sqlfmt:
                                for l in stmt.split("\n"):
                                    suggestions.append(f"  - {l}")
                                for l in sqlfmt.split("\n"):
                                    suggestions.append(f"  + {l}")
                                suggestions.append("")
                if suggestions:
                    print("\n  Suggested changes:")
                    [print(x) for x in suggestions]
    sys.exit(returncode)
