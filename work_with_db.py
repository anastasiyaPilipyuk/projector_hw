from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'  # звязати з таблиці

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    subjects = relationship("StudentSubject", back_populates="student")

    def __str__(self):
        return f'This is a student {self.name}. Age: {self.age}'

    def __repr__(self):
        return f'This is a student {self.name}. Age: {self.age}'


class Subject(Base):
    __tablename__ = 'subject'  # звязати з таблиці

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    students = relationship("StudentSubject", back_populates="subject")

    def __str__(self):
        return f'{self.title}'

    def __repr__(self):
        return f'{self.title}'


class StudentSubject(Base):
    __tablename__ = 'student_subject'  # звязати з таблиці

    student_id = Column(Integer, ForeignKey('student.id'), primary_key=True)
    subject_id = Column(Integer, ForeignKey('subject.id'), primary_key=True)

    student = relationship("Student", back_populates="subjects")
    subject = relationship("Subject", back_populates="students")

    def __str__(self):
        return f'Student: {self.student.name}. Subject: {self.subject.name}. Grade: {self.grade}'

    def __repr__(self):
        return f'Student: {self.student.name}. Subject: {self.subject.name}. Grade: {self.grade}'


DATABASE_URI = 'postgresql://{user}:{password}@{host}:{port}/{database}'

engine = create_engine(
    DATABASE_URI.format(
        host='localhost',
        database='postgres',
        user='alksandr',
        password='password',
        port=5432,
    )
)

Session = sessionmaker(bind=engine)
with Session() as session:
    students_with_english_class = session.query(Student).join(StudentSubject).join(Subject).\
                                filter(Subject.name == 'English').all()
    for student in students_with_english_class:
        print(student.name)


