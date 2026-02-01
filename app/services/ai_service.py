from app.utils.logger import logger

def generate_ai_response(prompt: str) -> str:
    logger.info("Mock AI invoked")

    text = prompt.lower()

    if "password" in text or "login" in text:
        return (
            "To reset your password, go to the login page and click "
            "'Forgot Password'. Follow the instructions sent to your "
            "registered email address."
        )

    if "refund" in text or "return" in text:
        return (
            "Refunds are typically processed within 5–7 business days "
            "after approval. You will receive a confirmation email once "
            "the refund is completed."
        )

    if "account" in text or "delete" in text:
        return (
            "To delete your account, please navigate to Account Settings "
            "and submit a deletion request. Our support team will verify "
            "and process it within 24 hours."
        )

    return (
        "Thank you for reaching out to support. "
        "Your request has been received, and our team will respond shortly."
    )
