# Snap Class

Snap Class is an attendance app for classrooms. Instead of calling out names one by one, a teacher can take a photo of the class or record the students saying "I am present", and the app marks attendance automatically using face and voice recognition.

It is built with Python and Streamlit, and the data is stored in Supabase.

## Features

**For students**
- Log in with your face (no password needed)
- Register a new profile with your face, and optionally your voice
- Join a subject using a subject code, a link, or a QR code
- See how many classes you attended in each subject
- Unenroll from a subject

**For teachers**
- Register and log in with a username and password
- Create subjects (code, name and section)
- Share a subject using a link or QR code
- Take attendance from classroom photos (camera or upload, multiple photos allowed)
- Take attendance by voice
- Review the results before saving them
- See past attendance records for every subject

## How it works

- **Face recognition:** `dlib` finds the faces in a photo and turns each one into a 128-number embedding. An SVM classifier (scikit-learn) matches it to a student, and a distance check makes sure the match is close enough.
- **Voice recognition:** `librosa` splits the recording into speech segments, and `resemblyzer` creates a voice embedding for each one. It is compared with the stored voice of every enrolled student.
- **Database:** Supabase stores teachers, students, subjects and attendance logs. Teacher passwords are hashed with `bcrypt`.
- **QR codes:** `segno` generates the QR code for joining a subject.

## Tech stack

- Python 3.13
- Streamlit
- Supabase
- dlib, face_recognition_models, scikit-learn
- resemblyzer, librosa
- bcrypt, segno, Pillow, pandas, numpy

## Project structure

```
SNAPCLASS/
├── app.py                      # Entry point, decides which screen to show
├── requirements.txt
├── .streamlit/
│   └── secrets.toml            # Supabase keys (not committed)
└── src/
    ├── components/             # Reusable UI pieces and dialogs
    │   ├── dialog_add_photo.py
    │   ├── dialog_attendance_results.py
    │   ├── dialog_auto_enroll.py
    │   ├── dialog_create_subject.py
    │   ├── dialog_enroll.py
    │   ├── dialog_share_subject.py
    │   ├── dialog_voice_attendance.py
    │   ├── header.py
    │   └── subject_card.py
    ├── database/
    │   ├── config.py           # Supabase connection
    │   └── db.py               # All database queries
    ├── pipelines/
    │   ├── face_pipeline.py    # Face detection and recognition
    │   └── voice_pipeline.py   # Voice recognition
    ├── screens/
    │   ├── home_screen.py
    │   ├── student_screen.py
    │   └── teacher_screen.py
    └── ui/
        └── base_layout.py      # Custom CSS and styling
```

## Getting started

### 1. Clone the repo

```bash
git clone https://github.com/<your-username>/snapclass.git
cd snapclass
```

### 2. Create a virtual environment

```bash
python -m venv myenv
source myenv/bin/activate      # On Windows: myenv\Scripts\activate
```

### 3. Install the requirements

```bash
pip install -r requirements.txt
```

### 4. Set up Supabase

Create a project on [Supabase](https://supabase.com) and add these tables:

| Table | Columns |
|-------|---------|
| `teachers` | `teacher_id`, `username`, `password`, `name` |
| `students` | `student_id`, `name`, `face_embedding`, `voice_embedding` |
| `subjects` | `subject_id`, `subject_code`, `name`, `section`, `teacher_id` |
| `subject_students` | `student_id`, `subject_id` |
| `attendance_logs` | `student_id`, `subject_id`, `timestamp`, `is_present` |

`face_embedding` and `voice_embedding` store lists of numbers, so use a `jsonb` (or `float8[]`) column for them.

### 5. Add your secrets

Create a file at `.streamlit/secrets.toml`:

```toml
SUPABASE_URL = "your-supabase-project-url"
SUPABASE_KEY = "your-supabase-key"
```

Do not push this file to GitHub. Make sure it is listed in `.gitignore`.

### 6. Run the app

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`.

## How to use

**As a teacher**
1. Click **Teacher Portal** and register an account.
2. Go to **Manage Subjects** and create a subject.
3. Share the subject code or QR code with your students.
4. Go to **Take Attendance**, pick a subject, and either add photos and run face analysis, or use voice attendance.
5. Check the results and click **Confirm & Save**.

**As a student**
1. Click **Student Portal** and let the camera scan your face.
2. If you are new, enter your name (and record your voice if you want voice attendance) to create a profile.
3. Click **Enroll in Subject** and enter the code from your teacher.

## Tips for better results

- Use clear, well-lit photos where faces are easy to see.
- For voice attendance, record in a quiet room and let each student speak one at a time.
- Students should register their face with a front-facing photo.

## Known limitations

- Face matching can get less accurate with poor lighting, masks, or faces that are very small in the photo.
- Voice attendance works only for students who added a voice profile during registration.

## Future ideas

- Export attendance as CSV or PDF
- Edit attendance after saving
- Attendance reports and charts for each student

## Author

Made by **Hemant Kaushal**.

## License

Add a license of your choice here (for example MIT).
