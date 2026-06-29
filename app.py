import os

# ❌ VULNERABILITY 1: Hardcoded sensitive AWS API Key (Gitleaks should catch this)
AWS_SECRET_KEY = "AKIAIMNOF7ER8STEFAKEKEY" 

def greet():
    return "Hello, Secure CI/CD!"

# ❌ VULNERABILITY 2: Using eval() on user input (Semgrep should catch this)
def dangerous_execution(user_input):
    return eval(user_input) 

if __name__ == "__main__":
    print(greet())
