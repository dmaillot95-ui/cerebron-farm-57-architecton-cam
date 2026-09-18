import subprocess,sys,json,pathlib
r=subprocess.run([sys.executable,"worker/cam_mvp.py"],check=False); assert r.returncode==0
x=json.loads(pathlib.Path("artifacts/cam_mvp.json").read_text()); assert x["passed"] is True and x["cut_path_length_mm"]==40.0
