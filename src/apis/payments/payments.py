from fastapi import APIRouter

router = APIRouter()


@router.post("/payment")
async def process_payment():
    """
    Process a payment.
    Returns:
      A dictionary containing the result of the payment.
    Example:
      {
        "result": "Success"
      }
      or
      {
        "result": "Failure"
      }
      or
      {
        "result": "Error"
      }
    """
    return {"result": "Success"}
