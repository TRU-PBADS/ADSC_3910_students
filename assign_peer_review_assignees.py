#!/usr/bin/env python3
"""
Standalone script to assign all usernames from the peer review issue to that issue.
This script can be run manually to perform the assignment immediately.

Usage:
    python3 assign_peer_review_assignees.py [GITHUB_TOKEN]
    
If GITHUB_TOKEN is not provided as argument, it will look for it in environment variable.
"""

import os
import re
import sys
from github import Github

def extract_usernames_from_issue_body(issue_body):
    """Extract GitHub usernames mentioned in the issue body."""
    # Pattern to match @username mentions
    username_pattern = r'@([a-zA-Z0-9_-]+)'
    usernames = re.findall(username_pattern, issue_body)
    
    # Remove duplicates and return as set
    unique_usernames = list(set(usernames))
    
    print(f"Found {len(unique_usernames)} unique usernames: {', '.join(sorted(unique_usernames))}")
    return unique_usernames

def assign_users_to_issue(github_client, repo_name, issue_number, usernames):
    """Assign the extracted usernames to the specified issue."""
    try:
        repo = github_client.get_repo(repo_name)
        issue = repo.get_issue(issue_number)
        
        print(f"Processing issue #{issue_number}: {issue.title}")
        
        # Get current assignees
        current_assignees = [assignee.login for assignee in issue.assignees]
        print(f"Current assignees ({len(current_assignees)}): {', '.join(current_assignees) if current_assignees else 'None'}")
        
        # Filter out usernames that are already assigned
        new_assignees = [username for username in usernames if username not in current_assignees]
        
        if not new_assignees:
            print("✅ All usernames are already assigned to the issue.")
            return True
        
        print(f"Adding {len(new_assignees)} new assignees: {', '.join(sorted(new_assignees))}")
        
        # Assign the new users to the issue
        issue.add_to_assignees(*new_assignees)
        
        print(f"✅ Successfully assigned {len(new_assignees)} new users to issue #{issue_number}")
        
        # Verify the assignment worked
        updated_issue = repo.get_issue(issue_number)
        final_assignees = [assignee.login for assignee in updated_issue.assignees]
        print(f"Final assignees ({len(final_assignees)}): {', '.join(sorted(final_assignees))}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error assigning users to issue: {str(e)}")
        return False

def main():
    """Main function to orchestrate the assignee extraction and assignment."""
    
    # Get GitHub token from command line argument or environment variable
    github_token = None
    if len(sys.argv) > 1:
        github_token = sys.argv[1]
    else:
        github_token = os.getenv('GITHUB_TOKEN')
    
    if not github_token:
        print("❌ GitHub token is required. Provide it as:")
        print("   1. Command line argument: python3 assign_peer_review_assignees.py YOUR_TOKEN")
        print("   2. Environment variable: export GITHUB_TOKEN=YOUR_TOKEN")
        sys.exit(1)
    
    # Repository and issue configuration
    repo_owner = "TRU-PBADS"
    repo_name = "ADSC_3910_students"
    issue_number = 4
    
    full_repo_name = f"{repo_owner}/{repo_name}"
    print(f"🚀 Processing repository: {full_repo_name}, Issue: #{issue_number}")
    
    # Initialize GitHub client
    try:
        github_client = Github(github_token)
        
        # Test authentication
        user = github_client.get_user()
        print(f"✅ Authenticated as: {user.login}")
        
    except Exception as e:
        print(f"❌ Failed to authenticate with GitHub: {str(e)}")
        sys.exit(1)
    
    try:
        # Get the repository and issue
        repo = github_client.get_repo(full_repo_name)
        issue = repo.get_issue(issue_number)
        
        print(f"📋 Found issue: '{issue.title}'")
        
        # Extract usernames from issue body
        usernames = extract_usernames_from_issue_body(issue.body)
        
        if not usernames:
            print("❌ No usernames found in the issue body")
            return False
        
        # Assign users to the issue
        success = assign_users_to_issue(github_client, full_repo_name, issue_number, usernames)
        
        if success:
            print(f"\n🎉 Task completed successfully! All {len(usernames)} usernames have been assigned to issue #{issue_number}")
        else:
            print(f"\n❌ Task failed. Please check the error messages above.")
        
        return success
        
    except Exception as e:
        print(f"❌ Error processing issue: {str(e)}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)