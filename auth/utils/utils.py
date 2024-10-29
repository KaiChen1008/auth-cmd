import hmac
import base64
import hashlib
import struct
import time
import csv
from auth.utils.params import TOKEN_PATH

TIME_STEP = 30


def config_exists() -> bool:
    return TOKEN_PATH.exists()


def has_token(name: str) -> bool:
    if not config_exists():
        return False

    with open(TOKEN_PATH, mode="r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == name:
                return True
    return False


def generate_totp(secret, digits=6, digest_method=hashlib.sha1):
    # Decode the base32-encoded secret key
    key = base64.b32decode(secret, True)

    # Get the current time, divide by time step and convert to an integer
    current_time = int(time.time()) // TIME_STEP

    # Pack the current time into a byte array (8 bytes, big-endian)
    counter = struct.pack(">Q", current_time)

    # Create HMAC-SHA digest using the secret key and the counter
    hmac_digest = hmac.new(key, counter, digest_method).digest()

    # Extract the dynamic offset from the last byte
    offset = hmac_digest[-1] & 0x0F

    # Get a 4-byte slice of the digest, starting at the offset
    truncated_hash = hmac_digest[offset : offset + 4]

    # Convert the truncated hash to an integer (big-endian) and mask the most significant bit
    otp_value = struct.unpack(">I", truncated_hash)[0] & 0x7FFFFFFF

    # Compute the OTP by taking modulo 10^digits (to ensure the right number of digits)
    otp = otp_value % (10**digits)

    # Zero-pad the OTP if necessary and return it as a string
    return f"{otp:0{digits}d}"


if __name__ == "__main__":
    SECRET = "aaa"
    print(generate_totp(SECRET, 30, 8))
