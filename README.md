# Number Classification API

## Overview
The **Number Classification API** is a FastAPI-based service that takes a number as input and returns its mathematical properties, along with a fun fact fetched from the Numbers API.

## Features
- Determines if a number is **prime** or **perfect**.
- Identifies whether a number is **even**, **odd**, or an **Armstrong number**.
- Calculates the **sum of the digits**.
- Fetches a **fun fact** about the number from [Numbers API](http://numbersapi.com/).
- Returns responses in **JSON format**.
- Handles **invalid input gracefully** with proper error messages and status codes.
- Fully **deployed and accessible via a public endpoint**.

## Technology Stack
- **Backend Framework**: FastAPI (Python)
- **Deployment**: Vercel
- **Version Control**: GitHub

## API Specification
### Endpoint
```
GET /api/classify-number?number=<number>
```

### Request Parameters
| Parameter | Type   | Required | Description |
|-----------|--------|----------|-------------|
| number    | int    | Yes      | The number to classify |

### Response Formats
#### **200 OK (Valid Input)**
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is a narcissistic number."
}
```

#### **400 Bad Request (Invalid Input)**
```json
{
    "number": "3.24",
    "error": true
}
```

## Setup and Installation
### Pre-requisites
- Python 3.8+
- pip

### Installation Steps
1. **Clone the repository**
   ```sh
   git clone https://github.com/thegirlSynth/hng-stage1-backend.git
   cd hng-stage1-backend
   ```

2. **Create a virtual environment** (optional but recommended)
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the API locally**
   ```sh
   uvicorn main:app --reload
   ```

The API will be available at `http://127.0.0.1:8000/api/classify-number`.


## Testing
To test the API, you can:
- Use **Postman** or **cURL**:
  ```sh
  curl -X GET "http://your-deployed-url/api/classify-number?number=371" -H "accept: application/json"
  ```
- Open in a browser: `http://your-deployed-url/api/classify-number?number=371`

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Add new feature"`).
4. Push to your branch (`git push origin feature-branch`).
5. Open a pull request.

## License
This project is licensed under the MIT License.

## Author
**Cynthia Uche** – [GitHub](https://github.com/thegirlSynth) | [LinkedIn](https://linkedin.com/in/thecynthiauche)

