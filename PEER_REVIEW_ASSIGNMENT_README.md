# Peer Review Assignee Assignment

This repository contains automation to assign all GitHub usernames mentioned in the "Peer review assignment" issue as assignees to that issue.

## How It Works

The solution extracts all `@username` mentions from the peer review issue body and automatically assigns those users as assignees to the issue.

## Solutions Provided

### 1. GitHub Actions Workflow (Automatic)

The workflow `.github/workflows/assign-peer-reviewers.yml` automatically runs when:
- The peer review assignment issue is opened or edited
- Manually triggered via GitHub Actions UI

**Benefits:**
- Fully automated
- Runs whenever the issue is updated
- No manual intervention required

### 2. Standalone Script (Manual)

For immediate execution, use the standalone script `assign_peer_review_assignees.py`:

```bash
# Install dependencies
pip install PyGithub

# Run the script (provide your GitHub token)
python3 assign_peer_review_assignees.py YOUR_GITHUB_TOKEN

# Or set token as environment variable
export GITHUB_TOKEN=your_token_here
python3 assign_peer_review_assignees.py
```

**Benefits:**
- Can be run immediately
- Provides detailed output and verification
- Works independently of GitHub Actions

## Current Issue Status

The script targets issue #4 "Peer review assignment" which contains 14 unique GitHub usernames:

- MotunGreat
- Vinish99
- EstherAbik
- mint-thai
- ChaitanyaThirampuram
- cynthiandrea7
- shivagpro
- Mr-Gholam
- vishu0713
- ThiwankaKT
- nra2629
- Maggy9310
- HanPing0131
- DEFINATE2001

## Features

- ✅ Extracts usernames automatically from issue content
- ✅ Avoids duplicate assignments
- ✅ Provides detailed logging and verification
- ✅ Works with any issue containing @username mentions
- ✅ Handles errors gracefully

## Requirements

- Python 3.6+
- PyGithub library
- GitHub token with `issues:write` permission