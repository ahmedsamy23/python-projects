import mysql.connector

# الاتصال بقاعدة البيانات
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='madrsa',
    use_unicode=True
)

cr = connection.cursor()

# دالة لحفظ وإغلاق الاتصال بقاعدة البيانات
def commit_close():
    connection.commit()
    cr.close()

# دالة لجلب بيانات الطلاب والمواد
def fetch_data():
    # جلب بيانات الطلاب
    cr.execute("SELECT id, user_name, email, password FROM students")
    students = cr.fetchall()

    # جلب بيانات المواد
    cr.execute("SELECT sub_id, sub_name FROM subjects")
    subjects = cr.fetchall()
    
    return students, subjects

# تعريف الكلاس Member
class Member:
    def __init__(self, id, name, email, password, degree, sub_name):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.degree = degree
        self.sub_name = sub_name

    def options(self):
        options = """ view degree / add member / delete / close
                     (v / a / d / q):  """
        while True:
            ask = input(options)
            if ask == "v":
                self.view()
            elif ask == "a":
                self.add()
            elif ask == "d":
                self.delete()
            elif ask == "q":
                commit_close()
                print("APP Closed.")
                break
            else:
                print("invalid Error")
    
    def view(self):
        # عرض بيانات الطالب حسب ID
        try:
            cr.execute(f"SELECT id, user_name, email, password FROM students WHERE id = {self.id}")
            stu_view = cr.fetchone()  # جلب صف واحد فقط

            if stu_view:
                print(f"id: {stu_view[0]} \nuser_name: {stu_view[1]} \nEmail: {stu_view[2]} \nPassword: {stu_view[3]}")
            else:
                print("Student Not Exist")
                
        except Exception as e:
            print(f"ERROR: {e}")

    def add(self):
        # إضافة عضو جديد إذا لم يكن موجودًا
        try:
            cr.execute(f"SELECT id FROM students WHERE id = {self.id}")
            if cr.fetchone():
                print("Student Exist")
                
            else:
                cr.execute(f'INSERT INTO students (id, user_name, email, password) VALUES ({self.id}, "{self.name}", "{self.email}", "{self.password}")')
                print("Student Added succesfully")
        except Exception as e:
            print(f"ERROR: {e}")
    
    def delete(self):

        delete_user = input("Are You Sure You Want To Delete Your Email (y/n)? ").lower()
        try:
            while True :
                if delete_user == "y":
                    cr.execute(f"SELECT id FROM students WHERE id = {self.id}")
                    if cr.fetchone():
                        cr.execute(f"DELETE * FROM student WHERE id = {self.id}")
                        commit_close()
                        print("Student Deleted.")
                elif delete_user == "n":
                    break
                else :
                    print("Invalid Input!,Try Again")
                    continue
        except Exception as e:
            print(f"ERROR: {e}")

# إدخال بيانات العضو
mem_id = int(input("Enter Your id: "))
mem_name = input("Enter Your Name: ")
mem_email = input("Enter Your Email: ").strip()
mem_password = input("Enter Your Password: ").strip()
mem_degree = input("Enter Your Degree: ").strip()
mem_subname = input("Enter Subject Name: ").strip()

# إنشاء كائن من الكلاس Member وتشغيل الخيارات
user_1 = Member(mem_id, mem_name, mem_email, mem_password, mem_degree, mem_subname)
user_1.options()
