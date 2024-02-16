import os
from dotenv import load_dotenv
from jira import JIRA

load_dotenv()

secret_key = os.environ.get("TOKEN")

jira = JIRA(server="https://jiracloud.cit.com.br/", token_auth=secret_key)

projects = jira.projects()

keys = sorted(project.key for project in projects)[11]

commit_message = os.environ.get("COMMIT_MESSAGES")

issue_key = commit_message.split(':')[0].strip('[').strip(']')
issue = jira.issue(issue_key)

print("Título da issue = ", issue.fields.summary)
print("Descrição da issue = ", issue.fields.description)
