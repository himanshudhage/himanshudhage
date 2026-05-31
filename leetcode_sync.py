import requests
import datetime
import subprocess
import json

USERNAME = "gakshatb"

query = """
query userProfileCalendar($username: String!) {
  matchedUser(username: $username) {
    userCalendar {
      submissionCalendar
    }
  }
}
"""

url = "https://leetcode.com/graphql"

res = requests.post(url,
    json={"query": query, "variables": {"username": USERNAME}},
    headers={"Content-Type": "application/json"}
)

data = res.json()
calendar = data["data"]["matchedUser"]["userCalendar"]["submissionCalendar"]

today = datetime.date.today().isoformat()

# If activity exists today
if today in calendar and calendar[today] > 0:
    with open("leetcode_commits.txt", "a") as f:
        f.write(f"{today} : {calendar[today]}\n")

    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", f"leetcode {today}"])
