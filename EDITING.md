# Editing this course ✏️

This repository holds one ICoBC course as a single LiaScript file, `README.md`.
Everything the learner sees comes from that file. You need no software to change
it: GitHub can do it in the browser.

## Look at the course first

- Repository: <https://github.com/ICoBC/icb-h03-selective-disclosure-privacy-preserving-proofs>
- Rendered in LiaScript: <https://liascript.github.io/course/?https://raw.githubusercontent.com/ICoBC/icb-h03-selective-disclosure-privacy-preserving-proofs/main/README.md>
- Published web module: <https://academy.icobc.net/courses/icb-h03/>

## Change something

1. Open `README.md` in this repository and select the pencil (**Edit this file**).
2. Make your change. Keep the structure below.
3. Scroll down, describe your change in one line and select **Propose changes**.
4. Open the pull request. The automatic check runs, then an ICoBC editor reviews it.

## The structure the Academy expects

| Part | Meaning |
|---|---|
| The comment block at the very top | author, version, language, narrator and the ICoBC style block. Raise `version` when you change the content. |
| `# Title` | the course title, followed by one quoted line as the summary |
| `## About this course` | who it is for, outcomes, workload, assessment, badge |
| `## 1. …` to `## 5. …` | one level-2 heading per module, level-3 headings inside |
| `## Assessment and badge` | the final knowledge check; these questions are the scored ones |
| `## Sources and further reading` | only sources that really exist |

## Questions

Single choice, exactly four options, exactly one correct, and an explanation
between two lines of asterisks:

```markdown
**Question 1.** What does the criteria element tell a reader?

[( )] Who issued the credential
[(X)] What the earner had to do
[( )] When the credential expires
[( )] Which framework it aligns to
****
Criteria describe the requirements. Evidence then shows that they were met.
****
```

Questions with several correct answers (`[[X]]`) work in LiaScript and in the web
module, but not in the scored final check. Keep the final check to single choice.

## House style

- British English: recognise, organisation, colour, centre, programme, licence (noun), per cent.
- Dates as "4 November 2026". No em dashes.
- No invented statistics, quotes, article numbers or sources. Mark anything that
  needs checking with `<!-- VERIFY: ... -->`; the check lists these.
- Name standards, frameworks and public bodies, never commercial products.
- Graphics are inline `<svg>` with `<title>` and `<desc>`, in the ICoBC colours.
  No external images, no `@import`, no scripts: the file must work offline.

## What happens after the merge

ICoBC rebuilds the web module and the SCORM package from this file. The course
appears on the Academy with the new version number.

## Licence

Content: CC BY 4.0, International Council on Badges and Credentials e.V.. The ICoBC name, logo, illustrations and signatures are
not covered by that licence. See `LICENSE`.
