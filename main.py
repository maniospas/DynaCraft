from dynacraft.interpreter import interpret


if __name__ == "__main__":
    # input_str = ("""
    #     def c1() {
    #         return 1.0;
    #     }
    #     def test(float x) {
    #         print("hello21");
    #     }
    #     def test(int x) {
    #         print("hello21");
    #     }
    #     def test(int x) {
    #         print("hello21");
    #     }
    #     c1 a = c1();
    #     test(a);
    #  """)
    # input_str = ("""
    #         def vector(){ object o = object();  return o;}
    #         def vector2d(float x, float y){ vector v = vector();  float v.x = x; float v.y = y; return v;}
    #         def vector3d(float x, float y, float z){ vector2d v = vector2d(x, y);  float v.z = z;  return v;}
    #         vector2d vec = vector2d(5.0,3.0);
    #         vector3d vec3 = vector3d(5.0,3.0,1.0);
    #         print(vec);
    #
    #         def norm(float a, vector2d b){ object o = object(); float o.result = a + b.x + b.y; print(b); return o;}
    #         float c = 4.0;
    #         norm a = norm(1.0, vec);
    #         float res = a.result;
    #         print(res);
    #
    #      """)

    # input_str = ("""
    #             def vector(){ object o = object();  return o;}
    #             def vector2d(float x, float y){ vector v = vector();  float v.x = x; float v.y = y; return v;}
    #             def vector3d(float x, float y, float z){ print("heeeeeeey"); vector2d v = vector2d(x, y);  float v.z = z;  return v;}
    #             vector2d vec = vector2d(5.0,3.0);
    #             vector3d vec3 = vector3d(5.0,3.0,1.0);
    #             print(vec);
    #
    #             def norm(vector2d b){ object o = object(); float o.result = b.x + b.y;  return o;}
    #             def norm(vector3d b){ object o = object(); float o.result = b.x + b.y + b.z;  return o;}
    #             norm a = norm(vec);
    #             norm b = norm(vec3);
    #             float res = a.result;
    #             float resb = b.result;
    #
    #             print(res);
    #             print(resb);
    #
    #
    #             vector2d vec2 = vector3d(5.0,3.0,1.0);
    #
    #             print(vec2);
    #
    #          """)

    # input_str = ("""
    #                 def vector(){ object o = object();  return o;}
    #                 def vector2d(float x, float y){ vector v = vector();  float v.x = x; float v.y = y; return v;}
    #                 def vector3d(float a, float b, float z){ vector2d v = vector2d(a, b);  float v.z = z; float v.k =  3.0; return v;}
    #
    #
    #
    #                 vector2d vec2 = vector2d(5.0,3.0);
    #
    #                 def norm(vector2d v){ object o = object(); float o.result = v.x + v.y; return o;}
    #                 def norm(vector3d v){ object o = object(); float o.result = v.x + v.y + v.z; return o;}
    #
    #                 norm n2 = norm(vec2);
    #                 norm n3 = norm(vec2);
    #                 float a = n3.result;
    #
    #                 vector2d vec3 = vector3d(5.0,3.0,1.0);
    #                 norm n3 = norm(vec3
    #                 +);
    #                 float b = n3.result;
    #                 print(b);
    #
    #
    #              """)

    # input_str = ("""
    #                     def vector(){ object o = object();  float o.i = 5.0; return o;}
    #                     def vector2d(float x, float y){ vector v = vector();  float v.x = x + v.i; float v.y = y; return v;}
    #
    #                    vector2d v = vector2d(2.0, 5.0);
    #
    #                    float a = v.i;
    #
    #                    print(a);
    #                     print(23);
    #
    #                  """)

    # input_str = ("""
    #                         def sum(float a, float b){ float result = a + b; return result;}
    #
    #                         float a = sum(2.0, 2.0);
    #                         print(a);
    #
    #
    #                      """)

    # input_str = ("""
    #                         def test(){ object o = object(); bool o.reason = false; return o;}
    #                         test t = test();
    #                         bool a = t.reason;
    #                         print(a);
    #
    #                         """)
    # input_str = ("""
    #                 float x = 1.0;
    #                 x = 2.0;
    #                 print(x);
    # """)

    # input_str = ("""
    #                             def vector(string a) {
    #                                                                  object o = object();
    #                                                                  string o.x = a;
    #                                                                  return o;
    #                                                                 }
    #                             string t = "eric";
    #                             vector v = vector("eric");
    #                             string a = v.x;
    #
    #                             print(v);
    #
    #                             """)

    # input_str = ("""
    #                         def vector(float a) {
    #                                                              object o = object();
    #                                                              float o.x = a;
    #                                                              return o;
    #                                                             }
    #
    #                         vector v = vector(8.0);
    #                         float a = v.x;
    #
    #                         print(a);
    #                         print("23");
    #
    #                         def vector2d(vector a) {            vector v = vector(2.0);
    #
    #                                                             float v.y = 3.0 + v.x;
    #                                                             v.x = 3.0;
    #                                                             return v;
    #                                                             }
    #
    #                         vector2d v2 = vector2d(v);
    #                         float test2 = v2.x ;
    #                         print(test2);
    #
    #                         """)

    # input_str = ("""
    #                 def mapping(int key, float val){ object o = object();
    #                             map[int, float] o.test = map[int, float]();
    #                             o.test[key] = val;
    #                             return o;
    #                             }
    #                 print(23);
    #                 float a = 1.2;
    #                 print(a);
    #
    #                 mapping t = mapping(1, 0.3);
    #                 float a = t.test[1];
    #                 t.test[2]=1.2;
    #                 float b = t.test[2];
    #                 print(b);
    #
    #                 print(t);
    #                 for key in t.test : { print(key); }
    #
    #             """)

    # input_str = ("""
    #             object x = object();
    #             int a = 1;
    #             map[int, map[int, float]] x.test = map[int, map[int, float]]();
    #             x.test[a] = map[int, float];
    #             x.test[1][3] = 0.3;
    #             float result = x.test[1][3];
    #             print(x.test[a][3]);
    #             """)
    #
    # input_str = ("""
    #                 int a = 1;
    #                 map[int, map[int, float]] test = map[int, map[int, float]]();
    #                 test[a] = map[int, float];
    #                 test[2] = map[int, float];
    #                 test[1][3] = 0.3;
    #                 test[1][4] = 0.5;
    #                 test[2][1] = 0.1;
    #                 del test[1][3];
    #                 print(test[1][4]);
    #                 """)

    # input_str = ("""
    #                     int a = 1;
    #                     object o = object();
    #                     map[int, float] o.test = map[int, float]();
    #                     o.test[a] = 0.3;
    #                     o.test[2] = 0.5;
    #                     for key in test : {
    #                                         print(o.test[key]);
    #                                         }
    #                     print(test[1]);
    #                     """)


    # input_str = ("""
    #                     def Student(string name, int age) {
    #                                                          object s = object();
    #                                                          string s.name = name;
    #                                                          int s.age = age;
    #                                                          bool s.isExpelled = false;
    #                                                          return s;
    #                                                         }
    #                     Student s1 = Student("eric", 21);
    #
    #                     string name = s1.name;
    #                     int age = s1.age;
    #                     bool expelled = s1.isExpelled;
    #                     print(name);
    #                     print(age);
    #                     print(expelled);
    #
    #                     def ExpelledStudent(Student s, string reason) {
    #                                                                     Student es = s;
    #                                                                     es.isExpelled = true;
    #                                                                     string es.reason = reason;
    #                                                                     return es;
    #                                                                 }
    #
    #                     ExpelledStudent e1 =ExpelledStudent(s1, "cheated on exams");
    #                     bool newExpFlag = e1.isExpelled;
    #                     string reason = e1.reason;
    #                     print(newExpFlag);
    #                     print(reason);
    #
    #
    #                     def School() {
    #                                     object o = object();
    #                                     map[int, Student] o.students = map[int, Student]();
    #                                     map[int, ExpelledStudent] o.expelledStudents = map[int, ExpelledStudent]();
    #                                     return o;
    #
    #                                     }
    #
    #                     School sch = School();
    #
    #                     print(sch);
    #
    #                    def addStudent(School school, int studentID, Student s){
    #                                                                             School sch = school;
    #                                                                             print(sch);
    #
    #                                                                             sch.students[studentID] = s;
    #
    #                                                                             return sch;
    #                                                                            }
    #
    #                    addStudent res =    addStudent(sch, 12, s1);
    #                    print(res);
    #
    #                    def expelStudent(School school, int studentID, string reason) {
    #                                                                                     Student s = school.students[studentID];
    #                                                                                     ExpelledStudent es = ExpelledStudent(s, reason);
    #                                                                                     del school.students[studentID];
    #                                                                                     school.expelledStudents[studentID] = es;
    #                                                                                     return school;
    #                                                                                     }
    #
    #                    expelStudent expS = expelStudent(sch, 12, s1);
    #
    #
    #                    School mySchool = School();
    #                    Student alice = Student("Alice", 16);
    #                    Student bob = Student("Bob", 17);
    #
    #                    School mySchool = addStudent(mySchool, 1, alice);
    #                    School  mySchool = addStudent(mySchool, 2, bob);
    #
    #                    School mySchool = expelStudent(mySchool, 1, "Cheating on exams");
    #
    #                    for key in mySchool.students : {
    #                                                     Student student = mySchool.students[key];
    #                                                     string name = student.name + "is enrolled";
    #                                                     print(name);
    #                                                 }
    #
    #                    for key in mySchool.expelledStudents : {
    #                                                                 ExpelledStudent expelled = mySchool.expelledStudents[key];
    #                                                                 string name = expelled.name + "is expelled";
    #                                                                 print(name);
    #                                                         }
    #
    #
    #
    #                     """)

    # input_str = ("""
    #                         def Student(string name, int age) {
    #                                                              object s = object();
    #                                                              string s.name = name;
    #                                                              int s.age = age;
    #                                                              bool s.isExpelled = false;
    #                                                              return s;
    #                                                             }
    #
    #                         Student s1 = Student("Eric", 21);
    #                         string name = s1.name;
    #                         int age = s1.age;
    #                         bool expelled = s1.isExpelled;
    #                         print(name);
    #                         print(age);
    #                         print(expelled);
    #
    #                         def ExpelledStudent(Student s, string reason) {
    #                                                                         Student es = s;
    #                                                                         es.isExpelled = true;
    #                                                                         string es.reason = reason;
    #                                                                         return es;
    #                                                                         }
    #
    #                         ExpelledStudent e1 = ExpelledStudent(s1, "Cheated on exams");
    #                         bool newExpFlag = e1.isExpelled;
    #                         string reason = e1.reason;
    #                         print(newExpFlag);
    #                         print(reason);
    #
    #                         def School() {
    #                                         object o = object();
    #                                         map[int, Student] o.students = map[int, Student]();
    #                                         map[int, ExpelledStudent] o.expelledStudents = map[int, ExpelledStudent]();
    #                                         return o;
    #                                         }
    #
    #                         School sch = School();
    #                         print(sch);
    #
    #                         def addStudent(School school, int studentID, Student s) {
    #                                                                                     School sch = school;
    #                                                                                     sch.students[studentID] = s;
    #                                                                                     return sch;
    #                                                                                 }
    #
    #                         School res = addStudent(sch, 12, s1);
    #                         print(res);
    #
    #                         def expelStudent(School school, int studentID, string reason) {
    #                                                                                         Student s = school.students[studentID];
    #                                                                                         ExpelledStudent es = ExpelledStudent(s, reason);
    #                                                                                         del school.students[studentID];
    #                                                                                         school.expelledStudents[studentID] = es;
    #                                                                                         return school;
    #                                                                                         }
    #
    #
    #                         School expS = expelStudent(sch, 12, "Cheating on exams");
    #
    #                         School mySchool = School();
    #                         Student alice = Student("Alice", 16);
    #                         Student bob = Student("Bob", 17);
    #                         mySchool = addStudent(mySchool, 1, alice);
    #                         mySchool = addStudent(mySchool, 2, bob);
    #
    #                         mySchool = expelStudent(mySchool, 1, "Cheating on exams");
    #
    #                         def updateStudentDetails(School school, int studentID, string newName, int newAge) {
    #                                                                                                                 Student s = school.students[studentID];
    #                                                                                                                 s.name = newName;
    #                                                                                                                 s.age = newAge;
    #                                                                                                                 school.students[studentID] = s;
    #                                                                                                                 print(school.students[studentID]);
    #                                                                                                                 return school;
    #                                                                                                             }
    #
    #                         mySchool = updateStudentDetails(mySchool, 2, "Robert", 18);
    #
    #                         def reenrollStudent(School school, int expelledID) {
    #                                                                             ExpelledStudent es = school.expelledStudents[expelledID];
    #                                                                             es.isExpelled = false;
    #                                                                             del school.expelledStudents[expelledID];
    #                                                                             school.students[expelledID] = es;
    #                                                                             print(school.students[expelledID]);
    #                                                                             return school;
    #                                                                             }
    #
    #
    #                         mySchool = reenrollStudent(mySchool, 1);
    #
    #
    #                         def generateReport(School school) {
    #                                                             print("Enrolled Students:");
    #                                                             for key in school.students : {
    #                                                                                                 Student student = school.students[key];
    #                                                                                                 string text = student.name + key + "is enrolled";
    #                                                                                                 print(text);
    #                                                                                             }
    #
    #                                                             print("Expelled Students:");
    #
    #                                                             for key in school.expelledStudents : {
    #                                                                                                   ExpelledStudent expelled = school.expelledStudents[key];
    #                                                                                                   string text = expelled.name + key + "was expelled for" + expelled.reason;
    #                                                                                                   print(text);
    #                                                                                                   }
    #                                                             }
    #
    #                         Student charlie = Student("Charlie", 18);
    #
    #                         mySchool = addStudent(mySchool, 3, charlie);
    #
    #                         mySchool = expelStudent(mySchool, 3, "Frequent absenteeism");      //comment
    #
    #                         //generate results
    #                         generateReport(mySchool);
    #
    #                         """)

    # input_str = ("""
    #
    #                             def Employee(int id) {
    #                                                                                 object o = object();
    #                                                                                 int o.id = id;
    #                                                                                 return o;
    #                                                                             }
    #
    #
    #                             Employee emp1 = Employee(1);
    #                             Employee emp2 = Employee(2);
    #                             Employee emp3 = Employee(3);
    #                             float id = 2.0;
    #                             if emp2.id <= 6.0 : {print("ok");}
    #                                     """)

    ##Employee System
    # input_str = ("""
    #
    #                         def Employee(string name, int id, float salary) {
    #                                                                             object o = object();
    #                                                                             string o.name = name;
    #                                                                             int o.id = id;
    #                                                                             float o.salary = salary;
    #                                                                             return o;
    #                                                                         }
    #                         def Manager(string name, int id, float salary, string department) {
    #                                                                                             object o = Employee(name, id, salary);
    #                                                                                             string o.department = department;
    #                                                                                             return o;
    #                                                                                             }
    #
    #                         def Department(string name) {
    #                                                         object o = object();
    #                                                         string o.name = name;
    #                                                         map[int, Employee] o.employees = map[int, Employee]();
    #                                                         return o;
    #                                                     }
    #
    #                         Department sales = Department("Sales");
    #                         Department hr = Department("HR");
    #
    #                         Employee emp1 = Employee("John Doe", 101, 50000.0);
    #                         Employee emp2 = Employee("Jane Smith", 102, 52000.0);
    #                         sales.employees[101] = emp1;
    #                         sales.employees[102] = emp2;
    #
    #                         Manager mgr1 = Manager("Alice Johnson", 201, 80000.0, "Sales");
    #                         sales.employees[201] = mgr1;
    #
    #
    #                         Employee emp3 = Employee("Bob Brown", 103, 48000.0);
    #                         hr.employees[103] = emp3;
    #
    #                         print(mgr1);
    #
    #                         def printEmployeeDetails(Employee e) {
    #                                                                 string details = "Name: " + e.name + ", ID: " + e.id + ", Salary: " + e.salary;
    #                                                                 print(details);
    #                                                             }
    #
    #                         def printManagerDetails(Manager m) {
    #                                                                 string details = "Manager: " + m.name + ", ID: " + m.id + ", Salary: " + m.salary + ", Department: " + m.department;
    #                                                                 print(details);
    #                                                             }
    #
    #                         def handleEmployee(Employee e) {
    #                                                         if e.id >= 200 : {  printManagerDetails(e); }
    #                                                         else: {printEmployeeDetails(e);}
    #                                                         }
    #                         for key in sales.employees : {
    #                                                         Employee e = sales.employees[key];
    #                                                         handleEmployee(e);
    #                                                         }
    #
    #                         for key in hr.employees : {
    #                                                     Employee e = hr.employees[key];
    #                                                     handleEmployee(e);
    #                                                     }
    #
    #                                 """)

    # this is a correct one school system
    # input_str = ("""
    #
    #                     def Student(string name, int age) {
    #                                                         object student = object();
    #                                                         string student.name = name;
    #                                                         int student.age = age;
    #                                                         bool student.isExpelled = false;
    #                                                         return student;
    #                                                         }
    #
    #                     def ExpelledStudent(object student, string reason) {
    #                                                                         student.isExpelled = true;
    #                                                                         string student.reason = reason;
    #                                                                         return student;
    #                                                                         }
    #
    #                     def School() {
    #                                     object school = object();
    #                                     map[int, object] school.enrolledStudents = map[int, object]();
    #                                     map[int, object] school.expelledStudents = map[int, object]();
    #                                     return school;
    #                                     }
    #
    #                     def addStudent(object school, int id, object student) {
    #                                                                             school.enrolledStudents[id] = student;
    #                                                                             return school;
    #                                                                             }
    #
    #                     def expelStudent(object school, int id, string reason) {
    #                                                                             object student = school.enrolledStudents[id];
    #                                                                             student = ExpelledStudent(student, reason);
    #                                                                             school.expelledStudents[id] = student;
    #                                                                             del school.enrolledStudents[id];
    #                                                                             return school;
    #                                                                             }
    #
    #                     def updateStudentDetails(object school, int id, string newName, int newAge) {
    #                                                                                                 object student = school.enrolledStudents[id];
    #                                                                                                 student.name = newName;
    #                                                                                                 student.age = newAge;
    #                                                                                                 school.enrolledStudents[id] = student;
    #                                                                                                 return school;
    #                                                                                                 }
    #
    #                     def reenrollStudent(object school, int id) {
    #                                                                 object student = school.expelledStudents[id];
    #                                                                 student.isExpelled = false;
    #                                                                 school.enrolledStudents[id] = student;
    #                                                                 del school.expelledStudents[id];
    #                                                                 return school;
    #                                                                 }
    #
    #
    #                     def generateReport(object school) {
    #                                                         string enrolledHeader = "Enrolled Students:";
    #                                                         print(enrolledHeader);
    #                                                         for key in school.enrolledStudents: {
    #                                                                                             object student = school.enrolledStudents[key];
    #                                                                                             string details = "ID: " + key + ", Name: " + student.name + ", Age: " + student.age + ", Expelled: " + student.isExpelled;
    #                                                                                             print(details);
    #                                                                                             }
    #
    #                                                         string expelledHeader = "Expelled Students:";
    #                                                         print(expelledHeader);
    #                                                         for key in school.expelledStudents: {
    #                                                                                              object student = school.expelledStudents[key];
    #                                                                                              string details = "ID: " + key + ", Name: " + student.name + ", Age: " + student.age + ", Expelled: " + student.isExpelled + ", Reason: " + student.reason;
    #                                                                                              print(details);
    #                                                                                             }
    #                                                         return school;
    #                                                         }
    #
    #
    #                     object mySchool = School();
    #
    #                     object student1 = Student("Alice", 14);
    #                     object student2 = Student("Bob", 15);
    #                     mySchool = addStudent(mySchool, 1, student1);
    #                     mySchool = addStudent(mySchool, 2, student2);
    #
    #
    #                     mySchool = expelStudent(mySchool, 2, "Behavior Issues");
    #
    #
    #                     mySchool = updateStudentDetails(mySchool, 1, "Alice Smith", 15);
    #
    #
    #                     mySchool = reenrollStudent(mySchool, 2);
    #
    #
    #                     generateReport(mySchool);
    #
    #                             """)

    input_str = ("""
                def fun9(string k, string g){ print(k);  }
def fun3(float g, float i){ object o = object();  float f = 1.9; float h = f - f / f; float c = 16.5 / 2.6 / f; return o; }
fun9 d = fun9(k, l);

             """)

    # input_str = ("""
    #     def print(float x) {
    #         string message = "hello21";
    #         print(message);
    #     }
    #     float a = 1.0;
    #
    #
    #     print(a);
    #  """)

    # input_str = ("""
    #             def sum(int x, int y) {
    #                 int z = x + y;
    #                 return z;
    #             }
    #             def sum(float x, float y) {
    #                 float z = x + y + 1;
    #                 return z;
    #             }
    #
    #             float a = sum(2.0,  4.0);
    #             print(a);
    #             print("2");
    #          """)

    interpret(input_str)

    # Display the parse tree
