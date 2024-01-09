# Hospital_Management_System

Brief about the project:
This project aims to develop a user-friendly website for efficient hospital management. The website provides comprehensive information about the hospital, its departments, and the doctors on board. Patients can easily schedule appointments online, checking doctor availability, while doctors can conveniently view and manage their appointments.

Impact and usefulness in real world:
This website streamlines the appointment process for both doctors and patients. Doctors benefit from an organised view of their appointments, and patients can avoid the hassle of physically visiting the hospital for booking appointments. Additionally, patients can explore hospital details and facilities online before planning a visit.

Team members:
Sowmya K S
Mahadevu M P

Technologies and Tools used: 
Architecture: Object Relational Mapping
Front-end : HTML, CSS, JS
Back-end : Python
Database : SQLite
Framework : Django
Code Editor : Visual Studio Code
Version Control : Git & Github

Requirements : 
asgiref==3.7.2
certifi==2023.11.17
charset-normalizer==3.3.2
Django==5.0
idna==3.6
razorpay==1.4.1
requests==2.31.0
sqlparse==0.4.4
tzdata==2023.4
urllib3==2.1.0

Brief of all the functionalities implemented:
Patient App:
- The  patient can register to the application using the e-mail id and other details like full name, age, blood group, phone number, address, password.
- During registration, OTP validation is performed using the OTP sent to the entered email id.
- After registration, login can be performed using registered email-id and password.
- On login, the patient can access the various details of the hospital including details about departments, doctors and facilities provided.
- The main feature of this application is that the patients can book their appointments and pay for it online based on the availability of the doctor.
- Log out functionality is also implemented as the users can log out once they complete their work.

	Doctor App:
- The  Doctor can register to the application using his e-mail id and other details like full name, degree, specialisation, years of experience, phone number, address, password.
- During registration, OTP validation is performed using the OTP sent to the entered email id.
- After registration, login can be performed using registered email-id and password.
- On login, the doctor can access the various details of the hospital including details about departments, doctors and facilities provided.
- The main feature of this application is that the doctors can view all their appointments  in an organised way.
- Log out functionality is also implemented as the users can log out once they complete their work.
