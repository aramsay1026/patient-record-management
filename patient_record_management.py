import csv
from binary_search_tree import Node, BinarySearchTree
from graphviz import Digraph


class PatientRecord:
    def __init__(self, patient_id, name, age, diagnosis,
                 blood_pressure, pulse, body_temperature):
        # Store all fields for one patient record.
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        self.blood_pressure = blood_pressure
        self.pulse = pulse
        self.body_temperature = body_temperature

    def __str__(self):
        # Control how the record prints when printing
        return (f"Patient ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, "
                f"Diagnosis: {self.diagnosis}, Blood Pressure: {self.blood_pressure}, "
                f"Pulse: {self.pulse}, Body Temperature: {self.body_temperature}")


class PatientRecordManagementSystem:
    def __init__(self):
        # Start with an empty Binary Search Tree.
        self.bst = BinarySearchTree()

    def add_patient_record(self, patient_id, name, age, diagnosis,
                           blood_pressure, pulse, body_temperature):
        # Create a new patient record and insert it into the BST
        # Avg runtime O(height of tree)
        record = PatientRecord(patient_id, name, age, diagnosis,
                               blood_pressure, pulse, body_temperature)
        node = Node(patient_id, record)
        self.bst.insert(node)

    def search_patient_record(self, patient_id):
        # Return the record for the given ID or None if not found
        # Avg runtime O(height of tree)
        node = self.bst.search(patient_id)
        return node.value if node else None

    def delete_patient_record(self, patient_id):
        # Remove a patient by ID if it exists in the tree. 
        # Avg runtime O(height of tree)
        self.bst.remove(patient_id)

    def display_all_records(self):
        # Print all records in sorted order using inorder traversal. 
        # Runtime O(n)

        def visit(node):
            # Visit function to print each node's value.
            print(node.value)

        self.bst.inorder_traversal(self.bst.root, visit)

    def build_tree_from_csv(self, file_path):
        # Read patient data from CSV and insert each row into the BST
        # Runtime O(n log n) avg
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header row

            for row in reader:  # Loop over all rows. Loop runtime: O(n)
                patient_id = int(row[0])
                name = row[1]
                age = int(row[2])
                diagnosis = row[3]
                blood_pressure = row[4]
                pulse = int(row[5])
                body_temp = float(row[6])

                self.add_patient_record(patient_id, name, age, diagnosis,
                                        blood_pressure, pulse, body_temp)

    def visualize_tree(self, filename="patient_records_tree"):
        # Create a Graphviz diagram of the BST and save as PNG
        # Runtime O(n)
        dot = Digraph()
        self._add_nodes(dot, self.bst.root)
        dot.render(filename, format='png', cleanup=True)

    def _add_nodes(self, dot, node):
        # Recursively add nodes and edges to the Graphviz object
        # Runtime O(n)
        if node is None:
            return

        dot.node(str(node.key), str(node.key))

        if node.left:
            dot.edge(str(node.key), str(node.left.key))
            self._add_nodes(dot, node.left)

        if node.right:
            dot.edge(str(node.key), str(node.right.key))
            self._add_nodes(dot, node.right)
