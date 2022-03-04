def check_if_desired_seq(x):
    x = x.upper()
    if len(x) != 102:
        print("Incorrect length")
        return False
    if "GCC" not in x:
        print("GGC not present in sequence")
        return False
    if not (x.endswith("CTTCTGCC") and x.startswith("CGCACC") and "AAGG" in x):
        print("Not selected the right sequence")
        return False
    return True
