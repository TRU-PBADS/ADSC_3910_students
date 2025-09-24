#!/usr/bin/env python3
"""
Script to extract GitHub usernames from peer review issue and assign them as assignees.
"""

import os
import re
import sys
from github import Github

def extract_usernames_from_issue_body(issue_body):
    """
    Extract GitHub usernames mentioned in the issue body.
    Looks for @username patterns in the issue content.
    """
    # Pattern to match @username mentions
    username_pattern = r'@([a-zA-Z0-9_-]+)'
    usernames = re.findall(username_pattern, issue_body)
    
    # Remove duplicates and return as set
    unique_usernames = list(set(usernames))
    
    print(f"Found usernames: {unique_usernames}")
    return unique_usernames

def assign_users_to_issue(github_client, repo_name, issue_number, usernames):
    """
    Assign the extracted usernames to the specified issue.
    """
    try:
        repo = github_client.get_repo(repo_name)
        issue = repo.get_issue(issue_number)
        
        print(f"Processing issue #{issue_number}: {issue.title}")
        
        # Get current assignees
        current_assignees = [assignee.login for assignee in issue.assignees]
        print(f"Current assignees: {current_assignees}")
        
        # Filter out usernames that are already assigned
        new_assignees = [username for username in usernames if username not in current_assignees]
        
        if not new_assignees:
            print("All usernames are already assigned to the issue.")
            return
        
        print(f"Adding new assignees: {new_assignees}")
        
        # Assign the new users to the issue
        issue.add_to_assignees(*new_assignees)
        
        print(f"Successfully assigned {len(new_assignees)} new users to issue #{issue_number}")
        
    except Exception as e:
        print(f"Error assigning users to issue: {str(e)}")
        sys.exit(1)

def main():
    """Main function to orchestrate the assignee extraction and assignment."""
    
    # Get environment variables
    github_token = os.getenv('GITHUB_TOKEN')
    repo_owner = os.getenv('REPO_OWNER')
    repo_name = os.getenv('REPO_NAME')
    issue_number = int(os.getenv('ISSUE_NUMBER', '4'))
    
    if not all([github_token, repo_owner, repo_name]):
        print("Missing required environment variables")
        sys.exit(1)
    
    full_repo_name = f"{repo_owner}/{repo_name}"
    print(f"Processing repository: {full_repo_name}, Issue: #{issue_number}")
    
    # Initialize GitHub client
    github_client = Github(github_token)
    
    try:
        # Get the repository and issue
        repo = github_client.get_repo(full_repo_name)
        issue = repo.get_issue(issue_number)
        
        print(f"Found issue: {issue.title}")
        
        # Extract usernames from issue body
        usernames = extract_usernames_from_issue_body(issue.body)
        
        if not usernames:
            print("No usernames found in the issue body")
            return
        
        # Assign users to the issue
        assign_users_to_issue(github_client, full_repo_name, issue_number, usernames)
        
    except Exception as e:
        print(f"Error processing issue: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()