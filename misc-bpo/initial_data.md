# Data explanation glossary for bpo

## stage

- '2', test needed', 'A test which exercises the issue and can be used as a unit test is needed'
- '3', 'needs patch', 'A patch is needed to fix the issue'
- '4', 'patch review', 'A patch is available and is awaiting a review by trusted developer'
- '5', 'commit review','A patch is available and is awaiting a review by a core developer'
- '6','committed/rejected', 'The issue has been resolved'

## issue_type

- 'crash', '1'
- 'compile error', order='2'
- 'resource usage', order='3'
- 'security', order='4'
- 'behavior', order='5'
- 'performance', order='6'
- 'feature request', order='7'

## component

- "None", order="1"
- "2to3 (2.x to 3.0 conversion tool)", order="2"
- "Build", order="3"
- "ctypes", order="4"
- "Demos and Tools", order="5"
- "Distutils", order="6"
- "Documentation", order="7"
- "Extension Modules", order="8"
- "IDLE", order="9"
- "Installation", order="10"
- "Interpreter Core", order="11"
- "Library (Lib)", order="12"
- "Macintosh", order="13"
- "Regular Expressions", order="14"
- "Tests", order="15"
- "Tkinter", order="16"
- "Unicode", order="17"
- "Windows", order="18"

## version

- 'Python 3.1', order='1'
- 'Python 3.0', order='2'
- 'Python 2.7', order='3'
- 'Python 2.6', order='4'
- 'Python 2.5', order='5'
- 'Python 2.4', order='6'
- '3rd party', order='7'


## severity

- 'critical', order='1'
- 'urgent', order='2'
- 'major', order='3'
- 'normal', order='4'
- 'minor', order='5'

## priority

- 'release blocker', order='1', 'Blocks a release')
- 'deferred blocker', order='2', 'Blocks a future release')
- 'critical', order='3','Might block a future release')
- 'high', order='4', 'important but will not block')
- 'normal', order='5'
- 'low', order='6', 'E.g. spelling errors in documentation'

## status

- 'open', order='1'
- 'closed', order='2'
- 'pending', order='3', 'user feedback required')

## resolution

- 'accepted', order='1'
- 'duplicate', order='2'
- 'fixed', order='3'
- 'invalid', order='4'
- 'later', order='5'
- 'out of date', order='6
- 'postponed', order='7'
- 'rejected', order='8'
- 'remind', order='9'
- 'wont fix', order='10'
- 'works for me', order='11'

## "keyword"

- "26backport", "Backport 3.0 feature from 2.6"
- "64bit", "Affects 64-bit platforms only"
- "easy", "This is an easy task (e.g. suitable for GHOP or "bug day - beginners)"
- "needs review", "This issue has a patch which needs the review of a - developer."
- "patch", "Contains patch"
