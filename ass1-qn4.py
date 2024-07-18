def opposite_face_number(face_number):
    if face_number < 1 or face_number >6:
        return "invalid input."
    return 7-face_number

face_number = int(input("enter a dice face number :"))

print("the opposite face number is :",opposite_face_number(face_number))