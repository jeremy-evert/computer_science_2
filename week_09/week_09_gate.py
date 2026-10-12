"""Week 9 gate: search/order tradeoff, with a self-documenting hardware profile.

Stdlib only. Run:  python week_09_gate.py

Prints a hardware profile first, then times a linear lookup against
sort-once + bisect lookup over the same data, then prints a World Bible entry.
"""
import bisect
import datetime
import os
import platform
import random
import sys
import time


def cpu_loop_proxy(seconds=0.5):
    """Count tight-loop iterations for `seconds`; return iterations/second."""
    count = 0
    end = time.perf_counter() + seconds
    while time.perf_counter() < end:
        count += 1
    return count / seconds


def peak_memory_kb():
    """Peak memory of this process in KB, or a note if unavailable."""
    try:
        import resource  # Linux/Mac only

        return str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    except ImportError:
        pass
    try:  # Windows: peak working set via ctypes (stdlib)
        import ctypes
        from ctypes import wintypes

        class PMC(ctypes.Structure):
            _fields_ = [
                ("cb", wintypes.DWORD),
                ("PageFaultCount", wintypes.DWORD),
                ("PeakWorkingSetSize", ctypes.c_size_t),
                ("WorkingSetSize", ctypes.c_size_t),
                ("QuotaPeakPagedPoolUsage", ctypes.c_size_t),
                ("QuotaPagedPoolUsage", ctypes.c_size_t),
                ("QuotaPeakNonPagedPoolUsage", ctypes.c_size_t),
                ("QuotaNonPagedPoolUsage", ctypes.c_size_t),
                ("PagefileUsage", ctypes.c_size_t),
                ("PeakPagefileUsage", ctypes.c_size_t),
            ]

        pmc = PMC()
        pmc.cb = ctypes.sizeof(pmc)
        k32 = ctypes.windll.kernel32
        k32.GetCurrentProcess.restype = wintypes.HANDLE
        psapi = ctypes.windll.psapi
        psapi.GetProcessMemoryInfo.argtypes = [
            wintypes.HANDLE, ctypes.POINTER(PMC), wintypes.DWORD]
        if psapi.GetProcessMemoryInfo(
                k32.GetCurrentProcess(), ctypes.byref(pmc), pmc.cb):
            return str(pmc.PeakWorkingSetSize // 1024)
    except Exception:
        pass
    return "unavailable"


def free_memory_kb():
    """Free physical memory in KB (Windows), or a note.

    wmic is removed on current Windows 11, so use GlobalMemoryStatusEx via
    ctypes first and only fall back to wmic.
    """
    try:
        import ctypes

        class MemStatus(ctypes.Structure):
            _fields_ = [
                ("dwLength", ctypes.c_ulong),
                ("dwMemoryLoad", ctypes.c_ulong),
                ("ullTotalPhys", ctypes.c_ulonglong),
                ("ullAvailPhys", ctypes.c_ulonglong),
                ("ullTotalPageFile", ctypes.c_ulonglong),
                ("ullAvailPageFile", ctypes.c_ulonglong),
                ("ullTotalVirtual", ctypes.c_ulonglong),
                ("ullAvailVirtual", ctypes.c_ulonglong),
                ("ullAvailExtendedVirtual", ctypes.c_ulonglong),
            ]

        status = MemStatus()
        status.dwLength = ctypes.sizeof(status)
        if ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(status)):
            return str(status.ullAvailPhys // 1024)
    except Exception:
        pass
    try:
        out = os.popen("wmic OS get FreePhysicalMemory 2>nul").read()
        digits = [t for t in out.split() if t.isdigit()]
        return digits[0] if digits else "unavailable"
    except Exception:
        return "unavailable"


def hardware_profile():
    """Print the hardware block; return (processor, cpu_count, timestamp)."""
    processor = platform.processor() or "unknown"
    cpu_count = os.cpu_count()
    timestamp = datetime.datetime.now().isoformat()

    print("=== HARDWARE PROFILE ===")
    print(f"Run timestamp: {timestamp}")
    print(f"Processor: {processor}")
    print(f"Machine: {platform.machine()}")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Logical cores: {cpu_count}")
    print(f"Python version: {sys.version}")
    print(f"Python executable: {sys.executable}")
    print(f"CPU loop proxy (higher = faster machine): "
          f"{cpu_loop_proxy():,.0f} iterations/second")
    print(f"Peak memory used by this process (KB): {peak_memory_kb()}")
    print(f"Free physical memory (KB): {free_memory_kb()}")
    print()
    return processor, cpu_count, timestamp


def linear_search(items, target):
    for i, value in enumerate(items):
        if value == target:
            return i
    return -1


def binary_search(sorted_items, target):
    i = bisect.bisect_left(sorted_items, target)
    if i < len(sorted_items) and sorted_items[i] == target:
        return i
    return -1


def timed(fn, *args):
    start = time.perf_counter()
    result = fn(*args)
    return result, time.perf_counter() - start


def benchmark(n=100_000, lookups=200, seed=9):
    rng = random.Random(seed)
    data = rng.sample(range(n * 10), n)
    targets = rng.sample(data, lookups)

    # Sanity check: both searches must agree on the answer.
    ordered = sorted(data)
    assert all(
        data[linear_search(data, t)] == ordered[binary_search(ordered, t)]
        for t in targets[:5]
    )

    _, linear_s = timed(lambda: [linear_search(data, t) for t in targets])
    _, sort_s = timed(sorted, data)
    _, bisect_s = timed(lambda: [binary_search(ordered, t) for t in targets])

    print("=== BENCHMARK RESULTS ===")
    print(f"n = {n:,} items, {lookups} lookups")
    print(f"Linear search, unsorted:   {linear_s:.4f} s")
    print(f"Sort once:                 {sort_s:.4f} s")
    print(f"Bisect search, sorted:     {bisect_s:.6f} s")
    print(f"Sort + bisect total:       {sort_s + bisect_s:.4f} s")
    if sort_s + bisect_s < linear_s:
        print(f"Sorting first wins after {lookups} lookups.")
    else:
        print(f"Linear search wins at {lookups} lookups; sorting did not pay off.")
    print("Precondition: bisect is only correct on sorted data.")
    print()


def main():
    processor, cpu_count, timestamp = hardware_profile()
    benchmark()
    print("=== WORLD BIBLE ENTRY ===")
    print("Week 9: compared linear lookup with sort-once + bisect on the same data.")
    print("Tradeoff: sorting costs up front; it pays off only with many lookups,")
    print("and the sorted order must be maintained as data changes.")
    print(f"Hardware: {processor} | {cpu_count} cores | Run: {timestamp}")


if __name__ == "__main__":
    main()
