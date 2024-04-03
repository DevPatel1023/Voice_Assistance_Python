import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, \
    QLineEdit, QComboBox, QDateEdit, QSpinBox, QTableWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt, QDate


class TodoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Todo App")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.init_ui()

    def init_ui(self):
        self.task_id_label = QLabel("Item ID:")
        self.task_id_input = QLineEdit()

        self.title_label = QLabel("Title:")
        self.title_input = QLineEdit()

        self.priority_label = QLabel("Priority:")
        self.priority_combo = QComboBox()
        self.priority_combo.addItems(["High", "Medium", "Low"])

        self.deadline_label = QLabel("Deadline:")
        self.deadline_date = QDateEdit()
        self.deadline_date.setDate(QDate.currentDate())

        self.duration_label = QLabel("Duration:")
        self.duration_spin = QSpinBox()
        self.duration_spin.setSuffix(" hours")
        self.duration_spin.setMinimum(1)
        self.duration_spin.setMaximum(24)

        self.add_button = QPushButton("Add Task")
        self.add_button.clicked.connect(self.add_task)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Item ID", "Title", "Priority", "Deadline", "Duration"])
        self.table.horizontalHeader().setStretchLastSection(True)

        self.layout.addWidget(self.task_id_label)
        self.layout.addWidget(self.task_id_input)
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.title_input)
        self.layout.addWidget(self.priority_label)
        self.layout.addWidget(self.priority_combo)
        self.layout.addWidget(self.deadline_label)
        self.layout.addWidget(self.deadline_date)
        self.layout.addWidget(self.duration_label)
        self.layout.addWidget(self.duration_spin)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.table)

    def add_task(self):
        item_id = self.task_id_input.text()
        title = self.title_input.text()
        priority = self.priority_combo.currentText()
        deadline = self.deadline_date.date().toString(Qt.ISODate)
        duration = self.duration_spin.value()

        if not item_id or not title:
            QMessageBox.warning(self, "Warning", "Please enter Item ID and Title")
            return

        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        self.table.setItem(row_position, 0, QTableWidgetItem(item_id))
        self.table.setItem(row_position, 1, QTableWidgetItem(title))
        self.table.setItem(row_position, 2, QTableWidgetItem(priority))
        self.table.setItem(row_position, 3, QTableWidgetItem(deadline))
        self.table.setItem(row_position, 4, QTableWidgetItem(str(duration)))

        self.clear_inputs()

    def clear_inputs(self):
        self.task_id_input.clear()
        self.title_input.clear()
        self.priority_combo.setCurrentIndex(0)
        self.deadline_date.setDate(QDate.currentDate())
        self.duration_spin.setValue(1)
        app.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    todo_app = TodoApp()
    todo_app.show()
    sys.exit(app.exec_())
