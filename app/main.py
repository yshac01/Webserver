from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pathlib
import psutil
import socket
import os
import time
from datetime import datetime, timedelta  # Fixed import

app = FastAPI()

BASE_DIR = pathlib.Path(__file__).parent
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

# System information functions
def get_system_info():
    """Get basic system information"""
    hostname = socket.gethostname()
    uptime_seconds = time.time() - psutil.boot_time()
    uptime = str(timedelta(seconds=uptime_seconds)).split('.')[0]  # Fixed datetime.timedelta to just timedelta
    
    return {
        "hostname": hostname,
        "uptime": uptime,
        "os": os.uname().sysname,
        "release": os.uname().release,
        "machine": os.uname().machine
    }

def get_cpu_info():
    """Get CPU information"""
    cpu_temp = None
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            cpu_temp = float(f.read()) / 1000
    except:
        cpu_temp = "N/A"
    
    return {
        "usage": psutil.cpu_percent(interval=1),
        "cores": psutil.cpu_count(logical=False),
        "threads": psutil.cpu_count(logical=True),
        "temperature": cpu_temp,
        "freq": psutil.cpu_freq().current if hasattr(psutil, "cpu_freq") else "N/A"
    }

def get_memory_info():
    """Get memory information"""
    mem = psutil.virtual_memory()
    return {
        "total": mem.total,
        "available": mem.available,
        "used": mem.used,
        "percent": mem.percent,
        "free": mem.free
    }

def get_disk_info():
    """Get disk information"""
    disk = psutil.disk_usage('/')
    return {
        "total": disk.total,
        "used": disk.used,
        "free": disk.free,
        "percent": disk.percent
    }

# API endpoints for system data
@app.get("/api/system")
async def system_info():
    return JSONResponse({
        "system": get_system_info(),
        "cpu": get_cpu_info(),
        "memory": get_memory_info(),
        "disk": get_disk_info()
    })

# Existing routes
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "Home"})

@app.get("/system", response_class=HTMLResponse)
async def system_page(request: Request):
    return templates.TemplateResponse("system.html", {"request": request, "title": "System Monitor"})

@app.get("/finance", response_class=HTMLResponse)
async def finance_page(request: Request):
    return templates.TemplateResponse("finance.html", {"request": request, "title": "Finance Dashboard"})










