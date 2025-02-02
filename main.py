import json
import requests
from fastapi import FastAPI, Query, Response
from fastapi.middleware.cors import CORSMiddleware
from utils import is_prime, is_perfect, digit_sum, get_number_properties


app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

NUMBERS_API_URL = "http://numbersapi.com/{}/math"

@app.get("/api/classify-number")
async def classify_number(number: str = Query(..., description="The number to classify")):
    try:
        number = int(number)  # Manual validation

        # Determine properties
        properties = get_number_properties(number)


        # Get fun fact
        response = requests.get(NUMBERS_API_URL.format(number))
        fun_fact = response.text if response.status_code == 200 else "No fun fact available"

        return {
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect(number),
            "properties": properties,
            "digit_sum": digit_sum(number),
            "fun_fact": fun_fact
        }

    except ValueError:
        response_data = {"number": number, "error": True}
        return Response(content=json.dumps(response_data), media_type="application/json", status_code=400)
