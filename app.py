import pickle
import base64

def load_user_session(session_data):
    # ❌ CRITICAL SECURITY FLAW: Insecure Deserialization
    # Using pickle.loads on untrusted user input allows arbitrary code execution.
    # Semgrep SAST should flag this immediately as an absolute showstopper.
    decoded_data = base64.b64decode(session_data)
    return pickle.loads(decoded_data)

if __name__ == "__main__":
    # A dummy encoded string representing a user session token
    sample_token = "gASVIQAAAAAAAACMCXNoZWxscmVvc5SMAlVTNCSDhG9SMC4="
    print("Attempting to load secure session...")
    try:
        load_user_session(sample_token)
    except Exception as e:
        print("Session data processing completed.")
