def read_log(file_name):
    with open(file_name, "r") as file:
        return file.readlines()
    
def analyze_log_levels(lines):
    total = 0
    error_count = 0
    warning_count = 0
    info_count = 0

    for line in lines:
        total += 1
        
        if "ERROR" in line:
            error_count += 1
        elif "WARNING" in line:
            warning_count += 1
        elif "INFO" in line:
            info_count += 1

    return {
        "total": total,
        "error_count": error_count,
        "warning_count": warning_count,
        "info_count": info_count
}

def print_report(report):
    print("LOG LEVEL ANALYSIS REPORT")
    print("-------------------------")
    print(f"Total lines: {report['total']}")
    print(f"ERROR count: {report['error_count']}")
    print(f"WARNING count: {report['warning_count']}")
    print(f"INFO count: {report['info_count']}")

def main():
    file_name = "sample.log"
    lines = read_log(file_name)
    results = analyze_log_levels(lines)
    print_report(results)

main()