log1_list = {"A101", "B202", "C303", "A101", "D404"}
log2_events = {"C303", "E505", "F606", "B202"}
log1_events = set(log1_list)
common_events = log1_events.intersection(log2_events)
all_events = log1_events.union(log2_events)
print("Intersection of logs : ", common_events)
print("Union of logs: ", all_events)