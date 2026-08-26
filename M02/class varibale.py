class TrainingBatch:
    batch_name = "Python Batch 1"

    def __init__(self, student_name):
        self.student_name = student_name


student1_name = input().strip()
student2_name = input().strip()
special_batch = input().strip()
new_shared_batch = input().strip()

student1 = TrainingBatch(student1_name)
student2 = TrainingBatch(student2_name)

student1.batch_name = special_batch

TrainingBatch.batch_name = new_shared_batch

print(f"Class Batch: {TrainingBatch.batch_name}")
print(f"{student1.student_name} Batch: {student1.batch_name}")
print(f"{student2.student_name} Batch: {student2.batch_name}")