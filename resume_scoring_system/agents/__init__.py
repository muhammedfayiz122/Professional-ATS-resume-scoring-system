import os, importlib

pkg_path = "my_package"
for f in os.listdir(pkg_path):
    if f.endswith(".py") and f != "__init__.py":
        module = importlib.import_module(f"{pkg_path}.{f[:-3]}")
        globals().update({k: v for k, v in vars(module).items() if callable(v)})