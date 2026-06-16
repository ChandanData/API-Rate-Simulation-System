# API Rate Simulation System

This project was developed as part of the AICTE – EduSkills Virtual Internship Program under the Python Full Stack Development domain.

The goal of this project is to understand how API rate limiting works in real-world applications. Modern web services receive thousands of requests every second, and rate limiting helps control traffic, prevent misuse, and ensure fair usage of resources.

Using Python, I built a simple simulation system that processes API request logs, tracks user activity, applies different rate-limiting algorithms, and generates analytics on allowed and blocked requests.

---

## What This Project Does

The system takes API request logs as input and performs the following tasks:

* Parses and processes raw request logs
* Counts requests made by each user
* Implements a Fixed Window Rate Limiter
* Implements a Sliding Window Log Limiter
* Generates analytics showing allowed and blocked requests
* Simulates real-world API traffic management

---

## Project Highlights

- Implemented Fixed Window Rate Limiting Algorithm
- Implemented Sliding Window Log Rate Limiting Algorithm
- Parsed and processed API request logs
- Generated request analytics and user statistics
- Simulated real-world API traffic management
- Built using Python and core Data Structures

---

## Technologies Used

- Python 3
- JSON
- Dictionaries & Lists
- Data Structures & Algorithms
- VS Code
- Git
- GitHub

---

## Project Structure

```
API-Rate-Simulation-System/
│
├── log_parser.py
├── user_request_counter.py
├── fixed_window_limiter.py
├── sliding_window_limiter.py
├── rate_limit_analytics.py
├── sample_logs.txt
├── README.md
└── screenshots/
```

---

## Modules Implemented

### 1. Log Parser

This module reads raw request logs and converts them into structured JSON data.

Example Input:

```text
10 user1
20 user1
30 user2
```

Example Output:

```json
[
  {"time":10,"user":"user1"},
  {"time":20,"user":"user1"},
  {"time":30,"user":"user2"}
]
```

---

### 2. User Request Counter

This module tracks how many requests each user has made.

Example Output:

```json
{
  "user1": 4,
  "user2": 3,
  "user3": 2
}
```

---

### 3. Fixed Window Rate Limiter

This implementation divides time into fixed intervals and limits the number of requests a user can make within each interval.

It is simple, efficient, and commonly used in many systems.

---

### 4. Sliding Window Log Limiter

This implementation uses a rolling time window instead of fixed intervals.

It provides more accurate rate limiting and handles traffic spikes more effectively.

---

### 5. Rate Limit Analytics

This module generates useful statistics such as:

* Total requests
* Allowed requests
* Blocked requests

Example Output:

```json
{
  "user1": {
    "total": 5,
    "allowed": 3,
    "blocked": 2
  }
}
```

---

## Sample Test Data

The project uses a sample log file:

```text
10 user1
20 user1
30 user1
40 user2
50 user2
65 user1
75 user3
80 user2
95 user1
120 user3
130 user3
140 user2
```

Stored in:

```text
sample_logs.txt
```

---

## How to Run

Using PowerShell:

```powershell
Get-Content sample_logs.txt | python log_parser.py
Get-Content sample_logs.txt | python user_request_counter.py
Get-Content sample_logs.txt | python fixed_window_limiter.py
Get-Content sample_logs.txt | python sliding_window_limiter.py
Get-Content sample_logs.txt | python rate_limit_analytics.py
```

---

## What I Learned

Through this project, I learned:

* How API rate limiting works
* Different rate-limiting techniques
* Backend traffic management concepts
* Data parsing and processing
* Working with JSON data
* Python data structures
* Problem solving and debugging
* Git and GitHub project management

---

## Challenges Faced

One of the biggest challenges was managing request history for the Sliding Window algorithm and ensuring accurate request tracking.

To solve this, I used efficient data structures and filtering techniques to maintain only the relevant request history.

I also created sample log datasets to test different traffic scenarios and edge cases.

---

## Future Improvements

Some features that can be added in the future:

* Token Bucket Rate Limiter
* Leaky Bucket Algorithm
* FastAPI Integration
* Redis Support
* Real-Time Dashboard
* Docker Deployment
* Cloud Deployment

---

##  References

* Python Documentation: https://docs.python.org/3/
* API Rate Limiting Concepts
* Data Structures and Algorithms
* Backend System Design Principles

---

## Developer

**Chandan Kumar Jha**

B.Tech – Computer Science & Technology.

AICTE – EduSkills Virtual Internship Project

### Connect With Me

GitHub:
https://github.com/ChandanData

LinkedIn:
https://www.linkedin.com/in/chandan-kumar-jha-099977286

---

## License

This project is developed for educational and learning purposes as part of the AICTE – EduSkills Virtual Internship Program.

---

If you found this project interesting, feel free to star the repository and share your feedback.
