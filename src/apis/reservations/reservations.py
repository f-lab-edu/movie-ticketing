from fastapi import APIRouter

router = APIRouter()


@router.post("/reservations")
async def make_reservation(showtime_id: int, seat_number: str):
    """
    Make a reservation for a showtime and seat.
    Returns the reservation ID.
    Example request:
    {
        "showtime_id": XXX,
        "seat_number": "A1"
    }
    Example response:
    {
        "Result": "Success",
        "reservation_id": XXX
    }

    Example error response:

    {
        "error": "Showtime not found"
    }
    Status code : 404 not found

    {
        "error": "Seat not found"
    }
    Status code : 404 not found

    {
        "error": "Showtime ID is required"
    }
    Status code: 400 Bad Request

    {
        "error": "Internal server error"
    }
    Status code : 500 Internal Server Error
    """
    return {"Result": "Success", "reservation_id": 123}


@router.get("/reservations/{user_id}")
async def get_reservations(user_id: int):
    """
    Get all reservations for a user.
    Returns a list of reservation IDs.
    Example response:
    {
        "reservations": [
            "Reservation 1",
            "Reservation 2"
        ]
    }
    Example error response:
    {
        "error": "User not found"
    }
    Status code : 404 not found

    {
        "error": "Invalid user ID"
    }
    Status code: 400 Bad Request

    {
        "error": "User ID is required"
    }
    Status code: 400 Bad Request
    """
    return {"reservations": ["Reservation 1", "Reservation 2"]}
