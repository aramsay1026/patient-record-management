# **Patient Record Management System**

A Python program that uses a **Binary Search Tree (BST)** to efficiently store, search, delete, and visualize patient medical records.
It demonstrates core data structures concepts including tree traversal, node-based storage, recursive algorithms, and Graphviz-based visualization.

---

## **What It Does**

* Loads patient records from a CSV file into a Binary Search Tree
* Stores each patient as a custom `PatientRecord` object
* Supports searching patient records by ID
* Supports deletion and insertion of records
* Displays patient data using **inorder**, **preorder**, and **postorder** traversals
* Generates **Graphviz** visualizations of the BST structure
* Demonstrates object-oriented programming and data structure design

---

## **Technologies Used**

* **Python 3.11+**
* **Jupyter Notebook** (`main.ipynb` for building the tree, printing output, and generating images)
* **Graphviz** (for tree visualization)
* **Git** (branching, merging, and version control screenshots included)
* **UML Diagram** created in Miro

---

## **How to Run**

### **1. Clone this repository:**

```bash
git clone https://github.com/aramsay1026/patient-record-management.git
cd patient-record-management
```

---

### **2. Install Graphviz (required for visualization)**

**Using pip:**

```bash
pip install graphviz
```

If you're using Anaconda:

```bash
conda install graphviz
```

---

### **3. Open the project notebook**

Launch Jupyter:

```bash
jupyter notebook
```

Then open:

```
main.ipynb
```

Run all cells to:

* Build the tree
* Display records
* Search records
* Delete and insert new records
* Generate Graphviz diagrams 