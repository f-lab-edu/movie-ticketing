from fastapi import APIRouter
from datetime import datetime

router = APIRouter()


@router.get("/movies")
async def get_movies(date: datetime, theater_id: int = None):
    """
    Get movies by date and theater_id
    :param date: datetime
    :param theater_id: int
    :return:

    Example:
    {
        "movies": [
            "Movie 1",
            "Movie 2"
        ]
    }
    """
    return {"movies": ["Movie 1", "Mocie 2"]}


@router.get("/theaters")
async def get_theaters():
    """
    Example:
    {
        "theaters": [
            "Theater 1",
            "Theater 2"
        ]
    }
    Example error response:
    {
        "error": "Theaters not found"
    }
    """
    return {"theaters": ["Theater 1", "Theater 2"]}


@router.get("/showtimes")
async def get_showtimes(movie_id: int, theater_id: int, date: datetime):
    """
    Example:
    {
        "showtimes": [
            "Showtime 1",
            "Showtime 2"
        ]
    }
    Example error response:
    {
        "error": "Showtimes not found"
    }
    """
    return {"showtimes": ["Showtime 1", "Showtime 2"]}
