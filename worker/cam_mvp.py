import json,math,pathlib,re
program=["G0 X0 Y0","G1 X10 Y0","G1 X10 Y10","G1 X0 Y10","G1 X0 Y0"]
x=y=0.0; length=0.0; supported=True
for line in program:
 m=re.fullmatch(r"G([01]) X(-?\\d+(?:\\.\\d+)?) Y(-?\\d+(?:\\.\\d+)?)",line)
 if not m: supported=False; break
 nx,ny=float(m.group(2)),float(m.group(3));
 if m.group(1)=="1": length+=math.hypot(nx-x,ny-y)
 x,y=nx,ny
passed=supported and math.isclose(length,40.0,rel_tol=1e-12)
out={"benchmark":"restricted_gcode_square","engine":"PY-CAM-MVP","program":program,"cut_path_length_mm":length,"passed":passed,"evidence_level":"E2","limitations":["digital parser benchmark","no collision check","no physical machine execution"]}
pathlib.Path("artifacts").mkdir(exist_ok=True); pathlib.Path("artifacts/cam_mvp.json").write_text(json.dumps(out,indent=2),encoding="utf-8"); print(json.dumps(out,indent=2)); raise SystemExit(0 if passed else 1)
