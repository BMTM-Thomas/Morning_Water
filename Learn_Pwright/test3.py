all_domain_names = ["domain_name1", "domain_name2", "domain_name3", "domain_name4", "domain_name5"]

try:
    for index, item in enumerate(all_domain_names):
        print(f"Index: {index}, Domain: {item}")
except Exception as e:
    print(f"Error: {e}")