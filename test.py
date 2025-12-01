from patient_record_management import PatientRecordManagementSystem

prms = PatientRecordManagementSystem()

prms.add_patient_record(5, "Alice", 30, "Cold", "120/80", 70, 37.1)
prms.add_patient_record(2, "Bob", 52, "Flu", "130/90", 80, 38.0)
prms.add_patient_record(8, "Charlie", 41, "Allergies", "110/70", 68, 36.9)

print("All records (inorder):")
prms.display_all_records()

print("\nSearch for ID 2:")
print(prms.search_patient_record(2))

print("\nDelete ID 5 and show records again:")
prms.delete_patient_record(5)
prms.display_all_records()

