import os
from dotenv import load_dotenv
from jira import JIRA

load_dotenv()

secret_key = os.environ.get("TOKEN")

jira = JIRA(server="https://jiracloud.cit.com.br/", token_auth=secret_key)

projects = jira.projects()

keys = sorted(project.key for project in projects)[11]

my_commit = "[GOPS-3098]: test commit"

issue = jira.issue("GOPS-3098")

print(issue.get_field('description'))
