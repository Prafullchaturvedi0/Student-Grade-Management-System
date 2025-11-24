import subprocess
import sys




def test_starts():
# attempt to run the script and ensure it exits cleanly when sent EOF
    p = subprocess.Popen([sys.executable, "grades_system.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    out, err = p.communicate(input="\n11\n") # send a newline then choose Exit
    assert p.returncode == 0
    assert "Student Grades Management System" in out or "Exit" in out or "Close the program" in out