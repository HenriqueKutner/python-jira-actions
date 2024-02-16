import os
from dotenv import load_dotenv
from jira import JIRA

load_dotenv()

secret_key = os.environ.get("TOKEN")

jira = JIRA(server="https://jiracloud.cit.com.br/", token_auth=secret_key)

projects = jira.projects()

keys = sorted(project.key for project in projects)[11]

commit_messages = os.environ.get("COMMIT_MESSAGES")

if commit_messages:
    commit_messages = commit_messages.split("\n")
    for commit_message in commit_messages:
        print("commit_message = ", commit_message)

# issue_key = commit_message.split(':')[0].strip('[').strip(']')

# issue = jira.issue(issue_key)

# print(issue.fields.description)
