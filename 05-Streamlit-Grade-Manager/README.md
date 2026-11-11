# Streamlit Student Grade Manager

A browser-based grade manager built with Streamlit. Add students and marks to
view their grades and the class average, highest mark, and lowest mark.
Student data stays in Streamlit session state across app reruns.

## Grading scale

| Mark | Grade |
| --- | --- |
| 90–100 | A |
| 80–89 | B |
| 70–79 | C |
| 60–69 | D |
| 0–59 | E |

Marks may be decimal values from 0 to 100. Names cannot be blank.

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run grade_app.py
```

Open the local URL printed by Streamlit in your browser.
